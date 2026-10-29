import random
from core import *
from tail import W
# Samarqand uslubidagi 42-topshiriq: reaksiya tenglamalarini tugallash (shartlar bilan), 2- va 4-reaksiya mahsulotlarini nomlash.
RX=[
("CH3–CH=CH2 + KMnO4 + H2O (0 °C) →","3CH3–CH=CH2 + 2KMnO4 + 4H2O → 3CH3–CH(OH)–CH2OH + 2MnO2↓ + 2KOH","propandiol-1,2",'alk'),
("CH3–CH=CH2 + HBr →","CH3–CH=CH2 + HBr → CH3–CHBr–CH3 (Markovnikov qoidasi)","2-brompropan",'alk'),
("CH2=CH–CH=CH2 + Br2 (1 : 1, 1,4-birikish) →","CH2=CH–CH=CH2 + Br2 → BrCH2–CH=CH–CH2Br","1,4-dibrombuten-2",'alk'),
("C6H5–CH3 + KMnO4 + H2SO4 (t) →","5C6H5–CH3 + 6KMnO4 + 9H2SO4 → 5C6H5–COOH + 3K2SO4 + 6MnSO4 + 14H2O","benzoy kislota",'ar'),
("C6H5–CH3 + Cl2 (yorug'lik) →","C6H5–CH3 + Cl2 → C6H5–CH2Cl + HCl","xlormetilbenzol (benzilxlorid)",'ar'),
("C6H5–NO2 + H2 (Ni, t) →","C6H5–NO2 + 3H2 → C6H5–NH2 + 2H2O","anilin",'ar'),
("CH3–C≡CH + 2HCl →","CH3–C≡CH + 2HCl → CH3–CCl2–CH3","2,2-dixlorpropan",'alk'),
("CH3–CHCl–CH3 + KOH (spirtli eritma, t) →","CH3–CHCl–CH3 + KOH → CH3–CH=CH2 + KCl + H2O","propen",'hal'),
("CH3–CHCl–CH3 + KOH (suvli eritma) →","CH3–CHCl–CH3 + KOH → CH3–CH(OH)–CH3 + KCl","propanol-2",'hal'),
("CH3–CH(OH)–CH3 + CuO (t) →","CH3–CH(OH)–CH3 + CuO → CH3–CO–CH3 + Cu + H2O","propanon",'oh'),
("H2N–CH2–COOH + NaOH →","H2N–CH2–COOH + NaOH → H2N–CH2–COONa + H2O","natriy aminoetanoat (glitsinat)",'am'),
("H2N–CH2–COOH + HCl →","H2N–CH2–COOH + HCl → [H3N–CH2–COOH]Cl","glitsin gidroxloridi",'am'),
("C6H5–OH + Br2 (suvli eritma) →","C6H5–OH + 3Br2 → C6H2Br3–OH↓ + 3HBr","2,4,6-tribromfenol",'ar'),
("HCOOCH3 + NaOH (t) →","HCOOCH3 + NaOH → HCOONa + CH3OH","metanol (va natriy formiat)",'es'),
("CH3–CHO + H2 (Ni, t) →","CH3–CHO + H2 → CH3–CH2–OH","etanol",'ald'),
("CH≡CH + H2O (Hg²⁺, H⁺) →","CH≡CH + H2O → CH3–CHO","etanal",'alk'),
("CH3–CH2–OH + CH3–COOH (H2SO4, t) ⇌","CH3–CH2–OH + CH3–COOH ⇌ CH3–COO–CH2–CH3 + H2O","etilatsetat (etil etanoat)",'es'),
("CH3–NH2 + HCl →","CH3–NH2 + HCl → [CH3–NH3]Cl","metilammoniy xlorid",'am'),
("2CH3–Cl + 2Na →","2CH3–Cl + 2Na → CH3–CH3 + 2NaCl","etan",'hal'),
("CH3–CH2–OH (H2SO4 kons., 170 °C) →","CH3–CH2–OH → CH2=CH2 + H2O","etilen",'oh'),
("C6H6 + HNO3 (H2SO4 kons., t) →","C6H6 + HNO3 → C6H5–NO2 + H2O","nitrobenzol",'ar'),
("CH3–CH2–CH(OH)–CH3 (H2SO4 kons., t) →","CH3–CH2–CH(OH)–CH3 → CH3–CH=CH–CH3 + H2O (Zaysev qoidasi)","buten-2",'oh'),
("CH3–COOH + Cl2 (P, t) →","CH3–COOH + Cl2 → CH2Cl–COOH + HCl","xlorsirka kislota",'acid'),
("C6H5–NH2 + Br2 (suvli eritma) →","C6H5–NH2 + 3Br2 → C6H2Br3–NH2↓ + 3HBr","2,4,6-tribromanilin",'ar'),
("CH3–CH2–CHO + Ag2O (NH3, t) →","CH3–CH2–CHO + Ag2O → CH3–CH2–COOH + 2Ag↓","propan kislota",'ald'),
("C6H12O6 (bijg'ish) →","C6H12O6 → 2C2H5OH + 2CO2↑","etanol (va karbonat angidrid)",'ug'),
("2CH3–CH2–OH (H2SO4 kons., 140 °C) →","2CH3–CH2–OH → CH3–CH2–O–CH2–CH3 + H2O","dietil efir (etoksietan)",'oh'),
("CH3–CH=CH–CH3 + H2O (H⁺) →","CH3–CH=CH–CH3 + H2O → CH3–CH(OH)–CH2–CH3","butanol-2",'alk'),
("H2N–CH2–COOH + H2N–CH2–COOH →","2H2N–CH2–COOH → H2N–CH2–CO–NH–CH2–COOH + H2O","glitsilglitsin (dipeptid)",'am'),
]
def w42_complete(r):
    for _ in range(100):
        pick=r.sample(RX,7)
        if len(set(x[3] for x in pick))>=5: break
    text=("Organik moddalarning xossalarini bilgan holda reaksiya tenglamalarini tugallang va tenglashtiring. 3- va 5-reaksiyalarda hosil bo'lgan asosiy organik mahsulotlarni sistematik nomenklatura bo'yicha nomlang. "
          "Hosil bo'lgan organik moddalarning tuzilish formulalarini yozing.")
    bands=["%s"%x[0] for x in pick]
    sol=[]
    for i,x in enumerate(pick):
        s=x[1]
        if i in (2,4): s+=" — nomi: **%s**"%x[2]
        sol.append(s)
    score=[(4,0),(4,0),(3,0),(4,0),(4,0),(3,0),(3,0)]
    return W("42",text,bands,sol,score)
