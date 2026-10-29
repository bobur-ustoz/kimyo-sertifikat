import random
from core import *
from tail import W
from more3 import SC41, f2
# Samarqand darajasidagi 41-topshiriqlar: uzviy ketma-ket jarayonlar, noma'lum modda/kation, normal bo'lmagan sharoitda gaz (PV = nRT).
R=8.314

# ---------- A) Fe(II) sulfat kristallogidrati: H2O2 bilan oksidlash, cho'ktirish, kuydirish ----------
def w41_iron(r):
    nw=r.choice([4,5,7]); a=r.choice([0.05,0.1,0.2]); T=400; P=83.14; vm=R*T/P
    Mc=152+18*nw; m=a*Mc; mH2O2sol=a/2*34/0.034
    text=("Tarkibi FeSO4·nH2O bo'lgan kristallogidratning %s g namunasi suvda eritildi va unga sulfat kislota hamda %s g 3,4 %% li vodorod peroksid eritmasi qo'shildi "
          "(H2O2 va H2SO4 qoldiqsiz sarflandi, Fe²⁺ to'liq oksidlandi). Hosil bo'lgan eritmaga mo'l NaOH eritmasi qo'shilib, cho'kma ajratildi va doimiy massagacha kuydirildi. "
          "Kuydirish vaqtida ajralgan suv bug'i 127 °C va 83,14 kPa da o'lchandi (R = 8,314 J/(mol·K)).")%(f2(m,2),f2(mH2O2sol,0))
    bands=["Oksidlash, cho'ktirish va kuydirish reaksiyalarining tenglamalarini yozing va tenglashtiring.",
           "Kristallogidratdagi n ni aniqlang (tarkibini yozing).",
           "Kuydirishdan hosil bo'lgan qattiq moddaning massasini (g) toping.",
           "Fe³⁺ ni to'liq cho'ktirish uchun sarflangan NaOH miqdorini (mol) hisoblang.",
           "Kuydirishda ajralgan suv bug'ining hajmini (l) aniqlang."]
    sol=["2FeSO4 + H2O2 + H2SO4 → Fe2(SO4)3 + 2H2O; Fe2(SO4)3 + 6NaOH → 2Fe(OH)3↓ + 3Na2SO4; 2Fe(OH)3 → Fe2O3 + 3H2O (t)",
         "n(H2O2) = %s·0,034/34 = %s mol → n(FeSO4) = 2·%s = %s mol; M(kristallogidrat) = %s/%s = %s g/mol; 152 + 18n = %s → n = %s: **FeSO4·%sH2O**"%(f2(mH2O2sol,0),f2(a/2,3),f2(a/2,3),f2(a,3),f2(m,2),f2(a,3),f2(Mc,0),f2(Mc,0),nw,nw),
         "n(Fe2O3) = n(Fe)/2 = %s mol → m = %s·160 = **%s g**"%(f2(a/2,3),f2(a/2,3),f2(a/2*160,2)),
         "n(NaOH) = 3·n(Fe³⁺) = 3·%s = **%s mol**"%(f2(a,3),f2(3*a,3)),
         "n(H2O) = 3·%s = %s mol; V = nRT/P = %s·8,314·400/83,14 = **%s l**"%(f2(a/2,3),f2(1.5*a,3),f2(1.5*a,3),f2(1.5*a*vm,2))]
    return W("41",text,bands,sol,SC41)

# ---------- B) KMnO4 qisman parchalanishi + konts. HCl ----------
def w41_kmno4(r):
    n0,d=r.choice([(0.2,0.5),(0.2,0.8),(0.3,0.6),(0.4,0.5),(0.4,0.75)]); nO2=n0*d/2; T=300; P=83.14; vm=R*T/P
    m0=n0*158; mres=m0-32*nO2; VO2=nO2*vm
    text=("%s g KMnO4 qizdirilganda qisman parchalandi (2KMnO4 → K2MnO4 + MnO2 + O2). Ajralgan kislorodning hajmi 27 °C va 83,14 kPa da %s l ga teng bo'ldi (R = 8,314 J/(mol·K)). "
          "Qattiq qoldiq mo'l konsentrlangan xlorid kislota bilan qizdirildi (K2MnO4, MnO2 va parchalanmay qolgan KMnO4 ning barchasi reaksiyaga kirishdi).")%(f2(m0,1),f2(VO2,2))
    Cl=2.5*n0-2*nO2; HCl=8*n0-4*nO2; salts=n0*(74.5+126)
    bands=["Parchalanish va qattiq qoldiqning xlorid kislota bilan reaksiyalarini yozing va tenglashtiring (elektron balans).",
           "KMnO4 ning necha foizi parchalanganini aniqlang.",
           "Qattiq qoldiq massasini (g) va undagi MnO2 ning massa ulushini (%) toping.",
           "Ajralgan xlorning umumiy hajmini (l, n.sh.) va sarflangan HCl miqdorini (mol) hisoblang.",
           "Reaksiyadan so'ng eritmadagi tuzlarning (KCl va MnCl2) umumiy massasini (g) toping."]
    sol=["2KMnO4 → K2MnO4 + MnO2 + O2↑; K2MnO4 + 8HCl → 2KCl + MnCl2 + 2Cl2 + 4H2O; MnO2 + 4HCl → MnCl2 + Cl2 + 2H2O; 2KMnO4 + 16HCl → 2KCl + 2MnCl2 + 5Cl2 + 8H2O",
         "n(O2) = PV/RT = %s mol; parchalangan KMnO4 = 2·%s = %s mol; n(KMnO4) = %s/158 = %s mol → **%s %%**"%(f2(nO2,3),f2(nO2,3),f2(2*nO2,3),f2(m0,1),f2(n0,3),f2(d*100,0)),
         "m(qoldiq) = %s − 32·%s = **%s g**; MnO2: %s mol · 87 = %s g → ω = **%s %%**"%(f2(m0,1),f2(nO2,3),f2(mres,2),f2(nO2,3),f2(nO2*87,2),f2(nO2*87/mres*100,1)),
         "Cl2: 2·%s + %s + 2,5·%s = %s mol → **%s l**; HCl: 8·%s + 4·%s + 8·%s = **%s mol**"%(f2(nO2,3),f2(nO2,3),f2(n0-2*nO2,3),f2(Cl,3),f2(Cl*22.4,2),f2(nO2,3),f2(nO2,3),f2(n0-2*nO2,3),f2(HCl,3)),
         "Kaliy balansi: n(KCl) = n(K) = %s mol (%s g); Mn balansi: n(MnCl2) = %s mol (%s g); jami **%s g**"%(f2(n0,3),f2(n0*74.5,2),f2(n0,3),f2(n0*126,2),f2(salts,2))]
    return W("41",text,bands,sol,SC41)

# ---------- E) termit jarayoni, noma'lum metall ----------
OXM=[('Fe',56,'Fe2O3',160),('Cr',52,'Cr2O3',152)]
def w41_thermite(r):
    M,Ar,ox,Mox=r.choice(OXM); b=r.choice([0.1,0.2]); e=r.choice([0.1,0.2]); a=2*b+e
    m=27*a+Mox*b; V1=1.5*e*22.4; V2=2*b*22.4
    text=("Alyuminiy kukuni va noma'lum M2O3 oksidi aralashmasi (jami %s g) qizdirilganda reaksiya oxirigacha bordi (M — oksidlanish darajasi +3 bo'lgan metall, M ning oksidlanish darajasi xlorid kislotada +2 ga o'tadi). "
          "Hosil bo'lgan qattiq mahsulot mo'l NaOH eritmasi bilan ishlanganda %s l (n.sh.) gaz ajraldi; erimay qolgan qoldiq esa mo'l xlorid kislota bilan %s l (n.sh.) gaz ajratdi.")%(f2(m,1),f2(V1,2),f2(V2,2))
    bands=["Termit jarayoni, mahsulotning NaOH va HCl bilan reaksiyalarini yozing va tenglashtiring.",
           "Aralashmadagi alyuminiyning umumiy miqdorini (mol) va ortib qolgan alyuminiy miqdorini hisoblang.",
           "Noma'lum M metallni aniqlang.",
           "Reaksiyada hosil bo'lgan Al2O3 massasini (g) toping.",
           "Mahsulotdagi ortiqcha alyuminiy va Al2O3 ni to'liq eritish uchun zichligi 1,22 g/ml bo'lgan 20 % li NaOH eritmasidan necha ml kerak? (Al2O3 + 2NaOH + 3H2O → 2Na[Al(OH)4]; 2Al + 2NaOH + 6H2O → 2Na[Al(OH)4] + 3H2)"]
    nNaOH=e+2*b; vol=nNaOH*40/0.2/1.22
    sol=["2Al + M2O3 → Al2O3 + 2M; 2Al + 2NaOH + 6H2O → 2Na[Al(OH)4] + 3H2↑ (Al2O3 ham NaOH da eriydi, gaz bermaydi); M + 2HCl → MCl2 + H2↑",
         "Ortiqcha Al: n = %s/(1,5·22,4) = **%s mol**; M ning miqdori: n(M) = %s/22,4 = %s mol → termitda sarflangan Al = %s mol; Al jami = %s + %s = **%s mol**"%(f2(V1,2),f2(e,2),f2(V2,2),f2(2*b,2),f2(2*b,2),f2(2*b,2),f2(e,2),f2(a,2)),
         "n(M2O3) = %s mol; m(Al) = %s g; m(M2O3) = %s − %s = %s g; M(M2O3) = %s/%s = %s → Ar(M) = (%s − 48)/2 = %s: **%s**"%(f2(b,2),f2(27*a,2),f2(m,1),f2(27*a,2),f2(m-27*a,2),f2(m-27*a,2),f2(b,2),f2(Mox,0),f2(Mox,0),f2(Ar,0),M),
         "n(Al2O3) = n(M2O3) = %s mol → m = %s·102 = **%s g**"%(f2(b,2),f2(b,2),f2(b*102,2)),
         "n(NaOH) = n(Al ort.) + 2·n(Al2O3) = %s + 2·%s = %s mol → m = %s g (100 %%) → 20 %% li eritma %s g → V = **%s ml**"%(f2(e,2),f2(b,2),f2(nNaOH,2),f2(nNaOH*40,1),f2(nNaOH*40/0.2,1),f2(vol,1))]
    text+=" Natriy tetragidroksoalyuminat saqlagan eritmadan mo'l CO2 o'tkazildi, hosil bo'lgan cho'kma qizdirilib, qoldiq Na2CO3 bilan suyuqlantirildi."
    bands+=["Eritmadan CO2 o'tkazilganda hosil bo'lgan cho'kma massasini (g) toping.","Cho'kma qizdirilganda hosil bo'lgan oksid massasini (g) hisoblang.","Oksid Na2CO3 bilan suyuqlantirilganda ajralgan gaz hajmini (l, n.sh.) aniqlang."]
    sol+=["Jami Al = %s mol (ortiqcha %s + Al2O3 dan 2·%s) → Na[Al(OH)4] + CO2 → Al(OH)3↓ + NaHCO3: **%s g**"%(f2(a,2),f2(e,2),f2(b,2),f2(78*a,2)),"2Al(OH)3 → Al2O3 + 3H2O: %s mol → **%s g**"%(f2(a/2,3),f2(a/2*102,2)),"Al2O3 + Na2CO3 → 2NaAlO2 + CO2: **%s l**"%f2(a/2*22.4,2)]
    return W("41",text,bands,sol,SC41)

# ---------- H) NO2 + O2 ning suvda yutilishi (ortiqcha komponent), gaz qonunlari ----------
def w41_no2o2(r):
    case=r.choice(['o2','no2']); T=300; P=83.14; vm=R*T/P
    if case=='o2':
        a=r.choice([0.4,0.8,1.2]); res=r.choice([0.1,0.2]); b=a/4+res; vres=res*vm; hno3=a; resname='O2'
        extra=46*a+32*(a/4); rem_n=res
    else:
        b=r.choice([0.1,0.2]); ex=r.choice([0.3,0.6]); a=4*b+ex; hno3=4*b+2*ex/3; vres=ex/3*vm; resname='NO'; extra=46*a+32*b-30*ex/3; rem_n=ex/3
    vmix=(a+b)*vm; W0=r.choice([300,500]); msol=W0+extra
    text=("NO2 va O2 aralashmasi (27 °C, 83,14 kPa da hajmi %s l) %d g suvga yuborildi. "
          "Yutilmay qolgan gaz hajmi shu sharoitda %s l bo'ldi. R = 8,314 J/(mol·K).")%(f2(vmix,1),W0,f2(vres,1))
    mmix=46*a+32*b
    bands=["Reaksiya tenglamalarini yozing va qaysi gaz ortiqcha bo'lganini aniqlang.",
           "Dastlabki aralashmadagi NO2 va O2 ning mol miqdorlarini hamda hajmiy ulushlarini (%) toping.",
           "Hosil bo'lgan eritmadagi HNO3 ning massasini (g) va massa ulushini (%) hisoblang.",
           "Dastlabki aralashmadagi NO2 va O2 ning massalarini (g) toping.",
           "Dastlabki aralashmaning havoga nisbatan zichligini (M(havo) = 29 g/mol) aniqlang."]
    sol=["Ortiqcha gaz: **%s** (yutilmay qolgan). "%resname+("4NO2 + O2 + 2H2O → 4HNO3" if case=='o2' else "4NO2 + O2 + 2H2O → 4HNO3; ortiqcha NO2: 3NO2 + H2O → 2HNO3 + NO↑"),
         "n(umumiy) = PV/RT = %s mol; qoldiq %s = %s mol. "%(f2(a+b,2),resname,f2(rem_n,2))+("a = NO2, b − a/4 = %s → NO2 = **%s mol**, O2 = **%s mol**"%(f2(res,2),f2(a,2),f2(b,2)) if case=='o2' else "NO = ex/3 = %s → ortiqcha NO2 = %s; 4b + ex = %s: NO2 = **%s mol**, O2 = **%s mol**"%(f2(rem_n,2),f2(3*rem_n,2),f2(a,2),f2(a,2),f2(b,2)))+"; φ(NO2) = %s %%, φ(O2) = %s %%"%(f2(a/(a+b)*100,1),f2(b/(a+b)*100,1)),
         "n(HNO3) = %s mol → m = %s g; eritma massasi = %d + %s = %s g → ω = **%s %%**"%(f2(hno3,3),f2(hno3*63,2),W0,f2(extra,2),f2(msol,2),f2(hno3*63/msol*100,2)),
         "m(NO2) = 46·%s = **%s g**; m(O2) = 32·%s = **%s g**"%(f2(a,2),f2(46*a,2),f2(b,2),f2(32*b,2)),
         "M(o'rt) = (46·%s + 32·%s)/%s = %s g/mol → D(havo) = **%s**"%(f2(a,2),f2(b,2),f2(a+b,2),f2(mmix/(a+b),2),f2(mmix/(a+b)/29,2))]
    text+=" Olingan nitrat kislota eritmasiga stexiometrik miqdorda CaCO3 qo'shildi, hosil bo'lgan tuz eritmasi bug'latilib, qoldiq doimiy massagacha qizdirildi, ajralgan gazlar suvga yuttirildi."
    bands+=["Kislotani neytrallash uchun sarflangan CaCO3 massasini (g) va ajralgan CO2 hajmini (l, n.sh.) toping.","Bug'latib qizdirilgandan keyin qolgan qattiq moddaning massasini (g) hisoblang.","Ajralgan gazlar suvga yuttirilganda qayta hosil bo'lgan HNO3 massasini (g) aniqlang."]
    sol+=["2HNO3 + CaCO3 → Ca(NO3)2 + CO2 + H2O: n(CaCO3) = %s mol → **%s g**; CO2 **%s l**"%(f2(hno3/2,3),f2(hno3/2*100,2),f2(hno3/2*22.4,2)),"2Ca(NO3)2 → 2CaO + 4NO2 + O2: CaO = %s mol → **%s g**"%(f2(hno3/2,3),f2(hno3/2*56,2)),"NO2 = %s mol, O2 = %s mol (4 : 1) → 4NO2 + O2 + 2H2O → 4HNO3: **%s g**"%(f2(hno3,3),f2(hno3/4,3),f2(hno3*63,2))]
    return W("41",text,bands,sol,SC41)

NEW41=[w41_iron,w41_kmno4,w41_thermite,w41_no2o2]
