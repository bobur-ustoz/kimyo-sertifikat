from core import *
import math
# ======== 33-35 stories (A-F options) ========
def _opts(r,vals,nd=None):
    """vals: three correct numbers; returns option strings (6) and letters of answers"""
    nd=2
    cor=[fmt(round(v,2),nd) for v in vals]
    extra=[]
    for v in vals:
        for f in (2,0.5,1.5,0.8):
            t=fmt(round(v*f,2),nd)
            if t not in cor and t not in extra and v*f>0: extra.append(t)
    r.shuffle(extra)
    pool=cor+extra[:3]
    r.shuffle(pool); L='ABCDEF'
    return pool,[L[pool.index(c)] for c in cor]
def story1(r):
    a=r.choice([0.2,0.3,0.4]); b=r.choice([0.1,0.2]); w=r.choice([100,200])
    h2=a/2; mass=a*23+b*62; naoh=(a+2*b)*40; sol=w+mass-h2*2
    om=naoh/sol*100; mnao=b*62; macet=(a+2*b)*60
    txt="Na va Na2O dan iborat %s g aralashma %d g suvda to'liq eritildi, bunda %s l (n.sh.) vodorod ajraldi. Hosil bo'lgan eritma sirka kislota bilan to'liq neytrallandi."%(fmt(mass,2),w,fmt(h2*22.4,2))
    qs=["Hosil bo'lgan eritmadagi NaOH ning massa ulushini (%) aniqlang.","Dastlabki aralashmadagi Na2O massasini (g) aniqlang.","Neytrallash uchun sarflangan sirka kislota massasini (g) aniqlang."]
    sol_=["n(Na) = 2n(H2) = %s mol; Na2O = %s − %s = %s g; NaOH = %s + %s = %s mol = %s g; eritma %s g → %s %%"%(fmt(a),fmt(mass,2),fmt(a*23,2),fmt(mnao,2),fmt(a),fmt(2*b),fmt(a+2*b),fmt(naoh,2),fmt(sol,2),fmt(om,2)),"m(Na2O) = %s g"%fmt(mnao,2),"CH3COOH + NaOH → CH3COONa + H2O: %s mol · 60 = %s g"%(fmt(a+2*b),fmt(macet,2))]
    return txt,qs,[om,mnao,macet],1,sol_,"9-sinf (Na, Na2O); 10-sinf (sirka kislota)"
def story2(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.05,0.1]);
    m=a*64+b*144; gas_c2h2=a; gas_ch4=3*b
    M_=(a*26+gas_ch4*16)/(a+gas_ch4); D=M_/2; o2=a*2.5+gas_ch4*2; ald=a*0.8*44
    txt="CaC2 (%s g) va Al4C3 (%s g) dan iborat aralashma mo'l suv bilan to'liq reaksiyaga kirishdi."%(fmt(a*64,2),fmt(b*144,2))
    qs=["Hosil bo'lgan gazlar aralashmasining vodorodga nisbatan zichligini aniqlang.","Hosil bo'lgan gazlar aralashmasini to'liq yoqish uchun zarur kislorod hajmini (l, n.sh.) aniqlang.","Aralashmadagi to'yinmagan uglevodorod Kucherov reaksiyasi bo'yicha 80 % unum bilan reaksiyaga kirishsa, hosil bo'lgan aldegid massasini (g) aniqlang."]
    sol_=["CaC2 → C2H2: %s mol; Al4C3 → 3CH4: %s mol; M(o'rt.) = %s; D = %s"%(fmt(a),fmt(gas_ch4),fmt(M_,2),fmt(D,2)),"C2H2 + 2,5O2 (%s mol) + CH4 + 2O2 (%s mol) = %s mol → %s l"%(fmt(a*2.5),fmt(gas_ch4*2),fmt(a*2.5+gas_ch4*2),fmt(o2*22.4,2)),"C2H2 → CH3CHO: %s · 0,8 = %s mol → %s g"%(fmt(a),fmt(a*0.8),fmt(ald,2))]
    return txt,qs,[D,o2*22.4,ald],2,sol_,"Tashev (CaC2, Al4C3 gidrolizi); 10-sinf (Kucherov, yonish)"
def story3(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2])  # CaCO3 a, Na2CO3 b
    m=a*100+b*106; V=(a+b)*22.4;
    naoh_m=r.choice([2,3]); n_naoh=(a+b)*r.choice([1.0,1.5]); co2=a+b
    # CO2 + NaOH -> Na2CO3 if n_naoh>=2*co2 ; else mix; choose n_naoh = 2*co2 or 1.5 co2
    if abs(n_naoh-2*co2)<1e-9: prod='Na2CO3'; pm=co2*106
    else:
        x=n_naoh-co2; y=co2-x; prod='NaHCO3'; pm=y*84
    hcl=2*(a+b)
    txt="CaCO3 va Na2CO3 dan iborat %s g aralashma mo'l xlorid kislota bilan reaksiyaga kirishdi. Ajralgan gaz %s mol NaOH tutgan eritmadan o'tkazildi."%(fmt(m,2),fmt(n_naoh,2))
    qs=["Ajralgan gazning hajmini (l, n.sh.) aniqlang.","Aralashmani to'liq eritish uchun sarflangan HCl miqdorini (mol) aniqlang.","Gaz NaOH eritmasidan o'tkazilganda hosil bo'lgan tuz (%s) massasini (g) aniqlang."%prod]
    sol_=["n(CO2) = n(CaCO3) + n(Na2CO3) = %s mol → %s l"%(fmt(co2),fmt(V,2)),"CaCO3 + 2HCl; Na2CO3 + 2HCl: n(HCl) = 2·%s = %s mol"%(fmt(co2),fmt(hcl)),"NaOH : CO2 = %s : %s → %s %s g"%(fmt(n_naoh,2),fmt(co2),prod,fmt(pm,2))]
    return txt,qs,[V,hcl,pm],3,sol_,"9-sinf (uglerod, karbonatlar); Tashev"
def story4(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2])  # ethanol a, phenol b
    mass=a*46+b*94; H2=(a+b)/2*22.4; naoh=b*40; br=b*331
    txt="Etanol va fenoldan iborat %s g aralashma natriy bilan to'liq reaksiyaga kirishganda %s l (n.sh.) vodorod ajraldi. Xuddi shu massadagi aralashma NaOH eritmasi bilan (faqat fenol) va bromli suv bilan (faqat fenol) ham reaksiyaga kirishadi."%(fmt(mass,2),fmt(H2,2))
    qs=["Aralashmadagi fenol massasini (g) aniqlang.","Fenolni to'liq neytrallash uchun zarur NaOH massasini (g) aniqlang.","Mo'l bromli suv bilan reaksiyada hosil bo'lgan tribromfenol massasini (g) aniqlang."]
    sol_=["x + y = %s; 46x + 94y = %s → fenol %s mol = %s g"%(fmt(a+b),fmt(mass,2),fmt(b),fmt(b*94,2)),"C6H5OH + NaOH → C6H5ONa + H2O: %s g"%fmt(naoh,2),"C6H5OH + 3Br2 → C6H2Br3OH + 3HBr: %s mol · 331 = %s g"%(fmt(b),fmt(br,2))]
    return txt,qs,[b*94,naoh,br],4,sol_,"10-sinf §21, §23 (spirt, fenol)"
STORIES=[story1,story2,story3,story4]
def make3335(r,idx):
    for _ in range(30):
        txt,qs,vals,sid,sol,src=STORIES[idx%len(STORIES)](r)
        opts,key=_opts(r,vals,None)
        if len(set(opts))==6 and len(set(key))==3: break
    return dict(text=txt,qs=qs,opts=opts,key=key,sol=sol,vals=vals,src=src)
# ======== 36-40 short answers ========
# ======== written 41-43 ========
class W:
    def __init__(s,title,text,bands,sol,score): s.title=title;s.text=text;s.bands=bands;s.sol=sol;s.score=score
def w41_so2(r):
    x=r.choice([0.1,0.2]); ms=r.choice([100,200]); w0=r.choice([49,98,30]) if False else r.choice([49,30,63]);
    so2=4*x; V=1.0; o2_0=0.5*(6*x/2) if False else None
    # eq: SO2 : O2 : SO3 = 1:1:3 => SO2 = x, O2 = x, SO3 = 3x; initial SO2 = 4x, O2_0 = x + 1.5x = 2.5x
    o2_0=2.5*x; K=(3*x)**2/(x**2*x); alpha=3/4*100
    so3_m=3*x*80; h2so4_0=ms*w0/100; add=3*x*98; tot=h2so4_0+add; msol=ms+so3_m; om=tot/msol*100
    nb=tot/98; baso4=nb*233; vrate=2**2*2
    text="Hajmi 1 l bo'lgan idishga %s mol SO2 va ma'lum miqdorda O2 solindi hamda katalizator ishtirokida qizdirildi: 2SO2 + O2 ⇌ 2SO3. Muvozanat qaror topganda idishda SO2, O2 va SO3 ning mol nisbati 1 : 1 : 3 bo'ldi.\nHosil bo'lgan SO3 ning hammasi %d g %d %% li H2SO4 eritmasiga yuttirildi (oleum hosil bo'lmadi, SO3 to'liq suv bilan reaksiyaga kirishdi). Olingan eritmaga mo'l BaCl2 eritmasi qo'shildi."%(fmt(so2,2),ms,w0)
    bands=["O2 ning boshlang'ich miqdorini (mol) va muvozanat konstantasini (K) hisoblang.","SO2 ning necha foizi reaksiyaga kirishgan?","SO3 yuttirilgandan keyingi eritmada H2SO4 ning massa ulushini (%) aniqlang.","BaCl2 qo'shilganda hosil bo'lgan cho'kma massasini (g) toping.","Doimiy haroratda idish hajmi 2 marta kamaytirilsa (v = k·[SO2]²·[O2]), to'g'ri reaksiya tezligi necha marta o'zgaradi?"]
    sol=["SO2 : O2 : SO3 = 1 : 1 : 3 → SO2 = x, SO3 = 3x; x + 3x = %s → x = %s mol. O2 sarfi 1,5x = %s; O2 boshlang'ich = %s + %s = **%s mol**; [SO2] = %s, [O2] = %s, [SO3] = %s → K = [SO3]²/([SO2]²·[O2]) = **%s**"%(fmt(so2,2),fmt(x),fmt(1.5*3*x/3*1.0 if False else 1.5*x),fmt(x),fmt(1.5*x),fmt(o2_0,2),fmt(x),fmt(x),fmt(3*x),fmt(K,3)),
     "α = 3x/4x = **75 %**",
     "SO3 = %s mol = %s g; %d g %d %% li eritmada H2SO4 %s g; SO3 + H2O → H2SO4: +%s g; jami %s g; eritma %s g → ω = **%s %%**"%(fmt(3*x),fmt(so3_m,2),ms,w0,fmt(h2so4_0,2),fmt(add,2),fmt(tot,2),fmt(msol,2),fmt(om,2)),
     "H2SO4 + BaCl2 → BaSO4↓ + 2HCl: n(H2SO4) = %s mol → BaSO4 %s g = **%s g**"%(fmt(nb,3),fmt(nb*233,2),fmt(baso4,2)),
     "Hajm 2 marta kamayganda konsentratsiyalar 2 marta ortadi: v₂/v₁ = 2² · 2 = **8 marta ortadi**"]
    bands[4]+=" Shuningdek muvozanatda umumiy bosimning boshlang'ich bosimga nisbatini (T = const) toping."; sol[4]+="; n(muv.)/n(bosh.) = 5x/6,5x = **0,77**"
    bands[1]+=" Muvozanatda SO3 ning hajmiy ulushini (%) ham toping."; sol[1]+="; φ(SO3) = 3x/5x = **60 %**"
    bands[3]+=" BaCl2 sarfini (g) ham toping."; sol[3]+="; m(BaCl2) = %s·208 = **%s g**"%(fmt(nb,3),fmt(nb*208,2))
    return W("41",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
def w41_hyd(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2,0.05]); I=r.choice([5,10]); t=int(round(2*a*96500/I)); wat=r.choice([300,400,500])
    m=a*250+b*322; sol_m=m+wat; Cu=a*64; O2=a/2*32; after=sol_m-Cu-O2; wh=a*98/after*100; wn=b*142/after*100
    w1=a*160/sol_m*100; w2=b*142/sol_m*100; vO2=a/2*22.4; naoh=2*a*40; vol=naoh/0.2/1.22
    text="CuSO4·5H2O va Na2SO4·10H2O dan iborat %s g aralashma %d g suvda eritildi. Eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi; shu vaqt tugaganda eritmadagi Cu²⁺ ionlari to'liq tugagan edi."%(fmt(m,2),wat,I,t)
    bands=["Aralashmadagi kristallogidratlarning massalarini (g) aniqlang.","Dastlabki eritmada CuSO4 va Na2SO4 ning massa ulushlarini (%) toping.","Anodda ajralgan gazning hajmini (l, n.sh.) va elektroliz tugagandan keyingi eritma massasini (g) aniqlang.","Elektroliz tugagach eritmadagi H2SO4 va Na2SO4 ning massa ulushlarini (%) hisoblang.","Shu eritmani to'liq neytrallash uchun zichligi 1,22 g/ml bo'lgan 20 % li NaOH eritmasidan necha ml kerak?"]
    sol=["Q = %d·%d = %d C = %s mol e⁻; Cu²⁺ + 2e⁻ → Cu: n(Cu²⁺) = %s mol → CuSO4·5H2O **%s g**; Na2SO4·10H2O = %s − %s = **%s g** (%s mol)"%(I,t,I*t,fmt(I*t/96500,3),fmt(a),fmt(a*250,2),fmt(m,2),fmt(a*250,2),fmt(b*322,2),fmt(b)),
     "CuSO4 %s g; Na2SO4 %s g; eritma %s g → **%s %%** va **%s %%**"%(fmt(a*160,2),fmt(b*142,2),fmt(sol_m,2),fmt(w1,2),fmt(w2,2)),
     "Anod: 2H2O − 4e⁻ → O2 + 4H⁺: n(O2) = %s mol → **%s l**; eritma: %s − %s (Cu) − %s (O2) = **%s g**"%(fmt(a/2,3),fmt(vO2,2),fmt(sol_m,2),fmt(Cu,2),fmt(O2,2),fmt(after,2)),
     "2CuSO4 + 2H2O → 2Cu + O2 + 2H2SO4: H2SO4 %s mol = %s g → **%s %%**; Na2SO4 %s g → **%s %%**"%(fmt(a),fmt(a*98,2),fmt(wh,2),fmt(b*142,2),fmt(wn,2)),
     "H2SO4 + 2NaOH → Na2SO4 + 2H2O: NaOH %s mol = %s g; eritma %s g; V = %s/1,22 = **%s ml**"%(fmt(2*a),fmt(naoh,2),fmt(naoh/0.2,2),fmt(naoh/0.2,2),fmt(vol,1))]
    bands[4]+=" Agar tok kuchi 2 marta oshirilsa, xuddi shu miqdor Cu ajralishi uchun necha sekund kerak bo'ladi?"; sol[4]+="; t = %d/2 = **%d s**"%(t,t//2)
    bands[1]+=" Elektroliz davomida o'tgan zaryadni (C) ham hisoblang."; sol[1]+="; Q = %d·%d = **%d C**"%(I,t,I*t)
    bands[3]+=" Dastlabki CuSO4 ning massasini (g) ham hisoblang."; sol[3]+="; m(CuSO4) = %s·160 = **%s g**"%(fmt(a),fmt(a*160,2))
    return W("41",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
def w41_nh3(r):
    c=r.choice([(1,2,4),(2,2,4),(1,3,2),(1,1,2)]) ; N,H,A=c; V=2; K=A**2/(N*H**3)
    nN,nH,nA=N*V,H*V,A*V; N0=(N+A/2)*V; H0=(H+1.5*A)*V; alpha=1.5*A*V/H0*100; mNH3=nA*17; w=mNH3/(mNH3+800)*100; h2so4=nA/2*98; ms=h2so4/0.2
    text="%d l hajmli idishda N2 + 3H2 ⇌ 2NH3 reaksiyasi muvozanat holatiga keldi. Muvozanatda idishda %s mol N2, %s mol H2 va %s mol NH3 bor."%(V,fmt(nN),fmt(nH),fmt(nA))
    bands=["Muvozanat konstantasini (K) hisoblang.","Azot va vodorodning boshlang'ich konsentratsiyalarini (mol/l) aniqlang.","Vodorodning necha foizi reaksiyaga kirishgan?","Hosil bo'lgan ammiakning hammasi 800 g suvda eritildi. Eritmadagi ammiakning massa ulushini (%) hisoblang.","Shu eritmani (NH4)2SO4 hosil bo'lguncha neytrallash uchun 20 % li H2SO4 eritmasidan necha gramm kerak?"]
    sol=["Muvozanat konsentratsiyalari: [N2] = %s, [H2] = %s, [NH3] = %s mol/l; K = [NH3]²/([N2]·[H2]³) = **%s**"%(fmt(N),fmt(H),fmt(A),fmt(K,3)),
     "NH3 %s mol hosil bo'lgan → N2 sarfi %s mol, H2 sarfi %s mol; boshlang'ich N2 = **%s mol/l**, H2 = **%s mol/l**"%(fmt(nA),fmt(nA/2),fmt(1.5*nA),fmt(N0/V),fmt(H0/V)),
     "α(H2) = %s/%s = **%s %%**"%(fmt(1.5*nA),fmt(H0),fmt(alpha,1)),
     "m(NH3) = %s·17 = %s g; ω = %s/(%s + 800) = **%s %%**"%(fmt(nA),fmt(mNH3,2),fmt(mNH3,2),fmt(mNH3,2),fmt(w,2)),
     "2NH3 + H2SO4 → (NH4)2SO4: H2SO4 %s mol = %s g; eritma %s/0,2 = **%s g**"%(fmt(nA/2),fmt(h2so4,2),fmt(h2so4,2),fmt(ms,1))]
    bands[4]+=" Idish hajmi 2 marta kamaytirilsa, to'g'ri reaksiya tezligi (elementar deb hisoblang) necha marta ortadi?"; sol[4]+="; v ~ [N2][H2]³: 2⁴ = **16 marta**"
    bands[1]+=" H2 ning boshlang'ich massasini (g) ham toping."; sol[1]+="; m(H2) = %s·2 = **%s g**"%(fmt(H0),fmt(H0*2,2))
    bands[3]+=" Ajralgan NH3 hajmini (l, n.sh.) ham toping."; sol[3]+="; V = %s·22,4 = **%s l**"%(fmt(nA),fmt(nA*22.4,2))
    return W("41",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
def w41_nacl(r):
    m=r.choice([200,300,500]); w=r.choice([10,15,20]); I=r.choice([5,10]); t=r.choice([3860,1930,9650]); ne=I*t/96500
    nacl=m*w/100/58.5
    if ne/1 > nacl*0.95: return w41_nacl(r)
    H2=ne/2; Cl2=ne/2; naoh=ne; after=m-H2*2-Cl2*71; wn=naoh*40/after*100
    vol=naoh*36.5/0.1/1.05 if False else naoh*36.5/0.1
    text="%d g %d %% li NaCl eritmasi inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi."%(m,w,I,t)
    bands=["Katodda va anodda ajralgan gazlarning hajmlarini (l, n.sh.) hisoblang.","Elektrolizdan keyingi eritma massasini (g) aniqlang.","Elektrolizdan keyingi eritmada NaOH ning massa ulushini (%) toping.","Hosil bo'lgan NaOH ni to'liq neytrallash uchun 10 % li HCl eritmasidan necha gramm kerak?","Anodda ajralgan xlor KI eritmasidan o'tkazilsa, ajralgan yod massasini (g) aniqlang."]
    sol=["Q = %d·%d = %d C = %s mol e⁻; katod: 2H2O + 2e⁻ → H2 + 2OH⁻: n(H2) = %s mol → **%s l**; anod: 2Cl⁻ − 2e⁻ → Cl2: n(Cl2) = %s mol → **%s l**"%(I,t,I*t,fmt(ne,3),fmt(H2,3),fmt(H2*22.4,2),fmt(Cl2,3),fmt(Cl2*22.4,2)),
     "2NaCl + 2H2O → H2 + Cl2 + 2NaOH: m = %d − %s (H2) − %s (Cl2) = **%s g**"%(m,fmt(H2*2,2),fmt(Cl2*71,2),fmt(after,2)),
     "n(NaOH) = n(e⁻) = %s mol = %s g → ω = **%s %%**"%(fmt(ne,3),fmt(naoh*40,2),fmt(wn,2)),
     "NaOH + HCl → NaCl + H2O: HCl %s mol = %s g; eritma %s/0,1 = **%s g**"%(fmt(ne,3),fmt(ne*36.5,2),fmt(ne*36.5,2),fmt(ne*36.5/0.1,1)),
     "Cl2 + 2KI → 2KCl + I2: n(I2) = %s mol → **%s g**"%(fmt(Cl2,3),fmt(Cl2*254,2))]
    bands[4]+=" Anodda ajralgan xlorning massasini (g) ham toping."; sol[4]+="; m(Cl2) = %s·71 = **%s g**"%(fmt(Cl2,3),fmt(Cl2*71,2))
    bands[1]+=" Ajralgan gazlarning umumiy massasini (g) ham hisoblang."; sol[1]+="; m = %s + %s = **%s g**"%(fmt(H2*2,2),fmt(Cl2*71,2),fmt(H2*2+Cl2*71,2))
    bands[3]+=" Hosil bo'lgan NaCl massasini (g) ham hisoblang."; sol[3]+="; m(NaCl) = %s·58,5 = **%s g**"%(fmt(ne,3),fmt(ne*58.5,2))
    return W("41",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
W41=[w41_so2,w41_hyd,w41_nh3,w41_nacl]
# ---- 42 organic
EQ42=[("CH3–CH2–OH + CuO —t→","CH3CHO + Cu + H2O","etanal"),("CH3–CHO + H2 —Ni, t→","CH3CH2OH","etanol"),("C6H5–CH3 + Cl2 —yorug'lik→","C6H5CH2Cl + HCl","benzilxlorid"),("CH3COOH + C2H5OH ⇌ (H2SO4)","CH3COOC2H5 + H2O","etilatsetat"),("n CH2=CH2 →","(–CH2–CH2–)n","polietilen"),("C6H5NH2 + HCl →","[C6H5NH3]Cl","fenilammoniy xlorid"),("C6H12O6 —spirtli bijg'ish→","2C2H5OH + 2CO2","etanol"),
("C2H5Br + KOH(spirtli) →","CH2=CH2 + KBr + H2O","etilen"),("CH3–C≡CH + H2O —Hg²⁺→","CH3COCH3","propanon (aseton)"),("C6H6 + HNO3 —H2SO4→","C6H5NO2 + H2O","nitrobenzol"),("CH3CHO + Ag2O —NH3, t→","CH3COOH + 2Ag↓","etan (sirka) kislota"),("CH3COOCH3 + NaOH —t→","CH3COONa + CH3OH","natriy atsetat va metanol"),("H2N–CH2–COOH + NaOH →","H2N–CH2–COONa + H2O","glitsinning natriyli tuzi"),("n CH2=CH–CH=CH2 →","(–CH2–CH=CH–CH2–)n","polibutadiyen"),
("CH3COONa + NaOH —t→","CH4 + Na2CO3","metan"),("CH3–CH=CH2 + HBr →","CH3–CHBr–CH3","2-brompropan (Markovnikov)"),("C6H5OH + Br2 (mo'l, bromli suv) → ","C6H2Br3OH↓ + 3HBr","2,4,6-tribromfenol"),("C2H5OH —H2SO4(kons.), 170 °C→","CH2=CH2 + H2O","etilen"),("CH3–CH(OH)–CH3 + CuO —t→","CH3COCH3 + Cu + H2O","propanon"),("CaC2 + H2O →","C2H2 + Ca(OH)2","asetilen"),("HCOOH + Ag2O —NH3, t→","CO2 + H2O + 2Ag↓","karbonat angidrid"),("C2H5OH + Na →","C2H5ONa + ½H2","natriy etilat"),("C6H5NO2 + H2 —kat.→","C6H5NH2 + H2O","anilin"),("3C2H2 —C, t→","C6H6","benzol"),("CH3COOH + NaHCO3 →","CH3COONa + H2O + CO2","natriy atsetat"),("(C17H35COO)3C3H5 + NaOH →","3C17H35COONa + C3H5(OH)3","natriy stearat (sovun) va glitserin"),("C12H22O11 + H2O —H⁺→","C6H12O6 + C6H12O6","glyukoza va fruktoza"),("CH2=CH2 + Br2 →","CH2Br–CH2Br","1,2-dibrometan"),("CH4 + Cl2 —yorug'lik→","CH3Cl + HCl","xlormetan"),("2CH4 —1500 °C→","C2H2 + 3H2","asetilen")]
def w42(r,idx):
    n=7; pool=EQ42[:]; r.shuffle(pool); sel=pool[:n]
    pts=[4,4,3,4,4,3,3]; r.shuffle(pts)
    text="Reaksiya tenglamalarini tugallang va tenglang. Hosil bo'lgan organik moddalarning tuzilish formulalarini yozing va ularni nomlang."
    bands=[e[0] for e in sel]; sol=["%s %s — %s (%d ball)"%(e[0],e[1],e[2],p) for e,p in zip(sel,pts)]
    return W("42",text,bands,sol,[(p,0) for p in pts])
# ---- 43 inorganic/tahlil
def w43_nitrate(r):
    n=r.choice([0.2,0.4]); frac=r.choice([0.5,0.25]); dec=n*frac; start=n*188; resid=start-dec*108; cuo=dec*80; gas=dec*2.5*22.4; wat=r.choice([200,300]); hno3=dec*2*63; msol=wat+dec*2*46+dec*0.5*32; om=hno3/msol*100
    cu_t=n; fe=cu_t*56; cum=cu_t*64
    text="%s g Cu(NO3)2 qizdirilganda qisman parchalandi va qattiq qoldiq massasi %s g bo'ldi. Ajralgan gazlar aralashmasi %d g suvga to'liq yuttirildi. Qattiq qoldiq esa CuO ni to'liq eritadigan (ortiqcha bo'lmagan) miqdordagi suyultirilgan H2SO4 da eritildi, hosil bo'lgan eritmaga temir qipig'i solindi."%(fmt(start,2),fmt(resid,2),wat)
    bands=["Parchalanish reaksiyasi tenglamasini yozing. Parchalangan Cu(NO3)2 ning ulushini (%) va ajralgan gazlar hajmini (l, n.sh.) aniqlang.","Qattiq qoldiqdagi CuO ning massa ulushini (%) hisoblang.","Gazlar suvga yuttirilganda hosil bo'lgan eritmadagi HNO3 ning massa ulushini (%) toping (reaksiya tenglamasini yozing).","Temir qipig'i eritmadagi barcha Cu²⁺ ionlarini siqib chiqarishi uchun zarur temir massasini (g) va ajralgan mis massasini (g) aniqlang (reaksiya tenglamalarini yozing)."]
    sol=["2Cu(NO3)2 —t→ 2CuO + 4NO2 + O2. Massa kamayishi %s − %s = %s g; 2 mol (376 g) parchalanganda 216 g kamayadi → parchalangan %s mol; boshlang'ich %s mol → **%s %%**; gazlar NO2 %s + O2 %s mol → **%s l**"%(fmt(start,2),fmt(resid,2),fmt(start-resid,2),fmt(dec),fmt(n),fmt(frac*100,0),fmt(dec*2),fmt(dec/2),fmt(gas,2)),
     "CuO %s mol = %s g; ω = %s/%s = **%s %%**"%(fmt(dec),fmt(cuo,2),fmt(cuo,2),fmt(resid,2),fmt(cuo/resid*100,1)),
     "4NO2 + O2 + 2H2O → 4HNO3: HNO3 %s mol = %s g; eritma %d + %s + %s = %s g → **%s %%**"%(fmt(dec*2),fmt(hno3,2),wat,fmt(dec*2*46,2),fmt(dec/2*32,2),fmt(msol,2),fmt(om,2)),
     "CuO + H2SO4 → CuSO4 + H2O (%s mol); eritmada Cu²⁺: Cu(NO3)2 %s + CuSO4 %s = %s mol; Fe + Cu²⁺ → Fe²⁺ + Cu: Fe **%s g**, Cu **%s g**"%(fmt(dec),fmt(n-dec),fmt(dec),fmt(n),fmt(fe,2),fmt(cum,2))]
    bands.append("Ajralgan NO2 va O2 gazlari aralashmasining o'rtacha molyar massasini (g/mol) hisoblang."); sol.append("NO2 : O2 = 4 : 1 → M = (4·46 + 32)/5 = **43,2 g/mol**")
    return W("43",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
def w43_metals(r):
    X=[('Cu',64,'CuCl2','Cu(OH)2','qora CuS','havorang Cu(OH)2'),]
    n=r.choice([0.1,0.2]); nb=r.choice([0.1,0.2])
    zn=n*136; fe=nb*127
    text="Uch probirkada XCl2, YCl2 va ZCl2 tarkibli metall xloridlarining eritmalari bor. Har bir eritmaga reagentlar ta'sir ettirildi, kuzatuvlar jadvalda (\"—\" belgisi reaksiya bormasligini bildiradi, bo'sh kataklar bo'yicha ma'lumot berilmagan):\n\n| Reagent | XCl2 | YCl2 | ZCl2 |\n|---|---|---|---|\n| H2S | qora cho'kma | — | |\n| Na2S | qora cho'kma | qora cho'kma | oq cho'kma |\n| NaOH | havorang cho'kma | och yashil cho'kma | oq cho'kma |\n| Zn plastinka | qizil qoplama | | — |\n\nX, Y, Z — davriy sistemaning to'rtinchi davridagi metallar."
    bands=["Jadvalda kuzatilgan barcha reaksiyalarning molekulyar tenglamalarini yozing. XCl2 eritmasiga tushirilgan Zn plastinkada %s mol X ajralgan bo'lsa, plastinka massasi qanchaga (g) o'zgargan?"%fmt(n),"X, Y, Z metallarni aniqlang va tuzlarning formulalarini yozing. XCl2 tarkibida X ning massa ulushi 47,4 % ekanini hisob bilan tasdiqlang.","%s g YCl2 eritmasiga mo'l NaOH qo'shildi, hosil bo'lgan cho'kma havoda to'liq oksidlanguncha qoldirildi. Barcha reaksiya tenglamalarini yozing va oxirgi cho'kma massasini (g) aniqlang."%fmt(fe,2),"ZCl2 ning %s g massasi mo'l NaOH eritmasi bilan reaksiyaga kirishganda hosil bo'lgan kompleks tuz massasini (g) hisoblang (reaksiya tenglamalarini yozing)."%fmt(zn,2)]
    sol=["CuCl2 + H2S → CuS↓ + 2HCl; CuCl2 + Na2S → CuS↓ + 2NaCl; FeCl2 + Na2S → FeS↓ + 2NaCl; ZnCl2 + Na2S → ZnS↓ + 2NaCl; CuCl2 + 2NaOH → Cu(OH)2↓ + 2NaCl; FeCl2 + 2NaOH → Fe(OH)2↓ + 2NaCl; ZnCl2 + 2NaOH → Zn(OH)2↓ + 2NaCl; CuCl2 + Zn → ZnCl2 + Cu. %s mol Cu ajraladi, %s mol Zn erigan: Δm = %s·(64 − 65) = **−%s g** (plastinka kamayadi)"%(fmt(n),fmt(n),fmt(n),fmt(n,2)),
     "X = Cu (qora CuS, havorang Cu(OH)2, Zn bilan mis ajraladi); Y = Fe (och yashil Fe(OH)2, qora FeS); Z = Zn (oq ZnS, oq amfoter Zn(OH)2). ω(Cu) = 64/135 = **47,4 %**",
     "n(FeCl2) = %s/127 = %s mol. FeCl2 + 2NaOH → Fe(OH)2↓ + 2NaCl; 4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3: Fe(OH)3 %s mol · 107 = **%s g**"%(fmt(fe,2),fmt(nb),fmt(nb),fmt(nb*107,2)),
     "ZnCl2 + 2NaOH → Zn(OH)2↓ + 2NaCl; Zn(OH)2 + 2NaOH → Na2[Zn(OH)4]; n(ZnCl2) = %s mol → Na2[Zn(OH)4] (M = 179) = **%s g**"%(fmt(n),fmt(n*179,2))]
    bands.append("Hosil bo'lgan Cu(OH)2 cho'kmasi (%s mol) qizdirilganda hosil bo'ladigan CuO massasini (g) hisoblang."%fmt(n)); sol.append("Cu(OH)2 → CuO + H2O: %s mol · 80 = **%s g**"%(fmt(n),fmt(n*80,2)))
    return W("43",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
def w43_mix(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2]); c=r.choice([0.1,0.05]); mass=a*27+b*56+c*64
    h2_naoh=a*1.5*22.4; h2_hcl=(a*1.5+b)*22.4; no2=c*2*22.4; feoh3=b*107
    text="Alyuminiy, temir va misdan iborat %s g aralashma mo'l NaOH eritmasi bilan reaksiyaga kirishganda %s l (n.sh.) vodorod ajraldi. Xuddi shunday tarkibli ikkinchi aralashma (%s g) mo'l xlorid kislota bilan reaksiyaga kirishganda %s l (n.sh.) vodorod ajraldi (temir FeCl2 ga o'tdi)."%(fmt(mass,2),fmt(h2_naoh,2),fmt(mass,2),fmt(h2_hcl,2))
    bands=["Aralashmadagi har bir metallning massasini (g) va massa ulushini (%) aniqlang (reaksiya tenglamalarini yozing).","Xlorid kislota bilan reaksiyadan keyin qolgan qoldiq konsentrlangan HNO3 da to'liq eritildi. Ajralgan gazning hajmini (l, n.sh.) aniqlang.","Xlorid kislota bilan olingan eritmaga mo'l NaOH qo'shildi, hosil bo'lgan cho'kma ajratib olinib, havoda to'liq oksidlanguncha qoldirildi. Cho'kma massasini (g) toping.","Mis nitrat eritmasi bug'latilib, quruq tuz qizdirilganda hosil bo'ladigan qattiq qoldiq massasini (g) va gazlar aralashmasining hajmini (l, n.sh.) aniqlang."]
    sol=["NaOH bilan faqat Al: 2Al + 2NaOH + 6H2O → 2Na[Al(OH)4] + 3H2: n(Al) = %s mol = %s g; HCl bilan: Fe + 2HCl → FeCl2 + H2: n(Fe) = %s mol = %s g; Cu = %s g. ω: Al %s %%, Fe %s %%, Cu %s %%"%(fmt(a),fmt(a*27,2),fmt(b),fmt(b*56,2),fmt(c*64,2),fmt(a*27/mass*100,1),fmt(b*56/mass*100,1),fmt(c*64/mass*100,1)),
     "Cu + 4HNO3(kons.) → Cu(NO3)2 + 2NO2 + 2H2O: NO2 %s mol → **%s l**"%(fmt(c*2),fmt(no2,2)),
     "AlCl3 + 4NaOH → Na[Al(OH)4] + 3NaCl (eriydi); FeCl2 + 2NaOH → Fe(OH)2↓ + 2NaCl; 4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3: **%s g**"%fmt(feoh3,2),
     "2Cu(NO3)2 → 2CuO + 4NO2 + O2: CuO %s mol = **%s g**; NO2 %s + O2 %s = %s mol → **%s l**"%(fmt(c),fmt(c*80,2),fmt(2*c),fmt(c/2),fmt(2.5*c),fmt(2.5*c*22.4,2))]
    bands.append("Aralashmadagi alyuminiyni eritish uchun (2Al + 2NaOH + 6H2O → 2Na[Al(OH)4] + 3H2) 10 % li NaOH eritmasidan necha gramm kerak?"); sol.append("n(NaOH) = n(Al) = %s mol → %s g; eritma %s/0,1 = **%s g**"%(fmt(a),fmt(a*40,2),fmt(a*40,2),fmt(a*400,1)))
    return W("43",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
def w43_tahlil(r):
    g=r.choice([9,18,36]); n=g/180
    text="Laboratoriyada 1–4-raqamli probirkalarda tartibsiz holda glyukoza, kraxmal kleysteri, tuxum oqsili va glitserin eritmalari bor. Ularni aniqlash uchun quyidagi tajribalar o'tkazildi:\na) 1-probirkaga yodning spirtdagi eritmasidan qo'shildi — eritma ko'k rangga bo'yaldi.\nb) 2-probirkaga ishqor eritmasi va bir necha tomchi mis(II)-sulfat qo'shilganda eritma qizil-binafsha rangga bo'yaldi; boshqa porsiyasiga konsentrlangan HNO3 qo'shib qizdirilganda sariq rang paydo bo'ldi.\nc) 3- va 4-probirkalarga yangi cho'ktirilgan Cu(OH)2 qo'shilganda ikkalasida ham cho'kma erib, ko'k eritma hosil bo'ldi. 3-probirka qizdirilganda avval sariq, so'ng qizil cho'kma tushdi, 4-probirkada esa o'zgarish bo'lmadi."
    bands=["Glyukozaning Cu(OH)2 bilan reaksiya tenglamasini yozing. %s g glyukoza mo'l Cu(OH)2 bilan qizdirilganda hosil bo'lgan qizil cho'kmaning massasini (g) hisoblang."%fmt(g,0),"1–4-probirkalardagi moddalarni aniqlang (probirka raqami bilan moslab yozing).","a), b) va c) bo'yicha kuzatilgan rang o'zgarishlarining sababini tushuntiring: qaysi funksional guruh yoki bog' bilan bog'liq?","Tajribada probirkani qizdirish va konsentrlangan HNO3 bilan ishlashda qanday xavfsizlik qoidalariga rioya qilish kerak? Kamida uchta qoida yozing."]
    sol=["CH2OH–(CHOH)4–CHO + 2Cu(OH)2 → CH2OH–(CHOH)4–COOH + Cu2O↓ + 2H2O; n(glyukoza) = %s/180 = %s mol → Cu2O %s mol · 144 = **%s g**"%(fmt(g,0),fmt(n),fmt(n),fmt(n*144,2)),
     "1 — kraxmal kleysteri (yod bilan ko'k); 2 — tuxum oqsili (biuret va ksantoprotein reaksiyalari); 3 — glyukoza; 4 — glitserin",
     "a) kraxmal yod bilan ko'k rang beradi. b) oqsil: ishqoriy muhitda CuSO4 bilan qizil-binafsha rang — peptid bog' (–CO–NH–) uchun biuret reaksiyasi; kons. HNO3 bilan sariq rang — aromatik halqali aminokislota qoldiqlari (ksantoprotein). c) glyukoza va glitserin Cu(OH)2 ni eritib ko'k kompleks hosil qiladi (ko'p atomli spirt guruhlari); faqat glyukozada aldegid guruh bor, qizdirilganda Cu2O gacha qaytariladi",
     "Probirka qisqichda tik, og'zi odamga qaratilmagan holda ohista qizdiriladi; kons. kislotani ko'zoynak va qo'lqopda ehtiyotlik bilan ishlatish, teriga tushsa ko'p suv bilan yuvish; reaktivlarni tatib ko'rmaslik; ortiqcha reaktivni idishga qaytarmaslik; kichik miqdorda ishlash"]
    bands.append("Glyukozaning (%s g) spirtli bijg'ishida ajraladigan CO2 hajmini (l, n.sh.) hisoblang."%fmt(g,0)); sol.append("C6H12O6 → 2C2H5OH + 2CO2: n(CO2) = 2·%s = %s mol → **%s l**"%(fmt(n),fmt(2*n),fmt(2*n*22.4,2)))
    return W("43",text,bands,sol,[(6,3),(2,1),(3,3),(2,2),(2,1)])
W43=[w43_nitrate,w43_metals,w43_mix,w43_tahlil]
# ---- extra table questions
def tbl_mix(r):
    m1=r.choice([100,200,300]); m2=r.choice([200,300,400]); w1=r.choice([10,15,20]); w2=r.choice([25,30,40]); w=(m1*w1+m2*w2)/(m1+m2)
    q=numq("Jadvalda ikki tuz eritmasi haqida ma'lumot berilgan:\n\n| Eritma | Massasi, g | Massa ulushi, %% |\n|---|---|---|\n| 1 | %d | %d |\n| 2 | %d | %d |\n\nEritmalar aralashtirilganda hosil bo'lgan eritmaning massa ulushini (%%) aniqlang."%(m1,w1,m2,w2),w,[(w1+w2)/2,w1+w2,(m1*w2+m2*w1)/(m1+m2),w*0.9],"m(tuz) = %s g; m(eritma) = %d g; ω = %s %%"%(fmt((m1*w1+m2*w2)/100,2),m1+m2,fmt(w,2)),"Tirkashev III bob (eritmalar, jadval)",2)
    q.kind='table'; return q
def tbl_eq(r):
    a=r.choice([2,3,4]); b=r.choice([4,6]); x=r.choice([1,2]); V=r.choice([2,4])
    # N2 + 3H2 <-> 2NH3, initial moles N2=a, H2=b? make eq NH3 = 2x
    n2=a-x; h2=b-3*x
    if n2<=0 or h2<=0: return tbl_eq(r)
    K=((2*x/V)**2)/((n2/V)*(h2/V)**3)
    q=numq("N2 + 3H2 ⇌ 2NH3 reaksiyasi %d l hajmli idishda o'tkazildi. Moddalar miqdori jadvalda berilgan:\n\n| Modda | N2 | H2 | NH3 |\n|---|---|---|---|\n| Boshlang'ich miqdor, mol | %d | %d | 0 |\n| Muvozanatdagi miqdor, mol | — | — | %d |\n\nMuvozanat konstantasini (K) hisoblang."%(V,a,b,2*x),K,[K*2,K/2,K*V,K/V],"NH3 %d mol → N2 sarfi %d, H2 sarfi %d; muvozanatda N2 %d, H2 %d mol; [N2] = %s, [H2] = %s, [NH3] = %s; K = %s"%(2*x,x,3*x,n2,h2,fmt(n2/V),fmt(h2/V),fmt(2*x/V),fmt(K,3)),"Tirkashev VI bob (muvozanat, jadval)",3)
    q.kind='table'; return q
