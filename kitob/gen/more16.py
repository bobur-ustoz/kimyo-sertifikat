import random
from core import *
from tail import W
from more3 import SC41, f2
# 41/43 uchun bilvosita shartli ssenariylar: noma'lum element nisbat/ulushdan aniqlanadi, so'ng ketma-ket jarayonlar (5 band).
F=96500; V=22.4

# ---------- 41: nitrat sikli (noma'lum metall; qoldiq ulushi; yutilish; erish; elektroliz) ----------
MET=[('Cu',64),('Pb',207),('Ni',59)]
def w41_nitrate_cycle(r):
    X,Ax=r.choice(MET); a=r.choice([0.1,0.2]); Wt=r.choice([200,300]); fe=r.choice([0.5,0.6,0.8]); I=10
    Ms=Ax+124; m=a*Ms; frac=(Ax+16)/Ms*100; x=fe*a; t=round(2*F*x/I)
    sol0=Wt+m; solE=sol0-x*Ax-16*x; wN=a*Ms/sol0*100
    text=("X – oksidlanish darajasi +2 bo'lgan metall. X(NO3)2 tuzining %s g namunasi doimiy massagacha qizdirilganda hosil bo'lgan qattiq qoldiq massasi tuz massasining %s %% ini tashkil etdi. "
          "Ajralgan gazlar aralashmasi sovitilib, %d g suvga to'liq yuttirildi; so'ngra qattiq qoldiq hosil bo'lgan eritmada to'liq eritildi (kislota qoldiqsiz sarflandi). "
          "Olingan eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (X ning bir qismi eritmada qoldi).")%(f2(m,2),f2(frac,1),Wt,I,t)
    bands=["Barcha jarayonlarning reaksiya tenglamalarini yozing va tenglashtiring; qoldiq massa ulushidan foydalanib, X metallni aniqlang.",
           "Qizdirishda ajralgan gazlar tarkibini (mol) toping va ularni suvga yuttirishdan hosil bo'lgan HNO3 massasini (g) hisoblang.",
           "Qoldiq erigandan keyingi eritmada X(NO3)2 ning massa ulushini (%) hisoblang. Natijani dastlabki tuz massasi va suv massasi orqali tushuntiring.",
           "Elektrolizda katodda ajralgan metall massasini (g) va anodda ajralgan gaz hajmini (l, n.sh.) toping.",
           "Elektroliz tugagach eritmadagi X(NO3)2 va HNO3 ning massa ulushlarini (%) aniqlang."]
    sol=["2X(NO3)2 → 2XO + 4NO2↑ + O2↑; 4NO2 + O2 + 2H2O → 4HNO3; XO + 2HNO3 → X(NO3)2 + H2O; 2X(NO3)2 + 2H2O → 2X + O2 + 4HNO3 (elektroliz). Qoldiq: (Ar + 16)/(Ar + 124) = %s → Ar(X) = **%s → %s**"%(f2(frac/100,4),f2(Ax,0),X),
         "n(tuz) = %s/%s = %s mol → NO2 = %s mol, O2 = %s mol (4 : 1 – to'liq yutiladi); n(HNO3) = %s mol → **%s g**"%(f2(m,2),f2(Ms,0),f2(a,3),f2(2*a,3),f2(a/2,3),f2(2*a,3),f2(126*a,2)),
         "Eritma massasi = %d + 46·%s + 32·%s + %s = %s g; XO + 2HNO3 → X(NO3)2: tuz %s g → ω = %s/%s = **%s %%** (barcha tuz qaytadan eritmada: ω = m(tuz)/(m(tuz) + m(suv)))"%(Wt,f2(2*a),f2(a/2,3),f2(a*(Ax+16),2),f2(sol0,2),f2(m,2),f2(m,2),f2(sol0,2),f2(wN,2)),
         "Q = %d·%d = %d C; n(X) = %s/(2·96500) = %s mol → **%s g**; O2 = %s/2 = %s mol → **%s l**"%(I,t,I*t,f2(I*t,0),f2(x,3),f2(x*Ax,2),f2(x,3),f2(x/2,4),f2(x/2*V,2)),
         "Eritma massasi = %s − %s − %s = %s g; X(NO3)2 qoldi %s mol = %s g → **%s %%**; HNO3 hosil bo'ldi 2·%s = %s mol = %s g → **%s %%**"%(f2(sol0,2),f2(x*Ax,2),f2(x/2*32,2),f2(solE,2),f2(a-x,3),f2((a-x)*Ms,2),f2((a-x)*Ms/solE*100,2),f2(x,3),f2(2*x,3),f2(2*x*63,2),f2(2*x*63/solE*100,2))]
    return W("41",text,bands,sol,SC41)

# ---------- 41: noma'lum galogenid (massalar nisbati) -> oksidlash -> HX -> neytrallash ----------
HAL=[('Cl',35.5),('Br',80),('I',127)]
def w41_halide_id(r):
    X,Ax=r.choice(HAL); n=r.choice([0.1,0.2,0.4]); Wt=r.choice([100,200]);
    Ms=39+Ax; m=n*Ms; ag=n*(108+Ax); ratio=(108+Ax)/Ms
    hx=n*(1+Ax); sol1=Wt+hx; w=hx/sol1*100; naoh=n*40/0.1; sol2=sol1+naoh; nax=n*(23+Ax); wn=nax/sol2*100
    text=("KX (X – galogen) tuzining %s g namunasi mo'l AgNO3 eritmasi bilan ta'sirlashganda hosil bo'lgan cho'kma massasi tuz massasidan %s marta katta bo'ldi. "
          "Xuddi shunday massadagi KX namunasi MnO2 va sulfat kislota bilan qizdirilib, ajralgan oddiy modda vodorod bilan to'liq reaksiyaga kiritildi, hosil bo'lgan gaz %d g suvda eritildi. "
          "Olingan eritma 10 %% li NaOH eritmasi bilan to'liq neytrallandi.")%(f2(m,2),f2(ratio,3),Wt)
    bands=["KX ning AgNO3 bilan reaksiyasi tenglamasini yozing va nisbatdan foydalanib X galogenni aniqlang.",
           "KX ni MnO2 va H2SO4 bilan oksidlash reaksiyasini yozing; ajralgan oddiy moddaning massasini (g) va sarflangan MnO2 massasini (g) hisoblang.",
           "Oddiy modda vodorod bilan reaksiyaga kirishganda hosil bo'lgan HX massasini (g) va uning suvdagi eritmasida massa ulushini (%) toping.",
           "Neytrallash uchun sarflangan 10 % li NaOH eritmasining massasini (g) aniqlang.",
           "Neytrallangan eritmadagi NaX ning massa ulushini (%) hisoblang."]
    sol=["KX + AgNO3 → AgX↓ + KNO3: (108 + Ar)/(39 + Ar) = %s → Ar(X) = %s: **%s**"%(f2(ratio,3),f2(Ax,1),X),
         "2KX + MnO2 + 2H2SO4 → K2SO4 + MnSO4 + X2 + 2H2O: n(KX) = %s/%s = %s mol → X2 = %s mol → **%s g**; MnO2 = %s mol → **%s g**"%(f2(m,2),f2(Ms,1),f2(n,3),f2(n/2,3),f2(n*Ax,2),f2(n/2,3),f2(n/2*87,2)),
         "X2 + H2 → 2HX: n(HX) = %s mol → m = %s·%s = **%s g**; eritma = %d + %s = %s g → ω = **%s %%**"%(f2(n,3),f2(n,3),f2(1+Ax,1),f2(hx,2),Wt,f2(hx,2),f2(sol1,2),f2(w,2)),
         "HX + NaOH → NaX + H2O: n(NaOH) = %s mol = %s g → 10 %% li eritma **%s g**"%(f2(n,3),f2(n*40,2),f2(naoh,1)),
         "Eritma = %s + %s = %s g; m(NaX) = %s·%s = %s g → ω = **%s %%**"%(f2(sol1,2),f2(naoh,1),f2(sol2,2),f2(n,3),f2(23+Ax,1),f2(nax,2),f2(wn,2))]
    return W("41",text,bands,sol,SC41)

# ---------- 41: CuSO4 + NaCl aralashmasi elektrolizi: ketma-ket razryad va yakuniy muhit ----------
def w41_electro_mix(r):
    a=r.choice([0.1,0.2]); c=r.choice([1,3]); b=a*c; I=10
    e=max(2*a,b)+r.choice([0.2,0.4]); t=round(e*F/I)
    h=(e-2*a)/2; o=(e-b)/4; mt=160*a+58.5*b; Wt=500
    mCl=b/2*71; Hmass=2*h; Omass=32*o; Cu=64*a
    solf=Wt+mt-Cu-mCl-Hmass-Omass
    if b<2*a:
        extra=("H2SO4",a-b/2,98); medium="kislotali"; nNa2=b/2; ex_txt="H2SO4 %s mol"%f2(a-b/2,3)
    else:
        extra=("NaOH",b-2*a,40); medium="ishqoriy"; nNa2=a; ex_txt="NaOH %s mol"%f2(b-2*a,3)
    text=("%d g suvda CuSO4 va NaCl dan iborat %s g aralashma eritildi (tuzlarning mol nisbati %d : %d). Eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi "
          "(jarayonda Cu²⁺ va Cl⁻ ionlari to'liq tugadi, suv ham elektrolizga uchradi).")%(Wt,f2(mt,2),1,c,I,t)
    bands=["Katod va anodda ketma-ket boradigan jarayonlar tenglamalarini yozing; tuzlarning dastlabki miqdorlarini (mol) aniqlang.",
           "Katodda ajralgan mis massasini (g) va vodorod hajmini (l, n.sh.) hisoblang.",
           "Anodda ajralgan xlor va kislorod hajmlarini (l, n.sh.) toping.",
           "Elektroliz tugagach eritmaning muhitini (kislotali, neytral yoki ishqoriy) asoslang va undagi ortiqcha moddaning miqdorini (mol) aniqlang.",
           "Elektrolizdan keyin eritma massasini (g) va undagi Na2SO4 ning massa ulushini (%) hisoblang."]
    sol=["Katod: Cu²⁺ + 2e⁻ → Cu; so'ng 2H2O + 2e⁻ → H2 + 2OH⁻. Anod: 2Cl⁻ − 2e⁻ → Cl2; so'ng 2H2O − 4e⁻ → O2 + 4H⁺. 160x + 58,5·%d x = %s → x = n(CuSO4) = **%s mol**, n(NaCl) = **%s mol**"%(c,f2(mt,2),f2(a,3),f2(b,3)),
         "n(e⁻) = %d·%d/96500 = %s mol; Cu: 2·%s = %s mol e⁻ → Cu **%s g**; qolgan %s mol e⁻ → H2 = **%s mol = %s l**"%(I,t,f2(e,3),f2(a,3),f2(2*a,3),f2(Cu,2),f2(e-2*a,3),f2(h,3),f2(h*V,2)),
         "Cl2 = %s/2 = %s mol → **%s l**; qolgan %s mol e⁻ → O2 = %s/4 = %s mol → **%s l**"%(f2(b,3),f2(b/2,3),f2(b/2*V,2),f2(e-b,3),f2(e-b,3),f2(o,3),f2(o*V,2)),
         "Net: H⁺ = 4·%s = %s mol, OH⁻ = 2·%s = %s mol → farq %s (= 2·n(CuSO4) − n(NaCl)) → muhit **%s**; ortiqcha: **%s**"%(f2(o,3),f2(4*o,3),f2(h,3),f2(2*h,3),f2(abs(2*a-b),3),medium,ex_txt),
         "Eritma = %d + %s − %s − %s − %s − %s = **%s g**; Na2SO4: %s mol = %s g → ω = **%s %%**"%(Wt,f2(mt,2),f2(Cu,2),f2(mCl,2),f2(Hmass,2),f2(Omass,2),f2(solf,2),f2(nNa2,3),f2(nNa2*142,2),f2(nNa2*142/solf*100,2))]
    return W("41",text,bands,sol,SC41)

# ---------- 43: noma'lum metall + alyuminiy aralashmasi ----------
def w43_unknown_metal_base(r):
    X,Ax=r.choice([('Mg',24),('Fe',56)]); a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2,0.3])
    m=27*a+Ax*b; V1=1.5*a*V; V2=(1.5*a+b)*V
    text=("Alyuminiy va noma'lum X metalldan (X – oksidlanish darajasi +2 bo'lgan metall) iborat %s g aralashma mo'l NaOH eritmasi bilan ta'sirlashganda %s l (n.sh.) gaz ajraldi. "
          "Shunday massali ikkinchi namuna mo'l xlorid kislotada eritilganda %s l (n.sh.) gaz ajraldi. Xlorid kislotali eritmaga mo'l NaOH eritmasi qo'shilib, cho'kma ajratildi, havoda to'liq oksidlanguncha tutildi va kuydirildi; "
          "filtratdan mo'l CO2 o'tkazildi.")%(f2(m,2),f2(V1,2),f2(V2,2))
    bands=["Barcha reaksiyalarning tenglamalarini yozing va tenglashtiring.",
           "Aralashmadagi Al va X ning miqdorlarini (mol) aniqlang va X metallni toping.",
           "Aralashmadagi metallarning massa ulushlarini (%) hisoblang.",
           "Kuydirishdan hosil bo'lgan qattiq moddaning formulasini aniqlang va massasini (g) hisoblang.",
           "Filtratdan CO2 o'tkazilganda hosil bo'lgan cho'kma massasini (g) toping."]
    if X=='Mg': solid,Msol,eq="MgO",b*40,"Mg(OH)2 → MgO + H2O"
    else: solid,Msol,eq="Fe2O3",b/2*160,"4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3; 2Fe(OH)3 → Fe2O3 + 3H2O"
    sol=["2Al + 2NaOH + 6H2O → 2Na[Al(OH)4] + 3H2↑; 2Al + 6HCl → 2AlCl3 + 3H2↑; X + 2HCl → XCl2 + H2↑; AlCl3 + 4NaOH → Na[Al(OH)4] + 3NaCl; XCl2 + 2NaOH → X(OH)2↓ + 2NaCl; %s; Na[Al(OH)4] + CO2 → Al(OH)3↓ + NaHCO3"%eq,
         "NaOH da faqat Al: n(Al) = %s/(1,5·22,4) = **%s mol**; HCl da: %s/22,4 = %s mol = 1,5·%s + n(X) → n(X) = **%s mol**; M = (%s − %s)/%s = %s → **%s**"%(f2(V1,2),f2(a,3),f2(V2,2),f2(V2/V,3),f2(a,3),f2(b,3),f2(m,2),f2(27*a,2),f2(b,3),f2(Ax,1),X),
         "ω(Al) = %s/%s = **%s %%**; ω(%s) = **%s %%**"%(f2(27*a,2),f2(m,2),f2(27*a/m*100,1),X,f2(Ax*b/m*100,1)),
         "Cho'kma %s (amfoter Al(OH)3 ishqorda eriydi) → kuydirilganda **%s**: m = **%s g**"%("X(OH)2" if X=='Mg' else "Fe(OH)2 (havoda Fe(OH)3 ga o'tadi)",solid,f2(Msol,2)),
         "n(Na[Al(OH)4]) = n(Al) = %s mol → Al(OH)3 = **%s g**"%(f2(a,3),f2(78*a,2))]
    text+=" Hosil bo'lgan Al(OH)3 nitrat kislotada eritildi, eritma bug'latilib, qoldiq doimiy massagacha qizdirildi, ajralgan gazlar suvga yuttirildi."
    bands+=["Al(OH)3 ni eritish uchun sarflangan HNO3 miqdorini (mol) toping.","Al(NO3)3 qizdirilganda ajralgan gazlar hajmini (l, n.sh.) hisoblang.","Gazlar suvga yuttirilganda hosil bo'lgan HNO3 massasini (g) aniqlang."]
    sol+=["Al(OH)3 + 3HNO3 → Al(NO3)3 + 3H2O: n(HNO3) = 3·%s = **%s mol**"%(f2(a,3),f2(3*a,3)),"4Al(NO3)3 → 2Al2O3 + 12NO2 + 3O2: NO2 = %s mol, O2 = %s mol → **%s l**"%(f2(3*a,3),f2(0.75*a,3),f2(3.75*a*V,2)),"4NO2 + O2 + 2H2O → 4HNO3: n = %s mol → **%s g**"%(f2(3*a,3),f2(3*a*63,2))]
    return W("43",text,bands,sol,SC41)

from more12 import _w
import more10
w43_unknown_metal=_w(w43_unknown_metal_base,[0,1,(2,5),(3,6),(4,7)])
w43_thermite=_w(more10.w41_thermite,[0,1,(2,5),(3,6),(4,7)])
w43_no2o2=_w(more10.w41_no2o2,[0,1,(2,5),(3,6),(4,7)])
NEW41C=[w41_nitrate_cycle,w41_halide_id,w41_electro_mix]
NEW43C=[w43_unknown_metal]
