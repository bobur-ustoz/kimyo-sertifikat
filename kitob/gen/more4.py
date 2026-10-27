from core import *
from more3 import W,SC41,SC43,f2
import math
def lg(x): return math.log10(x)
# ===================================================================== 41 — umumiy kimyo (yangi turlar)
def w41_oleum(r):
    x=r.choice([0.5,1,2]); y=r.choice([0.25,0.5,1]); w=r.choice([200,300,400,500]); m=98*x+80*y
    tot=x+y; msol=m+w; om=tot*98/msol*100; wso3=80*y/m*100
    naoh=2*tot*40; Vnaoh=naoh/0.10/1.11; ba=tot*233
    text="Tarkibida %s mol H2SO4 va %s mol SO3 bo'lgan oleum namunasi %d g suvda eritildi."%(f2(x,2),f2(y,2),w)
    bands=["Oleumdagi SO3 ning massa ulushini (%) hisoblang.","SO3 suv bilan reaksiyaga kirishgandan so'ng eritmadagi H2SO4 ning umumiy miqdorini (mol) toping (reaksiya tenglamasini yozing).","Hosil bo'lgan eritmadagi H2SO4 ning massa ulushini (%) aniqlang.","Shu eritmani to'liq neytrallash uchun zichligi 1,11 g/ml bo'lgan 10 % li NaOH eritmasidan necha ml kerak?","Eritmaga mo'l BaCl2 eritmasi qo'shilganda hosil bo'ladigan cho'kma massasini (g) toping."]
    sol=["m(oleum) = %s·98 + %s·80 = %s g; ω(SO3) = %s/%s = **%s %%**"%(f2(x),f2(y),f2(m),f2(80*y),f2(m),f2(wso3,2)),"SO3 + H2O → H2SO4: n = %s + %s = **%s mol**"%(f2(x,2),f2(y,2),f2(tot,2)),"m(H2SO4) = %s·98 = %s g; m(eritma) = %s + %d = %s g → **%s %%**"%(f2(tot,2),f2(tot*98),f2(m),w,f2(msol),f2(om,2)),"H2SO4 + 2NaOH → Na2SO4 + 2H2O: m(NaOH) = %s g; eritma %s g; V = %s/1,11 = **%s ml**"%(f2(naoh),f2(naoh/0.1),f2(naoh/0.1),f2(Vnaoh,1)),"H2SO4 + BaCl2 → BaSO4↓ + 2HCl: %s·233 = **%s g**"%(f2(tot,2),f2(ba,2))]
    bands[4]+=" Hosil bo'lgan eritmaning zichligi 1,4 g/ml bo'lsa, uning molyar konsentratsiyasini (mol/l) toping."; sol[4]+="; C = 10·ω·ρ/M = 10·%s·1,4/98 = **%s mol/l**"%(f2(om,2),f2(om*1.4*10/98,2))
    bands[1]+=" Hosil bo'lgan eritmadagi suvning massasini (g) ham hisoblang."; sol[1]+="; m(H2O) = %d − 18·%s = **%s g**"%(w,f2(y,2),f2(w-18*y,2))
    bands[3]+=" Hosil bo'lgan Na2SO4 massasini (g) ham toping."; sol[3]+="; m(Na2SO4) = %s·142 = **%s g**"%(f2(tot,2),f2(tot*142,2))
    return W("41",text,bands,sol,SC41)
def w41_vant(r):
    g=r.choice([2,3,4]); dT=r.choice([20,30,40]); k=dT//10; t1=g**k*r.choice([1,2,3])
    a=r.choice([('2NO + O2 → 2NO2',2,1,['NO','O2']),('2SO2 + O2 → 2SO3',2,1,['SO2','O2']),('H2 + I2 → 2HI',1,1,['H2','I2']),('N2 + 3H2 → 2NH3',1,3,['N2','H2'])])
    eq,pa,pb,nm=a; c0=r.choice([0.1,0.2]); v0=r.choice([1,2,4])*1e-3
    kk=v0/(c0**pa*c0**pb); f_v=2**(pa+pb)
    text="Elementar %s reaksiyasi 30 °C da %d minutda tugaydi. Reaksiyaning temperatura koeffitsiyenti γ = %d. Boshlang'ich konsentratsiyalar [%s] = [%s] = %s mol/l bo'lganda boshlang'ich tezlik %s mol/(l·min) ga teng."%(eq,t1,g,nm[0],nm[1],f2(c0,2),fmt(v0*1000,0)+'·10⁻³')
    bands=["Reaksiya tezligi konstantasini (k) hisoblang va kinetik tenglamani yozing.","Harorat %d °C ga oshirilganda reaksiya tezligi necha marta ortadi?"%dT,"Harorat %d °C ga oshirilganda reaksiya necha minutda tugaydi?"%dT,"Idish hajmi 2 marta kamaytirilsa, 30 °C da tezlik necha marta o'zgaradi?","%s ning konsentratsiyasini 3 marta oshirib, %s niki o'zgarmasa, tezlik necha marta o'zgaradi?"%(nm[0],nm[1])]
    sol=["v = k·[%s]^%d·[%s]^%d; k = %s/(%s^%d·%s^%d) = **%s**"%(nm[0],pa,nm[1],pb,fmt(v0,5),f2(c0,2),pa,f2(c0,2),pb,f2(kk,3)),"v₂/v₁ = γ^(ΔT/10) = %d^%d = **%d marta**"%(g,k,g**k),"t₂ = %d/%d = **%s min**"%(t1,g**k,f2(t1/g**k,2)),"2^(%d+%d) = **%d marta ortadi**"%(pa,pb,f_v),"3^%d = **%d marta ortadi**"%(pa,3**pa)]
    bands[4]+=" Shuningdek harorat 30 °C dan 10 °C gacha pasaytirilsa tezlik necha marta kamayadi?"; sol[4]+="; %d^2 = **%d marta kamayadi**"%(g,g**2)
    bands[3]+=" Idish hajmi 3 marta oshirilsa tezlik necha marta kamayadi?"; sol[3]+="; 3^%d = **%d marta kamayadi**"%(pa+pb,3**(pa+pb))
    return W("41",text,bands,sol,SC41)
def w41_gasmix(r):
    nco=r.choice([0.1,0.2,0.3]); nco2=r.choice([0.1,0.2,0.05]); V=(nco+nco2)*22.4; m=28*nco+44*nco2; D=m/(nco+nco2)/2
    o2=nco/2*22.4; mna=nco2*106; mf=m/(nco+nco2)
    text="CO va CO2 dan iborat gazlar aralashmasi (n.sh.) %s l hajm egallaydi va massasi %s g."%(f2(V,2),f2(m,2))
    bands=["Aralashmadagi gazlarning mol miqdorlarini hisoblang.","Aralashmaning vodorodga nisbatan zichligini va gazlarning hajmiy ulushlarini (%) aniqlang.","Aralashmani to'liq yoqish uchun zarur kislorod hajmini (l, n.sh.) toping.","Yonishdan keyingi gazlar mo'l NaOH eritmasidan o'tkazildi. Hosil bo'lgan Na2CO3 massasini (g) hisoblang (CO2 + 2NaOH → Na2CO3 + H2O).","Aralashmaning o'rtacha molyar massasini (g/mol) toping."]
    sol=["x + y = %s; 28x + 44y = %s → n(CO) = **%s mol**, n(CO2) = **%s mol**"%(f2(nco+nco2,2),f2(m,2),f2(nco,2),f2(nco2,2)),"M = %s; D(H2) = **%s**; φ(CO) = %s %%, φ(CO2) = %s %%"%(f2(mf,2),f2(D,2),f2(nco/(nco+nco2)*100,1),f2(nco2/(nco+nco2)*100,1)),"2CO + O2 → 2CO2: %s mol · 0,5 · 22,4 = **%s l**"%(f2(nco,2),f2(o2,2)),"CO2 jami = %s mol → Na2CO3 = %s mol = **%s g**"%(f2(nco+nco2,2),f2(nco+nco2,2),f2((nco+nco2)*106,2)),"M(o'rt.) = m/n = **%s g/mol**"%f2(mf,2)]
    bands[4]+=" Shu miqdor CO ni yoqish uchun havo (21 % O2) hajmi qancha (l, n.sh.)?"; sol[4]+="; V(havo) = %s/0,21 = **%s l**"%(f2(o2,2),f2(o2/0.21,2))
    bands[1]+=" Aralashmaning to'liq massasini (g) ham ayting."; sol[1]+="; m = **%s g**"%f2(m,2)
    bands[3]+=" NaOH sarfini (g) ham toping."; sol[3]+="; m(NaOH) = 2·%s·40 = **%s g**"%(f2(nco+nco2,2),f2((nco+nco2)*80,2))
    return W("41",text,bands,sol,SC41)
ISO=[('³⁵Cl','³⁷Cl',35,37,75,'Cl'),('⁶³Cu','⁶⁵Cu',63,65,70,'Cu'),('¹⁰B','¹¹B',10,11,20,'B'),('⁷⁹Br','⁸¹Br',79,81,50,'Br'),('²⁴Mg','²⁶Mg',24,26,80,'Mg')]
NZ={'Cl':17,'Cu':29,'B':5,'Br':35,'Mg':12}
def w41_isotope(r):
    a,b,ma,mb,pa,el=r.choice(ISO); avg=(ma*pa+mb*(100-pa))/100; Z=NZ[el]; n=r.choice([0.5,1,2]); mm=r.choice([7.1,14.2,28.4,71]) if el=='Cl' else r.choice([6.4,12.8,32,64])
    NA=6.02
    nat=mm/avg; nhv=nat*(100-pa)/100; neu=nat*((ma-Z)*pa+(mb-Z)*(100-pa))/100
    text="Tabiiy %s ikki izotopdan iborat: %s (%d %%) va %s (%d %%). %s g shu element namunasi olingan (Z = %d, N_A = 6,02·10²³)."%({'Cl':'xlor','Cu':'mis','B':'bor','Br':'brom','Mg':'magniy'}[el],a,pa,b,100-pa,f2(mm,2),Z)
    bands=["Elementning o'rtacha nisbiy atom massasini hisoblang.","Namunadagi atomlarning umumiy miqdorini (mol) toping.","Og'irroq izotop (%s) atomlarining miqdorini (mol) hisoblang."%b,"Namunadagi neytronlarning umumiy miqdorini (mol) toping.","Namunadagi atomlar sonini (10²³ birligida) aniqlang."]
    sol=["Ar = (%d·%d + %d·%d)/100 = **%s**"%(ma,pa,mb,100-pa,f2(avg,2)),"n = %s/%s = **%s mol**"%(f2(mm,2),f2(avg,2),f2(nat,3)),"n(%s) = %s·%d/100 = **%s mol**"%(b,f2(nat,3),100-pa,f2(nhv,3)),"N(neytron) = Σ (A − Z)·ulush: **%s mol**"%f2(neu,3),"N = n·N_A = %s·6,02·10²³ = **%s·10²³**"%(f2(nat,3),f2(nat*NA,2))]
    bands[4]+=" Namunadagi protonlar sonining neytronlar soniga nisbatini ham toping."; sol[4]+="; n(p)/n(n) = %s/%s = **%s**"%(f2(Z*nat,3),f2(neu,3),f2(Z*nat/neu,3))
    bands[1]+=" Namunadagi protonlar sonini (mol) ham toping."; sol[1]+="; n(p) = Z·n = %d·%s = **%s mol**"%(Z,f2(nat,3),f2(Z*nat,3))
    bands[3]+=" Bitta atom massasini (g) ham hisoblang."; sol[3]+="; m(atom) = %s/(6,02·10²³) = **%s·10⁻²³ g**"%(f2(avg,2),f2(avg/6.02,2))
    return W("41",text,bands,sol,SC41)
HY=[('CH3COONa','CH3COOH',82,1e-5),('CH3COONa','CH3COOH',82,1e-4),('NaNO2','HNO2',69,5e-4),('HCOONa','HCOOH',68,1e-4)]
def w41_hydrol(r):
    s,ac,M_,Ka=r.choice(HY); c=r.choice([0.1,0.01,1]); Kw=1e-14; Kh=Kw/Ka; OH=math.sqrt(Kh*c); pH=14+lg(OH); h=OH/c*100; V=0.5; m=c*V*M_
    text="%s tuzining %s mol/l li suvli eritmasi berilgan. %s ning dissotsilanish konstantasi Ka = %s, K(suv) = 1·10⁻¹⁴."%(s,f2(c,3),ac,('%s·10^%d'%(fmt(Ka/10**math.floor(lg(Ka)),1),math.floor(lg(Ka)))))
    bands=["Tuzning gidrolizlanish reaksiyasi tenglamasini yozing va gidroliz konstantasini (Kh) hisoblang.","Eritmadagi OH⁻ ionlarining konsentratsiyasini (mol/l) toping.","Eritmaning pH ini hisoblang.","Gidrolizlanish darajasini (%) aniqlang.","Shunday eritmadan 500 ml tayyorlash uchun necha gramm %s kerak?"%s]
    sol=["%s + H2O ⇄ %s + NaOH; Kh = Kw/Ka = **%s**"%(s,ac,('%s·10^%d'%(fmt(Kh/10**math.floor(lg(Kh)),2),math.floor(lg(Kh)))) ),"[OH⁻] = √(Kh·c) = **%s·10^%d mol/l**"%(fmt(OH/10**math.floor(lg(OH)),2),math.floor(lg(OH))),"pOH = %s → **pH = %s**"%(f2(-lg(OH),2),f2(pH,2)),"h = [OH⁻]/c = **%s %%**"%f2(h,4),"m = c·V·M = %s·0,5·%s = **%s g**"%(f2(c,3),fmt(M_),f2(m,2))]
    bands[4]+=" Eritma 10 marta suyultirilsa gidrolizlanish darajasi necha marta ortadi?"; sol[4]+="; h ~ 1/√c: √10 = **3,16 marta**"
    bands[1]+=" pOH ni ham hisoblang."; sol[1]+="; pOH = −lg[OH⁻] = **%s**"%f2(-lg(OH),2)
    bands[3]+=" Eritmadagi H⁺ konsentratsiyasini (mol/l) ham toping."; sol[3]+="; [H⁺] = 10⁻¹⁴/[OH⁻] = **%s mol/l**"%(lambda e:'%s·10^%d'%(fmt(1e-14/OH/10**e,2),e))(math.floor(lg(1e-14/OH)))
    return W("41",text,bands,sol,SC41)
FAR=[('CuSO4','Cu',64,2,'AgNO3','Ag',108,1),('CuCl2','Cu',64,2,'AgNO3','Ag',108,1),('CuSO4','Cu',64,2,'AgNO3','Ag',108,1),('NiSO4','Ni',59,2,'AgNO3','Ag',108,1)]
def w41_far2(r):
    s1,m1,M1,z1,s2,m2,M2,z2=r.choice([x for x in FAR if x[0]!='NiSO4'])
    n1=r.choice([0.05,0.1,0.2]); Q_=n1*z1*96500; I=r.choice([5,10,2]); t=int(Q_//I) if Q_%I==0 else None
    if t is None: I=5; t=int(Q_//I)
    ne=n1*z1; n2=ne/z2; m1m=n1*M1; m2m=n2*M2
    text="Ketma-ket ulangan ikkita elektrolizyorda %s va %s eritmalari inert elektrodlar bilan elektroliz qilindi. Birinchi elektrolizyorning katodida %s g %s ajraldi (F = 96500 C/mol)."%(s1,s2,f2(m1m,2),m1)
    bands=["Elektrolizyordan o'tgan zaryad miqdorini (C) hisoblang.","Tok kuchi %d A bo'lsa, elektroliz necha sekund davom etgan?"%I,"Ikkinchi elektrolizyorning katodida ajralgan %s massasini (g) aniqlang."%m2,"Birinchi elektrolizyor anodida ajralgan gaz hajmini (l, n.sh.) toping.","Ikkala elektrolizyorda o'tgan elektronlar sonini (mol) taqqoslab, ularning teng ekanligini isbotlang."]
    gas=('O2' if 'SO4' in s1 else 'Cl2'); vg=(ne/4 if gas=='O2' else ne/2)*22.4
    sol=["n(%s) = %s mol; Q = n·z·F = %s·%d·96500 = **%s C**"%(m1,f2(n1,3),f2(n1,3),z1,fmt(Q_,0)),"t = Q/I = %s/%d = **%d s**"%(fmt(Q_,0),I,t),"n(e⁻) = %s mol; n(%s) = %s/%d = %s mol → **%s g**"%(f2(ne,3),m2,f2(ne,3),z2,f2(n2,3),f2(m2m,2)),"%s: n = %s mol → **%s l**"%(gas,f2(ne/4 if gas=='O2' else ne/2,3),f2(vg,2)),"Ketma-ket ulanishda har bir elektrolizyordan bir xil zaryad o'tadi: n(e⁻) = %s mol ikkala holda"%f2(ne,3)]
    bands[4]+=" Agar tok kuchi 2 marta oshirilsa, shuncha zaryad o'tishi uchun necha sekund kerak?"; sol[4]+="; t = %d/2 = **%d s**"%(t,t//2)
    bands[1]+=" O'tgan elektronlar miqdorini (mol) ham toping."; sol[1]+="; n(e⁻) = Q/F = **%s mol**"%f2(ne,3)
    bands[3]+=" Ikkinchi elektrolizyor katodida ajralgan metallning miqdorini (mol) ham toping."; sol[3]+="; n(%s) = **%s mol**"%(m2,f2(n2,3))
    return W("41",text,bands,sol,SC41)
EQM=[('magniy','Mg',24,12),('rux','Zn',65,32.5),('kalsiy','Ca',40,20),('alyuminiy','Al',27,9),('temir (II)','Fe',56,28)]
def w41_equiv(r):
    nm,sy,Ar,E=r.choice(EQM); V=r.choice([1.12,2.24,3.36,4.48]); m=V*E/11.2; ox=m+m*8/E
    val=Ar/E
    text="%s g noma'lum metall kislota bilan to'liq reaksiyaga kirishib, %s l (n.sh.) vodorod ajratdi. (Vodorodning ekvivalent hajmi V_E(H2) = 11,2 l/mol.)"%(f2(m,2),f2(V,2))
    bands=["Metallning ekvivalent massasini (g/mol) hisoblang.","Metallning valentligi %d bo'lsa, uning atom massasini hisoblab, metallni aniqlang."%round(val),"Shu metallning oksidi formulasini yozing va molyar massasini hisoblang.","%s g metall to'liq yonganda hosil bo'lgan oksid massasini (g) toping."%f2(m,2),"Yonishga sarflangan kislorod hajmini (l, n.sh.) aniqlang."]
    oxf={'Mg':'MgO','Zn':'ZnO','Ca':'CaO','Al':'Al2O3','Fe':'FeO'}[sy]; Mox=M(oxf)
    sol=["E = m·11,2/V = %s·11,2/%s = **%s g/mol**"%(f2(m,2),f2(V,2),f2(E,2)),"Ar = E·valentlik = %s·%d = %s → **%s**"%(f2(E,2),round(val),f2(Ar,1),sy),"**%s**, M = **%s g/mol**"%(oxf,fmt(Mox)),"m(oksid) = m + m(O) = %s + %s·8/%s = **%s g**"%(f2(m,2),f2(m,2),f2(E,2),f2(ox,2)),"m(O) = %s g = %s mol O → n(O2) = %s mol → **%s l**"%(f2(m*8/E,2),f2(m/E/2,3),f2(m/E/4,3),f2(m/E/4*22.4,2))]
    bands[4]+=" Shuningdek metall xloridida (MCl2) metallning massa ulushini (%) toping."; sol[4]+="; ω = %s/(%s + 71) = **%s %%**"%(fmt(Ar),fmt(Ar),f2(Ar/(Ar+71)*100,1))
    bands[1]+=" Ajralgan vodorodning massasini (g) ham hisoblang."; sol[1]+="; m(H2) = %s/11,2 = **%s g**"%(f2(V,2),f2(V/11.2,3))
    bands[3]+=" Metall oksidining ekvivalent massasini (g/mol) ham aniqlang."; sol[3]+="; E(oksid) = E(Me) + 8 = **%s g/mol**"%f2(E+8,2)
    return W("41",text,bands,sol,SC41)
def w41_molar(r):
    w,rho=r.choice([(20,1.14),(40,1.30),(30,1.22),(49,1.39),(10,1.07)]); M_=98
    C=10*w*rho/M_; Cn=2*C; mol=w*rho*10/ (M_*(100-w)/100) /1000 *1000/ (rho*10*(100-w)/100) if False else (w/M_)/((100-w)/1000)
    V=r.choice([100,250,500]); c2=r.choice([0.1,0.2,0.5]); vol=c2*V/C
    naoh=2*C*0.1*40
    text="Sulfat kislotaning massa ulushi %d %% bo'lgan eritmasining zichligi %s g/ml."%(w,f2(rho,2))
    bands=["Eritmaning molyar konsentratsiyasini (mol/l) hisoblang.","Eritmaning normal konsentratsiyasini (ekv/l) toping.","Eritmaning molyal konsentratsiyasini (mol/kg) aniqlang.","Shu eritmadan %d ml %s mol/l li eritma tayyorlash uchun necha ml olish kerak?"%(V,f2(c2,2)),"100 ml shu eritmani to'liq neytrallash uchun necha gramm NaOH kerak?"]
    sol=["C = 10·ω·ρ/M = 10·%d·%s/98 = **%s mol/l**"%(w,f2(rho,2),f2(C,3)),"Cn = 2C = **%s ekv/l**"%f2(Cn,3),"%d g H2SO4 %d g suvda: n = %s mol → **%s mol/kg**"%(w,100-w,f2(w/98,3),f2(w/98/((100-w)/1000),3)),"V₁ = C₂V₂/C₁ = %s·%d/%s = **%s ml**"%(f2(c2,2),V,f2(C,3),f2(vol,2)),"n(H2SO4) = %s·0,1 = %s mol; NaOH = 2·%s·40 = **%s g**"%(f2(C,3),f2(C*0.1,3),f2(C*0.1,3),f2(naoh,2))]
    bands[4]+=" 250 ml shu eritmadagi H2SO4 massasini (g) ham hisoblang."; sol[4]+="; m = C·V·M = %s·0,25·98 = **%s g**"%(f2(C,3),f2(C*0.25*98,2))
    bands[1]+=" Sulfat kislotaning ekvivalent massasini (g/ekv) ham aniqlang."; sol[1]+="; E = 98/2 = **49 g/ekv**"
    bands[3]+=" 100 ml eritmadagi suvning massasini (g) ham hisoblang."; sol[3]+="; m(eritma) = 100·%s = %s g; suv = **%s g**"%(f2(rho,2),f2(100*rho,1),f2(100*rho*(100-w)/100,1))
    return W("41",text,bands,sol,SC41)
W41M=[w41_oleum,w41_vant,w41_gasmix,w41_isotope,w41_hydrol,w41_far2,w41_equiv,w41_molar]
