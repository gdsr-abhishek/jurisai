from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path, WindowsPath
from FlagEmbedding import BGEM3FlagModel
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models


load_dotenv()
import os
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
def retrieve_text_data(path:WindowsPath)->str:
    data=''
    with open(str(path.parent)+'/'+str(path.stem)+'.txt','r',encoding='utf-8') as file:
        data = file.read()
    return data 
def start_ingestion()->str:
    print(str(Path(__file__).parent.parent))
    directory = Path(str(Path(__file__).parent.parent)+'\\data\\processed')
    file_paths = list(directory.rglob('*.txt'))
    print(file_paths)
    file_data_tensor = [retrieve_text_data(file_path) for file_path in file_paths]
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False)
    text_chunks=[]
    for text,file_path in zip(file_data_tensor,file_paths):
        text_chunks += text_splitter.create_documents(texts=[text],metadatas=[{'source':str(file_path.stem)}])
    print(f"total chunks for 10 files :{len(text_chunks)}")
    model= BGEM3FlagModel(model_name_or_path='BAAI/bge-m3',use_fp16=True,devices='cpu')
    embeddings_list=[]
    texts = [chunk.page_content for chunk in text_chunks]
    embeddings = model.encode(sentences=texts, batch_size=12, max_length=8192)['dense_vecs']
    ingestion_metadata = [[chunk,embedding] for chunk,embedding in zip(text_chunks,embeddings)] 
    print(ingestion_metadata)

    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        timeout=60
    )
    
    # client.upsert(
    #     collection_name="jurisai",
    #     points=[models.PointStruct(id=idx,vector=embedding,payload={'source':chunk.metadata['source'],'page_content':chunk.page_content}) for idx, (chunk, embedding) in enumerate(ingestion_metadata)]
    # )
    batch_size = 50
    points = [models.PointStruct(id=idx,vector={'dense':embedding},payload={'source':chunk.metadata['source'],'page_content':chunk.page_content}) for idx, (chunk, embedding) in enumerate(ingestion_metadata)]

    for i in range(0, len(points), batch_size):
        client.upsert(
            collection_name="jurisai",
            points=points[i:i+batch_size]
        )
        print(f"Uploaded batch {i//batch_size + 1}")
start_ingestion()
    