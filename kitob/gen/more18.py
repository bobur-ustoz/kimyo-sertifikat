import random, math
from fractions import Fraction
from core import *
# 33-35: 5 bosqichli hikoyalar; 39-40: kasr/nisbat va bosqichli organik qisqa javoblar. Shartda reaksiya tenglamalari va "nima reaksiyaga kirishadi" izohlari yo'q.
V=22.4; F=96500
def _f(x,nd=2): return fmt(x,nd)

def st_alloy_oh(r):
    a,b=r.choice([(0.1,0.2),(0.2,0.1),(0.2,0.2),(0.1,0.3)]); m=65*a+56*b; vh=(a+b)*V
    txt="Rux va temir qotishmasi (%s g) mo'l suyultirilgan H2SO4 da eritilganda %s l (n.sh.) gaz ajraldi. Hosil bo'lgan eritmaga mo'l NaOH eritmasi qo'shilib, cho'kma ajratildi, havoda to'liq oksidlanguncha tutildi va doimiy massagacha kuydirildi."%(_f(m,2),_f(vh,2))
    qs=["Qotishmadagi temirning massasini (g) aniqlang.","Kuydirishdan so'ng qolgan qattiq moddaning massasini (g) toping.","Cho'kmani oksidlashga sarflangan kislorodning hajmini (l, n.sh.) hisoblang."]
    vals=[56*b,80*b,b/4*V]
    s=["Zn va Fe ikkalasi H2 beradi: x + y = %s/22,4 = %s; 65x + 56y = %s → x = %s, y = %s → m(Fe) = %s g"%(_f(vh,2),_f(a+b,2),_f(m,2),_f(a,2),_f(b,2),_f(56*b,2)),"Zn(OH)2 ishqorda eriydi, cho'kmada faqat Fe(OH)2 → Fe(OH)3 → Fe2O3: n(Fe2O3) = %s/2 → %s g"%(_f(b,2),_f(80*b,2)),"4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3: n(O2) = %s/4 = %s mol → %s l"%(_f(b,2),_f(b/4,3),_f(b/4*V,2))]
    return txt,qs,vals,s,"9-sinf (rux, temir; amfoterlik; gidroksidlarning oksidlanishi)"
def st_nitrate_ext(r):
    a=r.choice([0.1,0.2]); Wt=r.choice([200,300]); fe=r.choice([0.5,0.6,0.8]); I=10; t=round(2*F*fe*a/I)
    m=a*188; sol0=Wt+m; w1=126*a/(Wt+108*a)*100; w2=m/sol0*100; cu=fe*a*64
    txt="%s g Cu(NO3)2 doimiy massagacha qizdirildi, ajralgan gazlar aralashmasi sovitilib %d g suvga yuborildi. Qoldiq hosil bo'lgan eritmada to'liq eritildi (kislota qoldiqsiz sarflandi), so'ng eritma inert elektrodlar bilan %d A tok kuchida %d s elektroliz qilindi."%(_f(m,1),Wt,I,t)
    qs=["Gazlar yutilgach hosil bo'lgan kislotaning massa ulushini (%) toping.","Qoldiq erigandan keyin eritmada tuzning massa ulushini (%) hisoblang.","Elektrolizda katodda ajralgan metall massasini (g) aniqlang."]
    vals=[w1,w2,cu]
    s=["NO2 %s mol, O2 %s mol → HNO3 %s mol = %s g; eritma %d + %s g → %s %%"%(_f(2*a),_f(a/2,3),_f(2*a),_f(126*a,1),Wt,_f(108*a,1),_f(w1,2)),"Tuz qaytadan hosil bo'ladi: %s g / (%d + %s) = %s %%"%(_f(m,1),Wt,_f(m,1),_f(w2,2)),"Q = %d·%d = %d C → n(Cu) = %s mol → %s g"%(I,t,I*t,_f(fe*a,3),_f(cu,2))]
    return txt,qs,vals,s,"9-sinf; 11-sinf (nitratlar; elektroliz)"
def st_nacl_burn(r):
    I,t=r.choice([(5,1930),(10,965),(10,1930)]); Wt=r.choice([100,200]); n=I*t/F; m=n*58.5*r.choice([2,3])
    hcl=n*36.5; sol1=Wt+hcl; naoh=n*40/0.1; sol2=sol1+naoh; nacl=n*58.5
    txt="%s g NaCl suvda eritilib, eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi. Ajralgan gazlar aralashmasi yondirilib, hosil bo'lgan gaz %d g suvda eritildi, olingan eritma 10 %% li NaOH eritmasi bilan to'liq neytrallandi."%(_f(m,2),I,t,Wt)
    qs=["Olingan kislota eritmasining massa ulushini (%) hisoblang.","Neytrallash uchun sarflangan 10 % li NaOH eritmasining massasini (g) toping.","Neytrallangan eritmada tuzning massa ulushini (%) aniqlang."]
    vals=[hcl/sol1*100,naoh,nacl/sol2*100]
    s=["n(e⁻) = %s mol → H2 = Cl2 = %s mol → HCl = %s mol = %s g; ω = %s %%"%(_f(n,3),_f(n/2,3),_f(n,3),_f(hcl,2),_f(vals[0],2)),"HCl %s mol → NaOH %s mol = %s g → 10 %% li eritma %s g"%(_f(n,3),_f(n,3),_f(n*40,2),_f(naoh,1)),"NaCl %s mol = %s g; eritma = %s + %s = %s g → %s %%"%(_f(n,3),_f(nacl,2),_f(sol1,1),_f(naoh,1),_f(sol2,1),_f(vals[2],2))]
    return txt,qs,vals,s,"9-sinf; 11-sinf (elektroliz; vodorod xlorid; neytrallanish)"
def st_hydrate_red(r):
    a=r.choice([0.1,0.2,0.4]); m=a*250
    txt="%s g CuSO4·5H2O suvda eritilib, eritmaga mo'l NaOH qo'shildi; hosil bo'lgan cho'kma ajratilib qizdirildi, so'ng hosil bo'lgan qattiq modda vodorod oqimida to'liq qaytarildi."%_f(m,1)
    qs=["Qizdirishdan hosil bo'lgan qattiq moddaning massasini (g) aniqlang.","Qaytarishga sarflangan vodorodning hajmini (l, n.sh.) toping.","Oxirida olingan oddiy moddaning massasini (g) hisoblang."]
    vals=[a*80,a*V,a*64]
    s=["Cu(OH)2 → CuO + H2O: %s mol → %s g"%(_f(a,3),_f(a*80,2)),"CuO + H2 → Cu + H2O: V = %s·22,4 = %s l"%(_f(a,3),_f(a*V,2)),"Cu: %s mol → %s g"%(_f(a,3),_f(a*64,2))]
    return txt,qs,vals,s,"9-sinf (mis birikmalari; qaytarilish)"
def st_nh3_ext(r):
    a=r.choice([2,4,8]); e1=r.choice([Fraction(3,4),Fraction(4,5),Fraction(9,10)]); e2=r.choice([Fraction(4,5),Fraction(3,4),Fraction(1,2)])
    hn=a*float(e1)*float(e2); koh=hn
    txt="%d mol ammiak katalizator ishtirokida kislorod bilan oksidlandi: birinchi bosqichda uning %d/%d qismi azot(II) oksidga aylandi, hosil bo'lgan azot(II) oksidning %d/%d qismi esa nitrat kislotagacha qayta ishlandi. Olingan kislota mo'l KOH bilan neytrallandi."%(a,e1.numerator,e1.denominator,e2.numerator,e2.denominator)
    qs=["Hosil bo'lgan nitrat kislota massasini (g) hisoblang.","Neytrallanishda hosil bo'lgan tuz massasini (g) toping.","Neytrallash uchun sarflangan KOH massasini (g) aniqlang."]
    vals=[hn*63,hn*101,koh*56]
    s=["n(NO) = %d·%d/%d = %s mol; HNO3 = %s·%d/%d = %s mol → %s g"%(a,e1.numerator,e1.denominator,_f(a*float(e1),3),_f(a*float(e1),3),e2.numerator,e2.denominator,_f(hn,3),_f(hn*63,2)),"HNO3 + KOH → KNO3 + H2O: %s mol → %s g"%(_f(hn,3),_f(hn*101,2)),"KOH: %s mol → %s g"%(_f(hn,3),_f(koh*56,2))]
    return txt,qs,vals,s,"9-sinf (ammiak, nitrat kislota, nitratlar)"
def st_org_chain(r):
    n=r.choice([1,2]); y=r.choice([Fraction(4,5),Fraction(3,4),Fraction(9,10)]); fr=r.choice([Fraction(2,3),Fraction(1,2),Fraction(3,4)])
    et=2*n*float(y); ac=et*float(fr)
    txt="%d mol glyukoza spirtli bijg'ishga uchradi (unum %d/%d). Hosil bo'lgan etanolning %d/%d qismi sirka kislotagacha oksidlandi; olingan kislota mo'l NaHCO3 eritmasi bilan ta'sirlashtirildi."%(n,y.numerator,y.denominator,fr.numerator,fr.denominator)
    qs=["Hosil bo'lgan etanol massasini (g) toping.","Oksidlanishdan hosil bo'lgan sirka kislota massasini (g) hisoblang.","NaHCO3 bilan ajralgan gazning hajmini (l, n.sh.) aniqlang."]
    vals=[et*46,ac*60,ac*V]
    s=["C6H12O6 → 2C2H5OH + 2CO2: n(C2H5OH) = 2·%d·%s = %s mol → %s g"%(n,_f(float(y),3),_f(et,3),_f(et*46,2)),"CH3COOH = %s·%s = %s mol → %s g"%(_f(et,3),_f(float(fr),3),_f(ac,3),_f(ac*60,2)),"CH3COOH + NaHCO3 → CH3COONa + CO2↑ + H2O: %s mol → %s l"%(_f(ac,3),_f(ac*V,2))]
    return txt,qs,vals,s,"10-sinf (uglevodlar, spirtlar, karbon kislotalar)"
NEWST2_OLD=[st_alloy_oh,st_nitrate_ext,st_nacl_burn,st_hydrate_red,st_nh3_ext,st_org_chain]

# ---------- elektroliz, pH, molyar konsentratsiya (CM) bilan qiyinlashtirilgan hikoyalar ----------
def st_hydrate_elec_ph(r):
    V_=r.choice([0.5,1]); p=r.choice([1,2]); x=10**(-p)*V_/2; I=5; t=round(2*F*x/I)
    n0=r.choice([x*2,x*3,x*4]); n0=round(n0,4); m=n0*250
    txt="%s g CuSO4·5H2O suvda eritilib, hajmi %d ml bo'lgan eritma tayyorlandi. Eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (eritma hajmi o'zgarmadi deb hisoblang). Elektrolizdan keyin eritmaga mo'l NaOH qo'shilib, hosil bo'lgan cho'kma ajratildi, qizdirildi, so'ng hosil bo'lgan qattiq modda vodorod oqimida to'liq qaytarildi."%(_f(m,2),round(V_*1000),I,t)
    qs=["Dastlabki eritmada CuSO4 ning molyar konsentratsiyasini (mol/l) hisoblang.","Elektroliz tugagach eritmaning pH ini aniqlang.","Oxirida olingan metall massasini (g) toping."]
    vals=[n0/V_,p,(n0-x)*64]
    s=["CM = %s/%s = %s mol/l"%(_f(n0,4),_f(V_,1),_f(n0/V_,3)),"Q = %d·%d = %d C → Cu = %s mol; 2CuSO4 + 2H2O → 2Cu + O2 + 2H2SO4: H⁺ = 2·%s = %s mol → [H⁺] = %s mol/l → pH = %d"%(I,t,I*t,_f(x,4),_f(x,4),_f(2*x,4),_f(2*x/V_,3),p),"Eritmada qolgan Cu²⁺ = %s − %s = %s mol → Cu(OH)2 → CuO → Cu: %s g"%(_f(n0,4),_f(x,4),_f(n0-x,4),_f((n0-x)*64,2))]
    return txt,qs,vals,s,"9-11-sinf (kristallogidratlar; elektroliz; pH; molyar konsentratsiya)"
def st_nacl_ph(r):
    V_=r.choice([0.5,1]); x=0.1*V_; I=5; t=round(x*F/I); c=r.choice([0.4,0.6]); n0=c*V_; Wt=r.choice([100,200])
    txt="%s mol/l li NaCl eritmasining %d ml i inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (eritma hajmi o'zgarmadi deb hisoblang). Ajralgan gazlar aralashmasi yondirilib, hosil bo'lgan gaz %d g suvda eritildi."%(_f(c,1),round(V_*1000),I,t,Wt)
    qs=["Elektrolizdan keyin eritmaning pH ini hisoblang.","Elektrolizdan keyin eritmada NaCl ning molyar konsentratsiyasini (mol/l) toping.","Olingan xlorid kislota eritmasining massa ulushini (%) aniqlang."]
    hcl=x*36.5; vals=[13,(n0-x)/V_,hcl/(Wt+hcl)*100]
    s=["n(e⁻) = %d·%d/96500 = %s mol → NaOH = %s mol → [OH⁻] = %s mol/l → pH = 13"%(I,t,_f(x,3),_f(x,3),_f(x/V_,2)),"NaCl qoldi: %s − %s = %s mol → %s mol/l"%(_f(n0,3),_f(x,3),_f(n0-x,3),_f((n0-x)/V_,3)),"H2 = Cl2 = %s mol → HCl %s mol = %s g; ω = %s/(%d + %s) = %s %%"%(_f(x/2,3),_f(x,3),_f(hcl,2),_f(hcl,2),Wt,_f(hcl,2),_f(vals[2],2))]
    return txt,qs,vals,s,"9-11-sinf (elektroliz; pH; molyar konsentratsiya)"
def st_nitrate_ph(r):
    a=r.choice([0.1,0.2]); V_=a*20; fe=r.choice([0.5,0.8]); I=10; t=round(2*F*fe*a/I)
    txt="%s g Cu(NO3)2 doimiy massagacha qizdirildi, ajralgan gazlar suvga yuttirilib, hajmi %s l bo'lgan eritma tayyorlandi. Qoldiq shu eritmada to'liq eritildi (kislota qoldiqsiz sarflandi), olingan eritma (hajmi o'zgarmadi deb hisoblang) %d A tok kuchi bilan %d s inert elektrodlarda elektroliz qilindi."%(_f(a*188,1),_f(V_,1),I,t)
    qs=["Gazlar yutilgach hosil bo'lgan eritmaning pH ini aniqlang.","Qoldiq erigandan so'ng Cu(NO3)2 ning molyar konsentratsiyasini (mol/l) hisoblang.","Elektrolizda katodda ajralgan metall massasini (g) toping."]
    vals=[1,a/V_,fe*a*64]
    s=["HNO3 = 2·%s = %s mol → [H⁺] = %s/%s = %s mol/l → pH = 1"%(_f(a,2),_f(2*a,2),_f(2*a,2),_f(V_,1),_f(2*a/V_,2)),"CuO + 2HNO3 → Cu(NO3)2 + H2O: n = %s mol → CM = %s/%s = %s mol/l"%(_f(a,2),_f(a,2),_f(V_,1),_f(a/V_,3)),"Q = %d·%d = %d C → Cu = %s mol → %s g"%(I,t,I*t,_f(fe*a,3),_f(fe*a*64,2))]
    return txt,qs,vals,s,"9-11-sinf (nitratlar; pH; elektroliz)"
def st_alloy_cm(r):
    a,b=r.choice([(0.1,0.2),(0.2,0.1),(0.2,0.2),(0.1,0.3)]); Vs=r.choice([0.5,1]); m=65*a+56*b; vh=(a+b)*V
    txt="Rux va temir qotishmasi (%s g) mo'l suyultirilgan H2SO4 da eritilganda %s l (n.sh.) gaz ajraldi; hosil bo'lgan eritmaning hajmi %d ml. Eritmaga mo'l NaOH qo'shilib, cho'kma ajratildi, havoda to'liq oksidlanguncha tutildi va doimiy massagacha kuydirildi."%(_f(m,2),_f(vh,2),round(Vs*1000))
    qs=["Eritmada FeSO4 ning molyar konsentratsiyasini (mol/l) aniqlang.","Kuydirishdan so'ng qolgan qattiq moddaning massasini (g) toping.","Cho'kmani oksidlashga sarflangan kislorodning hajmini (l, n.sh.) hisoblang."]
    vals=[b/Vs,80*b,b/4*V]
    s=["x + y = %s; 65x + 56y = %s → x = %s, y = %s; CM(FeSO4) = %s/%s = %s mol/l"%(_f(a+b,2),_f(m,2),_f(a,2),_f(b,2),_f(b,2),_f(Vs,1),_f(b/Vs,3)),"Zn(OH)2 ishqorda eriydi; cho'kmada Fe(OH)2 → Fe(OH)3 → Fe2O3: %s g"%_f(80*b,2),"4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3: %s mol → %s l"%(_f(b/4,3),_f(b/4*V,2))]
    return txt,qs,vals,s,"9-sinf; 11-sinf (rux, temir; amfoterlik; molyar konsentratsiya)"
def st_nh3_ph(r):
    a=r.choice([2,4,8]); e1=r.choice([Fraction(3,4),Fraction(4,5),Fraction(9,10)]); e2=r.choice([Fraction(4,5),Fraction(3,4),Fraction(1,2)])
    hn=a*float(e1)*float(e2); V_=hn*10
    txt="%d mol ammiakning %d/%d qismi azot(II) oksidga oksidlandi, hosil bo'lgan oksidning %d/%d qismi nitrat kislotagacha qayta ishlandi. Kislota suvda eritilib, hajmi %s l bo'lgan eritma tayyorlandi, so'ng eritma mo'l KOH bilan neytrallandi."%(a,e1.numerator,e1.denominator,e2.numerator,e2.denominator,_f(V_,2))
    qs=["Hosil bo'lgan nitrat kislota massasini (g) hisoblang.","Kislota eritmasining pH ini aniqlang.","Neytrallash uchun sarflangan KOH massasini (g) toping."]
    vals=[hn*63,1,hn*56]
    s=["NO = %s mol; HNO3 = %s·%d/%d = %s mol → %s g"%(_f(a*float(e1),3),_f(a*float(e1),3),e2.numerator,e2.denominator,_f(hn,3),_f(hn*63,2)),"[H⁺] = %s/%s = 0,1 mol/l → pH = 1"%(_f(hn,3),_f(V_,2)),"KOH: %s mol → %s g"%(_f(hn,3),_f(hn*56,2))]
    return txt,qs,vals,s,"9-sinf; 11-sinf (ammiak; nitrat kislota; pH)"
def st_org_ph(r):
    n=r.choice([1,2]); y=r.choice([Fraction(4,5),Fraction(3,4),Fraction(9,10)]); fr=r.choice([Fraction(2,3),Fraction(1,2),Fraction(3,4)])
    et=2*n*float(y); ac=et*float(fr); V_=ac*10
    txt="%d mol glyukoza spirtli bijg'ishga uchradi (unum %d/%d). Hosil bo'lgan etanolning %d/%d qismi sirka kislotagacha oksidlandi; olingan kislota suvda eritilib, hajmi %s l bo'lgan eritma tayyorlandi (kislotaning dissotsilanish darajasi 1 %%). Shu miqdordagi sirka kislota mo'l NaHCO3 bilan ham ta'sirlashtirildi."%(n,y.numerator,y.denominator,fr.numerator,fr.denominator,_f(V_,2))
    qs=["Hosil bo'lgan etanol massasini (g) toping.","Sirka kislota eritmasining pH ini hisoblang.","NaHCO3 bilan ajralgan gazning hajmini (l, n.sh.) aniqlang."]
    vals=[et*46,3,ac*V]
    s=["n(C2H5OH) = 2·%d·%s = %s mol → %s g"%(n,_f(float(y),3),_f(et,3),_f(et*46,2)),"CH3COOH = %s mol; CM = %s/%s = 0,1 mol/l; [H⁺] = 0,1·0,01 = 10⁻³ → pH = 3"%(_f(ac,3),_f(ac,3),_f(V_,2)),"CO2 = %s mol → %s l"%(_f(ac,3),_f(ac*V,2))]
    return txt,qs,vals,s,"10-11-sinf (uglevodlar, karbon kislotalar; pH; dissotsilanish darajasi)"
NEWST2=[st_hydrate_elec_ph,st_nacl_ph,st_nitrate_ph,st_alloy_cm,st_nh3_ph,st_org_ph]

# ---------------- 39-40: bosqichli, kasr/nisbatli organik qisqa javoblar ----------------
ALC=[('CH3OH',32,1),('C2H5OH',46,2),('C3H7OH',60,3),('C4H9OH',74,4)]
def s_alc_ag(r):
    nm,M_,c=r.choice(ALC); n=r.choice([0.2,0.4]); fr=r.choice([Fraction(3,4),Fraction(1,2),Fraction(2,5),Fraction(3,5)])
    if abs(float(fr)*n*10-round(float(fr)*n*10))>1e-9: fr=Fraction(1,2)
    kag=4 if c==1 else 2; ag=float(fr)*n*kag*108
    t="Bir atomli to'yingan noma'lum spirtning %s g miqdori natriy bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi. Shu spirtning %d/%d qismi mis(II) oksid bilan oksidlandi, hosil bo'lgan modda mo'l ammiakli kumush oksid eritmasi bilan qizdirildi. Ajralgan kumush massasini (g) toping."%(_f(n*M_,1),_f(n/2*V,2),fr.numerator,fr.denominator)
    return numq(t,ag,[ag/2 if kag==4 else ag*2,float(fr)*n*2*108*0.5,n*kag*108,ag*1.5],"n(H2) = %s mol → n(spirt) = %s mol; M = %s/%s = %s → %s; %s qismi = %s mol → %s (%s Ag) → %s g"%(_f(n/2,3),_f(n,3),_f(n*M_,1),_f(n,3),_f(M_,0),nm,_frac(fr),_f(float(fr)*n,3),"HCHO" if c==1 else "aldegid","4" if c==1 else "2",_f(ag,2)),"10-sinf (spirtlar, aldegidlar)",2)
def _frac(f): return "%d/%d"%(f.numerator,f.denominator)
def s_alkene_hydr(r):
    c=r.choice([('C3H6',42,'propen'),('C4H8',56,'buten'),('C5H10',70,'penten')]); n=r.choice([0.1,0.2,0.4]); fr=r.choice([Fraction(2,5),Fraction(3,4),Fraction(1,2)])
    nh=float(fr)*n; br=n*160
    t="Noma'lum alkenning %s g miqdori mo'l brom suvi bilan to'liq reaksiyaga kirishganda %s g brom sarflandi. Xuddi shu alkenning %d/%d qismi gidratlanib spirtga aylantirildi, hosil bo'lgan spirt natriy bilan ta'sirlashtirildi. Ajralgan vodorod hajmini (l, n.sh.) toping."%(_f(n*c[1],1),_f(br,1),fr.numerator,fr.denominator)
    ans=nh/2*V
    return numq(t,ans,[nh*V,ans*2,ans/2,n/2*V],"n(Br2) = %s mol = n(alken); M = %s/%s = %s → %s; gidratlangan %s mol → spirt %s mol → H2 = %s mol → %s l"%(_f(br/160,3),_f(n*c[1],1),_f(n,3),_f(c[1],0),c[2],_f(nh,3),_f(nh,3),_f(nh/2,3),_f(ans,3)),"10-sinf (alkenlar, spirtlar)",3)
ACID=[('CH3COOH',60,'sirka kislota'),('C2H5COOH',74,'propion kislota'),('C3H7COOH',88,'moy kislota')]
def s_acid_ester(r):
    nm,M_,name=r.choice(ACID); n=r.choice([0.3,0.6]); fr=r.choice([Fraction(1,3),Fraction(2,3)]); y=r.choice([Fraction(3,4),Fraction(4,5),Fraction(1,2)])
    ne=float(fr)*n*float(y); me=ne*(M_+28)
    if abs(ne*100-round(ne*100))>1e-9: fr=Fraction(1,3) if n==0.3 else Fraction(2,3); y=Fraction(3,4); ne=float(fr)*n*float(y); me=ne*(M_+28)
    t="Bir asosli to'yingan karbon kislotaning %s g miqdori mo'l NaHCO3 bilan ta'sirlashganda %s l (n.sh.) gaz ajraldi. Shu kislotaning %d/%d qismi mo'l etanol bilan esterlandi (efir unumi %d/%d). Hosil bo'lgan murakkab efirning massasini (g) toping."%(_f(n*M_,1),_f(n*V,2),fr.numerator,fr.denominator,y.numerator,y.denominator)
    return numq(t,me,[me*2,me/2,float(fr)*n*(M_+28),n*(M_+28)*float(y)],"n(CO2) = %s mol = n(kislota); M = %s → %s; esterlangan %s·%s mol, unum %s → efir (M = %s + 28 = %s) %s mol → %s g"%(_f(n,3),_f(n*M_,1),name,_frac(fr),_f(n,3),_frac(y),_f(M_,0),_f(M_+28,0),_f(ne,3),_f(me,2)),"10-sinf (karbon kislotalar, murakkab efirlar)",2)
def s_halo_fraction(r):
    c=r.choice([('C2H6',30,'etan'),('C3H8',44,'propan'),('C4H10',58,'butan')]); n=r.choice([0.5,1,2]); fr=r.choice([Fraction(1,2),Fraction(3,4),Fraction(2,5)])
    if abs(float(fr)*n*10-round(float(fr)*n*10))>1e-9: fr=Fraction(1,2)
    nc=float(fr)*n
    t="Vodorodga nisbatan zichligi %s bo'lgan alkanning %s g miqdorining %d/%d qismi yorug'likda xlor bilan monoxlorlandi, hosil bo'lgan xloralkan mo'l KOH ning suvli eritmasi bilan gidrolizlandi. Hosil bo'lgan spirtning massasini (g) toping."%(_f(c[1]/2,1),_f(n*c[1],1),fr.numerator,fr.denominator)
    ans=nc*(c[1]+16)
    return numq(t,ans,[ans*2,ans/2,nc*(c[1]+35.5-1),n*(c[1]+16)],"M = 2·%s = %s → %s; n = %s mol; %s qismi = %s mol → xloralkan → spirt (M = %s + 16): %s g"%(_f(c[1]/2,1),_f(c[1],0),c[2],_f(n,3),_frac(fr),_f(nc,3),_f(c[1],0),_f(ans,2)),"10-sinf (alkanlar, galogenli hosilalar, spirtlar)",2)
SH_ORG=[s_alc_ag,s_alkene_hydr,s_acid_ester,s_halo_fraction]

# ================= xilma-xillikni oshirish: yangi hikoyalar, qisqa javoblilar, zanjirlar =================
def st_agno3_ph(r):
    V_=r.choice([0.5,1]); p=r.choice([1,2]); x=10**(-p)*V_; I=5; t=round(x*F/I)
    n0=round(r.choice([x*2,x*3,x*4]),4)
    txt="%s mol/l li AgNO3 eritmasining %d ml i inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (eritma hajmi o'zgarmadi deb hisoblang), so'ngra eritmaga mo'l NaCl eritmasi qo'shildi."%(_f(n0/V_,2),round(V_*1000),I,t)
    qs=["Katodda ajralgan kumush massasini (g) aniqlang.","Elektrolizdan keyin (NaCl qo'shilishidan oldin) eritmaning pH ini toping.","NaCl qo'shilganda hosil bo'lgan cho'kma massasini (g) hisoblang."]
    vals=[x*108,p,(n0-x)*143.5]
    s=["n(e⁻) = %d·%d/96500 = %s mol = n(Ag) → %s g"%(I,t,_f(x,4),_f(x*108,3)),"4AgNO3 + 2H2O → 4Ag + O2 + 4HNO3: H⁺ = %s mol → [H⁺] = %s/%s = %s mol/l → pH = %d"%(_f(x,4),_f(x,4),_f(V_,1),_f(x/V_,3),p),"Qolgan Ag⁺ = %s − %s = %s mol → AgCl: %s g"%(_f(n0,4),_f(x,4),_f(n0-x,4),_f((n0-x)*143.5,2))]
    return txt,qs,vals,s,"9-11-sinf (kumush nitrat elektrolizi; pH; cho'kma)"
def st_pb_ph(r):
    V_=r.choice([0.5,1]); p=r.choice([1,2]); x=10**(-p)*V_/2; I=5; t=round(2*F*x/I)
    n0=round(r.choice([x*2,x*3]),4)
    txt="Qo'rg'oshin(II) nitratning %s mol/l li eritmasidan %d ml olinib, inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (eritma hajmi o'zgarmadi deb hisoblang). Elektrolizdan keyin eritmaga mo'l KI eritmasi qo'shildi."%(_f(n0/V_,2),round(V_*1000),I,t)
    qs=["Katodda ajralgan qo'rg'oshin massasini (g) toping.","Elektroliz tugagach eritmaning pH ini hisoblang.","KI qo'shilganda hosil bo'lgan cho'kma massasini (g) aniqlang."]
    vals=[x*207,p,(n0-x)*461]
    s=["Q = %d·%d = %d C → Pb = %s mol → %s g"%(I,t,I*t,_f(x,4),_f(x*207,3)),"2Pb(NO3)2 + 2H2O → 2Pb + O2 + 4HNO3: H⁺ = 2·%s mol → [H⁺] = %s mol/l → pH = %d"%(_f(x,4),_f(2*x/V_,3),p),"Qolgan Pb²⁺ = %s mol → PbI2: %s g"%(_f(n0-x,4),_f((n0-x)*461,2))]
    return txt,qs,vals,s,"9-11-sinf (qo'rg'oshin nitrat elektrolizi; pH; cho'kma)"
NEWST2=NEWST2+[st_agno3_ph,st_pb_ph]

def s_ester_fraction(r):
    e=r.choice([('etilatsetat',88,2),('etilformiat',74,2),('metilatsetat',74,1),('propilformiat',88,3)]); n=r.choice([0.2,0.4,0.5]); fr=r.choice([Fraction(1,2),Fraction(3,4),Fraction(2,5)])
    if abs(float(fr)*n*100-round(float(fr)*n*100))>1e-9: fr=Fraction(1,2)
    na=float(fr)*n; c=e[2]
    t="%s g %s mo'l NaOH bilan qizdirilganda uning %d/%d qismi gidrolizlandi. Hosil bo'lgan spirt to'liq yondirildi. Yondirishda ajralgan CO2 hajmini (l, n.sh.) toping."%(_f(n*e[1],1),e[0],fr.numerator,fr.denominator)
    ans=na*c*V
    return numq(t,ans,[ans*2,ans/2,n*c*V,na*V],"n(efir) = %s/%d = %s mol; gidrolizlangani %s·%s = %s mol → spirt (%d C) %s mol → CO2 = %s l"%(_f(n*e[1],1),e[1],_f(n,3),_frac(fr),_f(n,3),_f(na,3),c,_f(na,3),_f(ans,2)),"10-sinf (murakkab efirlar; spirtlarning yonishi)",2)
def s_amine_chain(r):
    n=r.choice([0.2,0.4]); y=r.choice([Fraction(3,4),Fraction(1,2),Fraction(4,5)]); fr=r.choice([Fraction(1,2),Fraction(2,5),Fraction(3,4)])
    na=n*float(y); nb=na*float(fr)
    if abs(nb*100-round(nb*100))>1e-9: y=Fraction(1,2); fr=Fraction(1,2); na=n*0.5; nb=na*0.5
    t="%s g nitrobenzol qaytarilib anilin olindi (unum %d/%d). Hosil bo'lgan anilinning %d/%d qismi mo'l bromli suv bilan ta'sirlashtirildi. Hosil bo'lgan cho'kmaning massasini (g) toping."%(_f(n*123,1),y.numerator,y.denominator,fr.numerator,fr.denominator)
    ans=nb*330
    return numq(t,ans,[ans*2,ans/2,na*330,n*float(fr)*330],"n(C6H5NO2) = %s mol; anilin = %s·%s = %s mol; bromlangani %s·%s = %s mol → 2,4,6-tribromanilin (330 g/mol): %s g"%(_f(n,3),_f(n,3),_frac(y),_f(na,3),_frac(fr),_f(na,3),_f(nb,3),_f(ans,2)),"10-sinf (nitrobirikmalar, anilin)",2)
def s_alkyne_ag(r):
    n=r.choice([0.5,1,2]); f1=r.choice([Fraction(4,5),Fraction(3,4),Fraction(1,2)]); f2=r.choice([Fraction(1,2),Fraction(2,5),Fraction(3,5)])
    na=n*float(f1); ng=na*float(f2)
    if abs(ng*100-round(ng*100))>1e-9: f1=Fraction(1,2); f2=Fraction(1,2); na=n*0.5; ng=na*0.5
    t="%s l (n.sh.) atsetilen Kucherov reaksiyasi bo'yicha gidratlandi (unum %d/%d); hosil bo'lgan aldegidning %d/%d qismi ammiakli kumush oksid eritmasi bilan qizdirildi. Ajralgan kumush massasini (g) hisoblang."%(_f(n*V,1),f1.numerator,f1.denominator,f2.numerator,f2.denominator)
    ans=ng*2*108
    return numq(t,ans,[ans*2,ans/2,na*2*108,n*2*108],"n(C2H2) = %s mol; etanal = %s·%s = %s mol; reaksiyaga kirishgani %s·%s = %s mol → Ag: 2·%s = %s mol → %s g"%(_f(n,3),_f(n,3),_frac(f1),_f(na,3),_frac(f2),_f(na,3),_f(ng,3),_f(ng,3),_f(2*ng,3),_f(ans,2)),"10-sinf (alkinlar, aldegidlar)",2)
SH_ORG=SH_ORG+[s_ester_fraction,s_amine_chain,s_alkyne_ag]
