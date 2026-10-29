import random
from core import *
from tail import W
from more3 import f2
# ===== Ko'p bosqichli masalalar =====
# (1) organik unumli zanjirlar (3-5 bosqich); (2) 41/43 uchun 6-7 bosqichli ssenariylar (qizdirish -> yutish -> reaksiya -> elektroliz);
# (3) 1-19 uchun 2-4 bosqichli qisqa masalalar.
F=96500; V=22.4; R=8.314
def mk_scores(n):
    tot={4:[6,7,6,6],5:[6,5,5,5,4],6:[5,4,4,4,4,4],7:[5,4,4,3,3,3,3]}[n]
    out=[]
    for t in tot:
        m=round(t*0.6); out.append((m,t-m))
    return out

# -------------------------------------------------- (1) ORGANIK ZANJIRLAR --------------------------------------------------
# step: (sxemadagi modda, shu moddaning bir mol oldingisidan nechta mol hosil bo'lishi)
CH=[
 dict(name='metan→kumush',start=('CH4',16,'l'),scheme='CH4 → C2H2 → CH3CHO → Ag',steps=[('C2H2',0.5),('CH3CHO',1),('Ag',2)],M=108,final='kumush',src='10-sinf (metandan atsetilen, Kucherov, kumush ko\'zgu)'),
 dict(name='karbid→anilin',start=('CaC2',64,'g'),scheme='CaC2 → C2H2 → C6H6 → C6H5NO2 → C6H5NH2',steps=[('C2H2',1),('C6H6',1/3),('C6H5NO2',1),('C6H5NH2',1)],M=93,final='anilin',src='10-sinf (karbiddan atsetilen, benzol, anilin)'),
 dict(name='karbid→PVX',start=('CaC2',64,'g'),scheme='CaC2 → C2H2 → CH2=CHCl → (–CH2–CHCl–)n',steps=[('C2H2',1),('CH2=CHCl',1),('polimer zvenosi',1)],M=62.5,final='polivinilxlorid',src='10-sinf (polimerlar; vinilxlorid olinishi)'),
 dict(name='kraxmal→kauchuk',start=('(C6H10O5)n',162,'g'),scheme='(C6H10O5)n → C6H12O6 → C2H5OH → CH2=CH–CH=CH2 → (–CH2–CH=CH–CH2–)n',steps=[('C6H12O6',1),('C2H5OH',2),('C4H6',0.5),('kauchuk zvenosi',1)],M=54,final='divinil kauchuk',src='10-sinf (Lebedev usuli; sintetik kauchuk)'),
 dict(name='propen→aseton',start=('C3H6',42,'l'),scheme='CH3–CH=CH2 → CH3–CHCl–CH3 → CH3–CH(OH)–CH3 → CH3–CO–CH3',steps=[('2-xlorpropan',1),('propanol-2',1),('propanon',1)],M=58,final='aseton',src='10-sinf (alkenlar, galogenli hosilalar, spirtlar)'),
 dict(name='benzol→tribromanilin',start=('C6H6',78,'g'),scheme='C6H6 → C6H5NO2 → C6H5NH2 → C6H2Br3NH2',steps=[('C6H5NO2',1),('C6H5NH2',1),('tribromanilin',1)],M=330,final="2,4,6-tribromanilin",src='10-sinf (arenlar, anilin)'),
 dict(name='sirka→dipeptid',start=('CH3COOH',60,'g'),scheme='CH3COOH → ClCH2COOH → H2N–CH2–COOH → dipeptid',steps=[('ClCH2COOH',1),('glitsin',1),('dipeptid',0.5)],M=132,final='glitsilglitsin',src='10-sinf (aminokislotalar, peptidlar)'),
 dict(name='toluol→efir',start=('C6H5CH3',92,'g'),scheme='C6H5CH3 → C6H5COOH → C6H5COOC2H5',steps=[('C6H5COOH',1),('etilbenzoat',1)],M=150,final='etilbenzoat',src='10-sinf (arenlar, karbon kislotalar, murakkab efirlar)'),
 dict(name='etanol→kauchuk',start=('C2H5OH',46,'g'),scheme='2C2H5OH → CH2=CH–CH=CH2 → (–CH2–CH=CH–CH2–)n',steps=[('C4H6',0.5),('kauchuk zvenosi',1)],M=54,final='divinil kauchuk',src='10-sinf (Lebedev usuli)'),
 dict(name='etan→efir',start=('C2H6',30,'l'),scheme='C2H6 → C2H4 → C2H5OH → CH3COOC2H5',steps=[('C2H4',1),('C2H5OH',1),('etilatsetat',1)],M=88,final='etilatsetat',src='10-sinf (alkanlar, alkenlar, spirtlar, efirlar)'),
 dict(name='metan→formaldegid',start=('CH4',16,'l'),scheme='CH4 → CH3Cl → CH3OH → HCHO',steps=[('CH3Cl',1),('CH3OH',1),('HCHO',1)],M=30,final='formaldegid',src='10-sinf (galogenlash, gidroliz, spirtning oksidlanishi)'),
 dict(name='benzol→tribromfenol',start=('C6H6',78,'g'),scheme='C6H6 → C6H5Cl → C6H5OH → C6H2Br3OH',steps=[('C6H5Cl',1),('C6H5OH',1),('tribromfenol',1)],M=331,final='2,4,6-tribromfenol',src='10-sinf (arenlar, fenol)'),
 dict(name='propan→aseton',start=('C3H8',44,'l'),scheme='C3H8 → CH3–CH=CH2 → CH3–CH(OH)–CH3 → CH3–CO–CH3',steps=[('propen',1),('propanol-2',1),('propanon',1)],M=58,final='aseton',src='10-sinf (alkanlar, alkenlar, spirtlar, ketonlar)'),
 dict(name='benzol→polistirol',start=('C6H6',78,'g'),scheme='C6H6 → C6H5–C2H5 → C6H5–CH=CH2 → (–CH2–CH(C6H5)–)n',steps=[('etilbenzol',1),('stirol',1),('polistirol zvenosi',1)],M=104,final='polistirol',src='10-sinf (arenlar, polimerlar)'),
]

CH+=[
 dict(name='benzol→natriy fenolyat',start=('C6H6',78,'g'),scheme='C6H6 → C6H5Cl → C6H5OH → C6H5ONa',steps=[('C6H5Cl',1),('C6H5OH',1),('C6H5ONa',1)],M=116,final='natriy fenolyat',src='10-sinf (arenlar, fenol)'),
 dict(name='etilen→sirka kislota',start=('C2H4',28,'l'),scheme='C2H4 → C2H5OH → CH3CHO → CH3COOH',steps=[('C2H5OH',1),('CH3CHO',1),('CH3COOH',1)],M=60,final='sirka kislota',src='10-sinf (alkenlar, spirtlar, aldegidlar, kislotalar)'),
 dict(name='saxaroza→etanol',start=('C12H22O11',342,'g'),scheme='C12H22O11 → C6H12O6 (glyukoza va fruktoza) → C2H5OH',steps=[('monosaxaridlar',2),('etanol',2)],M=46,final='etanol',src='10-sinf (disaxaridlar; bijg\'ish)'),
 dict(name='metan→etilen',start=('CH4',16,'l'),scheme='CH4 → CH3Cl → C2H6 → C2H4',steps=[('CH3Cl',1),('C2H6',0.5),('C2H4',1)],M=28,final='etilen',src='10-sinf (alkanlar; Vyurs reaksiyasi; degidrogenlash)'),
 dict(name='etanol→glikol',start=('C2H5OH',46,'g'),scheme='C2H5OH → C2H4 → HOCH2–CH2OH',steps=[('C2H4',1),('etilenglikol',1)],M=62,final='etilenglikol',src='10-sinf (spirtlar, alkenlar, ko\'p atomli spirtlar)'),
 dict(name='nitrobenzol→fenilammoniy',start=('C6H5NO2',123,'g'),scheme='C6H5NO2 → C6H5NH2 → [C6H5NH3]Cl',steps=[('C6H5NH2',1),('fenilammoniy xlorid',1)],M=129.5,final='fenilammoniy xlorid',src='10-sinf (nitrobirikmalar, aminlar)'),
 dict(name='karbid→etanol',start=('CaC2',64,'g'),scheme='CaC2 → C2H2 → C2H4 → C2H5OH',steps=[('C2H2',1),('C2H4',1),('C2H5OH',1)],M=46,final='etanol',src='10-sinf (alkinlar, alkenlar, spirtlar)'),
]
def c_chain(r):
    ch=r.choice(CH); st,Ms,u=ch['start']; steps=ch['steps']
    n0=r.choice([0.5,1,2,4]) ;
    if u=='l': amt=n0*V*r.choice([1,2,5])/ (1 if n0>=1 else 1); unitstr='%s l (n.sh.) %s'%(f2(amt,1),st); n0=amt/V
    else: amt=n0*Ms; unitstr='%s g %s'%(f2(amt,1),st)
    nn=len(steps)
    et=[r.choice([0.8,0.75,0.9,0.6,0.5,0.4,0.85]) for _ in steps]
    purity=None
    if st=='CaC2' and r.random()<0.5:
        purity=r.choice([80,75,90]); n0=n0*purity/100
    prod=n0
    for (nm,k),e in zip(steps,et): prod=prod*k*e
    ans=prod*ch['M']
    ptxt=("Texnik %s tarkibida %d %% sof modda bor. "%(st,purity)) if purity else ""
    asks=r.choice(['fwd','rev','last'])
    etxt=', '.join('%d %%'%round(e*100) for e in et)
    stages=nn+(1 if purity else 0)
    sol_steps=n0
    sol="n(%s) = %s mol%s; "%(st,f2(n0,3),(" (sof modda)" if purity else ""))
    cur=n0; parts=[]
    for (nm,k),e in zip(steps,et):
        cur=cur*k*e; parts.append("%s: %s mol"%(nm,f2(cur,4)))
    sol+="; ".join(parts)+" → m = %s·%s = %s g"%(f2(cur,4),f2(ch['M'],1),f2(ans,2))
    if asks=='last':
        e1=et[:-1]; tail_=', '.join('%d %%'%round(e*100) for e in e1)
        start_txt=("%s g texnik %s (tarkibida %d %% sof modda)"%(f2(amt/ (purity/100) if False else (amt),1),st,purity) if purity else unitstr)
        t="%s dan quyidagi sxema bo'yicha %s g %s olindi: %s. Dastlabki %d bosqichning unumi ketma-ket %s ga teng. Oxirgi bosqichning unumini (%%) aniqlang."%(start_txt,f2(ans,2),ch['final'],ch['scheme'],nn-1,tail_)
        a_=et[-1]*100
        q=numq(t,a_,[a_/2,100-a_,a_*0.8 if a_*0.8<100 else a_*0.6,(et[-1]*0.5)*100],"Oxirgi bosqichgacha olingan modda: %s mol; nazariy mahsulot %s mol, amalda %s mol (%s g) → η = %s %%"%(f2(prod/et[-1]/steps[-1][1],4),f2(prod/et[-1],4),f2(prod,4),f2(ans,2),f2(a_,0)),ch['src'],0); q.ck=ch['name']; return q
    if asks=='fwd':
        t="%s%s dan quyidagi sxema bo'yicha %s olindi: %s. Bosqichlarning unumi ketma-ket %s ni tashkil qiladi. Olingan %s massasini (g) aniqlang."%(ptxt,unitstr,ch['final'],ch['scheme'],etxt,ch['final'])
        q=numq(t,ans,[ans*2,ans/2,prod*ch['M']/et[-1],n0*steps[0][1]*ch['M']],sol,ch['src'],2); q.ck=ch['name']; return q
    # teskari: oxirgi mahsulot massasi berilgan, boshlang'ich modda massasini topish
    sol2="Teskari hisob: n(%s) = %s/%s = %s mol; barcha koeffitsiyent va unumlarga bo'linadi → n(%s) = %s mol%s → %s"%(ch['final'],f2(ans,2),f2(ch['M'],1),f2(ans/ch['M'],4),st,f2(n0,3),(" (sof)" if purity else ""),("m = %s g (texnik)"%f2(n0/(purity/100)*Ms,2) if purity else ("m = %s g"%f2(n0*Ms,2) if u=='g' else "V = %s l"%f2(n0*V,2))))
    if purity: want=n0/(purity/100)*Ms; what="texnik %s massasi (g)"%st
    elif u=='g': want=n0*Ms; what="%s massasi (g)"%st
    else: want=n0*V; what="%s hajmi (l, n.sh.)"%st
    t="%s dan quyidagi sxema bo'yicha %s g %s olindi: %s. Bosqichlarning unumi ketma-ket %s ni tashkil qiladi. %sSarflangan %s ni aniqlang."%(st,f2(ans,2),ch['final'],ch['scheme'],etxt,ptxt,what)
    q=numq(t,want,[want*2,want/2,want*et[0],want*et[-1]],sol2,ch['src'],2); q.ck=ch['name']; return q

# glukoza -> etanol -> kislota/efir (bo'linish mantiqi)
def c_glu_ester(r):
    n=r.choice([0.5,1,2]); e1=r.choice([0.8,0.9,0.75]); e2=r.choice([0.8,0.5,0.6]); e3=r.choice([0.8,0.75,0.5])
    eth=2*n*e1; acid=eth/2*e2; ester=acid*e3
    t="%s g glukoza spirtli bijg'ishga uchradi (unum %d %%). Hosil bo'lgan etanolning yarmi sirka kislotagacha oksidlandi (unum %d %%), qolgan etanol bilan sirka kislota esterlandi (unum %d %%). Hosil bo'lgan murakkab efir massasini (g) hisoblang."%(f2(n*180,0),round(e1*100),round(e2*100),round(e3*100))
    return numq(t,ester*88,[ester*88*2,ester*88/2,eth*e2*e3*88,acid*88],"n(C2H5OH) = 2·%s·%s = %s mol; oksidlanganı: %s mol → CH3COOH %s·%s = %s mol; qolgan spirt %s mol (yetarli); efir: %s·%s = %s mol → %s g"%(f2(n),f2(e1),f2(eth,3),f2(eth/2,3),f2(eth/2,3),f2(e2),f2(acid,3),f2(eth/2,3),f2(acid,3),f2(e3),f2(ester,3),f2(ester*88,2)),"10-sinf (uglevodlar, spirtlar, kislotalar, efirlar)",2)

# alken aralashmasi: brom suvi + gidratlanish + Na (4 bosqich)
def c_alkene_hydration(r):
    a,b=r.choice([(0.1,0.2),(0.2,0.1),(0.2,0.3),(0.3,0.2),(0.1,0.3)]); e=r.choice([0.8,0.5,0.6]); m=28*a+42*b
    br=(a+b)*160; alc=(a*46+b*60)*e; h2=(a+b)*e/2*V
    t="Etilen va propendan iborat %s g aralashma mo'l bromli suv bilan to'liq reaksiyaga kirishdi. Xuddi shunday tarkibli ikkinchi porsiya gidratlandi (har bir alken uchun unum %d %%), hosil bo'lgan spirtlar aralashmasi natriy bilan ta'sirlashtirildi. Birinchi porsiyada sarflangan brom massasini va ikkinchi porsiyada ajralgan vodorod hajmini (l, n.sh.) yig'indisini toping."%(f2(m,1),round(e*100))
    ans=br+h2
    return numq(t,ans,[br,h2,ans*2,ans/2],"28x + 42y = %s; x = %s, y = %s mol; Br2: (x + y)·160 = %s g; spirtlar %s mol; H2 = %s·0,5 = %s mol → %s l; yig'indi %s"%(f2(m,1),f2(a),f2(b),f2(br,1),f2((a+b)*e,3),f2((a+b)*e,3),f2((a+b)*e/2,3),f2(h2,2),f2(ans,2)),"10-sinf (alkenlar: birikish, gidratlanish; spirtlar + Na)",2)

# amin: yonish -> CO2 -> ohakli suv; aralashmada ikki noma'lum (4 bosqich)
def c_organic_ca(r):
    a,b=r.choice([(0.1,0.1),(0.1,0.2),(0.2,0.1),(0.2,0.2)]);
    co2=2*a+3*b; mc=a*46+b*60  # etanol va propanol-1
    t="Etanol va propanol-1 aralashmasi (%s g) yondirildi. Hosil bo'lgan gazlar mo'l ohakli suvdan o'tkazilib, so'ng cho'kma doimiy massagacha qizdirildi. Qizdirilgandan keyingi qattiq qoldiq massasini (g) aniqlang."%f2(mc,1)
    ans=co2*56
    return numq(t,ans,[co2*100,ans/2,ans*2,co2*44],"46x + 60y = %s → x = %s, y = %s; CO2: 2x + 3y = %s mol; CaCO3 %s mol; CaCO3 → CaO + CO2: m(CaO) = %s g"%(f2(mc,1),f2(a),f2(b),f2(co2,2),f2(co2,2),f2(ans,2)),"10-sinf (spirtlarning yonishi; CO2 + Ca(OH)2)",1)

ORG34=[c_chain,c_chain,c_glu_ester,c_alkene_hydration,c_organic_ca]

# -------------------------------------------------- (3) 1-19: 2-4 bosqichli qisqa masalalar --------------------------------------------------
def q_nitrate_hno3(r):
    a=r.choice([0.1,0.2,0.4]); Wt=r.choice([100,200,300]); w=126*a/(Wt+108*a)*100
    t="%s mol Cu(NO3)2 to'liq parchalanguncha qizdirildi. Ajralgan gazlar aralashmasi %d g suvga to'liq yuttirildi (4NO2 + O2 + 2H2O → 4HNO3). Hosil bo'lgan eritmadagi HNO3 ning massa ulushini (%%) aniqlang."%(f2(a),Wt)
    return numq(t,w,[126*a/(Wt+46*2*a)*100,126*a/Wt*100,w*2,w/2],"2Cu(NO3)2 → 2CuO + 4NO2 + O2: NO2 %s mol, O2 %s mol (4:1 – to'liq yutiladi); m(HNO3) = %s g; eritma = %d + %s = %s g → %s %%"%(f2(2*a,2),f2(a/2,3),f2(126*a,1),Wt,f2(108*a,1),f2(Wt+108*a,1),f2(w,2)),"9-sinf (nitratlarning parchalanishi; NO2 ning yutilishi)",2)
def q_hydrate_heat(r):
    a=r.choice([0.1,0.2,0.4]); k=r.choice([2,3,4]); Wt=r.choice([100,200,300]); m=a*250
    left=m-a*18*k; sol=left+Wt
    w=a*160/(sol)*100
    t="%s g CuSO4·5H2O qizdirilganda massa %s g ga kamaydi. Qoldiq %d g suvda to'liq eritildi. Hosil bo'lgan eritmadagi CuSO4 ning massa ulushini (%%) aniqlang."%(f2(m,1),f2(a*18*k,1),Wt)
    return numq(t,w,[a*160/(m+Wt)*100,a*160/Wt*100,w*2,w/2],"n(CuSO4) = %s mol; m(CuSO4) = %s g; eritma massasi = %s − %s + %d = %s g → ω = %s %%"%(f2(a),f2(a*160,1),f2(m,1),f2(a*18*k,1),Wt,f2(sol,1),f2(w,2)),"9-sinf (kristallogidratlar)",2)
def q_nh3_water(r):
    a=r.choice([0.2,0.4,0.5]); Wt=r.choice([100,200,300])
    w=a*17/(Wt+a*17)*100
    t="%s mol NH4Cl ning mo'l NaOH eritmasi bilan qizdirilishidan ajralgan ammiak %d g suvga to'liq yuttirildi. Hosil bo'lgan eritmadagi ammiakning massa ulushini (%%) toping."%(f2(a),Wt)
    return numq(t,w,[a*17/Wt*100,a*35.5/(Wt)*100,w*2,w/2],"NH4Cl + NaOH → NaCl + NH3↑ + H2O: n(NH3) = %s mol = %s g; eritma %d + %s = %s g → %s %%"%(f2(a),f2(a*17,1),Wt,f2(a*17,1),f2(Wt+a*17,1),f2(w,2)),"9-sinf (ammiak olinishi va eritmasi)",2)
def q_alloy_burn(r):
    a,b=r.choice([(0.1,0.2),(0.2,0.2),(0.2,0.1),(0.1,0.1)]); h2=a+1.5*b; m=24*a+27*b
    t="Mg va Al dan iborat %s g qotishma mo'l xlorid kislotada eritildi. Ajralgan gaz kislorodda to'liq yondirildi. Hosil bo'lgan suvning massasini (g) hisoblang."%f2(m,1)
    return numq(t,h2*18,[h2*22.4,h2*9,h2*18*2,a*18],"24x + 27y = %s → x = %s, y = %s; H2: x + 1,5y = %s mol; 2H2 + O2 → 2H2O: m = %s g"%(f2(m,1),f2(a),f2(b),f2(h2,2),f2(h2*18,2)),"9-sinf (metallar, vodorod, suv)",1)
def q_kclo3_so2(r):
    n=r.choice([0.2,0.4]); e=r.choice([0.5,0.75,1.0]); o2=1.5*n*e; so2=o2; naoh=round(r.choice([1.25,1.5,1.75])*so2,2)
    if not (so2<naoh<2*so2): naoh=round(1.5*so2,2)
    # SO2 + NaOH: o'rta va nordon tuz
    u=naoh-so2; w=so2-u
    t="%s mol KClO3 qizdirilganda (unum %d %%) kislorod ajraldi. Shu kislorodda oltingugurt to'liq yondirildi (S ortiqcha), hosil bo'lgan gaz %s mol NaOH eritmasiga yuttirildi. Hosil bo'lgan tuzlar umumiy massasini (g) toping."%(f2(n),round(e*100),f2(naoh,2))
    ans=u*126+w*104
    return numq(t,ans,[so2*126,so2*104,ans*2,ans/2],"2KClO3 → 2KCl + 3O2: O2 = 1,5·%s·%s = %s mol; S + O2 → SO2 (%s mol); n(NaOH)/n(SO2) = %s → Na2SO3 %s mol + NaHSO3 %s mol; m = %s g"%(f2(n),f2(e),f2(o2,3),f2(so2,3),f2(naoh/so2,2),f2(u,3),f2(w,3),f2(ans,2)),"9-sinf (kislorod olinishi, oltingugurt oksidi + ishqor)",2)
def q_nacl_hcl(r):
    I=r.choice([5,10]); t_=r.choice([1930,3860,965]); Wt=r.choice([100,200,400])
    n=I*t_/(2*F); w=2*n*36.5/(Wt+2*n*36.5)*100
    t="NaCl eritmasi inert elektrodlar bilan %d A tok kuchi bilan %d s elektroliz qilindi. Ajralgan gazlar aralashmasi yondirilib, hosil bo'lgan gaz %d g suvda eritildi. Olingan kislota eritmasining massa ulushini (%%) aniqlang."%(I,t_,Wt)
    return numq(t,w,[n*36.5/(Wt+n*36.5)*100,2*n*36.5/Wt*100,w*2,w/2],"n(e) = %s mol → H2 = Cl2 = %s mol; H2 + Cl2 → 2HCl: %s mol = %s g; ω = %s/(%d + %s) = %s %%"%(f2(I*t_/F,3),f2(n,3),f2(2*n,3),f2(2*n*36.5,2),f2(2*n*36.5,2),Wt,f2(2*n*36.5,2),f2(w,2)),"9-sinf; 11-sinf (elektroliz; vodorod xlorid)",2)
def q_caco3_hcl(r):
    m=r.choice([50,100,200]); e=r.choice([0.4,0.5,0.6,0.8])
    ans=m/100*2*36.5
    t="%s g CaCO3 qizdirilganda uning %d %% i parchalandi. Qattiq qoldiq mo'l xlorid kislotada to'liq eritildi. Sarflangan HCl massasini (g) aniqlang."%(f2(m,0),round(e*100))
    return numq(t,ans,[ans*e,ans*(1-e),ans*2,m/100*36.5],"Qoldiqda CaO %s mol va CaCO3 %s mol: har biri 2HCl sarflaydi → 2·(%s) = %s mol; barcha Ca %s mol, shuning uchun unumga bog'liq emas; m = %s g"%(f2(m/100*e,3),f2(m/100*(1-e),3),f2(m/100,2),f2(2*m/100,2),f2(m/100,2),f2(ans,2)),"9-sinf (kalsiy birikmalari; mantiqiy masala)",2)
def q_cu_o2_h2so4(r):
    a=r.choice([0.1,0.2,0.4])
    t="%s g mis kukuni to'liq oksidlandi, hosil bo'lgan oksid 10 %% li H2SO4 eritmasining yetarli (stexiometrik) miqdorida eritildi. Hosil bo'lgan eritmadagi CuSO4 ning massa ulushini (%%) toping."%f2(a*64,1)
    ac=98*a/0.1; sol=a*80+ac; w=a*160/sol*100
    return numq(t,w,[a*160/ac*100,a*160/(a*64+ac)*100,w*2,w/2],"2Cu + O2 → 2CuO (%s g); CuO + H2SO4 → CuSO4 + H2O: H2SO4 %s g → eritma %s g; CuSO4 %s g → %s %%"%(f2(a*80,1),f2(98*a,1),f2(sol,1),f2(a*160,1),f2(w,2)),"9-sinf (mis va uning birikmalari)",2)

Q3=[q_nitrate_hno3,q_hydrate_heat,q_nh3_water,q_alloy_burn,q_kclo3_so2,q_nacl_hcl,q_caco3_hcl,q_cu_o2_h2so4]

# -------------------------------------------------- (2) 41 / 43 SSENARIYLAR --------------------------------------------------
def w41_nitrate_elec(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2,0.3]); Wt=r.choice([200,300]); f=r.choice([0.5,0.6,0.8]); I=10
    m0=a*187.5+b*85; t=round(2*F*f*a/I)
    nNO2=2*a; nO2=a/2+b/2; nO2res=b/2; msolN=Wt+108*a; wN=126*a/msolN*100
    acid=98*a/0.1; sol2=80*a+acid; wCu=160*a/sol2*100
    nCu=f*a; vO2=nCu/2*V; sol3=sol2-80*nCu; wCu2=160*a*(1-f)/sol3*100; wH=98*nCu/sol3*100
    text=("Cu(NO3)2 va NaNO3 dan iborat %s g aralashma doimiy massagacha qizdirildi (Cu(NO3)2 → CuO, NO2, O2; NaNO3 → NaNO2 + O2). Ajralgan gazlar aralashmasi sovitilib, %d g suvga yuborildi "
          "Qattiq qoldiq suvga tushirilganda NaNO2 erib, CuO erimay qoldi; cho'kma ajratilib, 10 %% li sulfat kislotaning stexiometrik miqdorida eritildi. "
          "Hosil bo'lgan eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (Cu²⁺ ning bir qismi eritmada qoldi).")%(f2(m0,2),Wt,I,t)
    bands=["Barcha jarayonlarning reaksiya tenglamalarini yozing va tenglashtiring.",
           "Qizdirishda ajralgan gazlarning mol miqdorlarini va yutilmay qolgan gaz hajmini (l, n.sh.) hisoblang.",
           "Gazlar yutilgandan keyingi eritmada HNO3 ning massa ulushini (%) toping.",
           "Qattiq qoldiqdagi NaNO2 va CuO massalarini (g) aniqlang.",
           "CuO sulfat kislotada erigandan keyingi eritmada CuSO4 ning massa ulushini (%) hisoblang.",
           "Elektrolizda katodda ajralgan mis massasini (g) va anodda ajralgan gaz hajmini (l, n.sh.) toping.",
           "Elektroliz tugagach eritmadagi CuSO4 va H2SO4 ning massa ulushlarini (%) aniqlang."]
    sol=["2Cu(NO3)2 → 2CuO + 4NO2↑ + O2↑; 2NaNO3 → 2NaNO2 + O2↑; 4NO2 + O2 + 2H2O → 4HNO3; CuO + H2SO4 → CuSO4 + H2O; 2CuSO4 + 2H2O → 2Cu + O2↑ + 2H2SO4 (elektroliz)",
         "n(Cu(NO3)2) = %s mol, n(NaNO3) = %s mol; NO2 = 2·%s = **%s mol**; O2 = %s/2 + %s/2 = **%s mol**; NO2 uchun O2 = %s/4 = %s mol sarflanadi → yutilmay qolgani %s mol = **%s l**"%(f2(a),f2(b),f2(a),f2(nNO2),f2(a),f2(b),f2(nO2),f2(nNO2),f2(nNO2/4,3),f2(nO2res,3),f2(nO2res*V,2)),
         "n(HNO3) = n(NO2) = %s mol = %s g; eritma massasi = %d + 46·%s + 32·%s = %d + %s = %s g → ω = **%s %%**"%(f2(nNO2),f2(126*a,1),Wt,f2(nNO2),f2(nNO2/4,3),Wt,f2(108*a,1),f2(msolN,1),f2(wN,2)),
         "CuO: %s mol → **%s g**; NaNO2: %s mol → **%s g**"%(f2(a),f2(80*a,1),f2(b),f2(69*b,1)),
         "n(H2SO4) = %s mol → 10 %% li eritma %s g; eritma = %s + %s = %s g; m(CuSO4) = %s g → ω = **%s %%**"%(f2(a),f2(acid,1),f2(80*a,1),f2(acid,1),f2(sol2,1),f2(160*a,1),f2(wCu,2)),
         "Q = I·t = %d·%d = %d C; n(e) = %s mol; n(Cu) = %s mol → **%s g**; anodda O2 = %s/2 = %s mol → **%s l**"%(I,t,I*t,f2(I*t/F,3),f2(nCu,3),f2(nCu*64,2),f2(nCu,3),f2(nCu/2,4),f2(vO2,2)),
         "Eritma massasi = %s − (64·%s + 32·%s) = %s g; CuSO4 qoldi: %s mol = %s g → ω = **%s %%**; H2SO4 hosil bo'ldi: %s mol = %s g → ω = **%s %%**"%(f2(sol2,1),f2(nCu,3),f2(nCu/2,4),f2(sol3,1),f2(a*(1-f),3),f2(160*a*(1-f),1),f2(wCu2,2),f2(nCu,3),f2(98*nCu,2),f2(wH,2))]
    return W("41",text,bands,sol,mk_scores(7))

def w41_nh3_cycle(r):
    y=r.choice([0.5,1.0]); n1=2; n2=6; Vv=2; Wt=r.choice([200,300]);
    nNH3=2*y; K=(nNH3/Vv)**2/(((n1-y)/Vv)*((n2-3*y)/Vv)**3)
    ntot0=n1+n2; nteq=ntot0-2*y; ratio=nteq/ntot0; Mavg=(28*n1+2*n2)/nteq; D=Mavg/2
    w=nNH3*17/(Wt+nNH3*17)*100; acid=nNH3/2*98/0.2; salt=nNH3/2*132; wN=28/132*100
    text=("Hajmi %d l bo'lgan yopiq idishga %d mol N2 va %d mol H2 solindi, katalizator ishtirokida qizdirilib muvozanat qaror toptirildi (muvozanatda %s mol NH3 hosil bo'ldi). Aralashma sovitilib, "
          "hosil bo'lgan ammiakning hammasi %d g suvda eritildi. Olingan ammiak eritmasi 20 %% li sulfat kislota eritmasi bilan to'liq neytrallandi (o'rta tuz hosil bo'lguncha), so'ng eritma bug'latilib, tuz ajratib olindi.")%(Vv,n1,n2,f2(nNH3,1),Wt)
    bands=["Reaksiya tenglamalarini yozing; jarayon sxemasini tuzing.",
           "Muvozanat konstantasini (K) hisoblang (konsentratsiyalar mol/l da).",
           "Muvozanat holatidagi bosimning boshlang'ich bosimga nisbatini (T = const) va gazlar aralashmasining vodorodga nisbatan zichligini toping.",
           "Ammiak eritmasida NH3 ning massa ulushini (%) hisoblang.",
           "Neytrallash uchun zarur 20 % li H2SO4 eritmasining massasini (g) aniqlang.",
           "Ajratib olingan tuz massasini (g) va undagi azotning massa ulushini (%) toping."]
    sol=["N2 + 3H2 ⇌ 2NH3; 2NH3 + H2SO4 → (NH4)2SO4",
         "Muvozanatda: NH3 %s mol; N2 %s − %s = %s mol; H2 %s − 3·%s = %s mol; [NH3] = %s, [N2] = %s, [H2] = %s mol/l; K = [NH3]²/([N2][H2]³) = **%s**"%(f2(nNH3,2),f2(n1),f2(y),f2(n1-y),f2(n2),f2(y),f2(n2-3*y),f2(nNH3/Vv,3),f2((n1-y)/Vv,3),f2((n2-3*y)/Vv,3),f2(K,3)),
         "n(umumiy): %s → %s mol; p₂/p₁ = %s/%s = **%s**; M(o'rt) = (28·%d + 2·%d)/%s = %s → D(H2) = **%s**"%(f2(ntot0,1),f2(nteq,1),f2(nteq,1),f2(ntot0,1),f2(ratio,3),n1,n2,f2(nteq,1),f2(Mavg,2),f2(D,2)),
         "m(NH3) = %s·17 = %s g; ω = %s/(%d + %s) = **%s %%**"%(f2(nNH3,1),f2(nNH3*17,1),f2(nNH3*17,1),Wt,f2(nNH3*17,1),f2(w,2)),
         "n(H2SO4) = n(NH3)/2 = %s mol = %s g → 20 %% li eritma **%s g**"%(f2(nNH3/2,2),f2(nNH3/2*98,1),f2(acid,1)),
         "n((NH4)2SO4) = %s mol → m = **%s g**; ω(N) = 28/132 = **%s %%**"%(f2(nNH3/2,2),f2(salt,1),f2(wN,1))]
    return W("41",text,bands,sol,mk_scores(6))

def w41_cu_mg(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2,0.3]); h=r.choice([0.1,0.2]); I=10
    m=64*a+24*b; m2=80*a+40*b; ac=98*(a+b)/0.1; sol1=m2+ac
    Qe=2*a+2*h; t=round(F*Qe/I); nO2=Qe/4; loss=80*a+18*h; sol2=sol1-loss
    import math as _m
    _g=_m.gcd(round(a*10),round(b*10)); _p,_q=round(a*10)//_g,round(b*10)//_g
    if r.random()<0.6:
        text=("Mis va magniy kukunlaridan iborat aralashmada mis va magniyning mol nisbati %d : %d. Aralashma havoda to'liq oksidlanganda uning massasi %s g ga ortdi. Hosil bo'lgan oksidlar 10 %% li sulfat kislotaning stexiometrik miqdorida eritildi. "
              "Olingan eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (jarayonda Cu²⁺ to'liq tugadi va suv ham elektrolizga uchradi).")%(_p,_q,f2(16*(a+b),2),I,t)
    else:
        text=("Mis va magniy kukunlaridan iborat %s g aralashma havoda to'liq oksidlandi, natijada qattiq modda massasi %s g bo'ldi. Hosil bo'lgan oksidlar 10 %% li sulfat kislotaning stexiometrik miqdorida eritildi. "
              "Olingan eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi (jarayonda Cu²⁺ to'liq tugadi va suv ham elektrolizga uchradi).")%(f2(m,2),f2(m2,2),I,t)
    bands=["Barcha jarayonlarning reaksiya tenglamalarini yozing va tenglashtiring.",
           "Dastlabki aralashmadagi mis va magniyning massalarini (g) aniqlang.",
           "Oksidlanishga sarflangan kislorodning hajmini (l, n.sh.) va kislota eritmasining massasini (g) hisoblang.",
           "Oksidlar erigandan keyingi eritmada CuSO4 va MgSO4 ning massa ulushlarini (%) toping.",
           "Elektrolizda katodda ajralgan mis massasini (g) va vodorod hajmini (l, n.sh.) hisoblang.",
           "Anodda ajralgan gaz hajmini (l, n.sh.) toping.",
           "Elektroliz tugagach eritmadagi MgSO4 va H2SO4 ning massa ulushlarini (%) aniqlang."]
    sol=["2Cu + O2 → 2CuO; 2Mg + O2 → 2MgO; CuO + H2SO4 → CuSO4 + H2O; MgO + H2SO4 → MgSO4 + H2O; 2CuSO4 + 2H2O → 2Cu + O2 + 2H2SO4; 2H2O → 2H2 + O2",
         "64x + 24y = %s; 80x + 40y = %s → x = %s, y = %s: m(Cu) = **%s g**, m(Mg) = **%s g**"%(f2(m,2),f2(m2,2),f2(a),f2(b),f2(64*a,2),f2(24*b,2)),
         "m(O2) = %s − %s = %s g → **%s l**; n(H2SO4) = x + y = %s mol → %s g 10 %% li eritma = **%s g**; eritma = %s + %s = %s g"%(f2(m2,2),f2(m,2),f2(m2-m,2),f2((m2-m)/32*V,2),f2(a+b),f2(98*(a+b),1),f2(ac,1),f2(m2,2),f2(ac,1),f2(sol1,1)),
         "CuSO4: %s g → ω = **%s %%**; MgSO4: %s g → ω = **%s %%**"%(f2(160*a,1),f2(160*a/sol1*100,2),f2(120*b,1),f2(120*b/sol1*100,2)),
         "Q = %d·%d = %d C → n(e) = %s mol; Cu²⁺ ga 2·%s = %s mol e⁻ → Cu **%s g**; qolgan %s mol e⁻ → H2 = **%s mol = %s l**"%(I,t,I*t,f2(Qe,3),f2(a),f2(2*a,2),f2(64*a,2),f2(2*h,2),f2(h,2),f2(h*V,2)),
         "Anodda barcha e⁻ O2 ga: n(O2) = %s/4 = %s mol → **%s l**"%(f2(Qe,3),f2(nO2,3),f2(nO2*V,2)),
         "Massa yo'qotilishi: Cu %s + H2 %s + O2 %s = %s g; eritma %s g; MgSO4 → **%s %%**; H2SO4 (CuSO4 elektrolizidan) %s mol = %s g → **%s %%**"%(f2(64*a,2),f2(2*h,2),f2(nO2*32,2),f2(loss,2),f2(sol2,1),f2(120*b/sol2*100,2),f2(a,2),f2(98*a,1),f2(98*a/sol2*100,2))]
    return W("41",text,bands,sol,mk_scores(7))

def w43_carb_naoh(r):
    x,y=r.choice([(0.3,0.2),(0.2,0.2),(0.3,0.1),(0.4,0.2)]); n=x+y; k=r.choice([1.25,1.5,1.75]); nNaOH=k*n
    u=nNaOH-n; w=n-u; m=100*x+84*y; dm=44*n
    hcl=2*n*36.5/0.1; resid=56*x+40*y; solm=resid+hcl
    from fractions import Fraction as _Fr
    _fr=_Fr(100*x).limit_denominator(500)/_Fr(84*y).limit_denominator(500)
    if r.random()<0.6 and max(_fr.numerator,_fr.denominator)<=40:
        text=("CaCO3 va MgCO3 dan iborat aralashmada ularning massalari nisbati %d : %d. Aralashma doimiy massagacha qizdirilganda massasi %s g ga kamaydi. Ajralgan gaz %s mol NaOH saqlagan eritmaga yuttirildi (gaz to'liq yutildi), hosil bo'lgan eritmaga mo'l BaCl2 eritmasi qo'shildi. "
              "Qizdirishdan qolgan qattiq qoldiq esa 10 %% li xlorid kislotaning stexiometrik miqdorida eritildi.")%(_fr.numerator,_fr.denominator,f2(dm,1),f2(nNaOH,2))
    else:
        text=("CaCO3 va MgCO3 dan iborat %s g aralashma doimiy massagacha qizdirilganda massasi %s g ga kamaydi. Ajralgan gaz %s mol NaOH saqlagan eritmaga yuttirildi (gaz to'liq yutildi), hosil bo'lgan eritmaga mo'l BaCl2 eritmasi qo'shildi. "
              "Qizdirishdan qolgan qattiq qoldiq esa 10 %% li xlorid kislotaning stexiometrik miqdorida eritildi.")%(f2(m,1),f2(dm,1),f2(nNaOH,2))
    bands=["Barcha reaksiyalarning tenglamalarini yozing va tenglashtiring.",
           "Dastlabki aralashmadagi karbonatlarning massalarini (g) aniqlang.",
           "Ajralgan gazning hajmini (l, n.sh.) hisoblang va hosil bo'lgan tuzlar tarkibini (o'rta/nordon) aniqlang.",
           "Gaz yutilgandan keyingi eritmadagi tuzlarning massalarini (g) toping.",
           "BaCl2 qo'shilganda hosil bo'lgan cho'kma massasini (g) hisoblang.",
           "Qoldiq erigan eritmaning massasini (g) va undagi tuzlarning massa ulushlarini (%) toping."]
    sol=["CaCO3 → CaO + CO2; MgCO3 → MgO + CO2; CO2 + 2NaOH → Na2CO3 + H2O; CO2 + NaOH → NaHCO3; Na2CO3 + BaCl2 → BaCO3↓ + 2NaCl; CaO + 2HCl → CaCl2 + H2O; MgO + 2HCl → MgCl2 + H2O",
         "n(CO2) = %s/44 = %s mol; 100x + 84y = %s; x + y = %s → x = %s, y = %s: m(CaCO3) = **%s g**, m(MgCO3) = **%s g**"%(f2(dm,1),f2(n,2),f2(m,1),f2(n,2),f2(x),f2(y),f2(100*x,1),f2(84*y,1)),
         "V(CO2) = **%s l**; n(NaOH)/n(CO2) = %s (1 va 2 orasida) → ikkala tuz: Na2CO3 va NaHCO3"%(f2(n*V,2),f2(k,2)),
         "u + w = %s; 2u + w = %s → Na2CO3 u = %s mol (**%s g**), NaHCO3 w = %s mol (**%s g**)"%(f2(n,2),f2(nNaOH,2),f2(u,3),f2(106*u,2),f2(w,3),f2(84*w,2)),
         "Faqat Na2CO3 cho'kma beradi (Ba(HCO3)2 eriydi): n(BaCO3) = %s mol → **%s g**"%(f2(u,3),f2(197*u,2)),
         "n(HCl) = 2(x + y) = %s mol → 10 %% li eritma %s g; qoldiq %s g (CaO %s + MgO %s); eritma = **%s g**; CaCl2 %s g → **%s %%**; MgCl2 %s g → **%s %%**"%(f2(2*n,2),f2(hcl,1),f2(resid,1),f2(56*x,1),f2(40*y,1),f2(solm,1),f2(111*x,1),f2(111*x/solm*100,2),f2(95*y,1),f2(95*y/solm*100,2))]
    text+=" Qoldiqning HCl dagi eritmasiga mo'l Na2CO3 eritmasi qo'shilib, hosil bo'lgan cho'kma ajratildi va doimiy massagacha qizdirildi; ajralgan gaz mo'l ohakli suvga yuborildi."
    bands+=["Na2CO3 qo'shilganda hosil bo'lgan cho'kmalarning umumiy massasini (g) hisoblang.","Cho'kma qizdirilganda massa necha gramga kamayadi?","Ohakli suvga yuborilganda hosil bo'lgan cho'kma massasini (g) toping."]
    sol+=["CaCl2 + Na2CO3 → CaCO3↓; MgCl2 + Na2CO3 → MgCO3↓: karbonatlar dastlabki aralashmadagidek – 100·%s + 84·%s = **%s g**"%(f2(x,2),f2(y,2),f2(m,1)),"Massa kamayishi dastlabki qizdirishdagidek: 44·%s = **%s g**"%(f2(n,2),f2(dm,1)),"CO2 = %s mol → CO2 + Ca(OH)2 → CaCO3↓: **%s g**"%(f2(n,2),f2(100*n,1))]
    return W("43",text,bands,sol,mk_scores(6))

def w43_ammonium(r):
    for _ in range(100):
        a=r.choice([0.1,0.2,0.3,0.4]); b=r.choice([0.05,0.1,0.15]); c=r.choice([0.2,0.25,0.3,0.4,0.5])
        nn=a+2*b; q=nn/c
        if 1.05<q<1.95: break
    y=nn-c; x=c-y
    m=53.5*a+132*b; VN=nn*V; bas=233*b
    text=("NH4Cl va (NH4)2SO4 dan iborat %s g aralashmaning bir porsiyasi mo'l NaOH eritmasi bilan qizdirilganda %s l (n.sh.) gaz ajraldi. Xuddi shunday massali ikkinchi porsiya suvda eritilib, mo'l BaCl2 eritmasi bilan ta'sirlashtirildi. "
          "Birinchi porsiyadan ajralgan gaz %s mol H3PO4 saqlagan eritmaga to'liq yuttirildi (NH4H2PO4 va (NH4)2HPO4 aralashmasi hosil bo'ldi).")%(f2(m,2),f2(VN,2),f2(c,2))
    bands=["Barcha reaksiyalarning tenglamalarini yozing va tenglashtiring.",
           "Dastlabki aralashmadagi tuzlarning massalarini (g) aniqlang.",
           "Ikkinchi porsiyada hosil bo'lgan cho'kma massasini (g) hisoblang.",
           "Fosfat kislotaga yuttirilganda hosil bo'lgan tuzlarning mol miqdorlarini toping.",
           "Hosil bo'lgan fosfat tuzlari aralashmasining massasini (g) va undagi azot massa ulushini (%) aniqlang.",
           "Birinchi porsiyada ishlatilgan NaOH ning minimal massasini (g) hisoblang."]
    mix=115*x+132*y; N=14*x+28*y
    sol=["NH4Cl + NaOH → NaCl + NH3↑ + H2O; (NH4)2SO4 + 2NaOH → Na2SO4 + 2NH3↑ + 2H2O; (NH4)2SO4 + BaCl2 → BaSO4↓ + 2NH4Cl; NH3 + H3PO4 → NH4H2PO4; 2NH3 + H3PO4 → (NH4)2HPO4",
         "53,5x + 132y = %s; x + 2y = %s/22,4 = %s → x = %s, y = %s: m(NH4Cl) = **%s g**, m((NH4)2SO4) = **%s g**"%(f2(m,2),f2(VN,2),f2(nn,2),f2(a),f2(b),f2(53.5*a,2),f2(132*b,2)),
         "n(BaSO4) = n((NH4)2SO4) = %s mol → **%s g**"%(f2(b,3),f2(bas,2)),
         "NH3 %s mol, H3PO4 %s mol (nisbat %s): u + v = %s; u + 2v = %s → NH4H2PO4 **%s mol**, (NH4)2HPO4 **%s mol**"%(f2(nn,2),f2(c,2),f2(q,2),f2(c,2),f2(nn,2),f2(x,3),f2(y,3)),
         "m = 115·%s + 132·%s = **%s g**; n(N) = %s mol → %s g → ω = **%s %%**"%(f2(x,3),f2(y,3),f2(mix,2),f2(nn,2),f2(N,2),f2(N/mix*100,2)),
         "n(NaOH) = a + 2b = %s mol → **%s g**"%(f2(nn,2),f2(nn*40,1))]
    text+=" Hosil bo'lgan fosfat tuzlari aralashmasi mo'l NaOH bilan qizdirilganda ajralgan gaz 300 g suvga yuttirildi va olingan eritma 10 %% li HCl eritmasi bilan to'liq neytrallandi." % ()
    bands+=["Fosfat tuzlari aralashmasi NaOH bilan qizdirilganda ajralgan gazning hajmini (l, n.sh.) toping.","Gaz 300 g suvga yuttirilganda eritmadagi moddaning massa ulushini (%) hisoblang.","Eritmani neytrallash uchun sarflangan 10 % li HCl eritmasining massasini (g) aniqlang."]
    sol+=["NH4H2PO4 → 1 NH3, (NH4)2HPO4 → 2 NH3: x + 2y = %s mol (dastlabki NH3 bilan bir xil) → **%s l**"%(f2(nn,2),f2(nn*V,2)),"ω = %s·17/(300 + %s·17) = **%s %%**"%(f2(nn,2),f2(nn,2),f2(nn*17/(300+nn*17)*100,2)),"NH3 + HCl → NH4Cl: n(HCl) = %s mol = %s g → 10 %% li eritma **%s g**"%(f2(nn,2),f2(nn*36.5,2),f2(nn*36.5/0.1,1))]
    return W("43",text,bands,sol,mk_scores(6))

def w43_fe_mix(r):
    a,b=r.choice([(0.1,0.1),(0.2,0.1),(0.1,0.2),(0.2,0.2)]); W0=r.choice([300,400,500])
    mFe=56*(a/2+b); M=108*a+64*b; D=M-mFe
    nFe=a/2+b; sol_f=W0+mFe-M; wFe=180*nFe/sol_f*100
    nO2=nFe/4; fe2o3=nFe/2*160
    text=("Tarkibida AgNO3 va Cu(NO3)2 bo'lgan %d g eritmaga temir plastinka tushirildi (Ag⁺ va Cu²⁺ ning hammasi o'rnini bosdi). Plastinkada ajralgan metallar massasi %s g, plastinka massasi esa %s g ga ortdi. "
          "Plastinka olingach, eritmaga mo'l NaOH eritmasi qo'shildi, hosil bo'lgan cho'kma havoda to'liq oksidlanib, so'ng doimiy massagacha kuydirildi.")%(W0,f2(M,2),f2(D,2))
    bands=["Barcha reaksiyalarning tenglamalarini yozing va tenglashtiring.",
           "Eritmadagi AgNO3 va Cu(NO3)2 ning miqdorlarini (mol) toping.",
           "Eritmaga o'tgan temirning massasini (g) hisoblang.",
           "Plastinka olingandan keyin eritmadagi Fe(NO3)2 ning massa ulushini (%) aniqlang.",
           "Cho'kmani oksidlashga sarflangan kislorodning hajmini (l, n.sh.) hisoblang.",
           "Kuydirishdan hosil bo'lgan qattiq moddaning massasini (g) toping."]
    sol=["Fe + 2AgNO3 → Fe(NO3)2 + 2Ag; Fe + Cu(NO3)2 → Fe(NO3)2 + Cu; Fe(NO3)2 + 2NaOH → Fe(OH)2↓ + 2NaNO3; 4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3; 2Fe(OH)3 → Fe2O3 + 3H2O",
         "m(erigan Fe) = %s − %s = %s g → n(Fe) = %s mol = a/2 + b; 108a + 64b = %s; → a = **%s mol**, b = **%s mol**"%(f2(M,2),f2(D,2),f2(mFe,2),f2(nFe,3),f2(M,2),f2(a),f2(b)),
         "m(Fe) = **%s g** (ortgan massa: ajralgan metall − erigan temir)"%f2(mFe,2),
         "Eritma massasi = %d + %s − %s = %s g; Fe(NO3)2: %s mol → %s g → ω = **%s %%**"%(W0,f2(mFe,2),f2(M,2),f2(sol_f,2),f2(nFe,3),f2(180*nFe,2),f2(wFe,2)),
         "n(O2) = n(Fe(OH)2)/4 = %s/4 = %s mol → **%s l**"%(f2(nFe,3),f2(nO2,4),f2(nO2*V,2)),
         "n(Fe2O3) = %s/2 = %s mol → m = **%s g**"%(f2(nFe,3),f2(nFe/2,4),f2(fe2o3,2))]
    text+=" Kuydirishdan hosil bo'lgan oksid alyuminiy bilan qizdirilganda (alyuminotermiya) metall hosil bo'ldi; bu metall mo'l xlorid kislotada eritilib, ajralgan gaz qizdirilgan mis(II) oksid ustidan o'tkazildi."
    bands+=["Alyuminotermiyada sarflangan alyuminiy massasini (g) hisoblang.","Metallning xlorid kislota bilan reaksiyasida ajralgan gaz hajmini (l, n.sh.) toping.","Gaz mis(II) oksid bilan reaksiyaga kirishganda hosil bo'lgan mis massasini (g) aniqlang."]
    sol+=["Fe2O3 + 2Al → Al2O3 + 2Fe: n(Al) = n(Fe) = %s mol → **%s g**"%(f2(nFe,3),f2(27*nFe,2)),"Fe + 2HCl → FeCl2 + H2: **%s l**"%f2(nFe*22.4,2),"H2 + CuO → Cu + H2O: n(Cu) = %s mol → **%s g**"%(f2(nFe,3),f2(nFe*64,2))]
    return W("43",text,bands,sol,mk_scores(6))


SC5=[(6,3),(2,1),(3,3),(2,2),(2,1)]   # spetsifikatsiya: 5 bandli topshiriq (M 15 + A 10 = 25)
def to5(w,groups):
    # bandlarni (ketma-ket) 5 tagacha birlashtiramiz: spetsifikatsiya 41/43 uchun 3-5 band talab qiladi
    bands=[];sol=[]
    for g in groups:
        g=g if isinstance(g,tuple) else (g,)
        bands.append(' '.join(w.bands[i] for i in g)); sol.append('; '.join(w.sol[i] for i in g))
    w.bands=bands; w.sol=sol; w.score=SC5
    return w

def _w(f,groups):
    def g(r): return to5(f(r),groups)
    g.__name__=f.__name__
    return g
NEW41B=[_w(w41_nitrate_elec,[(0,1),(2,3),4,5,6]),_w(w41_nh3_cycle,[(0,1),2,3,4,5]),_w(w41_cu_mg,[(0,1),2,3,(4,5),6])]
NEW43=[_w(w43_carb_naoh,[(0,1),2,(3,6),(4,7),(5,8)]),_w(w43_ammonium,[(0,1),2,(3,6),(4,7),(5,8)]),_w(w43_fe_mix,[(0,1),2,(3,6),(4,7),(5,8)])]

HARD_UM={'eritma %/M/eruvchanlik':[q_nitrate_hno3,q_hydrate_heat],'elektroliz':[q_nacl_hcl],'mol/stexiometriya':[q_alloy_burn,q_caco3_hcl],'qonunlar/gaz/ekvivalent':[q_kclo3_so2]}
HARD_INORG3={'S/SO2/H2SO4':[q_kclo3_so2],'N/NH3/HNO3':[q_nh3_water,q_nitrate_hno3],'IIA/IIIA metallar (Ca,Mg,Al)':[q_alloy_burn,q_caco3_hcl],'d-metallar (Fe,Cu,Zn,Cr)':[q_cu_o2_h2so4],'tuzlarning termik parchalanishi':[q_nitrate_hno3],'galogenlar':[q_nacl_hcl],'suv qattiqligi':[q_hydrate_heat]}
