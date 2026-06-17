# Grounding Audit Report

- API: `http://localhost:8080`
- top_k: 5
- queries audited: 30

For each query: read the retrieved chunks, then mark every sentence of the expected answer as **[S]upported** or **[U]nsupported**. If most sentences are U, the expected answer — not the model — is the bug. Verify any factual disagreement against the source PDF, not from memory.

---

## [001] What are the penalties for hacking under the IT Act?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=it_act_2000_updated  score=1.0000
    programmes, computer commands, design and layout and programme analysis of computer resource in  any
    form.  6[66. Computer related offences.–If any person, dishonestly or fraudulently, does any act
    referred to  in section 43, he shall be punishable with imprisonment for a term which may extend
    to three years or  with fine which may extend to five lakh rupees or with both.
    1. Subs. by Act 7 of 2017, s. 169, for ―Cyber Appellate Tribunal‖ (w.e.f. 26-5-2017).  2. Subs.
    by notification No. S.O. 1015(E) (w.e.f. 19-9-2002).  3. Subs. by Act 10 of 2009, s. 31, for
    ―penalty‖ (w.e.f. 27-10-2009).  4. Subs. by s. 31, ibid., for ―penalty imposed‖ (w.e.f.
    27-10-2009).  5. Subs. by s. 2, ibid., for ―Digital Signature‖ (w.e.f. 27-10-2009).  6. Subs. by
    s. 32, ibid., for sections 66 and 67 (w.e.f. 27-10-2009). 24    Explanation.–For the purposes of
    this section,–
  [2] source=it_act_2000_updated  score=0.9125
    computer resource.  69B. Power to authorise to monitor and collect traffic data or information
    through any computer  resource for cyber security.  70. Protected system.  70A. National nodal
    agency.  70B. Indian Computer Emergency Response Team to serve as national agency for incident
    response.  71. Penalty for misrepresentation.  72. Penalty for Breach of confidentiality and
    privacy.  72A. Punishment for disclosure of information in breach of lawful contract.  73.
    Penalty for publishing electronic signature Certificate false in certain particulars.  74.
    Publication for fraudulent purpose.  75. Act to apply for offence or contravention committed
    outside India.  76. Confiscation.  77. Compensation, penalties or confiscation not to interfere
    with other punishment.  77A. Compounding of offences.  77B. Offences with three years
    imprisonment to be bailable.  78. Power to investigate offences.  CHAPTER XII  INTERMEDIARIES
    NOT TO BE LIABLE IN CERTAIN CASES
  [3] source=it_act_2000_updated  score=0.8943
    this Act, if it is not paid, shall he recovered as an arrear of land  revenue and the licence or the
    5[electronic  signature] Certificate, as the case may be, shall be suspended till the penalty is
    paid.  CHAPTER XI  OFFENCES  65. Tampering with computer source documents .–Whoever knowingly or
    intentionally conceals,  destroys or alters or intentionally or knowingly causes another to
    conceal, destroy, or alter any computer  source code used for a computer, computer programme,
    computer system or computer network, when the  computer source code is required to be kept or
    maintained by law for the time being in force, shall be  punishable with imprisonment up to
    three years, or with fine which may exten d up to two lakh rupees, or  with both.
    Explanation.–For the purposes of this section, ―computer source code ‖ means the listing of
    programmes, computer commands, design and layout and programme analysis of computer resource in
    any form.
  [4] source=it_act_2000_updated  score=0.8004
    other electronic record, which may be transmitted with the message.]  66B. Punishment for
    dishonestly receiving stolen computer resource or communication   device.–Whoever dishonestly
    receive  or retains any stolen computer resource or communication device  knowing or having
    reason to believe the same to be stolen c omputer resource or communication device,  shall be
    punished with imprisonment of either description for a term which may extend to three years or
    with fine which may extend to rupees one lakh or with both.  66C. Punishment for identity theft
    .–Whoever, fraud ulently or dishonestly make use of the  electronic signature, password or any
    other unique identification feature of any other person, shall be  punished with imprisonment of
    either description for a term which may extend to three years and shall  also be liable to fine
    which may extend to rupees one lakh.  66D. Punishment for cheating by personation by using
    computer resource.–Whoever, by means of
  [5] source=RTI-2005_Nov_2025  score=0.7659
    (b) require the public authority to compensate the complainant for any loss or other detriment
    suffered;  (c) impose any of the penalties provided under this Act;  (d) reject the application.
    (9) The Central Information Commission or State Information Commission, as the case may be,
    shall  give notice of its decision, including any right of appeal, to the complainant and the
    public authority.  (10) The Central Information Commission or State Information Commission, as
    the case may be,  shall decide the appeal in accordance with such procedure as may be
    prescribed.  20. Penalties.—(1)Where the Central Information Commission or the State Information
    Commission,  as the case may be, at the time of deciding any complaint or appeal is of the
    opinion that the Central  Public Information Officer or the State Public Information Officer, as
    the case may be, has, without any  reasonable cause, refused to receive an application for
    information or has not furnished information

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the IT Act, the penalties for hacking and related offenses can vary based on the specific violation
- [ ] S / U — Here are key penalties:
- [ ] S / U — 1
- [ ] S / U — **Section 66** (Computer Related Offences): If a person dishonestly or fraudulently engages in activities as described in Section 43, they can face:
- [ ] S / U — - Imprisonment for up to 3 years, or
- [ ] S / U — - A fine up to 5 lakh rupees, or
- [ ] S / U — - Both imprisonment and fine.
- [ ] S / U — 2
- [ ] S / U — **Section 65** (Tampering with Computer Source Documents): A person who conceals, destroys, or alters computer source code can be punished with:
- [ ] S / U — - Imprisonment for up to 3 years, or
- [ ] S / U — - A fine up to 2 lakh rupees, or
- [ ] S / U — - Both imprisonment and fine.
- [ ] S / U — 3
- [ ] S / U — **Section 66C** (Identity Theft): Those who fraudulently use another's electronic signature or unique identification features can be punished with:
- [ ] S / U — - Imprisonment for up to 3 years, and
- [ ] S / U — - A fine up to 1 lakh rupees.
- [ ] S / U — 4
- [ ] S / U — **Section 66B** (Receiving Stolen Computer Resource): Anyone who dishonestly receives stolen computer resources can be punished with:
- [ ] S / U — - Imprisonment for up to 3 years, or
- [ ] S / U — - A fine up to 1 lakh rupees, or
- [ ] S / U — - Both.
- [ ] S / U — These penalties reflect the seriousness of hacking and related offences under the IT Act.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [002] What is the punishment for identity theft under the IT Act?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=it_act_2000_updated  score=1.0000
    other electronic record, which may be transmitted with the message.]  66B. Punishment for
    dishonestly receiving stolen computer resource or communication   device.–Whoever dishonestly
    receive  or retains any stolen computer resource or communication device  knowing or having
    reason to believe the same to be stolen c omputer resource or communication device,  shall be
    punished with imprisonment of either description for a term which may extend to three years or
    with fine which may extend to rupees one lakh or with both.  66C. Punishment for identity theft
    .–Whoever, fraud ulently or dishonestly make use of the  electronic signature, password or any
    other unique identification feature of any other person, shall be  punished with imprisonment of
    either description for a term which may extend to three years and shall  also be liable to fine
    which may extend to rupees one lakh.  66D. Punishment for cheating by personation by using
    computer resource.–Whoever, by means of
  [2] source=POCSO-2012-32  score=0.8052
    knowing it to be false, thereby victimizing such child in any of the offences under this Act, shall
    be  punished with imprisonment, which may extend to one year or with fine or with both.  23.
    Procedure for media. —(1) No person shall make any report or present comments on any child  from
    any form of media or  studio or photographic facilities without having complet e and authentic
    information, which may have the effect of lowering his reputation or infringing upon his
    privacy.  (2) No reports in any media shall disclose, the identity of a child including his
    name, address,  photograph, family details, school, neighbourhood or any other particulars which
    may lead to disclosure   of identity of the child:  Provided that for reasons to be recorded in
    writing, the Special Court, competent to try the case under  the Act, may permit such
    disclosure, if in its opinion such disclosure is in the interest of the child.
  [3] source=Bharatiya_Nyaya_Sanhita  score=0.6208
    (b) A instigates B to burn Z’s house, B sets fire to the house and at the same time commits theft of
    property there. A, though guilty of abetting the burning of the house, is not guilty of abetting
    the theft; for the theft was a distinct act, and not a probable consequence of the burning. (c)
    A instigates B and C to break into an inhabited house at midnight for the purpose of robbery,
    and provides them with arms for that purpose. B and C break into the house, and being resisted
    by Z, one of the inmates, murder Z. Here, if that murder was the probable consequence of the
    abetment, A is liable to the punishment provided for murder. 52. If the act for which the
    abettor is liable under section 51 is committed in addition to the act abetted, and constitute a
    distinct offence, the abettor is liable to punishment for each of the offences. Punishment of
    abetment if act abetted is committed in consequence and where no express provision is made for
    its punishment. Punishment of abetment if
  [4] source=it_act_2000_updated  score=0.6113
    84B. Punishment for abetment of offences .–Whoever abets any offence shall, if the act abetted is
    committed in consequence of the abetment, and no express provision is made by this Act for the
    punishment of such abetment, be punished with the punishment provided for the offence under this
    Act.  Explanation.–An act or offence is said to be committed in consequence of abetment, when it
    is  committed in consequence of the instigation, or in pursuance of the conspiracy, or with the
    aid which  constitutes the abetment.  84C. Punishment for attempt to commit offences .–Whoever
    attempts to commit an offence  punishable by this Act or causes such an offence to be committed,
    and in such an attempt does any act  towards the commission of the offence, shall, where no
    express provision is made for the punishment of  such attempt, be punished with imprisonment of
    any description provided for the offence, for a term
  [5] source=Bharatiya_Nyaya_Sanhita  score=0.5702
    shall harm the reputation of any party, or knowing that it is likely to be used for that purpose,
    shall be punished with imprisonment of either description for a term which may extend to three
    years, and shall also be liable to fine. 337. Whoever forges a document or an electronic record,
    purporting to be a record or proceeding of or in a Court or an identity document issued by
    Government including voter identity card or Aadhaar Card, or a register of birth, marriage or
    burial, or a register kept by a public servant as such, or a certificate or document purporting
    to be made by a public servant in his official capacity, or an authority to institute or defend
    a suit, or to take any proceedings therein, or to confess judgment, or a power of attorney,
    shall be punished with imprisonment of either description for a term which may extend to seven
    years, and shall also be liable to fine. Explanation.—For the purposes of this section,
    “register” includes any list, data or

### Expected answer — sentence grounding checklist
- [ ] S / U — The punishment for identity theft under the IT Act is imprisonment for a term that may extend to three years, and the offender may also be liable to a fine that may extend to one lakh rupees.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [003] What does Section 65 of the IT Act say about tampering with computer source documents?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=it_act_2000_updated  score=1.0000
    this Act, if it is not paid, shall he recovered as an arrear of land  revenue and the licence or the
    5[electronic  signature] Certificate, as the case may be, shall be suspended till the penalty is
    paid.  CHAPTER XI  OFFENCES  65. Tampering with computer source documents .–Whoever knowingly or
    intentionally conceals,  destroys or alters or intentionally or knowingly causes another to
    conceal, destroy, or alter any computer  source code used for a computer, computer programme,
    computer system or computer network, when the  computer source code is required to be kept or
    maintained by law for the time being in force, shall be  punishable with imprisonment up to
    three years, or with fine which may exten d up to two lakh rupees, or  with both.
    Explanation.–For the purposes of this section, ―computer source code ‖ means the listing of
    programmes, computer commands, design and layout and programme analysis of computer resource in
    any form.
  [2] source=it_act_2000_updated  score=0.8181
    55. Orders constituting Appellate Tribunal to be final and not to invalidate its proceedings.  56.
    [Omitted.].  57. Appeal to Appellate Tribunal.  58. Procedure and powers of the Appellate
    Tribunal.  59. Right to legal representation.  60. Limitation.  61. Civil court not to have
    jurisdiction.  62. Appeal to High Court.  63. Compounding of contraventions. 3    SECTIONS  64.
    Recovery of penalty or compensation.  CHAPTER XI  OFFENCES  65. Tampering with computer source
    documents.  66. Computer related offences.  66A. Punishment for sending offensive messages
    through communication service, etc.  66B. Punishment for dishonestly receiving stolen computer
    resource or communication device.  66C. Punishment for identity theft.  66D. Punishment for
    cheating by personation by using computer resource.  66E. Punishment for violation of privacy.
    66F. Punishment for cyber terrorism.  67. Punishment for publishing or transmitting obscene
    material in electronic form.
  [3] source=it_act_2000_updated  score=0.5072
    computer, computer system or computer network;  (d) damages or causes to be damaged any computer,
    computer system or computer network, data,  computer data base or any other programmes residing
    in such computer, computer system or  computer network;  (e) disrupts or causes disruption of
    any computer, computer system or computer network;  (f) denies or causes the denial of access to
    any person authorised to access any computer,  computer system or computer network by any means;
    (g) provides any assistance to any person to facilitate access to a computer, computer system or
    computer network in contravention of the provisions of this Act, rules or regulations made
    thereunder;  (h) charges the services availed of by a person to the account of another person by
    tampering with  or manipulating any computer, computer system, or computer network;  1[(i)
    destroys, deletes or alters any information residing in a computer resource or diminishes its
  [4] source=it_act_2000_updated  score=0.4548
    programmes, computer commands, design and layout and programme analysis of computer resource in  any
    form.  6[66. Computer related offences.–If any person, dishonestly or fraudulently, does any act
    referred to  in section 43, he shall be punishable with imprisonment for a term which may extend
    to three years or  with fine which may extend to five lakh rupees or with both.
    1. Subs. by Act 7 of 2017, s. 169, for ―Cyber Appellate Tribunal‖ (w.e.f. 26-5-2017).  2. Subs.
    by notification No. S.O. 1015(E) (w.e.f. 19-9-2002).  3. Subs. by Act 10 of 2009, s. 31, for
    ―penalty‖ (w.e.f. 27-10-2009).  4. Subs. by s. 31, ibid., for ―penalty imposed‖ (w.e.f.
    27-10-2009).  5. Subs. by s. 2, ibid., for ―Digital Signature‖ (w.e.f. 27-10-2009).  6. Subs. by
    s. 32, ibid., for sections 66 and 67 (w.e.f. 27-10-2009). 24    Explanation.–For the purposes of
    this section,–
  [5] source=it_act_2000_updated  score=0.4402
    authorised access; or  (iii) introducing or causing to introduce any computer contaminant,  and by
    means of such conduct causes or is likely to cause death or injuries to persons or damage to or
    destruction of property or disrupts or knowing that it is likely to cause damage or disruption
    of supplies or  services essential to the life of the community or adversely affect the critical
    information infrastructure  specified under section 70; or  (B) knowingly or intentionally
    penetrates or a ccesses a computer resource without authorisation or  exceeding authorised
    access, and by means of such conduct obtains access to information, data or  computer data base
    that is restricted for reasons of the security of the State or foreign relations ; or any
    restricted information, data or computer data  base, with reasons to believe that such
    information, data  or computer data base so obtained may be used to cause or likely to cause
    injury to the interests of the

### Expected answer — sentence grounding checklist
- [ ] S / U — Section 65 of the IT Act states that whoever knowingly or intentionally conceals, destroys, or alters any computer source code required to be maintained by law, or causes someone else to do so, can face punishment
- [ ] S / U — This includes imprisonment for up to three years, a fine up to two lakh rupees, or both
- [ ] S / U — The term "computer source code" refers to the listings of programs, commands, design, layout, and analysis related to computer resources.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [004] What is the punishment for cyber terrorism under the IT Act?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=it_act_2000_updated  score=1.0000
    66E. Punishment for violation of privacy.  66F. Punishment for cyber terrorism.  67. Punishment for
    publishing or transmitting obscene material in electronic form.  67A. Punishment for publishing
    or transmitting of material containing sexually explicit act, etc., in  electronic form.  67B.
    Punishment for publishing or transmitting of material depicting children in sexually ex plicit
    act,  etc., in electronic form.  67C. Preservation and retention of information by
    intermediaries.  68. Power of Controller to give directions.  69. Power to issue directions for
    interception or monitoring or decryption of any information through  any computer resource.
    69A. Power to issue directions for blocking for public access of any information through any
    computer resource.  69B. Power to authorise to monitor and collect traffic data or information
    through any computer  resource for cyber security.  70. Protected system.  70A. National nodal
    agency.
  [2] source=it_act_2000_updated  score=0.9546
    or computer data base so obtained may be used to cause or likely to cause injury to the interests of
    the  sovereignty and integrity of India, the secur ity of the State, friendly relations with
    foreign States,  public order, decency or morality, or in relation to contempt of court,
    defamation or incitement to an  offence, or to the advantage of any foreign nation, group of
    individuals or otherwise,  commits the offence of cyber terrorism.  (2) Whoever commits or
    conspires to commit cyber terrorism shall be punishable with imprisonment  which may extend to
    imprisonment for life.  67. Punishment for publishing or transmitting obscene material in
    electronic form .–Whoever  publishes or transmits or causes to be published or transmitted in
    the electronic form, any material which  is lascivious or appeals to the prurient interest or if
    its effect is such as to tend to deprave and corrupt  persons who are likely, having r egard to
    all relevant circumstances, to read, see or hear the matter
  [3] source=it_act_2000_updated  score=0.9514
    reasonable expectation that–  (i) he or she could disrobe in privacy, without being concerned that
    an image of his private  area was being captured; or  (ii) any part of his or her private area
    would not be visible to the public, regardless of whether  that person is in a public or private
    place.  66F. Punishment for cyber terrorism.–(1) Whoever,–  (A) with intent to threaten the
    unity, integrity, security or sovereignty of India or to strike terror in  the people or any
    section of the people by–  (i) denying or cause the denial of access to any person authoris ed
    to access computer  resource; or  (ii) attempting to penetrate or access a computer resource
    without authorisa tion or exceeding  authorised access; or  (iii) introducing or causing to
    introduce any computer contaminant,  and by means of such conduct causes or is likely to cause
    death or injuries to persons or damage to or
  [4] source=it_act_2000_updated  score=0.7529
    punished with an imprisonment for a term which may extend to seven years and also be liable to fine.
    69B. Power to authorise to monitor and collect traffic data or information through any  computer
    resource for cyber security.–(1) The Central Government may, to enhance cyber security and  for
    identification, analysis and prevention of intrusion or spread of computer contaminant in the
    country,  by notification in the Official Gazette, authorise any agency of the Government to
    monitor and collect  traffic data or information generated, transmitted, received or stored in
    any computer resource.  (2) The intermediary or any person in -charge or the computer resource
    shall, when called upon by the  agency which has been authorised under sub -section ( 1),
    provide technical assistance and extend all  facilities to such agency to enable online acces s
    or to secure and provide online access to the computer
  [5] source=it_act_2000_updated  score=0.6863
    programmes, computer commands, design and layout and programme analysis of computer resource in  any
    form.  6[66. Computer related offences.–If any person, dishonestly or fraudulently, does any act
    referred to  in section 43, he shall be punishable with imprisonment for a term which may extend
    to three years or  with fine which may extend to five lakh rupees or with both.
    1. Subs. by Act 7 of 2017, s. 169, for ―Cyber Appellate Tribunal‖ (w.e.f. 26-5-2017).  2. Subs.
    by notification No. S.O. 1015(E) (w.e.f. 19-9-2002).  3. Subs. by Act 10 of 2009, s. 31, for
    ―penalty‖ (w.e.f. 27-10-2009).  4. Subs. by s. 31, ibid., for ―penalty imposed‖ (w.e.f.
    27-10-2009).  5. Subs. by s. 2, ibid., for ―Digital Signature‖ (w.e.f. 27-10-2009).  6. Subs. by
    s. 32, ibid., for sections 66 and 67 (w.e.f. 27-10-2009). 24    Explanation.–For the purposes of
    this section,–

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the IT Act, the punishment for cyber terrorism is as follows:
- [ ] S / U — 1
- [ ] S / U — Whoever commits or conspires to commit cyber terrorism can face imprisonment.
- [ ] S / U — 2
- [ ] S / U — The imprisonment may extend to **life imprisonment**.
- [ ] S / U — This applies if the individual intends to threaten the unity, integrity, security, or sovereignty of India or to instill terror in the people through various means as outlined in the Act.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [005] What are the penalties for publishing obscene material in electronic form?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=it_act_2000_updated  score=1.0000
    66E. Punishment for violation of privacy.  66F. Punishment for cyber terrorism.  67. Punishment for
    publishing or transmitting obscene material in electronic form.  67A. Punishment for publishing
    or transmitting of material containing sexually explicit act, etc., in  electronic form.  67B.
    Punishment for publishing or transmitting of material depicting children in sexually ex plicit
    act,  etc., in electronic form.  67C. Preservation and retention of information by
    intermediaries.  68. Power of Controller to give directions.  69. Power to issue directions for
    interception or monitoring or decryption of any information through  any computer resource.
    69A. Power to issue directions for blocking for public access of any information through any
    computer resource.  69B. Power to authorise to monitor and collect traffic data or information
    through any computer  resource for cyber security.  70. Protected system.  70A. National nodal
    agency.
  [2] source=it_act_2000_updated  score=0.8948
    or computer data base so obtained may be used to cause or likely to cause injury to the interests of
    the  sovereignty and integrity of India, the secur ity of the State, friendly relations with
    foreign States,  public order, decency or morality, or in relation to contempt of court,
    defamation or incitement to an  offence, or to the advantage of any foreign nation, group of
    individuals or otherwise,  commits the offence of cyber terrorism.  (2) Whoever commits or
    conspires to commit cyber terrorism shall be punishable with imprisonment  which may extend to
    imprisonment for life.  67. Punishment for publishing or transmitting obscene material in
    electronic form .–Whoever  publishes or transmits or causes to be published or transmitted in
    the electronic form, any material which  is lascivious or appeals to the prurient interest or if
    its effect is such as to tend to deprave and corrupt  persons who are likely, having r egard to
    all relevant circumstances, to read, see or hear the matter
  [3] source=it_act_2000_updated  score=0.8536
    conviction with imprisonment of either description for a term which may extend to five years and
    with  fine which may extend to ten lakh rupees and in the event of second or subsequent
    conviction with  imprisonment of either description for a term which may extend  to seven years
    and also with fine which  may extend to ten lakh rupees.  67B. Punishment for publishing or
    transmitting of material depicting children in sexually  explicit act, etc., in electronic
    form.–Whoever,–  (a) publishes or transmits or causes to be p ublished or transmitted material
    in any electronic form  which depicts children engaged in sexually explicit act or conduct; or
    (b) creates text or digital images, collects, seeks, browses, downloads, advertises, promotes,
    exchanges or distributes material in any electronic form depicting children in obscene or
    indecent or  sexually explicit manner; or 26    (c) cultivates, entices or induces children to
    online relationship with one or more children for and
  [4] source=it_act_2000_updated  score=0.8187
    persons who are likely, having r egard to all relevant circumstances, to read, see or hear the
    matter  contained or embodied in it, shall be punished on first conviction with imprisonment of
    either description  for a term which may extend to three years and with fine which may extend to
    fiv e lakh rupees and in the  event of second or subsequent conviction with imprisonment of
    either description for a term which may  extend to five years and also with fine which may
    extend to ten lakh rupees.  67A. Punishment for publishing or transmitting of material
    containing sexually explicit act, etc.,  in electronic form .–Whoever publishes or transmits or
    causes to be published or transmitted in the  electronic form any material which contains
    sexually explicit act or conduct shall be punished on first  conviction with imprisonment of
    either description for a term which may extend to five years and with
  [5] source=it_act_2000_updated  score=0.7818
    55. Orders constituting Appellate Tribunal to be final and not to invalidate its proceedings.  56.
    [Omitted.].  57. Appeal to Appellate Tribunal.  58. Procedure and powers of the Appellate
    Tribunal.  59. Right to legal representation.  60. Limitation.  61. Civil court not to have
    jurisdiction.  62. Appeal to High Court.  63. Compounding of contraventions. 3    SECTIONS  64.
    Recovery of penalty or compensation.  CHAPTER XI  OFFENCES  65. Tampering with computer source
    documents.  66. Computer related offences.  66A. Punishment for sending offensive messages
    through communication service, etc.  66B. Punishment for dishonestly receiving stolen computer
    resource or communication device.  66C. Punishment for identity theft.  66D. Punishment for
    cheating by personation by using computer resource.  66E. Punishment for violation of privacy.
    66F. Punishment for cyber terrorism.  67. Punishment for publishing or transmitting obscene
    material in electronic form.

### Expected answer — sentence grounding checklist
- [ ] S / U — The penalties for publishing or transmitting obscene material in electronic form under Section 67 of the IT Act are as follows:
- [ ] S / U — 1
- [ ] S / U — **First Conviction**: Imprisonment for a term that may extend up to **five years** and a fine that may extend up to **ten lakh rupees**.
- [ ] S / U — 2
- [ ] S / U — **Second or Subsequent Conviction**: Imprisonment for a term that may extend up to **seven years** and a fine that may extend up to **ten lakh rupees**.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [006] What is the punishment for cheating by personation using a computer resource?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=it_act_2000_updated  score=1.0000
    also be liable to fine which may extend to rupees one lakh.  66D. Punishment for cheating by
    personation by using computer resource.–Whoever, by means of  any communication device or
    compute r resource cheats by personation , shall be punished with  imprisonment of either
    description for a term which may extend to three years and shall also be liable to  fine which
    may extend to one lakh rupees.  66E. Punishment for violation of privacy.–Whoever, intentionally
    or knowingly captures, publishes  or transmits the image of a private area of any person without
    his or her consent, under circumstances  violating the privacy of that person, shall be punished
    with imprisonment which may extend to three years  or with fine not exceeding two lakh rupees,
    or with both.  Explanation.–For the purposes of this section–  (a) ―transmit‖ means to
    electronically send a visual image with the intent that it be viewed by a  person or persons;
  [2] source=it_act_2000_updated  score=0.9157
    other electronic record, which may be transmitted with the message.]  66B. Punishment for
    dishonestly receiving stolen computer resource or communication   device.–Whoever dishonestly
    receive  or retains any stolen computer resource or communication device  knowing or having
    reason to believe the same to be stolen c omputer resource or communication device,  shall be
    punished with imprisonment of either description for a term which may extend to three years or
    with fine which may extend to rupees one lakh or with both.  66C. Punishment for identity theft
    .–Whoever, fraud ulently or dishonestly make use of the  electronic signature, password or any
    other unique identification feature of any other person, shall be  punished with imprisonment of
    either description for a term which may extend to three years and shall  also be liable to fine
    which may extend to rupees one lakh.  66D. Punishment for cheating by personation by using
    computer resource.–Whoever, by means of
  [3] source=it_act_2000_updated  score=0.7758
    55. Orders constituting Appellate Tribunal to be final and not to invalidate its proceedings.  56.
    [Omitted.].  57. Appeal to Appellate Tribunal.  58. Procedure and powers of the Appellate
    Tribunal.  59. Right to legal representation.  60. Limitation.  61. Civil court not to have
    jurisdiction.  62. Appeal to High Court.  63. Compounding of contraventions. 3    SECTIONS  64.
    Recovery of penalty or compensation.  CHAPTER XI  OFFENCES  65. Tampering with computer source
    documents.  66. Computer related offences.  66A. Punishment for sending offensive messages
    through communication service, etc.  66B. Punishment for dishonestly receiving stolen computer
    resource or communication device.  66C. Punishment for identity theft.  66D. Punishment for
    cheating by personation by using computer resource.  66E. Punishment for violation of privacy.
    66F. Punishment for cyber terrorism.  67. Punishment for publishing or transmitting obscene
    material in electronic form.
  [4] source=Bharatiya_Nyaya_Sanhita  score=0.7302
    security, or anything which is signed or sealed, and which is capable of being converted into a
    valuable security, shall be punished with imprisonment of either description for a term which
    may extend to seven years, and shall also be liable to fine. 319. (1) A person is said to cheat
    by personation if he cheats by pretending to be some other person, or by knowingly substituting
    one person for or another, or representing that he or any other person is a person other than he
    or such other person really is. Explanation.—The offence is committed whether the individual
    personated is a real or imaginary person. Illustrations. (a) A cheats by pretending to be a
    certain rich banker of the same name. A cheats by personation. (b) A cheats by pretending to be
    B, a person who is deceased. A cheats by personation. (2) Whoever cheats by personation shall be
    punished with imprisonment of either description for a term which may extend to five years, or
    with fine, or with both.
  [5] source=Bharatiya_Nyaya_Sanhita  score=0.7160
    (2) Whoever cheats by personation shall be punished with imprisonment of either description for a
    term which may extend to five years, or with fine, or with both. Of  fraudulent deeds and
    dispositions of  property 320.Whoever dishonestly or fraudulently removes, conceals or delivers
    to any person, or transfers or causes to be transferred to any person, without adequate
    consideration, any property, intending thereby to prevent, or knowing it to be likely that he
    will thereby prevent, the distribution of that property according to law among his creditors or
    the creditors of any other person, shall be punished with imprisonment of either description for
    a term which shall not be less than six months but which may extend to two years, or with fine,
    or with both. 321. Whoever dishonestly or fraudulently prevents any debt or demand due to
    himself or to any other person from being made available according to law for payment of his
    debts

### Expected answer — sentence grounding checklist
- [ ] S / U — The punishment for cheating by personation using a computer resource is imprisonment for up to three years, and a fine that may extend to one lakh rupees.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [007] What does Section 66B say about receiving stolen computer resources?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

> ⚠️ retrieval failed: HTTP 500: Internal Server Error

---

## [008] What is the punishment for violation of privacy under the IT Act?
*domain:* `cyber`  ·  *expected_source:* `it_act_2000_updated`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=it_act_2000_updated  score=1.0000
    also be liable to fine which may extend to rupees one lakh.  66D. Punishment for cheating by
    personation by using computer resource.–Whoever, by means of  any communication device or
    compute r resource cheats by personation , shall be punished with  imprisonment of either
    description for a term which may extend to three years and shall also be liable to  fine which
    may extend to one lakh rupees.  66E. Punishment for violation of privacy.–Whoever, intentionally
    or knowingly captures, publishes  or transmits the image of a private area of any person without
    his or her consent, under circumstances  violating the privacy of that person, shall be punished
    with imprisonment which may extend to three years  or with fine not exceeding two lakh rupees,
    or with both.  Explanation.–For the purposes of this section–  (a) ―transmit‖ means to
    electronically send a visual image with the intent that it be viewed by a  person or persons;
  [2] source=it_act_2000_updated  score=0.7356
    computer resource.  69B. Power to authorise to monitor and collect traffic data or information
    through any computer  resource for cyber security.  70. Protected system.  70A. National nodal
    agency.  70B. Indian Computer Emergency Response Team to serve as national agency for incident
    response.  71. Penalty for misrepresentation.  72. Penalty for Breach of confidentiality and
    privacy.  72A. Punishment for disclosure of information in breach of lawful contract.  73.
    Penalty for publishing electronic signature Certificate false in certain particulars.  74.
    Publication for fraudulent purpose.  75. Act to apply for offence or contravention committed
    outside India.  76. Confiscation.  77. Compensation, penalties or confiscation not to interfere
    with other punishment.  77A. Compounding of offences.  77B. Offences with three years
    imprisonment to be bailable.  78. Power to investigate offences.  CHAPTER XII  INTERMEDIARIES
    NOT TO BE LIABLE IN CERTAIN CASES
  [3] source=it_act_2000_updated  score=0.7258
    imprisonment for a term which may extend to one year or with fine which may extend to one lakh
    rupees  or with both.  (8) No court shall take cognizance of any offence under this section,
    except on a complaint made by an  officer authorised in this behalf by the agency referred to in
    sub-section (1).]  71. Penalty for misrepresentation .–Whoever makes any misrepresentation to,
    or suppresses any  material fact from the Controller or the Certifying Authority for obtaining
    any licence or 1[electronic  signature] Certificate, as the case may be, shall be punished with
    imprisonment for a term which may  extend to two years, or with fine which may extend to one
    lakh rupees, or with both.  72. Penalty for Breach of confidentiality and privacy .–Save as
    otherwise provided in this Act or  any other law for the time being in force, if any person who,
    in pursuance of any of the powers conferred
  [4] source=it_act_2000_updated  score=0.6762
    any other law for the time being in force, if any person who, in pursuance of any of the powers
    conferred  under this Act, rules or regulations made thereunder, has secured access to any
    electronic record, book,  register, correspondence, information, document or other material
    without the consent of the person  concerned discloses such electronic record, book, register,
    correspondence, information, document or  other material to any other p erson shall be punished
    with imprisonment for a term which may extend to  two years, or with fine which may extend to
    one lakh rupees, or with both.  2[72A. Punishment for disclosure of information in breach of
    lawful contract .–Save as otherwise  provided in this Act or any other law for the time being in
    force, any person including an intermediary  who, while providing services under the terms of
    lawful contract, has secured access to any material
  [5] source=it_act_2000_updated  score=0.6382
    reasonable expectation that–  (i) he or she could disrobe in privacy, without being concerned that
    an image of his private  area was being captured; or  (ii) any part of his or her private area
    would not be visible to the public, regardless of whether  that person is in a public or private
    place.  66F. Punishment for cyber terrorism.–(1) Whoever,–  (A) with intent to threaten the
    unity, integrity, security or sovereignty of India or to strike terror in  the people or any
    section of the people by–  (i) denying or cause the denial of access to any person authoris ed
    to access computer  resource; or  (ii) attempting to penetrate or access a computer resource
    without authorisa tion or exceeding  authorised access; or  (iii) introducing or causing to
    introduce any computer contaminant,  and by means of such conduct causes or is likely to cause
    death or injuries to persons or damage to or

### Expected answer — sentence grounding checklist
- [ ] S / U — The punishment for violation of privacy under the IT Act (Section 66E) is imprisonment for a term that may extend to three years, or a fine not exceeding two lakh rupees, or both
- [ ] S / U — This applies to anyone who intentionally or knowingly captures, publishes, or transmits the image of a private area of any person without their consent, under circumstances that violate that person's privacy.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [009] What is the time limit to respond to an RTI application?
*domain:* `rti`  ·  *expected_source:* `RTI-2005_Nov_2025`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Motor-Vahicle-Act-1988-59  score=1.0000
    aggrieved by an order of a State Transport Authority or Regional Transport Authority, unless the
    application is made within thirty days from the date of the order:  Provided further that the
    Stat e Transport Appellate Tribunal may entertain the application after the  expiry of the said
    period of thirty days, if it is satisfied that the applicant was prevented by good and
    sufficient cause from making the application in time:  Provided also that the St ate Transport
    Appellate Tribunal shall not pass an order under this section  prejudicial to any person without
    giving him a reasonable opportunity of being heard.   91. Restriction of hours of work of
    drivers .—1[(1) The hours of work of any person engaged for  operating a transport vehicle shall
    be such as provided in the Motor Transport Workers Act, 1961 (27 of  1961).]  (2) A State
    Government may, by notification in the Official Gazette, grant such exemptions from the
  [2] source=RTI-2005_Nov_2025  score=0.8024
    officer, within one hundred days of the enactment of this Act, at each sub -divisional level or
    other sub - district level as a Central Assistant Public Information Officer or a State
    Assistant Public Information  Officer, as the case may be, to receive the applications for
    information or appeals under this Act for  forwarding the same forthwith to the Central Public
    Information Officer or the State Public Information  Officer or senior officer specified under
    sub -section ( 1) of section 19 or the Central Information  Commission or the State Information
    Commission, as the case may be:  Provided that where an application for information or appeal is
    given to a Central Assistant Public  Information Officer or a State Assistant Public Information
    Officer, as the case may be, a period of five  days shall be added in computing the period for
    response specified under sub-section (1) of section 7.
  [3] source=RTI-2005_Nov_2025  score=0.7541
    transfer:  Provided that the transfer of an application pursuant to this sub -section shall be made
    as soon as  practicable but in no case later than five days from the date of receipt of the
    application.  7. Disposal of request .—(1) Subject to the proviso to sub -section (2) of section
    5 or the proviso to  sub-section (3) of section 6, the Central Public Information Officer or
    State Public Information Officer, as  the case may be, on receipt of a request under section 6
    shall, as expeditiously as possible, and in any case  within thirty days of the receipt of the
    request, either provide the information on payment of such fee as  may be prescribed or reject
    the request for any of the reasons specified in sections 8 and 9:  Provided that where the
    information sought for concerns the life or liberty of a person, the same shall  be provided
    within forty-eight hours of the receipt of the request.
  [4] source=RTI-2005_Nov_2025  score=0.4891
    or the Central Information Commission or the State Information Commission, as the case may be;  (b)
    who has been refused access to any information requested under this Act;  (c) who has not been
    given a response to a request for information or access to information within  the time limit
    specified under this Act;  (d) who has been required to pay an amount of fee which he or she
    considers unreasonable;  (e) who believes that he or she has been given incomplete, misleading
    or false information under  this Act; and  (f) in respect of any other matter relating to
    requesting or obtaining access to records under this  Act.  (2) Where the Central Information
    Commission or State Information Commission, as the case may  be, is satisfied that there are
    reasonable grounds to inquire into the matter, it may initiate an inquiry in  respect thereof.
    (3) The Central Information Commission or State Information Commission, as the case may be,
    shall,
  [5] source=RTI-2005_Nov_2025  score=0.4611
    Provided that where the information sought for concerns the life or liberty of a person, the same
    shall  be provided within forty-eight hours of the receipt of the request.  (2) If the Central
    Public Information Officer or State Public Information Officer, as the case may be,  fails to
    give decision on the request for information within the period specified under sub -section (1),
    the  Central Public Information Officer or State Public Information Officer, as the case may be,
    shall be  deemed to have refused the request.  (3) Where a decision is taken to provide the
    information on payment of any further fee representing  the cost of providing the information,
    the Central Public Information Officer or State Public Information  Officer, as the case may be,
    shall send an intimation to the person making the request, giving—  (a) the details of further
    fees representing the cost of providing the information as determined by

### Expected answer — sentence grounding checklist
- [ ] S / U — The time limit to respond to an RTI application is generally within thirty days of receiving the request
- [ ] S / U — However, if the information requested concerns the life or liberty of a person, it must be provided within forty-eight hours
- [ ] S / U — If there is a delay in response, the Public Information Officer is deemed to have refused the request.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [010] What are the penalties for a Public Information Officer who refuses to provide information?
*domain:* `rti`  ·  *expected_source:* `RTI-2005_Nov_2025`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=RTI-2005_Nov_2025  score=1.0000
    reasonable cause, refused to receive an application for information or has not furnished information
    within the time specified under sub -section ( 1) of section 7 or malafidely denied the request
    for  information or knowingly given incorrect, incomplete or misleading information or destroyed
    information  which was the subject of the request or obstructed in any manner in furnishing the
    information, it shall 19    impose a penalty of two hundred and fifty rupees each day till
    application is received or information is  furnished, so however, the total amount of such
    penalty shall not exceed twenty-five thousand rupees:  Provided that the Central Public
    Information Officer or the State Public Information Officer, as the  case may be, shall be given
    a reasonable opportunity of being heard before any penalty is imposed on  him:  Provided further
    that the burden of proving that he acted reasonably and diligently shall be on the
  [2] source=RTI-2005_Nov_2025  score=0.8450
    (b) require the public authority to compensate the complainant for any loss or other detriment
    suffered;  (c) impose any of the penalties provided under this Act;  (d) reject the application.
    (9) The Central Information Commission or State Information Commission, as the case may be,
    shall  give notice of its decision, including any right of appeal, to the complainant and the
    public authority.  (10) The Central Information Commission or State Information Commission, as
    the case may be,  shall decide the appeal in accordance with such procedure as may be
    prescribed.  20. Penalties.—(1)Where the Central Information Commission or the State Information
    Commission,  as the case may be, at the time of deciding any complaint or appeal is of the
    opinion that the Central  Public Information Officer or the State Public Information Officer, as
    the case may be, has, without any  reasonable cause, refused to receive an application for
    information or has not furnished information
  [3] source=RTI-2005_Nov_2025  score=0.8147
    Provided that where the information sought for concerns the life or liberty of a person, the same
    shall  be provided within forty-eight hours of the receipt of the request.  (2) If the Central
    Public Information Officer or State Public Information Officer, as the case may be,  fails to
    give decision on the request for information within the period specified under sub -section (1),
    the  Central Public Information Officer or State Public Information Officer, as the case may be,
    shall be  deemed to have refused the request.  (3) Where a decision is taken to provide the
    information on payment of any further fee representing  the cost of providing the information,
    the Central Public Information Officer or State Public Information  Officer, as the case may be,
    shall send an intimation to the person making the request, giving—  (a) the details of further
    fees representing the cost of providing the information as determined by
  [4] source=RTI-2005_Nov_2025  score=0.7032
    him:  Provided further that the burden of proving that he acted reasonably and diligently shall be
    on the  Central Public Information Officer or the State Public Information Officer, as the case
    may be.  (2) Where the Central Information Commission or the State Information Commission, as
    the case  may be, at the time of deciding any complaint or appeal is of the opinion that the
    Central Public  Information Officer or the State Public Information Officer, as the case may be,
    has, without any  reasonable cause and persistently, failed to receive an application for
    information or has not furnished  information within the time specified under sub -section (1)
    of section 7 or malafidely denied the request  for information or knowingly given incorrect,
    incomplete or misleading information or destroyed  information which was the subject of the
    request or obstructed in any manner in furnishing the
  [5] source=Labour-Act  score=0.6626
    has the effect of imposing on the employer or the other person a financial liability  exceeding Rs
    1000/-, or  (3) By any person directed to pay a penalty.      Penalties   (1) Whoever being
    required under this Act to maintain any records or registers or to furnish  any information or
    return-  (a) Fails to maintain such register or record; or  (b) Willfully refuses or without
    lawful excuse neglects  to furnish such information or return;  or  (c) Willfully furnishes or
    causes to be furnished any information or return which he knows to  be false; or  (d) refuses to
    answer or willfully gives a false answer to any question necessary for obtaining  any
    information required to be furnished under this Act, 113    shall, for each such offence, be
    punishable with fine which shall not be less than Rs 1500/ - one but which may extend to Rs
    7500/-.    (2) Whoever-  (a) Willfully obstructs an Inspector in the discharge of his duties
    under this Act; or

### Expected answer — sentence grounding checklist
- [ ] S / U — The penalties for a Public Information Officer (PIO) who refuses to provide information include:
- [ ] S / U — 1
- [ ] S / U — A penalty of **Rs
- [ ] S / U — 250** for each day of delay in furnishing information, up to a maximum of **Rs
- [ ] S / U — 25,000**.
- [ ] S / U — 2
- [ ] S / U — If the PIO refuses to receive an application or does not provide information without reasonable cause, they may be subject to the same daily penalty and maximum limit.
- [ ] S / U — 3
- [ ] S / U — The PIO must be given a reasonable opportunity to present their case before any penalty is imposed.
- [ ] S / U — 4
- [ ] S / U — The burden of proof lies with the PIO to demonstrate that they acted reasonably and diligently in their duties.
- [ ] S / U — Additionally, the concerned commission may require the public authority to compensate the complainant for any losses suffered.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [011] Who can file an RTI application?
*domain:* `rti`  ·  *expected_source:* `RTI-2005_Nov_2025`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
    An appeal can be made against an order dismissing either wholly or part of an application made. The
    appeal can be made within 30 days of the date on which the order or direction was made . The
    appeal has to be made before the court of small causes or the District Court by following
    persons:  (1) By an employed person or any legal practitioner or any official of a registered
    trade union  authorized in writing to act on his behalf or any Inspector  under this Act, if the
    total  amount of wages claimed to have been withheld from the employed person exceeds Rs  20/-
    or from the unpaid group to which the employed person belongs or belonged exceeds  Rs 50, or
    (2) By the employer or other person responsible for  the payment of wages, if the total sum
    directed to be paid by way of wages and compensation exceeds Rs 300/ - or such direction  has
    the effect of imposing on the employer or the other person a financial liability  exceeding Rs
    1000/-, or
  [2] source=Labour-Act  score=0.9355
    certain rights and privileges under the Act. Minimum seven workers of an establishment (or seven
    employers) can form a trade union and apply to the Registrar for it registration.    The
    application for registration should be in the prescribed form and accompanied by the  prescribed
    fee, a copy of the rules of the union signed by at least 7 members, and a  statement containing
    (a) the names, addresses and occupations of the members making the application,   (b) the name
    of the trade union and the addresses of its head office, and   (c) the titles, names, ages,
    addresses and occupations of its office bearers.   If the unio n has been in existence for more
    than a year, then a statement of its assets and  liabilities in the prescribed form should be
    submitted along with the application.   The registrar may call for further information for
    satisfying himself that the application i s  complete and is in accordance with the provisions,
    and that the proposed name does not  resemble
  [3] source=RTI-2005_Nov_2025  score=0.7431
    it shall be the duty of the Central Information Commission or State Information Commission, as the
    case  may be, to receive and inquire into a complaint from any person,—    1. Subs. by Act 24 of
    2019, s. 3, for sub-section (5), (w.e.f. 24-10-2019). 17    (a) who has been unable to submit a
    request to a Central Public Information Officer or State  Public Information Officer, as the
    case may be, either by reason that no such officer has been  appointed under this Act, or
    because the Central Assistant Public Information Officer or State  Assistant Public Information
    Officer, as the case may be, has refused to accept his or her application  for information or
    appeal under this Act for forwarding the same to the Central Public Information  Officer or
    State Public Information Officer or senior officer specified in sub -section (1) of section 19
    or the Central Information Commission or the State Information Commission, as the case may be;
  [4] source=Labour-Act  score=0.5838
    wages by the person presenting the application; or  (b) That in any case in which compensation is
    directed to be paid under the applicant ought not to  have been compelled to seek redress under
    this section, the authority may direct that a penalty not  exceeding Rs 375/- to be paid to the
    State Government by the employer or other person responsible  for the payment of wages.   112
    A single application can also be made by the unpaid grou p of the employed persons. Employed
    persons can be said to belong to Unpaid Group:  (1) If they are borne by the same establishment,
    and  a. If deductions have been made from their wages for the same wage period in  contravention
    of the Act, or  b. Their wages for the s ame wage period have remained unpaid after the day
    fixed by  the Act.    An appeal can be made against an order dismissing either wholly or part of
    an application made. The  appeal can be made within 30 days of the date on which the order or
    direction was made . The
  [5] source=Motor-Vahicle-Act-1988-59  score=0.5328
    subject to such restrictions, limitations and conditions as may be prescribed by the said rules.
    69. General provision as to applications for permits .—(1) Every application for a permit shall
    be  made to the Regional Transport Authority of the region in which it is proposed to use the
    vehicle or  vehicles:  Provided that if it is proposed to use the vehi cle or vehicles in two or
    more regions lying within the  same State, the application shall be made to the Regional
    Transport Authority of the region in which the  major portion of the proposed route or area
    lies, and in case the portion of the proposed route  or area in  each of the regions is
    approximately equal, to the Regional Transport Authority of the region in which it  is proposed
    to keep the vehicle or vehicles:  Provided further that if it is proposed to use the vehicle or
    vehicles in two or more regions  lying in  different States, the application shall be made to
    the Regional Transport Authority of the region in which

### Expected answer — sentence grounding checklist
- [ ] S / U — Any person can file an RTI application
- [ ] S / U — This includes individuals who have been unable to submit a request due to the absence of a designated Central or State Public Information Officer or those whose applications were refused.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [012] What information is exempt from disclosure under the RTI Act?
*domain:* `rti`  ·  *expected_source:* `RTI-2005_Nov_2025`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=RTI-2005_Nov_2025  score=1.0000
    Act, access may be provided to that part of the record which does not contain any information which
    is  exempt from disclosure under this Act and which can reasonably be severed from any part th
    at contains  exempt information.  (2) Where access is granted to a part of the record under sub
    -section ( 1), the Central Public  Information Officer or State Public Information Officer, as
    the case may be, shall give a not ice to the  applicant, informing—  (a) that only part of the
    record requested, after severance of the record containing information  which is exempt from
    disclosure, is being provided;  (b) the reasons for the decision, including any findings on any
    material question of fact, referring  to the material on which those findings were based;  (c)
    the name and designation of the person giving the decision;  (d) the details of the fees
    calculated by him or her and the amount of fee which the applic ant is  required to deposit; and
  [2] source=RTI-2005_Nov_2025  score=0.9354
    Provided further that those matters which come under the exemptions specified in this section  shall
    not be disclosed;  1[(j) information which relates to personal information;]  (2)
    Notwithstanding anything in  the Official Secrets Act, 1923 (19 of 1923) nor any of the
    exemptions permissible in accordance with sub -section ( 1), a public authority may allow access
    to  information, if public interest in disclosure outweighs the harm to the protected interests.
    (3) Subject to the provisions of clauses ( a), (c) and (i) of sub-section (1), any information
    relating to  any occurrence, event or matter which has taken place, occurred or happened twenty
    years before the date  on which any request is made under section 6 shall be provided to any
    person making a request under that  section:  Provided that where any question arises as to the
    date from which the said period of twenty years has
  [3] source=RTI-2005_Nov_2025  score=0.8661
    request,—  (i) the reasons for such rejection;  (ii) the period within which an appeal against such
    rejection may be preferred; and  (iii) the particulars of the appellate authority.  (9) An
    information shall ordinarily be provided in the form in which it is sought unless it would
    disproportionately divert the resources of the public authority or would be detrimental to the
    safety or  preservation of the record in question.  8. Exemption from disclosure of
    information.—(1) Notwithstanding anything contained in this Act,  there shall be no obligation
    to give any citizen,—  (a) information, disclosure of which would prejudicially affect the
    sovereignty and integrity of  India, the security, strategic, scientific or economic interests
    of the State, relation with foreign State or  lead to incitement of an offence;  (b) information
    which has been expressly forbidden to be published by any court of law or  tribunal or the
    disclosure of which may constitute contempt of court;
  [4] source=RTI-2005_Nov_2025  score=0.7921
    (f) information received in confidence from foreign Government;  (g) information, the disclosure of
    which would endanger the life or physical safety of any person  or identify the source of
    information or assistance given in confidence for law enforcement or security  purposes;  (h)
    information which would impede the process of investigation or apprehension or prosecution  of
    offenders;  (i) cabinet papers including records of deliberations of the Council of Ministers,
    Secretaries and  other officers: 11    Provided that the decisions of Council of Ministers, the
    reasons thereof, and the material on the  basis of which the decisions were taken shall be made
    public after the decision has been taken, and  the matter is complete, or over:  Provided
    further that those matters which come under the exemptions specified in this section  shall not
    be disclosed;  1[(j) information which relates to personal information;]
  [5] source=RTI-2005_Nov_2025  score=0.7507
    section:  Provided that where any question arises as to the date from which the said period of
    twenty years has  to be computed, the decision of the Central Government shall be final, subject
    to the usual appeals  provided for in this Act.  9. Grounds for reject ion to access in certain
    cases .—Without prejudice to the provisions of               section 8, a Central Public
    Information Officer or a State Public Information Officer, as the case may be,  may reject a
    request for information where such a request for providing access would involve an  infringement
    of copyright subsisting in a person other than the State.  10. Severability.—(1) Where a request
    for access to information is rejected on the ground that it is in  relation to information which
    is exempt from disclosure, then, notwithstanding anything contained in this  Act, access may be
    provided to that part of the record which does not contain any information which is

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the RTI Act, the following information is exempt from disclosure:
- [ ] S / U — 1
- [ ] S / U — Information that prejudicially affects the sovereignty and integrity of India, its security, strategic, scientific, or economic interests, or relations with foreign states, or may incite an offense.
- [ ] S / U — 2
- [ ] S / U — Information that has been expressly forbidden to be published by any court or tribunal, or that could constitute contempt of court.
- [ ] S / U — 3
- [ ] S / U — Information received in confidence from a foreign government.
- [ ] S / U — 4
- [ ] S / U — Information whose disclosure would endanger the life or physical safety of any person or would reveal the source of information provided in confidence for law enforcement or security purposes.
- [ ] S / U — 5
- [ ] S / U — Information that would impede the process of investigation or prosecution of offenders.
- [ ] S / U — 6
- [ ] S / U — Cabinet papers, including records of deliberations of the Council of Ministers and other officers, though decisions of the Council of Ministers may be made public once finalized.
- [ ] S / U — 7
- [ ] S / U — Personal information that does not pertain to the public interest.
- [ ] S / U — These exemptions reflect the balance between the right to information and the protection of certain sensitive interests.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [013] What is the procedure to appeal under the RTI Act?
*domain:* `rti`  ·  *expected_source:* `RTI-2005_Nov_2025`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=protection_of_women_from_domestic_violence_act,_2005  score=1.0000
    (c) the cause of action has arisen,  shall be the competent court to grant a protection order and
    other orders under this Act and to try offences under this Act.  (2) Any order made under this
    Act shall be enforceable throughout India.  28. Procedure.—(1) Save as otherwise provided in
    this Act, all proceedings under sections 12,18,       19, 20, 21, 22 and 23 and offences under
    section 31 shall be governed by the provisions of  the Code of  Criminal Procedure, 1973 (2 of
    1974).  (2) Nothing in sub-section (1) shall prevent the court from laying down its own
    procedure for disposal  of an application under section 12 or under sub-section (2) of section
    23. 11    29. Appeal.—There shall lie an appeal to the Court of Session within thirty days f rom
    the date  on  which the order made by the Magistrate is served on the aggrieved person or the
    respondent,  as the case  may be, whichever is later.  CHAPTER V  MISCELLANEOUS
  [2] source=it_act_2000_updated  score=0.9692
    (5) The 1[Appellate Tribunal] shall send a copy of every order made by it to the parties to the
    appeal  and to the concerned Controller or adjudicating officer.  (6) The appeal filed before
    the 1[Appellate Tribunal] under sub-section (1) shall be dealt with by it as  expeditiously as
    possible and endeavour shall be made by it to dispose of the appeal finally within six  months
    from the date of receipt of the appeal.  58. Procedure and powers of the Appellate Tribunal
    ].–(1) The 1[Appellate Tribunal] shall not be  bound by the procedure laid down by the Code of
    Civil Procedure, 1908 (5 of 1908) but shall be guided  by the principles of natural justice and,
    subject to the other provisions of this Act and of any rules, the  1[Appellate Tribunal] shall
    have powers to regulate its own procedure including the place at which it shall  have its
    sittings.  (2) The 1[Appellate Tribunal] shall have, for the purposes of discharging its
    functions under this Act,
  [3] source=Labour-Act  score=0.9632
    An appeal can be made against an order dismissing either wholly or part of an application made. The
    appeal can be made within 30 days of the date on which the order or direction was made . The
    appeal has to be made before the court of small causes or the District Court by following
    persons:  (1) By an employed person or any legal practitioner or any official of a registered
    trade union  authorized in writing to act on his behalf or any Inspector  under this Act, if the
    total  amount of wages claimed to have been withheld from the employed person exceeds Rs  20/-
    or from the unpaid group to which the employed person belongs or belonged exceeds  Rs 50, or
    (2) By the employer or other person responsible for  the payment of wages, if the total sum
    directed to be paid by way of wages and compensation exceeds Rs 300/ - or such direction  has
    the effect of imposing on the employer or the other person a financial liability  exceeding Rs
    1000/-, or
  [4] source=the_maternity_benefit_act,_1961  score=0.9631
    (i) the authority to which an appeal shall lie agai nst the decision of the Inspector  under section
    17; the form and manner in which such  appeal may be made  and the procedure to be followed in
    disposal thereof;  (j) the form and manner in which complaints may be made to Inspectors under
    sub-section (1) of section 17 and the procedure to be followed by them when  making inquiries or
    causing inquiries to be made un der sub-section (2) of that  section;  (k) any other matter
    which is to be, or may be pres cribed.  1[(3) Every rule made by the Central Government unde r
    this section shall be laid  as soon as may be after it is made, before each Hou se of Parliament
    while it  is in session for a total period of thirty days whi ch may be comprised in one
    session 1[or in two or more successive sessions and  if, before the expiry of  the session
    immediately following the session or th e successive sessions,  aforesaid] both Houses agree in
    making any modifica tion in the rule or both
  [5] source=RTI-2005_Nov_2025  score=0.9240
    (b) require the public authority to compensate the complainant for any loss or other detriment
    suffered;  (c) impose any of the penalties provided under this Act;  (d) reject the application.
    (9) The Central Information Commission or State Information Commission, as the case may be,
    shall  give notice of its decision, including any right of appeal, to the complainant and the
    public authority.  (10) The Central Information Commission or State Information Commission, as
    the case may be,  shall decide the appeal in accordance with such procedure as may be
    prescribed.  20. Penalties.—(1)Where the Central Information Commission or the State Information
    Commission,  as the case may be, at the time of deciding any complaint or appeal is of the
    opinion that the Central  Public Information Officer or the State Public Information Officer, as
    the case may be, has, without any  reasonable cause, refused to receive an application for
    information or has not furnished information

### Expected answer — sentence grounding checklist
- [ ] S / U — To appeal under the RTI Act, follow these steps:
- [ ] S / U — 1
- [ ] S / U — **File the Appeal**: If you are dissatisfied with the response of the public authority, you can file an appeal before the Central Information Commission (CIC) or State Information Commission (SIC) depending on the authority.
- [ ] S / U — 2
- [ ] S / U — **Timeline**: You must file your appeal within 30 days from the date you received a decision or response from the public authority.
- [ ] S / U — 3
- [ ] S / U — **Notice of Decision**: Both the complainant and the public authority will receive a notice of the decision regarding the appeal.
- [ ] S / U — 4
- [ ] S / U — **Procedure**: The CIC or SIC will decide the appeal according to the prescribed procedures, which are laid down in the RTI Act.
- [ ] S / U — 5
- [ ] S / U — **Outcome**: The Commission may direct the public authority to comply with the RTI Act, provide the requested information, grant compensation, impose penalties, or reject the application.
- [ ] S / U — Ensure that you prepare and submit your appeal clearly, stating the reasons for your dissatisfaction with the initial response.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [014] What is the maximum penalty under the RTI Act?
*domain:* `rti`  ·  *expected_source:* `RTI-2005_Nov_2025`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
    in direct furtherance or support of any illegal  strike or lock-out   Imprisonment for 6 month and /
    or  fine upto Rs. 1000.      Sec.29  Breach of settlement or award binding under  the act
    Imprisonment for 6 month and / or  fine + an additional fine of Rs. 200 per  day if breach
    continues after  conviction.      Sec.30  Disclosing confidential information in  contravention
    of the provisions of Section 21   Imprisonment for 6 month and / or  fine Rs. 1000.
    Sec.30-A  Closing down any undertaking without  complying with the provisions of Section 25 -
    FFA   Imprisonment for 6 month and / or  fine Rs. 5000.     Sec.31(1)  Contravention of Section
    33 - Service  conditions remaining unchanged during  pendency of proceedings   Imprisonment for
    6 month and / or  fine Rs. 1000.     Sec.31(2)  Contravening any other provision whe re
    specific penalty is not provided for.   Fine upto Rs. 100.          Authorities Empowered By
    This Act   Name of Authority  Duties  Powers   Central
  [2] source=RTI-2005_Nov_2025  score=0.9379
    reasonable cause, refused to receive an application for information or has not furnished information
    within the time specified under sub -section ( 1) of section 7 or malafidely denied the request
    for  information or knowingly given incorrect, incomplete or misleading information or destroyed
    information  which was the subject of the request or obstructed in any manner in furnishing the
    information, it shall 19    impose a penalty of two hundred and fifty rupees each day till
    application is received or information is  furnished, so however, the total amount of such
    penalty shall not exceed twenty-five thousand rupees:  Provided that the Central Public
    Information Officer or the State Public Information Officer, as the  case may be, shall be given
    a reasonable opportunity of being heard before any penalty is imposed on  him:  Provided further
    that the burden of proving that he acted reasonably and diligently shall be on the
  [3] source=CPA-2019  score=0.9296
    which, such user or consumer, ought to have known, taking into account the characteristics of such
    product. CHAPTER VII O FFENCES AND PENALTIES 88. Whoever, fails to comply with any direction of
    the Central Authority under sections 20 and 21, shall be punished with imprisonment for a term
    which may extend to six months or with fine which may extend to twenty lakh rupees, or with
    both. 89. Any manufacturer or service provider who causes a false or misleading advertisement to
    be made which is prejudicial to the interest of consumers shall be punished with imprisonment
    for a term which may extend to two years and with fine which may extend to ten lakh rupees; and
    for every subsequent offence, be punished with imprisonment for a term which may extend to five
    years and with fine which may extend to fifty lakh rupees. 90. (1) Whoever, by himself or by any
    other person on his behalf, manufactures for
  [4] source=it_act_2000_updated  score=0.8903
    each such failure;  (b) file any return or furnish any information, books or other documents within
    the time specified  therefor in the regulations fails to file re turn or furnish the same within
    the time specified therefor in  the regulations, he shall be liable to a penalty not exceeding
    five thousand rupees for every day during  which such failure continues;  (c) maintain books of
    account or records, fails to maintain the same, he shall be liable to a penalty  not exceeding
    ten thousand rupees for every day during which the failure continues.  45. Residuary
    penalty.–Whoever contravenes any rules or regulations made under this Act, for the
    contravention of which no penalty has been separately provided, shall be liable to pay a
    compensation not  exceeding twenty -five thousand rupees to the person affected by such
    contravention or a penalty not  exceeding twenty-five thousand rupees.  46. Power to adjudicate
    .–(1) For the purpose of adjudging under this Chapter whether any person
  [5] source=it_act_2000_updated  score=0.7909
    persons who are likely, having r egard to all relevant circumstances, to read, see or hear the
    matter  contained or embodied in it, shall be punished on first conviction with imprisonment of
    either description  for a term which may extend to three years and with fine which may extend to
    fiv e lakh rupees and in the  event of second or subsequent conviction with imprisonment of
    either description for a term which may  extend to five years and also with fine which may
    extend to ten lakh rupees.  67A. Punishment for publishing or transmitting of material
    containing sexually explicit act, etc.,  in electronic form .–Whoever publishes or transmits or
    causes to be published or transmitted in the  electronic form any material which contains
    sexually explicit act or conduct shall be punished on first  conviction with imprisonment of
    either description for a term which may extend to five years and with

### Expected answer — sentence grounding checklist
- [ ] S / U — The maximum penalty under the RTI Act is ₹25,000
- [ ] S / U — This penalty can be imposed for failing to receive an application for information, not furnishing information in a timely manner, malafidely denying information, providing incorrect or misleading information, or obstructing the furnishing of information
- [ ] S / U — Penalties may accumulate at a rate of ₹250 per day until the application is processed or information is provided, but cannot exceed ₹25,000 in total.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [015] What is the full form of POCSO and what does it protect against?
*domain:* `pocso`  ·  *expected_source:* `POCSO`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=protection_of_women_from_domestic_violence_act,_2005  score=1.0000
    proceeding shall lie against the Protection Officer unless a complaint is filed with the previous
    sanction of  the State Government or an officer authorised by it in this behalf.  35. Protection
    of action taken in good faith .—No suit, prosecution or other legal proceeding shall   lie
    against the Protection Officer for any damage caused or likely to be caused by anything  which
    is in  good faith done or intended to be done under this Act or any rule or order made
    thereunder.  36. Act not in derogation of any other law. —The provisions of this Act shall be in
    addition to,  and  not in derogation of the provisions of any other law, for the time being in
    force.  37. Power of Ce ntral Government to make rules. —(1) The Central Government may, by
    notification, make rules for carrying out the provisions of this Act.  (2) In particular, and
    without prejudice to the generality of the foregoing power, such rules may   provide for all or
    any of the following matters, namely:—
  [2] source=Labour-Act  score=0.9626
    The Occupational Safety and Health Act, signed into law in 1970 by President Richard Nixon,  creates
    specific standards for workplace safety. The Act also provides for protection for
    "whistleblowers" who complain to governmental authorities about uns afe conditions while
    allowing workers the right to refuse to work under unsafe conditions in certain  circumstances.
    The Act allows states to take over the administration of OSHA in their  jurisdictions, so long
    as they adopt state laws at least as protectiv e of workers' rights as  under federal law.   The
    Immigration Reform and Control Act of 1986 provides narrow prohibitions against  certain types
    of employment discrimination based on immigration status.  The Worker Adjustment and Retraining
    Notification Act, b etter known by its acronym as the  WARN Act, requires private sector
    employers to give sixty days' notice of large -scale layoffs  and plant closures; it allows a
    number of exceptions for unforeseen emergencies and other
  [3] source=protection_of_women_from_domestic_violence_act,_2005  score=0.6125
    (2) In particular, and without prejudice to the generality of the foregoing power, such rules may
    provide for all or any of the following matters, namely:—  (a) the qualifications and experience
    which a Protection Officer shall possess under                               sub-section (2) of
    section 8;  (b) the terms and conditions of service of the Protection Officers and the other
    officers   subordinate to him, under sub-section (3) of section 8;  (c) the form and manner in
    which a domestic incident re port may be made under clause ( b) of  sub-section (1) of section
    9;  (d) the form and the manner in which an application for protection order may be made to the
    Magistrate under clause (c) of sub-section (1) of section 9; 12    (e) the form in which a
    complaint is to be filed under clause (d) of sub-section (1) of section 9;  (f) the other duties
    to be performed by the Protection Officer under clause (i) of sub-section (1) of  section 9;
  [4] source=protection_of_women_from_domestic_violence_act,_2005  score=0.4401
    such number of Protection Officers in each district as it may consider necessary and shall also
    notify the  area or areas within which a Protection Officer shall exercise the powers and
    perform the duties conferred  on him by or under this Act. 6    (2) The Protection Officers
    shall as far as possible be women and shall possess such  qualifications  and experience as may
    be prescribed.  (3) The terms and conditions of service of the Protection Officer and the other
    officers  subordinate to  him shall be such as may be prescribed.  9. Duties and functions of
    Protection Officers.—(1) It shall be the duty of the Protection Officer—  (a) to assist the
    Magistrate in the discharge of his functions under this Act;  (b) to make a domestic incident
    report to the Magistrate, in such form and in such manner as  may  be prescribed, upon receipt
    of a complaint of domestic violence and forward copies  thereof to the
  [5] source=POCSO-2012-32  score=0.3770
    1    THE PROTECTION OF CHILDREN FROM SEXUAL OFFENCES ACT, 2012  __________________  ARRANGEMENT OF
    SECTIONS  Last update- 28-02-2023  ____________________  CHAPTER I  PRELIMINARY  SECTIONS  1.
    Short title, extent and commencement.  2. Definitions.    CHAPTER II  SEXUAL OFFENCES AGAINST
    CHILDREN  A.—PENETRATIVE SEXUAL ASSAULT AND PUNISHMENT THEREFOR  3. Penetrative sexual assault.
    4. Punishment for penetrative sexual assault.  B.—AGGRAVATED PENETRATIVE SEXUAL ASSAULT AND
    PUNISHMENT THEREFOR  5. Aggravated penetrative sexual assault.  6. Punishment for aggravated
    penetrative sexual assault.  C.—SEXUAL ASSAULT AND PUNISHMENT THEREFOR  7. Sexual assault.  8.
    Punishment for sexual assault.  D.—AGGRAVATED SEXUAL ASSAULT AND PUNISHMENT THEREFOR  9.
    Aggravated sexual assault.  10. Punishment for aggravated sexual assault.  E.—SEXUAL HARASSMENT
    AND PUNISHMENT THEREFOR  11. Sexual harassment.  12. Punishment for sexual harassment.
    CHAPTER III

### Expected answer — sentence grounding checklist
- [ ] S / U — The full form of POCSO is the "Protection of Children from Sexual Offences." It protects against sexual offenses committed against children, including various forms of sexual assault, penetrative sexual assault, and sexual harassment.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [016] What are the penalties for penetrative sexual assault under POCSO?
*domain:* `pocso`  ·  *expected_source:* `POCSO`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=POCSO-2012-32  score=1.0000
    having committed any offence under this Act or any sexual offence punishable under any other law for
    the time being in force; or  (u) whoever  commits penetrative sexual assault on a child and
    makes the child to strip or parade  naked in public,  is said to commit aggravated penetrative
    sexual assault.  2[6. Punishment for aggravated penetrative sexual assault .—(1) Whoever commits
    aggravated  penetrative sexual assault shall be punished with rigorous imprisonment for a term
    which shall not be less  than twenty years, but which may extend to imprisonment for life, which
    shall mean imprisonment for the  remainder of natural life of that person and shall also be
    liable to fine, or with death.  (2) The fine imposed under sub-section (1) shall be just and
    reasonable and paid to the victim to meet  the medical expenses and rehabilitation of such
    victim.]  C. —SEXUAL ASSAULT AND PUNISHMENT THEREFOR
  [2] source=POCSO-2012-32  score=0.8449
    years] but which may extend to imprisonment for life, and shall also be liable to fine.   5[(2)
    Whoever commi ts penetrative sexual assault on a child below sixteen years of age shall be
    punished with imprisonment for a term which shall not be less than twenty years, but which may
    extend  to imprisonment for life, which shall mean imprisonment for the remainder of natural
    life of that person  and shall also be liable to fine.  (3) The fine imposed under sub-section
    (1) shall be just and reasonable and paid to the victim to meet  the medical expenses and
    rehabilitation of such victim.]
    1. Ins. by Act 25 of 2019, s. 2 (w.e.f. 16-08-2019).  2. Subs. by s. 2, ibid., for “the Juvenile
    Justice (Care and Protection of Children) Act, 2000 (56 of 2000)” (w.e.f. 16-08-2019).  3.
    Section 4 renumbered as section 4(1) thereof by s. 3, ibid (w.e.f. 16-08-2019).  4. Subs. by s.
    3, ibid., for “seven years” (w.e.f. 16-08-2019).
  [3] source=POCSO-2012-32  score=0.7370
    makes the child to do so with him or any other person; or  (b) he inserts, to any extent, any object
    or a part of the body, not being the penis, into the vagina,  the urethra or anus of the child
    or makes the child to do so with him or any other person; or  (c) he manipulates any part of the
    body of the child so as to cause penetration into the vagina,  urethra, anus or any part  of
    body of the child or makes the child to  do so with him or any other  person; or  (d) he applies
    his mouth to the penis, vagina, anus, urethra of the child or makes the child to do so  to such
    person or any other person.  4. Punishment for penetrative sexual assault. —3[(1)] Whoever
    commits penetrative sexual assault  shall be punished with imprisonment of either description
    for a term which shall not be less than 4[ten  years] but which may extend to imprisonment for
    life, and shall also be liable to fine.   5[(2) Whoever commi ts penetrative sexual assault on a
    child below sixteen years of age shall be
  [4] source=POCSO-2012-32  score=0.6538
    direct anyone to administer, help in getting administered any drug or hormone or any chemical
    substance,  to a child with the intent that such child attains early sexual maturity,]  is said
    to commit aggravated sexual assault.  10. Punishment for aggravated sexual assault.—Whoever,
    commits aggravated sexual assault shall  be punished with imprisonment of either description for
    a term  which shall not be less than five years but  which may extend to seven years, and shall
    also be liable to fine.  E.—SEXUAL HARASSMENT AND PUNISHMENT THEREFOR  11. Sexual harassment. —A
    person is said to commit sexual harassment upon a child when such  person with sexual intent,—
    (i) utters any word or makes any sound, or makes any gesture or exhibits any object or part of
    body with the  intention that such word or sound shall be heard, or such gesture or object or
    part of  body shall be seen by the child; or
  [5] source=POCSO-2012-32  score=0.6369
    the medical expenses and rehabilitation of such victim.]  C. —SEXUAL ASSAULT AND PUNISHMENT THEREFOR
    7. Sexual assault.—Whoever, with sexual intent touches the vagina, penis, anus or breast of the
    child  or makes the child touch the vagina, penis, anus or breast of such person or any other
    person, or does any  other act with sexual intent which involves  physical contact without
    penetration is said to commit sexual  assault.  8. Punishment for sexual assault. —Whoever,
    commits sexual assault,  shall be punished with  imprisonment of either  description for a term
    which shall not be less than three years but which may  extend to five years, and shall also be
    liable to fine.  D. —AGGRAVATED SEXUAL ASSAULT AND PUNISHMENT THEREFOR  9. Aggravated sexual
    assault.—(a) Whoever, being a police officer, commits sexual assault on a  child—  (i) within
    the limits of the police station or premises where he is appointed; or

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the POCSO Act, the penalties for penetrative sexual assault are as follows:
- [ ] S / U — 1
- [ ] S / U — **Penetrative Sexual Assault**:
- [ ] S / U — - The punishment is imprisonment for a term of no less than **ten years** and may extend to **life imprisonment**
- [ ] S / U — The individual may also be liable to a fine.
- [ ] S / U — 2
- [ ] S / U — **Aggravated Penetrative Sexual Assault**:
- [ ] S / U — - If the assault involves making the child strip or parade naked in public, the punishment is more severe: a minimum of **twenty years** of rigorous imprisonment, which may also extend to **life imprisonment** (meaning imprisonment for the remainder of the natural life of the individual), and can include the death penalty
- [ ] S / U — Additionally, a fine will be imposed, which must be just and reasonable, to assist the victim with medical expenses and rehabilitation.
- [ ] S / U — 3
- [ ] S / U — **Specific Case**: If the offence is committed against a child below sixteen years of age, the punishment remains the same as for aggravated penetrative sexual assault, emphasizing the seriousness of the crime against younger victims.
- [ ] S / U — In all cases, the fines are intended to support the victim's medical and rehabilitation needs.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [017] What is the age of a child as defined under POCSO?
*domain:* `pocso`  ·  *expected_source:* `POCSO`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
    India and also the UN Convention on the Rights of the Child. The Child is defined as a person in the
    0  to 18 years age group.  The Commission visualises a rights -based perspective flowing into
    National Policies and  Programmes, along with nuanced responses at the State, District and Block
    levels, taking care of  specificities and strengths of each region. In order to touch every
    child, it seeks a deeper penetration  to communities and households and expects that the ground
    experiences inform the support the  field receives from all the authorities at the higher level.
    Thus the Commission sees an indispensable  role for the State, sound institution-building
    processes, respect for decentralization at the level of  the local bodies at the community level
    and larger societal concern for children and their well-being.   Website:
    http://ncpcr.gov.in/index.htm  CHILD LABOUR (PROHIBITION AND REGULATION) ACT, 1986  & THE CHILD
    LABOUR (PROHIBITION  AND REGULATION) RULES, 1988
  [2] source=POCSO-2012-32  score=0.6743
    forces, as specified in the Schedule;  (d) “child” means any person below the age of eighteen years;
    1. The words “except the State of Jammu and Kashmir” omitted by Act 34 of 2019, s. 95 and the
    Fifth Schedule   (w.e.f. 31-10-2019).  2. 14th November, 2012, vide notification No. S.O. 2705
    (E), dated 9th November, 2012, see Gazette of India Extraordinary, Part  II, sec. 3(ii).     4
    1[(da) “child pornography” means any visual depiction of sex ually explicit conduct involving a
    child which include photograph, video, digital or computer generated image indistinguishable
    from an  actual child and image created, adapted, or modified, but appear to depict a child;]
    (e) “domestic relationship” shall have the same meaning as assigned to it in clause ( f) of
    section  2 of the Protection of Women from Domestic Violence Act, 2005 (43 of 2005);  (f)
    “penetrative sexual assault” has the same meaning as assigned to it in section 3;
  [3] source=Bharatiya_Nyaya_Sanhita  score=0.6071
    child shall at any age be employed or used for the purpose of prostitution or illicit intercourse
    with any person or for any unlawful and immoral purpose, or knowing it to be likely that such
    child will at any age be employed or used for any such purpose, shall be punished with
    imprisonment of either description for a term which may extend to ten years, and shall also be
    liable to fine. Explanation 1.—When a female under the age of eighteen years is sold, let for
    hire, or otherwise disposed of to a prostitute or to any person who keeps or manages a brothel,
    the person so disposing of such female shall, until the contrary is proved, be presumed to have
    disposed of her with the intent that she shall be used for the purpose of prostitution.
    Explanation 2.—For the purposes of this section “illicit intercourse” means sexual intercourse
    between persons not united by marriage or by any union or tie which, though
  [4] source=Bharatiya_Nyaya_Sanhita  score=0.6069
    is injured, but does not die; but the death of an unborn quick child with which she is pregnant is
    thereby caused. A is guilty of the offence defined in this section. Of offences against child
    93.Whoever being the father or mother of a child under the age of twelve years, or having the
    care of such child, shall expose or leave such child in any place with the intention of wholly
    abandoning such child, shall be punished with imprisonment of either description for a term
    which may extend to seven years, or with fine, or with both. Explanation.—This section is not
    intended to prevent the trial of the offender for murder or culpable homicide, as the case may
    be, if the child die in consequence of the exposure. 94.Whoever, by secretly burying or
    otherwise disposing of the dead body of a child whether such child die before or after or during
    its birth, intentionally conceals or endeavours to conceal the birth of such child, shall be
    punished with imprisonment of either description
  [5] source=POCSO-2012-32  score=0.5019
    34. Procedure in case of commission of offence by child and de termination of age by Special
    Court.—(1) Where any  offence under this Act is committed by a child, such child shall be dealt
    with  under the provisions of 1[the Juvenile Justice (Care and Protection of Children) Act, 2015
    (2 of 2016)].  (2) If any question arises in any proceeding before the Special Court whether a
    person is a child or  not, such question shall be  determined by the Special Court after
    satisfying itself about the age of such  person and it shall record in writing its reasons for
    such determination.  (3) No order made by the Special Court shall be deemed to be invalid merely
    by any subsequent proof  that the age of a personas determined by it under sub-section (2) was
    not the correct age of that person.  35. Period for recording of evidence of child and disposal
    of case.—(1) The evidence of the child

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the POCSO (Protection of Children from Sexual Offences) Act, a "child" is defined as any person below the age of eighteen years.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [018] What are the special courts under POCSO?
*domain:* `pocso`  ·  *expected_source:* `POCSO`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=POCSO-2012-32  score=1.0000
    Protection of Child Rights Act, 2005 (4 of 2006)or a Special Court designated for similar purposes
    under  any other law for the time being in force, then, s uch court shall be deemed to be a
    Special Court under  this section.   (2) While trying an offence under this Act, a Special Court
    shall also try an offence [other than the  offence referred to in sub -section (1)], with which
    the accused may, under the Code o f Criminal  Procedure, 1973 (2 of 1974) be charged at the same
    trial.  (3) The Special Court constituted under this Act, notwithstanding anything in the
    Information  Technology Act, 2000 (21 of 2000)shall have jurisdiction to try offences under
    section 67B of that Act in  so far as it relates to publication or transmission of sexually
    explicit material depicting children in any act,  or conduct or manner or facilitates abuse of
    children online.   29. Presumption as to certain offence s.—Where a person is prosecute d for
    committing or abetting
  [2] source=POCSO-2012-32  score=0.9608
    person in whom the child reposes trust or confidence.  (4) Where, in case the parent of the child or
    other person referred to in sub -section (3) cannot be  present, for any  reason, during the
    medical examination of the child, the medical examination shall be  conducted in the presence of
    a woman nominated by the head of the medical institution.  CHAPTER VII  SPECIAL COURTS  28.
    Designation of Special Courts. —(1) For the purposes  of providing a speedy trial, the State
    Government shall in consultation with the Chief Justice of the High Court, by notification in
    the Official  Gazette, designate for each district, a Court  of Session to be a Special Court to
    try the offences under the  Act:  Provided that if a Court of Session is notified as a
    children’s court under the Commissions for  Protection of Child Rights Act, 2005 (4 of 2006)or a
    Special Court designated for similar purposes under
  [3] source=POCSO-2012-32  score=0.9182
    CHAPTER VIII  PROCEDURE AND POWERS OF SPECIAL COURTS AND RECORDING OF EVIDENCE  33. Procedur e and
    powers of Special Court. —(1) A Special Court may take cognizance of any  offence, without the
    accused  being committed to it for trial, upon receiving a complaint of facts which  constitute
    such offence, or upon a police report of such facts.  (2) The Special Public Prosecutor, or as
    the case may be, the counsel appearing for the accused shall,  while recording the examination-
    in-chief, cross-examination or re-examination of the child, communicate  the questions to be put
    to the child to the  Special Court which shall in turn put those questions to the  child.  (3)
    The Special Court may, if it considers necessary, permit  frequent breaks for the child during
    the  trial.  (4) The Special Court shall create a child -friendly atmosphere by allowing a
    family member, a  guardian, a friend or a relative, in whom the child has trust or confidence,
    to be present in the court.
  [4] source=POCSO-2012-32  score=0.7636
    (2) For the purposes of sub-section (1), the Special Court may record the statement of a child
    through  video conferencing or by utilising single visibility mirrors or curtains or any other
    device.  37. Tri als to be conducted in camera .—The Special Court shall try cases in camera and
    in the  presence of the parents of the child or any other person in whom the child has trust or
    confidence:  Provided that where the Special Court is of the opinion that the child needs to be
    examined at a place  other than the  court, it shall proceed to issue a commission in accordance
    with t he provisions of section  284 of the Code of Criminal Procedure, 1973 (2 of 1974).   38.
    Assistance of an interpreter or expert whil e recording evidence of child. —(1) wherever
    necessary, the Court may take  the assistance of a translator or interpreter having  such
    qualifications,  experience and on payment of such fees as may be prescribed, while recording
    the evidence of the child.
  [5] source=POCSO-2012-32  score=0.6919
    Sessions and the person conducting a prosecution before a Special Court, shall be deemed to be a
    Public  Prosecutor.   32. Special Public Prosecutors. —(1) The State Government shall, by
    notification in the Official  Gazette, appoint a Special Public Prosecutor for every Special
    Court for conducting cases only under the  provisions of this Act.  (2) A person shall be
    eligible to be appointed as a Special Public Prosecutor under sub -section (1)  only if he had
    been in practice for not less than seven years as an advocate.  (3) Every person appointed as a
    Special Public Prosecutor under this section shall be deemed to be a  Public Prosecutor within
    the meaning of clause ( u) of section 2 of the Code of Criminal Procedure, 1973   (2 of 1974)and
    provision of that Code shall have effect accordingly.  CHAPTER VIII  PROCEDURE AND POWERS OF
    SPECIAL COURTS AND RECORDING OF EVIDENCE  33. Procedur e and powers of Special Court. —(1) A
    Special Court may take cognizance of any

### Expected answer — sentence grounding checklist
- [ ] S / U — The special courts under the POCSO Act (Protection of Children from Sexual Offences Act, 2012) are designated by the State Government in consultation with the Chief Justice of the High Court
- [ ] S / U — These courts are established to ensure a speedy trial for offences under the Act
- [ ] S / U — Key points about these special courts include:
- [ ] S / U — 1
- [ ] S / U — **Designation**: Each district has a designated Court of Session that functions as a Special Court for cases under the POCSO Act.
- [ ] S / U — 2
- [ ] S / U — **Jurisdiction**: The Special Courts also have jurisdiction over certain offences under other laws that relate to the abuse of children, such as those concerned with the publication of sexually explicit material involving children.
- [ ] S / U — 3
- [ ] S / U — **Procedure**: The courts are empowered to take cognizance of offences without the accused being committed for trial, based on complaints or police reports
- [ ] S / U — They provide a child-friendly environment during trials.
- [ ] S / U — 4
- [ ] S / U — **Conducting Trials**: Trials are conducted in camera (in private) and with provisions to ensure the comfort and safety of the child victim, including allowing supportive persons to be present and permitting breaks if needed.
- [ ] S / U — 5
- [ ] S / U — **Special Public Prosecutors**: Each Special Court has a designated Special Public Prosecutor, appointed by the State Government, who is specifically responsible for prosecuting cases under the POCSO Act.
- [ ] S / U — Overall, these courts aim to provide a sensitive and efficient legal process for the protection and welfare of children.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [019] What is the punishment for aggravated penetrative sexual assault under POCSO?
*domain:* `pocso`  ·  *expected_source:* `POCSO`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=POCSO-2012-32  score=1.0000
    having committed any offence under this Act or any sexual offence punishable under any other law for
    the time being in force; or  (u) whoever  commits penetrative sexual assault on a child and
    makes the child to strip or parade  naked in public,  is said to commit aggravated penetrative
    sexual assault.  2[6. Punishment for aggravated penetrative sexual assault .—(1) Whoever commits
    aggravated  penetrative sexual assault shall be punished with rigorous imprisonment for a term
    which shall not be less  than twenty years, but which may extend to imprisonment for life, which
    shall mean imprisonment for the  remainder of natural life of that person and shall also be
    liable to fine, or with death.  (2) The fine imposed under sub-section (1) shall be just and
    reasonable and paid to the victim to meet  the medical expenses and rehabilitation of such
    victim.]  C. —SEXUAL ASSAULT AND PUNISHMENT THEREFOR
  [2] source=POCSO-2012-32  score=0.7958
    direct anyone to administer, help in getting administered any drug or hormone or any chemical
    substance,  to a child with the intent that such child attains early sexual maturity,]  is said
    to commit aggravated sexual assault.  10. Punishment for aggravated sexual assault.—Whoever,
    commits aggravated sexual assault shall  be punished with imprisonment of either description for
    a term  which shall not be less than five years but  which may extend to seven years, and shall
    also be liable to fine.  E.—SEXUAL HARASSMENT AND PUNISHMENT THEREFOR  11. Sexual harassment. —A
    person is said to commit sexual harassment upon a child when such  person with sexual intent,—
    (i) utters any word or makes any sound, or makes any gesture or exhibits any object or part of
    body with the  intention that such word or sound shall be heard, or such gesture or object or
    part of  body shall be seen by the child; or
  [3] source=POCSO-2012-32  score=0.7028
    3. Section 4 renumbered as section 4(1) thereof by s. 3, ibid (w.e.f. 16-08-2019).  4. Subs. by s.
    3, ibid., for “seven years” (w.e.f. 16-08-2019).  5. Ins. by s. 3, ibid. (w.e.f. 16-08-2019).
    5    B.—AGGRAVATED PENETRATIVE SEXUAL ASSAULT AND PUNISHMENT THEREFOR  5. Aggravated penetrative
    sexual assault .—(a) Whoever, being a police officer, commits  penetrative sexual assault on a
    child —   (i) within the limits of the police station or premises at which he is appointed; or
    (ii) in the premises of any station house, whether or not situated in the police station, to
    which he  is appointed; or  (iii) in the course of his duties or otherwise; or  (iv) where he is
    known as, or identified as, a police officer; or  (b) whoever being a member of the armed forces
    or security forces commits penetrative sexual assault  on a child—  (i) within the limits of the
    area to which the person is deployed; or  (ii) in any areas under the command of the forces or
    armed forces; or
  [4] source=POCSO-2012-32  score=0.6849
    years] but which may extend to imprisonment for life, and shall also be liable to fine.   5[(2)
    Whoever commi ts penetrative sexual assault on a child below sixteen years of age shall be
    punished with imprisonment for a term which shall not be less than twenty years, but which may
    extend  to imprisonment for life, which shall mean imprisonment for the remainder of natural
    life of that person  and shall also be liable to fine.  (3) The fine imposed under sub-section
    (1) shall be just and reasonable and paid to the victim to meet  the medical expenses and
    rehabilitation of such victim.]
    1. Ins. by Act 25 of 2019, s. 2 (w.e.f. 16-08-2019).  2. Subs. by s. 2, ibid., for “the Juvenile
    Justice (Care and Protection of Children) Act, 2000 (56 of 2000)” (w.e.f. 16-08-2019).  3.
    Section 4 renumbered as section 4(1) thereof by s. 3, ibid (w.e.f. 16-08-2019).  4. Subs. by s.
    3, ibid., for “seven years” (w.e.f. 16-08-2019).
  [5] source=POCSO-2012-32  score=0.6800
    the medical expenses and rehabilitation of such victim.]  C. —SEXUAL ASSAULT AND PUNISHMENT THEREFOR
    7. Sexual assault.—Whoever, with sexual intent touches the vagina, penis, anus or breast of the
    child  or makes the child touch the vagina, penis, anus or breast of such person or any other
    person, or does any  other act with sexual intent which involves  physical contact without
    penetration is said to commit sexual  assault.  8. Punishment for sexual assault. —Whoever,
    commits sexual assault,  shall be punished with  imprisonment of either  description for a term
    which shall not be less than three years but which may  extend to five years, and shall also be
    liable to fine.  D. —AGGRAVATED SEXUAL ASSAULT AND PUNISHMENT THEREFOR  9. Aggravated sexual
    assault.—(a) Whoever, being a police officer, commits sexual assault on a  child—  (i) within
    the limits of the police station or premises where he is appointed; or

### Expected answer — sentence grounding checklist
- [ ] S / U — The punishment for aggravated penetrative sexual assault under the POCSO Act is:
- [ ] S / U — 1
- [ ] S / U — A minimum of twenty years of rigorous imprisonment.
- [ ] S / U — 2
- [ ] S / U — This imprisonment may extend to life imprisonment, which means imprisonment for the remainder of the person's natural life.
- [ ] S / U — 3
- [ ] S / U — The offender is also liable to pay a fine.
- [ ] S / U — 4
- [ ] S / U — In some cases, the punishment may be death.
- [ ] S / U — Additionally, any fine imposed is intended to be just and reasonable, and it will be paid to the victim to cover medical expenses and rehabilitation.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [020] What does POCSO say about mandatory reporting of offences?
*domain:* `pocso`  ·  *expected_source:* `POCSO`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=POCSO-2012-32  score=1.0000
    CHAPTER V  PROCEDURE FOR REPORTING OF CASES  19. Reporting of offences. —(1) Notwithstanding
    anything contained in the Code of Criminal  Procedure, 1973 (2 of1974)any person(including the
    child), who has apprehension that an offence under  this Act is likely to be committed or has
    knowledge that such  an offence has been committed, he sha ll  provide such information to,—
    (a) the Special Juvenile Police Unit; or  (b) the local police.  (2) Every report given under
    sub-section (1) shall be—  (a) ascribed an entry number and recorded in writing;  (b) be read
    over to the informant;  (c) shall be entered in a book to be kept by the Police Unit.  (3) Where
    the report under sub -section ( 1) is given by a child, the same shall be recorded under
    sub-section (2) in a simple language so that the child understands contents being recorded.  (4)
    In case contents are being recorded in the language not understood by the child or wherever it
    is
  [2] source=POCSO-2012-32  score=0.4671
    which is sexually exploitative of the child (including pornographic, sexually-related or making
    obscene  representation of a child or children) through the use of any medium, shall  provide
    such information to  the Special Juvenile Police Unit, or to the local police, as the case may
    be.  21. Punishment for failure to report or rec ord a case. —(1) Any person, who fails to
    report the  commission of an offence  under sub-section (1) of section 19 or section 20 or who
    fails to record such   11    offence under sub -section (2) of section 19 shall be  punished
    with imprisonment of either description  which may extend to six months or with fine or with
    both.  (2) Any person, being in-charge of any company or an institution (by whatever name
    called) who fails  to report the commis sion of an offence under sub -section ( 1) of section 19
    in respect of a subordinate  under his control, shall be punished with imprisonment for a term
    which may extend to one year and with  fine.
  [3] source=POCSO-2012-32  score=0.3705
    (6) The Special  Juvenile Police Unit or local police shall, without unnecessary delay but within a
    period of twenty -four hours, report the matter to the Child Welfare Committee and the Special
    Court or  where no Special Court has been designated, to the  Court of Session, including need
    of the chi ld for care  and protection and steps taken in this regard.  (7) No person shall
    incur any liability, whether civil or criminal, for giving the information in good  faith for
    the purpose of sub-section (1).  20. Obligation of media, studio and photographic facilities to
    report cases.—Any personnel of the  media or hotel or lodge or hospital or club or studio or
    photographic facilities, by whatever name called,  irrespective of the number of persons
    employed therein, shall, on coming across any material or obje ct  which is sexually
    exploitative of the child (including pornographic, sexually-related or making obscene
  [4] source=Motor-Vahicle-Act-1988-59  score=0.2787
    make regulations for the driving of motor vehicles.  119. Duty to obey traffic signs .—(1) Every
    driver of a motor vehicle shall drive the vehicle in  conformity with any indication given by
    mandatory traffic sign and in conformity with the driving  regulations made by the Central
    Government, and shall comply with all directions given to him by any  police officer for the
    time being engaged in the regulation of traffic in any public place.  (2) In this section
    “mandatory traffic sign” means a traffic sign included in Part A of the Schedule, or  any
    traffic sign of similar form (that is to say, consisting of or including a circular disc
    diplaying a device,                                                              1. Subs. by Act
    54 of 1994, s. 36, for “the Schedule” (w.e.f. 14-11-1994). 68    word or figure and having a red
    ground o r border) placed or erected for the purpose of regulating motor  vehicle traffic under
    sub-section (1) of section 116.
  [5] source=Bharatiya_Nyaya_Sanhita  score=0.2309
    (2) Whoever causes death of any person by rash and negligent driving of vehicle not amounting to
    culpable homicide, and escapes without reporting it to a police officer or a Magistrate soon
    after the incident, shall be punished with imprisonment of either description of a term which
    may extend to ten years, and shall also be liable to fine. 107.If any child, any person of
    unsound mind, any delirious person or any person in a state of intoxication, commits suicide,
    whoever abets the commission of such suicide, shall be punished with death or imprisonment for
    life, or imprisonment for a term not exceeding ten years, and shall also be liable to fine.
    108.If any person commits suicide, whoever abets the commission of such suicide, shall be
    punished with imprisonment of either description for a term which may extend to ten years, and
    shall also be liable to fine. 109.(1) Whoever does any act with such intention or knowledge, and
    under such

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the POCSO Act, any person (including a child) who suspects or has knowledge that an offence against a child has been committed must report this information to either the Special Juvenile Police Unit or the local police
- [ ] S / U — The report must be documented clearly, and if made by a child, it should be recorded in simple language that the child can understand.
- [ ] S / U — Failure to report such offences can lead to legal consequences
- [ ] S / U — Specifically, individuals who do not report are subject to imprisonment for up to six months, a fine, or both
- [ ] S / U — For those in charge of institutions who fail to report on behalf of a subordinate, the punishment can extend to one year of imprisonment and a fine.
- [ ] S / U — Additionally, anyone providing this information in good faith is protected from any civil or criminal liability.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [021] What are the rights of a consumer under the Consumer Protection Act?
*domain:* `consumer`  ·  *expected_source:* `CPA-2019`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=CPA-2019  score=1.0000
    protection of consumer rights under this Act within the State. 8. (1) The State Government shall, by
    notification, establish for every District with effect from such date as it may specify in such
    notification, a District Consumer Protection Council to be known as the District Council. (2)
    The District Council shall be an advisory council and consist of the following members, namely:—
    (a) the Collector of the district (by whatever name called), who shall be the Chairperson; and
    (b) such number of other official and non-official members representing such interests as may be
    prescribed. (3) The District Council shall meet as and when necessary but not less than two
    meetings shall be held every year. (4) The District Council shall meet at such time and place
    within the district as the Chairperson may think fit and shall observe such procedure in regard
    to the transaction of its business as may be prescribed.
  [2] source=CPA-2019  score=0.9542
    Short title, extent, commencement and application. THE CONSUMER PROTECTION ACT, 2019 NO. 35 OF  2019
    [9th August, 2019.] An Act to provide for protection of the interests of consumers and for the
    said purpose, to establish authorities for timely and effective administration and settlement of
    consumers' disputes and for matters connected therewith or incidental thereto. BE it enacted by
    Parliament in the Seventieth Year of the Republic of India as follows:— CHAPTER I PRELIMINARY 1.
    (1) This Act may be called the Consumer Protection Act, 2019. (2) It extends to the whole of
    India except the State of Jammu and Kashmir. (3) It shall come into force on such date as the
    Central Government may, by notification, appoint and different dates may be appointed for
    different States and for different provisions of this Act and any reference in any such
    provision to the commencement of this Act shall be construed as a reference to the coming into
    force of that provision.
  [3] source=CPA-2019  score=0.9430
    Chairperson may think fit and shall observe such procedure in regard to the transaction of its
    business as may be prescribed. 9. The objects of every District Council shall be to render
    advice on promotion and protection of consumer rights under this Act within the district.
    CHAPTER III C ENTRAL CONSUMER PROTECTION AUTHORITY 10. (1) The Central Government shall, by
    notification, establish with effect from such date as it may specify in that notification, a
    Central Consumer Protection Authority to be known as the Central Authority to regulate matters
    relating to violation of rights of consumers, unfair trade practices and false or misleading
    advertisements which are prejudicial to the interests of public and consumers and to promote,
    protect and enforce the rights of consumers as a class. (2) The Central Authority shall consist
    of a Chief Commissioner and such number of other Commissioners as may be prescribed, to be
    appointed by the Central Government to
  [4] source=CPA-2019  score=0.9324
    violation of consumers rights under this Act; (b) prevent unfair trade practices and ensure that no
    person engages himself in unfair trade practices; (c) ensure that no false or misleading
    advertisement is made of any goods or services which contravenes the provisions of this Act or
    the rules or regulations made thereunder; (d) ensure that no person takes part in the
    publication of any advertisement which is false or misleading. (2) Without prejudice to the
    generality of the provisions contained in sub-section (1), the Central Authority may, for any of
    the purposes aforesaid,— (a) inquire or cause an inquiry or investigation to be made into
    violations of consumer rights or unfair trade practices, either suo motu or on a complaint
    received or on the directions from the Central Government; (b) file complaints before the
    District Commission, the State Commission or the National Commission, as the case may be, under
    this Act;
  [5] source=CPA-2019  score=0.8701
    on the directions from the Central Government; (b) file complaints before the District Commission,
    the State Commission or the National Commission, as the case may be, under this Act; (c)
    intervene in any proceedings before the District Commission or the State Commission or the
    National Commission, as the case may be, in respect of any allegation of violation of consumer
    rights or unfair trade practices; (d) review the matters relating to, and the factors inhibiting
    enjoyment of, consumer rights, including safeguards provided for the protection of consumers
    under any other law for the time being in force and recommend appropriate remedial measures for
    their effective implementation; (e) recommend adoption of international covenants and best
    international practices on consumer rights to ensure effective enforcement of consumer rights;
    (f) undertake and promote research in the field of consumer rights; (g) spread and promote
    awareness on consumer rights;

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the Consumer Protection Act, 2019, consumers have the following rights:
- [ ] S / U — 1
- [ ] S / U — **Right to Protection**: Consumers are entitled to protection against hazardous goods and services.
- [ ] S / U — 2
- [ ] S / U — **Right to Information**: Consumers have the right to be informed about the quality, quantity, potency, purity, standard, and price of goods or services to make informed choices.
- [ ] S / U — 3
- [ ] S / U — **Right to Choice**: Consumers have the right to choose from a variety of products and services at competitive prices.
- [ ] S / U — 4
- [ ] S / U — **Right to Hearing**: Consumers are entitled to a fair hearing in case of any dispute or complaint about goods and services.
- [ ] S / U — 5
- [ ] S / U — **Right to Redress**: Consumers have the right to seek compensation for losses or damages suffered due to unfair trade practices or defective goods.
- [ ] S / U — 6
- [ ] S / U — **Right to Consumer Education**: Consumers have the right to be educated about their rights and responsibilities.
- [ ] S / U — The Central Consumer Protection Authority (CCPA) is empowered to regulate and enforce these rights, addressing violations and unfair trade practices.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [022] What is the procedure to file a consumer complaint?
*domain:* `consumer`  ·  *expected_source:* `CPA-2019`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=CPA-2019  score=1.0000
    omits or fails to take any action to represent his case within the time given by the District
    Commission, it shall proceed to settle the consumer dispute— Procedure on admission of
    complaint.20 THE GAZETTE OF INDIA EXTRAORDINARY [P ART II— (i) on the basis of evidence brought
    to its notice by the complainant and the opposite party, if the opposite party denies or
    disputes the allegations contained in the complaint, or (ii) ex parte  on the basis of evidence
    brought to its notice by the complainant, where the opposite party omits or fails to take any
    action to represent his case within the time given by the Commission; (c) decide the complaint
    on merits if the complainant fails to appear on the date of hearing. (4) For the purposes of
    sub-sections ( 2) and ( 3), the District Commission may, by order, require an electronic service
    provider to provide such information, documents or records, as may be specified in that order.
  [2] source=CPA-2019  score=0.9792
    appropriate laboratory and also as to the objection made in relation thereto under clause (f) and
    issue an appropriate order under section 39. (3) The District Commission shall, if the complaint
    admitted by it under sub-section (2) of section 36 relates to goods in respect of which the
    procedure specified in sub-section (2) cannot be followed, or if the complaint relates to any
    services,— (a) refer a copy of such complaint to the opposite party directing him to give his
    version of the case within a period of thirty days or such extended period not exceeding fifteen
    days as may be granted by the District Commission; (b) if the opposite party, on receipt of a
    copy of the complaint, referred to him under clause ( a) denies or disputes the allegations
    contained in the complaint, or omits or fails to take any action to represent his case within
    the time given by the District Commission, it shall proceed to settle the consumer dispute—
    Procedure on admission of
  [3] source=CPA-2019  score=0.9227
    inquire into or investigate complaints regarding violation of rights of consumers as a class, on
    matters relating to violations of consumer rights, unfair trade practices and false or
    misleading advertisements, within his jurisdiction and submit his report to the Central
    Authority or to the Commissioner of a regional office, as the case may be. 17. A complaint
    relating to violation of consumer rights or unfair trade practices or false or misleading
    advertisements which are prejudicial to the interests of consumers as a class, may be forwarded
    either in writing or in electronic mode, to any one of the authorities, namely, the District
    Collector or the Commissioner of regional office or the Central Authority. 18. (1) The Central
    Authority shall— (a) protect, promote and enforce the rights of consumers as a class, and
    prevent violation of consumers rights under this Act; (b) prevent unfair trade practices and
    ensure that no person engages himself in unfair trade practices;
  [4] source=CPA-2019  score=0.9126
    on the directions from the Central Government; (b) file complaints before the District Commission,
    the State Commission or the National Commission, as the case may be, under this Act; (c)
    intervene in any proceedings before the District Commission or the State Commission or the
    National Commission, as the case may be, in respect of any allegation of violation of consumer
    rights or unfair trade practices; (d) review the matters relating to, and the factors inhibiting
    enjoyment of, consumer rights, including safeguards provided for the protection of consumers
    under any other law for the time being in force and recommend appropriate remedial measures for
    their effective implementation; (e) recommend adoption of international covenants and best
    international practices on consumer rights to ensure effective enforcement of consumer rights;
    (f) undertake and promote research in the field of consumer rights; (g) spread and promote
    awareness on consumer rights;
  [5] source=CPA-2019  score=0.8720
    of its admission to the opposite party mentioned in the complaint directing him to give his version
    of the case within a period of thirty days or such extended period not exceeding fifteen days as
    may be granted by it; (b) if the opposite party on receipt of a complaint referred to him under
    clause (a) denies or disputes the allegations contained in the complaint, or omits or fails to
    take any action to represent his case within the time given by the District Commission, proceed
    to settle the consumer dispute in the manner specified in clauses (c) to (g); (c) if the
    complaint alleges a defect in the goods which cannot be determined without proper analysis or
    test of the goods, obtain a sample of the goods from the complainant, seal it and authenticate
    it in the manner as may be prescribed and refer the sample so sealed to the appropriate
    laboratory along with a direction that such laboratory to make an analysis or test, whichever
    may be necessary, with a view to

### Expected answer — sentence grounding checklist
- [ ] S / U — To file a consumer complaint in India, follow these steps:
- [ ] S / U — 1
- [ ] S / U — **Identify the Authority**: Determine the appropriate authority to address your complaint, which could be the District Commission, State Commission, or National Commission, depending on the value and nature of your complaint.
- [ ] S / U — 2
- [ ] S / U — **Prepare Your Complaint**: Draft a complaint detailing the violation of consumer rights, unfair trade practices, or misleading advertisements
- [ ] S / U — Include:
- [ ] S / U — - Your name and address
- [ ] S / U — - Details of the opposite party
- [ ] S / U — - Facts of the case
- [ ] S / U — - Relief sought
- [ ] S / U — 3
- [ ] S / U — **Mode of Submission**: File your complaint either in writing or electronically
- [ ] S / U — Ensure that you are clear and concise.
- [ ] S / U — 4
- [ ] S / U — **Submit the Complaint**: File the complaint with the relevant Commission
- [ ] S / U — You may need to submit a copy to the opposite party, which they will then have to respond to within 30 days (which can be extended by an additional 15 days).
- [ ] S / U — 5
- [ ] S / U — **Await Response**: If the opposite party denies the allegations or fails to respond, the Commission will proceed to settle the dispute based on the evidence provided by you.
- [ ] S / U — 6
- [ ] S / U — **Hearing**: Attend the hearing set by the Commission
- [ ] S / U — If you don’t appear, the case may still be decided based on the merits.
- [ ] S / U — 7
- [ ] S / U — **Follow-up**: If required, you may be asked to submit evidence or documents to back your complaint during the process.
- [ ] S / U — By adhering to these steps, you can effectively file a consumer complaint in India.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [023] What are the penalties for misleading advertisements under the Consumer Protection Act?
*domain:* `consumer`  ·  *expected_source:* `CPA-2019`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=CPA-2019  score=1.0000
    which, such user or consumer, ought to have known, taking into account the characteristics of such
    product. CHAPTER VII O FFENCES AND PENALTIES 88. Whoever, fails to comply with any direction of
    the Central Authority under sections 20 and 21, shall be punished with imprisonment for a term
    which may extend to six months or with fine which may extend to twenty lakh rupees, or with
    both. 89. Any manufacturer or service provider who causes a false or misleading advertisement to
    be made which is prejudicial to the interest of consumers shall be punished with imprisonment
    for a term which may extend to two years and with fine which may extend to ten lakh rupees; and
    for every subsequent offence, be punished with imprisonment for a term which may extend to five
    years and with fine which may extend to fifty lakh rupees. 90. (1) Whoever, by himself or by any
    other person on his behalf, manufactures for
  [2] source=CPA-2019  score=0.9852
    violation of consumers rights under this Act; (b) prevent unfair trade practices and ensure that no
    person engages himself in unfair trade practices; (c) ensure that no false or misleading
    advertisement is made of any goods or services which contravenes the provisions of this Act or
    the rules or regulations made thereunder; (d) ensure that no person takes part in the
    publication of any advertisement which is false or misleading. (2) Without prejudice to the
    generality of the provisions contained in sub-section (1), the Central Authority may, for any of
    the purposes aforesaid,— (a) inquire or cause an inquiry or investigation to be made into
    violations of consumer rights or unfair trade practices, either suo motu or on a complaint
    received or on the directions from the Central Government; (b) file complaints before the
    District Commission, the State Commission or the National Commission, as the case may be, under
    this Act;
  [3] source=CPA-2019  score=0.9161
    inquire into or investigate complaints regarding violation of rights of consumers as a class, on
    matters relating to violations of consumer rights, unfair trade practices and false or
    misleading advertisements, within his jurisdiction and submit his report to the Central
    Authority or to the Commissioner of a regional office, as the case may be. 17. A complaint
    relating to violation of consumer rights or unfair trade practices or false or misleading
    advertisements which are prejudicial to the interests of consumers as a class, may be forwarded
    either in writing or in electronic mode, to any one of the authorities, namely, the District
    Collector or the Commissioner of regional office or the Central Authority. 18. (1) The Central
    Authority shall— (a) protect, promote and enforce the rights of consumers as a class, and
    prevent violation of consumers rights under this Act; (b) prevent unfair trade practices and
    ensure that no person engages himself in unfair trade practices;
  [4] source=CPA-2019  score=0.9091
    Central Authority to refer matter for investigation or to other Regulator. Power of Central
    Authority to recall goods, etc. Power of Central Authority to issue directions and penalties
    against false or misleading advertisements.SEC. 1] THE GAZETTE OF INDIA EXTRAORDINARY 15
    Provided that the Central Authority may, for every subsequent contravention, prohibit such
    endorser from making endorsement in respect of any product or service for a period which may
    extend to three years. (4) Where the Central Authority is satisfied after investigation that any
    person is found to publish, or is a party to the publication of, a misleading advertisement, it
    may impose on such person a penalty which may extend to ten lakh rupees. (5) No endorser shall
    be liable to a penalty under sub-sections ( 2) and (3) if he has exercised due diligence to
    verify the veracity of the claims made in the advertisement regarding the product or service
    being endorsed by him.
  [5] source=CPA-2019  score=0.8974
    (2) Notwithstanding the order passed under sub-section (1), if the Central Authority is of the
    opinion that it is necessary to impose a penalty in respect of such false or misleading
    advertisement, by a manufacturer or an endorser, it may, by order, impose on manufacturer or
    endorser a penalty which may extend to ten lakh rupees: Provided that the Central Authority may,
    for every subsequent contravention by a manufacturer or endorser, impose a penalty, which may
    extend to fifty lakh rupees. (3) Notwithstanding any order under sub-sections ( 1) and ( 2),
    where the Central Authority deems it necessary, it may, by order, prohibit the endorser of a
    false or misleading advertisement from making endorsement of any product or service for a period
    which may extend to one year: Power of Central Authority to refer matter for investigation or to
    other Regulator. Power of Central Authority to recall goods, etc. Power of Central Authority to
    issue directions and penalties against false

### Expected answer — sentence grounding checklist
- [ ] S / U — Under the Consumer Protection Act, the penalties for misleading advertisements are as follows:
- [ ] S / U — 1
- [ ] S / U — **For manufacturers or service providers**:
- [ ] S / U — - First offence: Imprisonment of up to **two years** and a fine of up to **ten lakh rupees**.
- [ ] S / U — - Subsequent offences: Imprisonment of up to **five years** and a fine of up to **fifty lakh rupees**.
- [ ] S / U — 2
- [ ] S / U — **For endorsers (those promoting the advertisement)**:
- [ ] S / U — - A penalty may be imposed up to **ten lakh rupees** for misleading advertisements.
- [ ] S / U — - For subsequent offences, the penalty may increase to **fifty lakh rupees**.
- [ ] S / U — - Endorsers may also be prohibited from making endorsements for specified periods (up to **three years** for subsequent contraventions).
- [ ] S / U — 3
- [ ] S / U — **General non-compliance penalties**:
- [ ] S / U — - Failure to comply with directives from the Central Authority can lead to imprisonment for up to **six months** and a fine of up to **twenty lakh rupees**.
- [ ] S / U — These penalties emphasize the seriousness of misleading advertisements and aim to protect consumer interests.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [024] What is the time limit to file a consumer complaint?
*domain:* `consumer`  ·  *expected_source:* `CPA-2019`

> ⚠️ retrieval failed: HTTP 503: {"detail":"Search service unavailable"}

---

## [025] What is the pecuniary jurisdiction of the District Consumer Commission?
*domain:* `consumer`  ·  *expected_source:* `CPA-2019`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=CPA-2019  score=1.0000
    District Commission. Jurisdiction of District Commission.18 THE GAZETTE OF INDIA EXTRAORDINARY [P
    ART II— (3) The District Commission shall ordinarily function in the district headquarters and
    may perform its functions at such other place in the district, as the State Government may, in
    consultation with the State Commission, notify in the Official Gazette from time to time. 35.
    (1) A complaint, in relation to any goods sold or delivered or agreed to be sold or delivered or
    any service provided or agreed to be provided, may be filed with a District Commission by— (a)
    the consumer,— (i) to whom such goods are sold or delivered or agreed to be sold or delivered or
    such service is provided or agreed to be provided; or (ii) who alleges unfair trade practice in
    respect of such goods or service; (b) any recognised consumer association, whether the consumer
    to whom such goods are sold or delivered or agreed to be sold or delivered or such service is
    provided
  [2] source=CPA-2019  score=0.8958
    28. (1) The State Government shall, by notification, establish a District Consumer Disputes
    Redressal Commission, to be known as the District Commission, in each district of the State:
    Provided that the State Government may, if it deems fit, establish more than one District
    Commission in a district. (2) Each District Commission shall consist of— (a) a President; and
    (b) not less than two and not more than such number of members as may be prescribed, in
    consultation with the Central Government. Designation of any statutory authority or body to
    function as Central Authority. Appeal. Grants by Central Government. Accounts and audit.
    Furnishing of annual reports, etc. Establishment of District Consumer Disputes Redressal
    Commission.SEC. 1] THE GAZETTE OF INDIA EXTRAORDINARY 17 29. The Central Government may, by
    notification, make rules to provide for the qualifications, method of recruitment, procedure for
    appointment, term of office, resignation
  [3] source=CPA-2019  score=0.8808
    State; and (b) to call for the records and pass appropriate orders in any consumer dispute which is
    pending before or has been decided by any District Commission within the State, where it appears
    to the State Commission that such District Commission has exercised a jurisdiction not vested in
    it by law, or has failed to exercise a jurisdiction so vested or has acted in exercise of its
    jurisdiction illegally or with material irregularity. (2) The jurisdiction, powers and authority
    of the State Commission may be exercised by Benches thereof, and a Bench may be constituted by
    the President with one or more members as the President may deem fit: Provided that the senior-
    most member shall preside over the Bench. (3) Where the members of a Bench differ in opinion on
    any point, the points shall be decided according to the opinion of the majority, if there is a
    majority, but if the members are equally divided, they shall state the point or points on which
    they differ, and make a reference
  [4] source=CPA-2019  score=0.8023
    Chairperson may think fit and shall observe such procedure in regard to the transaction of its
    business as may be prescribed. 9. The objects of every District Council shall be to render
    advice on promotion and protection of consumer rights under this Act within the district.
    CHAPTER III C ENTRAL CONSUMER PROTECTION AUTHORITY 10. (1) The Central Government shall, by
    notification, establish with effect from such date as it may specify in that notification, a
    Central Consumer Protection Authority to be known as the Central Authority to regulate matters
    relating to violation of rights of consumers, unfair trade practices and false or misleading
    advertisements which are prejudicial to the interests of public and consumers and to promote,
    protect and enforce the rights of consumers as a class. (2) The Central Authority shall consist
    of a Chief Commissioner and such number of other Commissioners as may be prescribed, to be
    appointed by the Central Government to
  [5] source=CPA-2019  score=0.7842
    terms of an order of the District Commission, shall be entertained by the State Commission unless
    the appellant has deposited fifty per cent. of that amount in the manner as may be prescribed:
    Provided also that no appeal shall lie from any order passed under sub-section (1) of section 81
    by the District Commission pursuant to a settlement by mediation under section 80. 42. ( 1) The
    State Government shall, by notification, establish a State Consumer Disputes Redressal
    Commission, to be known as the State Commission, in the State. (2) The State Commission shall
    ordinarily function at the State capital and perform its functions at such other places as the
    State Government may in consultation with the State Commission notify in the Official Gazette:
    Provided that the State Government may, by notification, establish regional benches of the State
    Commission, at such places, as it deems fit. (3) Each State Commission shall consist of— (a) a
    President; and

### Expected answer — sentence grounding checklist
- [ ] S / U — The pecuniary jurisdiction of the District Consumer Commission is not explicitly stated in the provided context
- [ ] S / U — However, typically, the District Commission handles consumer disputes involving claims up to a certain monetary limit, which may be defined by state regulations or government notifications
- [ ] S / U — To find the exact limit, you may need to refer to the specific rules or notifications issued by the State Government under the Consumer Protection Act in your state.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [026] What is the definition of an industrial dispute under the Industrial Disputes Act?
*domain:* `labour`  ·  *expected_source:* `Labour-Act`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
    An industrial dispute may be defined as a conflict or difference of opinion between management  and
    workers on the terms of employm ent. It is a disagreement between an employer and  employees'
    representative; usually a trade union, over pay and other working conditions and can  result in
    industrial actions. When an industrial dispute occurs, both the parties, that is the  management
    and the workmen, try to pressurize each other. The management may resort to  lockouts while the
    workers may resort to strikes, picketing or gheraos.  As per Section 2(k) of Industrial Disputes
    Act, 1947, an industrial dispute is defined as any dispute or  difference between employees and
    employers, or between employers and workmen, or between 75    workmen and which is connected
    with the employment or non -employment or the terms of  employment or with the conditions of
    labour, of any person.    Objective of the Act
  [2] source=Labour-Act  score=0.8637
    Disputes Act is to secure industrial  peace and harmony by providing  machinery and procedure for
    the  investigation and settlement of  industrial disputes by negotiations.  This Act applies to
    every industrial  establishment carrying on any  business, trade, manufacture or  distribution
    of goods and services  irrespective of the number of  workmen employed therein. Every  person
    employed in an  establishment for hire or reward  including contract labour,  apprentices and
    part time employees  to do any manual, clerical, skilled,  unskilled, technical, operational or
    supervisory work, is covered by the  Act.    Prevention of unfair labour  practices.   Prior
    permission of  appropriate Government /  concerned labour authority for  laying off or
    retrenching the  workers or closing down the  industrial establishment.   Payment of
    compensation to  workers on account of closure  or lay off or retrenchment.  Industrial
    Employment  and Standing Orders  Act , 1946
  [3] source=Labour-Act  score=0.8443
    with the title, definitions, etc.   Chapter – II contains the various authorities under the Ac t.
    These  authorities include Conciliation Officers, Labour Courts and Tribunals.  Chapter – III
    contains the  main scheme of the Act such as reference of disputes to Labour Courts and
    Industrial Tribunals.   Chapter – IV lays down the procedure, power and d uties of the
    authorities constituted under the  Act.  Chapter – V contains provisions to prohibit strikes and
    lockouts, declaration of strikes and  lockouts as illegal, and provisions relating to lay -off
    and retrenchment and closure.  Chapter -VI  contains pro visions of various penalties under the
    Act.  Chapter –VII contains miscellaneous  provisions.  Definition of Industrial Disputes  An
    industrial dispute may be defined as a conflict or difference of opinion between management  and
    workers on the terms of employm ent. It is a disagreement between an employer and
  [4] source=Labour-Act  score=0.8428
    workmen and which is connected with the employment or non -employment or the terms of  employment or
    with the conditions of labour, of any person.    Objective of the Act  The objective of the
    Industrial Disputes Act is to secure industrial peace and harmony by providing  machinery and
    procedure for the investigation and settlement of industrial disputes by negotiations.   The Act
    also lays down:   (a) The provision for payment of compensation to the Workman on account of
    closure or lay  off or retrenchment.   (b) The procedure for prior permission of appropriate
    Government for laying off or  retrenching the workers or closing down industrial establishments
    (c) Unfair labour practices on part of an employer or a trade union or workers.    Applicability
    The Industrial Disputes Act extends to whole of India and applies to every industrial
    establishment  carrying on any business, trade, manufacture or distribution of goods and
    services irrespective of the
  [5] source=Labour-Act  score=0.6696
    factories employing more than 10  people and working with the aid of  power or employing 20 people
    and  working without the aid of power. It  covers all workers employed in the  factory premises
    or precincts directly  or through an agency including a  contractor, involved in any  
    Licensing and renewal of  licence under the Act.   Provision of adequate safety  measures
    within the factory  premises.   Provision of adequate welfare  measures like creche, canteen,
    wash room etc for the  workers.   Payment of wages as per the 138    manufacture. Some
    provisions of the  Act will vary according to the nature  of work of the establishment.
    provisions of the Act.   Payment of overtime wages.   Maintenance of registers.   Submission
    of returns.  Industrial Disputes Act ,  1947  The objective of the Industrial  Disputes Act is
    to secure industrial  peace and harmony by providing  machinery and procedure for the
    investigation and settlement of  industrial disputes by negotiations.

### Expected answer — sentence grounding checklist
- [ ] S / U — An industrial dispute is defined under the Industrial Disputes Act, 1947, as any disagreement or difference of opinion between employees and employers, or between employers and workmen, specifically related to employment, non-employment, terms of employment, or conditions of labor for any person
- [ ] S / U — This definition encompasses conflicts that can lead to strikes or lockouts.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [027] What are the conditions for a lawful strike under the Labour Act?
*domain:* `labour`  ·  *expected_source:* `Labour-Act`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
    11. To discharge or discriminate against any workmen for filing charges or testi fying against
    employer in any enquiry or proceeding relating to any industrial dispute.  12. To recruit
    workmen during a strike which is not an illegal strike.  13. Failure to implement award,
    settlement or agreement.  14. To indulge in acts of force or violence.  15. To refuse to bargain
    collectively, in good faith with the recognized trade unions.  16. Proposing or continuing a
    lock out deemed to be illegal under this act.  If the employer of any establishment commits any
    of these acts then he will be liable fo r an offence  of unfair labour practice.    Unfair
    labour practices on the part of workmen and trade unions of workmen 147    1.  To advise or
    actively support or instigate any strike deemed to be illegal   under the Industrial  Disputes
    Act, 1947.  2.  To coerce workm en in the exercise of their right to self -organization or to
    join a trade union or
  [2] source=Labour-Act  score=0.8063
    1. The propriety or legality of an order passed by an employer under the standing orders  2. The
    application and interpretation of standing order  3. Discharge or dismissal of workmen including
    re -instatement of, or grant of relief to,  workmen wrongfully dismissed.  4. Withdrawal of any
    customary concession or privilege  5. Illegality or otherwise of a strike or lock-out; and  6.
    All matters other than those being referred to Industrial Tribunals.  Stages of adjudication in
    labour or industrial disputes 186    The first is receiving a reference fr om the appropriate
    Government or filing of the labour  dispute in the Labour Court. The next step is sending notice
    to the Management and after  filing of the response by them, the matter is fixed for
    adjudication. The fourth step is  recording the evidence of the parties and hearing the
    arguments.  The final conclusion of the dispute   After hearing the parties, the Labour
    Court/Industrial Tribunal decides the dispute and the
  [3] source=Labour-Act  score=0.8034
    workmen and which is connected with the employment or non -employment or the terms of  employment or
    with the conditions of labour, of any person.    Objective of the Act  The objective of the
    Industrial Disputes Act is to secure industrial peace and harmony by providing  machinery and
    procedure for the investigation and settlement of industrial disputes by negotiations.   The Act
    also lays down:   (a) The provision for payment of compensation to the Workman on account of
    closure or lay  off or retrenchment.   (b) The procedure for prior permission of appropriate
    Government for laying off or  retrenching the workers or closing down industrial establishments
    (c) Unfair labour practices on part of an employer or a trade union or workers.    Applicability
    The Industrial Disputes Act extends to whole of India and applies to every industrial
    establishment  carrying on any business, trade, manufacture or distribution of goods and
    services irrespective of the
  [4] source=Labour-Act  score=0.7987
    recognized at all as compensation.  4k. THE TRADE UNIONS ACT, 1926:  The Trade Unions Act, 1926
    provides for registration of trade unions wit h a view to render lawful  organisation of labour
    to enable collective bargaining. It also confers on a registered trade union  certain protection
    and privileges.  The Act extends to the whole of India and applies to all kinds of unions of
    workers and associa tions  of employers, which aim at regularising labour management relations.
    A Trade Union is a  combination whether temporary or permanent, formed for regulating the
    relations not only  between workmen and employers but also between workmen and workmen or bet
    ween employers  and employers.   Registration  98    Registration of a trade union is not
    compulsory but is desirable since a registered trade union enjoys  certain rights and privileges
    under the Act. Minimum seven workers of an establishment (or seven
  [5] source=Labour-Act  score=0.7734
    administrative regulations enacted by the State Council, the ministerial rules and the judicial
    explanations of the Supreme People’s Court stipulate detailed rules concerning the various
    aspects of the employment relationship. Labour Union in China is controlled by the government
    through the All China Federation of Trade Unions, which is also the sole legal labour union in
    Mainland China. Strike is formally legal, but in fact is strictly forbidden.  According to the
    new 98 -article-long "Labor Contract Law", employees of at least 10 ye ars  standing are
    entitled to contracts that protect them from being dismissed without cause. The  new law also
    requires employers to contribute to employees' social security accounts and sets  wage standards
    for employees on probation and working overtime.  China's new labor contract law targets,
    primarily domestic companies that do not have labor  contracts and that generally fail to comply
    with China's old laws. Foreign companies have had a

### Expected answer — sentence grounding checklist
- [ ] S / U — The conditions for a lawful strike under the Labour Act include:
- [ ] S / U — 1
- [ ] S / U — The strike must not be deemed illegal under the Industrial Disputes Act, 1947.
- [ ] S / U — 2
- [ ] S / U — It should be connected with employment or non-employment, the terms of employment, or the conditions of labor.
- [ ] S / U — 3
- [ ] S / U — The strike should not involve acts of force or violence.
- [ ] S / U — 4
- [ ] S / U — Workmen should not be coerced in the exercise of their right to self-organization or to join a trade union.
- [ ] S / U — 5
- [ ] S / U — The strike should be in response to an employer's unfair labor practices such as failure to implement an award, settlement, or agreement.
- [ ] S / U — If any of these conditions are violated, the strike may be considered illegal.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [028] What is retrenchment under the Industrial Disputes Act?
*domain:* `labour`  ·  *expected_source:* `Labour-Act`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
    Disputes Act is to secure industrial  peace and harmony by providing  machinery and procedure for
    the  investigation and settlement of  industrial disputes by negotiations.  This Act applies to
    every industrial  establishment carrying on any  business, trade, manufacture or  distribution
    of goods and services  irrespective of the number of  workmen employed therein. Every  person
    employed in an  establishment for hire or reward  including contract labour,  apprentices and
    part time employees  to do any manual, clerical, skilled,  unskilled, technical, operational or
    supervisory work, is covered by the  Act.    Prevention of unfair labour  practices.   Prior
    permission of  appropriate Government /  concerned labour authority for  laying off or
    retrenching the  workers or closing down the  industrial establishment.   Payment of
    compensation to  workers on account of closure  or lay off or retrenchment.  Industrial
    Employment  and Standing Orders  Act , 1946
  [2] source=Labour-Act  score=0.9854
    workmen and which is connected with the employment or non -employment or the terms of  employment or
    with the conditions of labour, of any person.    Objective of the Act  The objective of the
    Industrial Disputes Act is to secure industrial peace and harmony by providing  machinery and
    procedure for the investigation and settlement of industrial disputes by negotiations.   The Act
    also lays down:   (a) The provision for payment of compensation to the Workman on account of
    closure or lay  off or retrenchment.   (b) The procedure for prior permission of appropriate
    Government for laying off or  retrenching the workers or closing down industrial establishments
    (c) Unfair labour practices on part of an employer or a trade union or workers.    Applicability
    The Industrial Disputes Act extends to whole of India and applies to every industrial
    establishment  carrying on any business, trade, manufacture or distribution of goods and
    services irrespective of the
  [3] source=Labour-Act  score=0.8710
    with the title, definitions, etc.   Chapter – II contains the various authorities under the Ac t.
    These  authorities include Conciliation Officers, Labour Courts and Tribunals.  Chapter – III
    contains the  main scheme of the Act such as reference of disputes to Labour Courts and
    Industrial Tribunals.   Chapter – IV lays down the procedure, power and d uties of the
    authorities constituted under the  Act.  Chapter – V contains provisions to prohibit strikes and
    lockouts, declaration of strikes and  lockouts as illegal, and provisions relating to lay -off
    and retrenchment and closure.  Chapter -VI  contains pro visions of various penalties under the
    Act.  Chapter –VII contains miscellaneous  provisions.  Definition of Industrial Disputes  An
    industrial dispute may be defined as a conflict or difference of opinion between management  and
    workers on the terms of employm ent. It is a disagreement between an employer and
  [4] source=Labour-Act  score=0.7439
     Reopening of closed undertakings.   Unfair labour practices.   Recovery of money due from
    employer.   Penalties.    Obligations and rights of employees.    When to consult and refer a
    dispute   When a dispute arises with the workers' union.    When there is a plan to change
    employment conditions.   When there is a strike.    When there is a lock-out.    When there
    is retrenchment of workmen.    When undertaking is being transferred    On closure of an
    establishment.    On re-opening establishment.      Offences/Penalties under the Act  77
    Section     Offence     Penalty     Sec.25-Q  Lay-Off or Retrenchment without prior  permission
    - Contravening the provisions of  Section 25-M or 25-(N)   Workman entitled to all benefits as
    if  they had not been laid off. Employer  shall be punishable with  imprisonment upto 1 month
    and / or  fine upto Rs. 1000.      Sec.25-R(1)  Illegal Closure: - Closing down an undertaking
    without complying with the provisions of
  [5] source=Labour-Act  score=0.7199
    carrying on any business, trade, manufacture or distribution of goods and services irrespective of
    the  number of workmen employed therein.   Every person employed in an establishment for hire or
    reward including contract labour, apprentices  and part time employees to do any manual,
    clerical, skilled, unskilled, technical, operational or  supervisory work, is covered by the
    Act.   This Act though does not apply to persons mainly in managerial or administrative
    capacity, persons  engaged in a supervisory capacity and drawing > 1600 p.m or executing
    managerial functions and  persons subject to Army Act, Air Force and Navy Act or those in police
    service or officer or employee  of a prison.  Important provisions of the Act   Defines
    industry, industrial dispute, layoff, lockout, retrenchment, trade union, strike,  wages,
    workman etc.   Provides machinery for inve stigating and settling disputes through works
    committees,

### Expected answer — sentence grounding checklist
- [ ] S / U — Retrenchment under the Industrial Disputes Act refers to the process of reducing the workforce in an industrial establishment
- [ ] S / U — This typically involves terminating the employment of workers as a cost-cutting measure due to financial constraints, business decisions, or other reasons.
- [ ] S / U — The Act mandates that prior permission from the appropriate government authority must be obtained before laying off or retrenching any workers
- [ ] S / U — Additionally, retrenched workers are entitled to compensation as provided by the Act
- [ ] S / U — The primary objectives of this regulation are to ensure fair treatment of workers and to prevent unfair labour practices by employers in relation to lay-offs and retrenchments.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [029] What are the penalties for illegal strikes under the Labour Act?
*domain:* `labour`  ·  *expected_source:* `Labour-Act`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
     Reopening of closed undertakings.   Unfair labour practices.   Recovery of money due from
    employer.   Penalties.    Obligations and rights of employees.    When to consult and refer a
    dispute   When a dispute arises with the workers' union.    When there is a plan to change
    employment conditions.   When there is a strike.    When there is a lock-out.    When there
    is retrenchment of workmen.    When undertaking is being transferred    On closure of an
    establishment.    On re-opening establishment.      Offences/Penalties under the Act  77
    Section     Offence     Penalty     Sec.25-Q  Lay-Off or Retrenchment without prior  permission
    - Contravening the provisions of  Section 25-M or 25-(N)   Workman entitled to all benefits as
    if  they had not been laid off. Employer  shall be punishable with  imprisonment upto 1 month
    and / or  fine upto Rs. 1000.      Sec.25-R(1)  Illegal Closure: - Closing down an undertaking
    without complying with the provisions of
  [2] source=Labour-Act  score=0.9992
    in direct furtherance or support of any illegal  strike or lock-out   Imprisonment for 6 month and /
    or  fine upto Rs. 1000.      Sec.29  Breach of settlement or award binding under  the act
    Imprisonment for 6 month and / or  fine + an additional fine of Rs. 200 per  day if breach
    continues after  conviction.      Sec.30  Disclosing confidential information in  contravention
    of the provisions of Section 21   Imprisonment for 6 month and / or  fine Rs. 1000.
    Sec.30-A  Closing down any undertaking without  complying with the provisions of Section 25 -
    FFA   Imprisonment for 6 month and / or  fine Rs. 5000.     Sec.31(1)  Contravention of Section
    33 - Service  conditions remaining unchanged during  pendency of proceedings   Imprisonment for
    6 month and / or  fine Rs. 1000.     Sec.31(2)  Contravening any other provision whe re
    specific penalty is not provided for.   Fine upto Rs. 100.          Authorities Empowered By
    This Act   Name of Authority  Duties  Powers   Central
  [3] source=Labour-Act  score=0.9306
    fine upto Rs. 1000.      Sec.26 (1)  Illegal str ikes by a workman - workman who  commences,
    continues or otherwise acts in  furtherance, of, a strike which is illegal under  that Act
    Imprisonment for 1 month and / or  fine upto Rs. 50.      Sec.26 (2)  Illegal lockout -employer
    who commences,  continues, or otherwise acts in furtherance of  a lock-out which is illegal
    under this Act   Imprisonment for 1 month and / or  fine upto Rs. 1000.     Sec.27  Instigation
    - Any person who instigates or  incites others to take part in, or otherwise acts  Imprisonment
    for 6 month and / or  fine upto Rs. 1000.     78    in furtherance of, a  strike or lock -out
    which is  illegal under that Act   Sec.28  Financial Assistance to a Strike - Any person  who
    knowingly expends or applies any money  in direct furtherance or support of any illegal  strike
    or lock-out   Imprisonment for 6 month and / or  fine upto Rs. 1000.      Sec.29  Breach of
    settlement or award binding under  the act
  [4] source=Labour-Act  score=0.9031
    with the title, definitions, etc.   Chapter – II contains the various authorities under the Ac t.
    These  authorities include Conciliation Officers, Labour Courts and Tribunals.  Chapter – III
    contains the  main scheme of the Act such as reference of disputes to Labour Courts and
    Industrial Tribunals.   Chapter – IV lays down the procedure, power and d uties of the
    authorities constituted under the  Act.  Chapter – V contains provisions to prohibit strikes and
    lockouts, declaration of strikes and  lockouts as illegal, and provisions relating to lay -off
    and retrenchment and closure.  Chapter -VI  contains pro visions of various penalties under the
    Act.  Chapter –VII contains miscellaneous  provisions.  Definition of Industrial Disputes  An
    industrial dispute may be defined as a conflict or difference of opinion between management  and
    workers on the terms of employm ent. It is a disagreement between an employer and
  [5] source=Labour-Act  score=0.8923
    11. To discharge or discriminate against any workmen for filing charges or testi fying against
    employer in any enquiry or proceeding relating to any industrial dispute.  12. To recruit
    workmen during a strike which is not an illegal strike.  13. Failure to implement award,
    settlement or agreement.  14. To indulge in acts of force or violence.  15. To refuse to bargain
    collectively, in good faith with the recognized trade unions.  16. Proposing or continuing a
    lock out deemed to be illegal under this act.  If the employer of any establishment commits any
    of these acts then he will be liable fo r an offence  of unfair labour practice.    Unfair
    labour practices on the part of workmen and trade unions of workmen 147    1.  To advise or
    actively support or instigate any strike deemed to be illegal   under the Industrial  Disputes
    Act, 1947.  2.  To coerce workm en in the exercise of their right to self -organization or to
    join a trade union or

### Expected answer — sentence grounding checklist
- [ ] S / U — Penalties for illegal strikes under the Labour Act are as follows:
- [ ] S / U — 1
- [ ] S / U — **Workman participation in an illegal strike (Section 26(1))**:
- [ ] S / U — - Imprisonment for up to **1 month** and/or a fine of up to **Rs
- [ ] S / U — 50**.
- [ ] S / U — 2
- [ ] S / U — **Instigation of illegal strike (Section 27)**:
- [ ] S / U — - Imprisonment for **up to 6 months** and/or a fine of up to **Rs
- [ ] S / U — 1000**.
- [ ] S / U — 3
- [ ] S / U — **Financial assistance to support an illegal strike (Section 28)**:
- [ ] S / U — - Imprisonment for **up to 6 months** and/or a fine of up to **Rs
- [ ] S / U — 1000**.
- [ ] S / U — These penalties apply to workmen and individuals involved in furthering illegal strikes as defined by the Act.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---

## [030] What is the procedure for lay-off under the Industrial Disputes Act?
*domain:* `labour`  ·  *expected_source:* `Labour-Act`

**✅ expected source present in retrieval**

### Retrieved chunks
  [1] source=Labour-Act  score=1.0000
    workmen and which is connected with the employment or non -employment or the terms of  employment or
    with the conditions of labour, of any person.    Objective of the Act  The objective of the
    Industrial Disputes Act is to secure industrial peace and harmony by providing  machinery and
    procedure for the investigation and settlement of industrial disputes by negotiations.   The Act
    also lays down:   (a) The provision for payment of compensation to the Workman on account of
    closure or lay  off or retrenchment.   (b) The procedure for prior permission of appropriate
    Government for laying off or  retrenching the workers or closing down industrial establishments
    (c) Unfair labour practices on part of an employer or a trade union or workers.    Applicability
    The Industrial Disputes Act extends to whole of India and applies to every industrial
    establishment  carrying on any business, trade, manufacture or distribution of goods and
    services irrespective of the
  [2] source=Labour-Act  score=0.9761
    Disputes Act is to secure industrial  peace and harmony by providing  machinery and procedure for
    the  investigation and settlement of  industrial disputes by negotiations.  This Act applies to
    every industrial  establishment carrying on any  business, trade, manufacture or  distribution
    of goods and services  irrespective of the number of  workmen employed therein. Every  person
    employed in an  establishment for hire or reward  including contract labour,  apprentices and
    part time employees  to do any manual, clerical, skilled,  unskilled, technical, operational or
    supervisory work, is covered by the  Act.    Prevention of unfair labour  practices.   Prior
    permission of  appropriate Government /  concerned labour authority for  laying off or
    retrenching the  workers or closing down the  industrial establishment.   Payment of
    compensation to  workers on account of closure  or lay off or retrenchment.  Industrial
    Employment  and Standing Orders  Act , 1946
  [3] source=Labour-Act  score=0.8321
    with the title, definitions, etc.   Chapter – II contains the various authorities under the Ac t.
    These  authorities include Conciliation Officers, Labour Courts and Tribunals.  Chapter – III
    contains the  main scheme of the Act such as reference of disputes to Labour Courts and
    Industrial Tribunals.   Chapter – IV lays down the procedure, power and d uties of the
    authorities constituted under the  Act.  Chapter – V contains provisions to prohibit strikes and
    lockouts, declaration of strikes and  lockouts as illegal, and provisions relating to lay -off
    and retrenchment and closure.  Chapter -VI  contains pro visions of various penalties under the
    Act.  Chapter –VII contains miscellaneous  provisions.  Definition of Industrial Disputes  An
    industrial dispute may be defined as a conflict or difference of opinion between management  and
    workers on the terms of employm ent. It is a disagreement between an employer and
  [4] source=Labour-Act  score=0.7031
    factories employing more than 10  people and working with the aid of  power or employing 20 people
    and  working without the aid of power. It  covers all workers employed in the  factory premises
    or precincts directly  or through an agency including a  contractor, involved in any  
    Licensing and renewal of  licence under the Act.   Provision of adequate safety  measures
    within the factory  premises.   Provision of adequate welfare  measures like creche, canteen,
    wash room etc for the  workers.   Payment of wages as per the 138    manufacture. Some
    provisions of the  Act will vary according to the nature  of work of the establishment.
    provisions of the Act.   Payment of overtime wages.   Maintenance of registers.   Submission
    of returns.  Industrial Disputes Act ,  1947  The objective of the Industrial  Disputes Act is
    to secure industrial  peace and harmony by providing  machinery and procedure for the
    investigation and settlement of  industrial disputes by negotiations.
  [5] source=Labour-Act  score=0.5509
    An industrial dispute may be defined as a conflict or difference of opinion between management  and
    workers on the terms of employm ent. It is a disagreement between an employer and  employees'
    representative; usually a trade union, over pay and other working conditions and can  result in
    industrial actions. When an industrial dispute occurs, both the parties, that is the  management
    and the workmen, try to pressurize each other. The management may resort to  lockouts while the
    workers may resort to strikes, picketing or gheraos.  As per Section 2(k) of Industrial Disputes
    Act, 1947, an industrial dispute is defined as any dispute or  difference between employees and
    employers, or between employers and workmen, or between 75    workmen and which is connected
    with the employment or non -employment or the terms of  employment or with the conditions of
    labour, of any person.    Objective of the Act

### Expected answer — sentence grounding checklist
- [ ] S / U — The procedure for lay-off under the Industrial Disputes Act includes the following steps:
- [ ] S / U — 1
- [ ] S / U — **Prior Permission**: Employers must obtain prior permission from the appropriate government or concerned labour authority before laying off any workers
- [ ] S / U — This applies to cases of lay-off, retrenchment, or closure of industrial establishments.
- [ ] S / U — 2
- [ ] S / U — **Payment of Compensation**: If a lay-off occurs, the employer is obliged to pay compensation to the affected workmen
- [ ] S / U — This is outlined in the Act to ensure financial support during the lay-off period.
- [ ] S / U — 3
- [ ] S / U — **Regulatory Compliance**: Employers must comply with the provisions set forth in the Industrial Disputes Act and any relevant Labour laws, which include ensuring transparency and adherence to specified procedures when implementing a lay-off.
- [ ] S / U — These steps are designed to secure industrial peace and harmonize employer-employee relations within the workforce.

### Verdict (fill in)
- [ ] Expected answer is fully grounded — keep as is
- [ ] Rewrite expected answer to only what chunks support
- [ ] Retrieval gap — fix chunking/indexing, not the answer
- [ ] Abstention case — expected answer should say 'not in context'
- [ ] Factual conflict with PDF — verify against source, correct ground truth

---
