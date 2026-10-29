from core import *
import re
COMB=['1, 2','1, 3','2, 3','1, 2, 3','2, 4','1, 4','3, 4','1, 3, 4','2, 3, 4','1, 2, 4','1','2','3','4']
def combo(r,flags,label):
    nums=[i+1 for i,f in enumerate(flags) if f]; ans=', '.join(map(str,nums))
    ws=[c for c in COMB if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws); return ans,ws[:3]
def stm(r,pool,k=4,want=True,intro=""):
    # pool: list of (statement, truth)
    for _ in range(50):
        it=r.sample(pool,k); fl=[t==want for _,t in it]
        if any(fl): break
    ans,ws=combo(r,fl,want)
    return ans,ws,it
# ---- IA metals
def c_iah2(r):
    mt=[('Na',23,'Na'),('K',39,'K'),('Li',7,'Li')]; a,b=r.sample(mt,2); na=r.choice([0.1,0.2,0.3]); nb=r.choice([0.1,0.2,0.3])
    mix=na*a[1]+nb*b[1]; h=(na+nb)/2*22.4
    return numq("%s va %s dan iborat %s g aralashma suv bilan reaksiyaga kirishdi. Ajralgan vodorodning hajmini (l, n.sh.) aniqlang."%(a[0],b[0],fmt(mix,2)),h,[h*2,h/2,(na+nb)*22.4,mix/2],"2M + 2H2O → 2MOH + H2: n(%s) = %s, n(%s) = %s mol → n(H2) = %s mol → %s l"%(a[0],fmt(na),b[0],fmt(nb),fmt((na+nb)/2,3),fmt(h,3)),"9-sinf (ishqoriy metallar)",2)
def c_nahco3(r):
    n=r.choice([0.2,0.3,0.4,0.5]); c=r.choice([0.2,0.3,0.4,0.5]);
    while not (c<n<2*c):
        n=r.choice([0.3,0.4,0.5,0.6]); c=r.choice([0.2,0.3,0.4])
    x=n-c; y=c-x  # Na2CO3 x, NaHCO3 y: x+y=c, 2x+y=n
    return numq("%s g natriy suvda eritildi, hosil bo'lgan eritmadan %s mol CO2 o'tkazildi. Hosil bo'lgan natriy gidrokarbonat massasini (g) aniqlang."%(fmt(n*23,2),fmt(c)),y*84,[x*106,(x+y)*84,n*84,y*106],"n(NaOH) = %s mol; x + y = %s; 2x + y = %s → Na2CO3 %s mol, NaHCO3 %s mol → %s g"%(fmt(n),fmt(c),fmt(n),fmt(x),fmt(y),fmt(y*84,2)),"9-sinf (ishqoriy metallar, uglerod)",2)
IAF=[("Natriy kerosin ostida saqlanadi",True),("Litiy eng yengil metall",True),("Natriy suv bilan reaksiyada H2 va NaOH hosil qiladi",True),("Kaliy suvdan og'ir",False),("Ishqoriy metallar tabiatda erkin holda uchraydi",False),("Natriyning olinishi suyuqlanma NaCl elektrolizi bilan",True),("Natriy atomining tashqi qavatida 2 ta elektron bor",False),("KOH – kuchli ishqor",True),("Ishqoriy metallar faqat oksidlovchi bo'ladi",False),("Natriy yonganda Na2O2 hosil bo'ladi",True),("Litiy odatiy sharoitda azot bilan reaksiyaga kirishadi (Li3N)",True)]
def t_iaf(r):
    ans,ws,it=stm(r,IAF)
    return Q("Ishqoriy metallar haqida qaysi fikrlar to'g'ri? "+'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(it)),ans,ws,'; '.join('%d) %s'%(i+1,'to\'g\'ri' if x[1] else 'noto\'g\'ri') for i,x in enumerate(it)),"9-sinf (ishqoriy metallar); Tashev",'theory')
# ---- IIA, IIIA
def c_almg(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2]); mt=r.choice([('Mg',24,1),('Zn',65,1),('Ca',40,1)])
    mix=a*27+b*mt[1]; h=a*1.5+b*mt[2]; V=h*22.4; w=a*27/mix*100
    ask=r.choice(['w','V'])
    if ask=='w': return numq("Alyuminiy va %s dan iborat %s g aralashma mo'l xlorid kislotada eritilganda %s l (n.sh.) vodorod ajraldi. Aralashmadagi alyuminiyning massa ulushini (%%) aniqlang."%(NAME2[mt[0]],fmt(mix,2),fmt(V,2)),w,[100-w,w/2,a*27,b*mt[1]/mix*100*1.0 if b*mt[1]/mix*100!=w else w*0.9],"27x + %d y = %s; 1,5x + y = %s → x = %s mol Al → ω = %s %%"%(mt[1],fmt(mix,2),fmt(h,3),fmt(a),fmt(w,1)),"9-sinf (Al, Mg, Ca)",1)
    return numq("Alyuminiy (%s mol) va %s (%s mol) aralashmasi mo'l xlorid kislotada eritildi. Ajralgan vodorodning hajmini (l, n.sh.) aniqlang."%(fmt(a),NAME2[mt[0]],fmt(b)),V,[(a+b)*22.4,V*2,V/2,(a*3+b)*22.4],"2Al → 3H2: %s mol; %s → H2: %s mol; jami %s mol = %s l"%(fmt(a*1.5),mt[0],fmt(b),fmt(h,3),fmt(V,2)),"9-sinf",2)
NAME2={'Mg':'magniy','Zn':'rux','Ca':'kalsiy','Fe':'temir','Cu':'mis'}
def c_alnaoh(r):
    me=r.choice([('Cu',64),('Fe',56),('Mg',24)]); a=r.choice([0.1,0.2,0.3]); b=r.choice([0.1,0.2]); mix=a*27+b*me[1]; V=a*1.5*22.4
    ask=r.choice(['V','w'])
    if ask=='V': return numq("Alyuminiy va %s dan iborat %s g aralashma mo'l NaOH eritmasida eritildi. Ajralgan gazning hajmini (l, n.sh.) aniqlang."%(NAME2[me[0]],fmt(mix,2)),V,[V*2,V/2,mix/27*22.4,a*22.4],"2Al + 2NaOH + 6H2O → 2Na[Al(OH)4] + 3H2: n(Al) = %s mol → n(H2) = %s mol → %s l"%(fmt(a),fmt(a*1.5),fmt(V,2)),"9-sinf (alyuminiy)",2)
    w=b*me[1]/mix*100
    return numq("Alyuminiy va %s dan iborat %s g aralashma mo'l NaOH eritmasida eritilganda %s l (n.sh.) gaz ajraldi. Aralashmadagi %s ning massa ulushini (%%) aniqlang."%(NAME2[me[0]],fmt(mix,2),fmt(V,2),NAME2[me[0]]),w,[100-w,w/2,a*27/mix*100*0.9,b*me[1]],"n(H2) = %s → n(Al) = %s mol (%s g); qolgan %s g %s → %s %%"%(fmt(V/22.4,2),fmt(a),fmt(a*27,2),fmt(b*me[1],2),me[0],fmt(w,1)),"9-sinf (alyuminiy)",1)
def c_co2ca(r):
    n=r.choice([0.2,0.3,0.4]); c=n*r.choice([1.5,2]) ;
    while c==2*n and False: pass
    hc=max(c-n,0)
    if c>2*n: c=2*n
    hc=c-n if c>n else 0
    return numq("%s mol Ca(OH)2 tutgan eritmadan %s mol karbonat angidrid o'tkazildi. Eritmada qolgan kalsiy gidrokarbonatning massasini (g) aniqlang."%(fmt(n),fmt(c)),hc*162,[n*100,c*162,(c-n)*100,hc*162*2],"CO2 + Ca(OH)2 → CaCO3 + H2O (%s mol); qolgan CO2 %s mol: CaCO3 + CO2 + H2O → Ca(HCO3)2 → %s mol = %s g"%(fmt(n),fmt(hc),fmt(hc),fmt(hc*162,2)),"9-sinf (uglerod; suv qattiqligi)",2)
def c_boil(r):
    n=r.choice([0.02,0.05,0.1]); what=r.choice(['CO2','CaCO3'])
    ans=n*22.4 if what=='CO2' else n*100
    return numq("%s mol Ca(HCO3)2 tutgan suv qaynatilganda %s %s ni toping%s."%(fmt(n),'ajralgan CO2 hajmini (l, n.sh.)' if what=='CO2' else "hosil bo'lgan CaCO3 cho'kma massasini (g)",'',''),ans,[ans*2,ans/2,ans*1.5,n*162],"Ca(HCO3)2 → CaCO3 + H2O + CO2: n = %s mol → %s"%(fmt(n),fmt(ans,2)),"9-sinf §24 (suv qattiqligi)",2)
def c_soda(r):
    a=r.choice([0.01,0.02,0.03]); b=r.choice([0.01,0.02,0.04]); c=r.choice([0.02,0.03])
    sol=(b+c)*106 if False else None
    # Ca(HCO3)2 a (temporary), CaSO4 b, MgCl2 c
    ans=(b+c)*106
    return numq("1 l suvda %s mol Ca(HCO3)2, %s mol CaSO4 va %s mol MgCl2 erigan. Suv qaynatilgandan keyin qolgan qattiqlikni yo'qotish uchun necha gramm soda (Na2CO3) kerak?"%(fmt(a),fmt(b),fmt(c)),ans,[(a+b+c)*106,b*106,c*106,(b+c)*53],"Qaynatganda Ca(HCO3)2 yo'qoladi; doimiy qattiqlik CaSO4 + MgCl2 = %s mol: Na2CO3 %s mol = %s g"%(fmt(b+c),fmt(b+c),fmt(ans,2)),"9-sinf §24 (doimiy qattiqlik, soda)",2)
# ---- d-metals
def c_cucuo(r):
    a=r.choice([6.4,12.8,3.2]); b=r.choice([0.1,0.2,0.05]); tot=a+b*80; salt=b*160
    return numq("Cu va CuO dan iborat %s g aralashma mo'l suyultirilgan H2SO4 da ishlandi, %s g qattiq qoldiq qoldi. Hosil bo'lgan tuz massasini (g) aniqlang."%(fmt(tot,2),fmt(a,2)),salt,[tot,a/64*160,salt*2,salt/2],"Cu erimaydi; m(CuO) = %s g = %s mol; CuO + H2SO4 → CuSO4 + H2O: %s g"%(fmt(b*80,2),fmt(b),fmt(salt,2)),"9-sinf (mis)",2)
def c_feoh(r):
    n=r.choice([0.1,0.2,0.05]); a=n*90
    return numq("%s g Fe(OH)2 havoda to'liq oksidlanib, Fe(OH)3 ga aylandi. Hosil bo'lgan Fe(OH)3 massasini (g) aniqlang."%fmt(a,2),n*107,[a,n*107*1.5,n*90*1.1,n*107/2],"4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3: n = %s mol → %s g"%(fmt(n),fmt(n*107,2)),"9-sinf (temir birikmalari)",2)
def c_fecl(r):
    n=r.choice([0.1,0.2,0.3]); d=n*(162.5-127)
    return numq("%s g temir bir qismi xlor bilan, xuddi shuncha qismi xlorid kislota bilan reaksiyaga kirishdi. Hosil bo'lgan tuzlar massalari farqini (g) aniqlang."%fmt(n*56,2),d,[n*162.5,n*127,d*2,n*35.5*2],"2Fe + 3Cl2 → 2FeCl3 (%s g); Fe + 2HCl → FeCl2 + H2 (%s g); farq %s g"%(fmt(n*162.5,2),fmt(n*127,2),fmt(d,2)),"9-sinf; Tashev (temir)",2)
def c_znzno(r):
    z=r.choice([0.1,0.2,0.05]); o=r.choice([0.1,0.2]); mix=z*65+o*81; V=z*22.4
    return numq("Zn va ZnO dan iborat %s g aralashma mo'l NaOH eritmasida eritilganda %s l (n.sh.) vodorod ajraldi. Aralashmadagi ZnO massasini (g) aniqlang."%(fmt(mix,2),fmt(V,2)),o*81,[z*65,mix,o*81*2,V],"Zn + 2NaOH + 2H2O → Na2[Zn(OH)4] + H2: n(Zn) = %s mol (%s g); ZnO = %s − %s = %s g"%(fmt(z),fmt(z*65,2),fmt(mix,2),fmt(z*65,2),fmt(o*81,2)),"9-sinf (rux, amfoterlik)",2)
def c_dich(r):
    n=r.choice([0.1,0.2,0.05]); what=r.choice(['Cr2O3','N2'])
    ans=n*152 if what=='Cr2O3' else n*22.4
    return numq("%s g (NH4)2Cr2O7 termik parchalandi ((NH4)2Cr2O7 → Cr2O3 + N2 + 4H2O). Hosil bo'lgan %s ni toping."%(fmt(n*252,2),'Cr2O3 massasini (g)' if what=='Cr2O3' else 'N2 hajmini (l, n.sh.)'),ans,[ans*2,ans/2,n*252,ans*1.5],"n((NH4)2Cr2O7) = %s mol → n(%s) = %s mol → %s"%(fmt(n),what,fmt(n),fmt(ans,2)),"9-sinf (xrom)",2)
DF=[("Temir sovuq konsentrlangan HNO3 da passivlanadi",True),("Mis suyultirilgan HCl bilan reaksiyaga kirishadi",False),("Fe(OH)2 havoda qo'ng'ir rangga o'tadi",True),("Zn(OH)2 amfoter xossaga ega",True),("Cr2O3 asosli oksid",False),("Cu(OH)2 qizdirilganda CuO ga parchalanadi",True),("Xrom (VI) oksidi (CrO3) kislotali oksid",True),("Temirning Cl2 bilan reaksiyasida FeCl2 hosil bo'ladi",False),("Mis nam havoda (CuOH)2CO3 qoplamasi bilan qoplanadi",True),("Rux eritmada Fe²⁺ ni siqib chiqara olmaydi",False)]
def t_df(r):
    ans,ws,it=stm(r,DF)
    return Q("d-metallar va ularning birikmalari haqida qaysi fikrlar to'g'ri? "+'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(it)),ans,ws,'; '.join('%d) %s'%(i+1,'to\'g\'ri' if x[1] else 'noto\'g\'ri') for i,x in enumerate(it)),"9-sinf; Tashev (Fe, Cu, Zn, Cr)",'theory')
# ---- nonmetals
def c_pyrite(r):
    m=r.choice([60,120,240]); y=r.choice([80,90,100]); n=m/120; h=n*2*98*y/100
    return numq("%s g FeS2 yondirilib, hosil bo'lgan SO2 dan H2SO4 olindi (jami unum %d %%). Sulfat kislota massasini (g) aniqlang."%(m,y),h,[n*98,h*2,n*2*98,h/2],"4FeS2 + 11O2 → 2Fe2O3 + 8SO2; 1 mol FeS2 → 2 mol H2SO4: %s mol → %s g (unum %d %%)"%(fmt(n),fmt(h,2),y),"Tashev (H2SO4 olinishi)",2)
def c_hno3(r):
    V=r.choice([5.6,11.2,22.4,44.8]); y=r.choice([80,90,100]); n=V/22.4*y/100; m=n*63
    return numq("%s l (n.sh.) ammiakdan nitrat kislota olindi (jami unum %d %%). Kislota massasini (g) aniqlang."%(fmt(V),y),m,[V/22.4*63,m*2,m/2,n*17],"NH3 → NO → NO2 → HNO3: n(HNO3) = %s mol → %s g"%(fmt(n,3),fmt(m,2)),"Tashev (HNO3 olinishi)",2)
def c_p(r):
    n=r.choice([0.1,0.2]); k=r.choice([1.5,2,3]);
    n_p=n; h=n_p  # P -> H3PO4
    kk={1.5:('NaH2PO4','Na2HPO4',120,142),2:('Na2HPO4',None,142,None),3:('Na3PO4',None,164,None)}
    if k==2: ans=n*142; nm='Na2HPO4'
    elif k==3: ans=n*164; nm='Na3PO4'
    else:
        # NaOH : H3PO4 = 1.5 -> NaH2PO4 0.5n and Na2HPO4 0.5n ; ask NaH2PO4
        ans=n*0.5*120; nm='NaH2PO4'
    return numq("%s g fosfor yondirilib, hosil bo'lgan oksid suvda eritildi (ortofosfat kislota), so'ng %s mol NaOH qo'shildi. Hosil bo'lgan %s massasini (g) aniqlang."%(fmt(n*31,2),fmt(n*k),nm),ans,[ans*2,ans/2,n*120,n*164 if nm!='Na3PO4' else n*142],"P → H3PO4 (%s mol); NaOH : H3PO4 = %s → %s %s mol = %s g"%(fmt(n),fmt(k),nm,fmt(ans/ (120 if nm=='NaH2PO4' else 142 if nm=='Na2HPO4' else 164),3),fmt(ans,2)),"Tashev (fosfor)",2)
def c_halo(r):
    nI=r.choice([0.1,0.2]); mc=r.choice([5,10]); mix=nI*150+mc; dm=nI*91.5;
    return numq("NaI va NaCl dan iborat %s g aralashma orqali mo'l xlor o'tkazilganda aralashma massasi %s g ga kamaydi. Aralashmadagi NaI ning massa ulushini (%%) aniqlang."%(fmt(mix,2),fmt(dm,2)),nI*150/mix*100,[100-nI*150/mix*100,nI*150,mc/mix*100,dm/mix*100],"2NaI + Cl2 → 2NaCl + I2: 1 mol NaI da Δm = 150 − 58,5 = 91,5 g; n(NaI) = %s mol → %s g → ω = %s %%"%(fmt(nI),fmt(nI*150,2),fmt(nI*150/mix*100,1)),"Tashev (galogenlar)",1)
NIT=[('Cu(NO3)2','CuO',80,188),('NaNO3','NaNO2',69,85),('AgNO3','Ag',108,170),('KNO3','KNO2',85,101),('Zn(NO3)2','ZnO',81,189),('Mg(NO3)2','MgO',40,148)]
def c_nitr(r):
    f,res,mr,mf=pick(r,NIT); n=r.choice([0.1,0.2,0.25]);
    return numq("%s g %s to'liq parchalanguncha qizdirildi. Qattiq qoldiq massasini (g) aniqlang."%(fmt(n*mf,2),f),n*mr,[n*mf,n*mr*2,n*mr/2,n*mf-n*mr],"%s qizdirilganda qoldiq %s: n = %s mol → %s g"%(f,res,fmt(n),fmt(n*mr,2)),"Tashev (nitratlar termik parchalanishi)",2)
def c_nacl_hcl(r):
    n=r.choice([0.2,0.5,1]); w=r.choice([200,250,500]); wt=n*36.5/(w+n*36.5)*100
    return numq("%s g NaCl ga mo'l kons. H2SO4 ta'sir ettirilib, ajralgan HCl %d g suvda eritildi. Hosil bo'lgan xlorid kislota massa ulushini (%%) aniqlang."%(fmt(n*58.5,2),w),wt,[n*36.5/w*100,wt*2,wt/2,n*58.5/(w+n*58.5)*100],"NaCl + H2SO4 → NaHSO4 + HCl: n(HCl) = %s mol = %s g; ω = %s/(%d + %s) = %s %%"%(fmt(n),fmt(n*36.5,2),fmt(n*36.5,2),w,fmt(n*36.5,2),fmt(wt,2)),"Tashev (HCl olinishi)",2)
def c_co2naoh(r):
    n=r.choice([0.2,0.3,0.4]); c=r.choice([0.1,0.15,0.2,0.3]);
    if c>=n: c=n/2
    # NaOH n mol, CO2 c mol (c<n<2c?) general
    if n>=2*c: res='Na2CO3'; m=c*106; sol="CO2 : NaOH = 1 : %s ≥ 1 : 2 → Na2CO3 %s mol"%(fmt(n/c),fmt(c))
    else:
        y=n-c; x=c-y; res='NaHCO3'; m=y*84; sol="x + y = %s; 2x + y = %s → NaHCO3 %s mol"%(fmt(c),fmt(n),fmt(y))
    return numq("%s mol NaOH tutgan eritmadan %s mol CO2 o'tkazildi. Hosil bo'lgan %s massasini (g) aniqlang."%(fmt(n),fmt(c),res),m,[m*2,m/2,n*40,c*84],sol+" → %s g"%fmt(m,2),"9-sinf (uglerod (IV) oksid)",2)
# theory: oxides/salts/acids
OXC=[('CO2','kislotali'),('Na2O','asosli'),('Al2O3','amfoter'),('NO','befarq'),('ZnO','amfoter'),('SO3','kislotali'),('CaO','asosli'),('CO','befarq'),('Cr2O3','amfoter'),('N2O','befarq'),('P2O5','kislotali'),('MgO','asosli'),('CrO3','kislotali'),('K2O','asosli')]
def t_oxcls(r):
    kind=r.choice(['kislotali','asosli','amfoter','befarq']); good=[x for x in OXC if x[1]==kind]; bad=[x for x in OXC if x[1]!=kind]
    k=r.randint(1,min(2,len(good))); lst=r.sample(good,k)+r.sample(bad,4-k); r.shuffle(lst)
    nums=[i+1 for i,x in enumerate(lst) if x[1]==kind]; ans=', '.join(map(str,nums)); ws=[c for c in COMB if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Quyidagi oksidlardan qaysilari %s oksidlar? %s"%(kind,'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(lst))),ans,ws[:3],'; '.join('%s – %s'%x for x in lst),"8-sinf; 9-sinf; Tashev (oksidlar sinflari)",'theory')
SALT=[('NaHCO3','nordon'),('(CuOH)2CO3','asosli'),('K2SO4','o\'rta'),('KAl(SO4)2','qo\'sh'),('Na2HPO4','nordon'),('Mg(OH)Cl','asosli'),('CaCO3','o\'rta'),('Na3PO4','o\'rta'),('KHSO4','nordon')]
def t_salt(r):
    kind=r.choice(['nordon','asosli','o\'rta']); good=[x for x in SALT if x[1]==kind]; bad=[x for x in SALT if x[1]!=kind]
    k=r.randint(1,2); lst=r.sample(good,k)+r.sample(bad,4-k); r.shuffle(lst)
    nums=[i+1 for i,x in enumerate(lst) if x[1]==kind]; ans=', '.join(map(str,nums)); ws=[c for c in COMB if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Quyidagi tuzlardan qaysilari %s tuz? %s"%(kind,'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(lst))),ans,ws[:3],'; '.join('%s – %s'%x for x in lst),"8-sinf; 9-sinf (tuzlar sinflari)",'theory')
PAIR=[('CuO','H2',True),('Cu','HCl',False),('Zn','NaOH',True),('Ag','H2SO4(suyult.)',False),('Fe','HCl',True),('Al2O3','NaOH',True),('CO2','CaO',True),('SiO2','H2O',False),('Cu','HNO3(kons.)',True),('Fe','HNO3(sovuq kons.)',False),('NaCl','HNO3',False),('Na2CO3','HCl',True),('ZnO','HCl',True),('Fe2O3','H2O',False),('CuSO4','NaOH',True),('MgCl2','KNO3',False)]
def t_react(r):
    want=r.choice([True,False]); lst=r.sample(PAIR,4)
    if not any(x[2]==want for x in lst): return t_react(r)
    nums=[i+1 for i,x in enumerate(lst) if x[2]==want]; ans=', '.join(map(str,nums)); ws=[c for c in COMB if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Qaysi juftliklar o'zaro reaksiyaga %s? %s"%('kirishadi' if want else 'kirishmaydi','; '.join('%d) %s va %s'%(i+1,x[0],x[1]) for i,x in enumerate(lst))),ans,ws[:3],'; '.join('%s + %s – %s'%(x[0],x[1],'boradi' if x[2] else 'bormaydi') for x in lst),"9-sinf; Tashev (anorganik birikmalar xossalari)",'theory')
FERT=[('NH4NO3','azotli'),('KCl','kaliyli'),('Ca(H2PO4)2','fosforli'),('(NH4)2SO4','azotli'),('K2SO4','kaliyli'),('CO(NH2)2','azotli'),('(NH4)2HPO4','murakkab (azot va fosforli)'),('KNO3','murakkab (azot va kaliyli)'),('Ca3(PO4)2','fosforli')]
def t_fert(r):
    kind=pick(r,['azotli','kaliyli','fosforli']); good=[x for x in FERT if x[1]==kind]; bad=[x for x in FERT if x[1]!=kind]
    k=min(len(good),r.randint(1,2)); lst=r.sample(good,k)+r.sample(bad,4-k); r.shuffle(lst)
    nums=[i+1 for i,x in enumerate(lst) if x[1]==kind]; ans=', '.join(map(str,nums)); ws=[c for c in COMB if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Quyidagi mineral o'g'itlardan qaysilari %s o'g'itlar jumlasiga kiradi? %s"%(kind,'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(lst))),ans,ws[:3],'; '.join('%s – %s'%x for x in lst),"Tashev (mineral o'g'itlar)",'theory')
def c_fert(r):
    f,e,k=pick(r,[('NH4NO3','N',2),('(NH4)2SO4','N',2),('CO(NH2)2','N',2),('KNO3','K',1),('K2SO4','K',2),('Ca(H2PO4)2','P',2)]);
    w=k*AM[e]/M(f)*100
    return numq("%s tarkibidagi %s ning massa ulushini (%%) aniqlang."%(f,{'N':'azot','K':'kaliy','P':'fosfor'}[e]),w,[w/2,w*2 if w*2<100 else w*0.8,M(f)/ (k*AM[e]) ,100-w],"ω = %d·%s/%s = %s %%"%(k,fmt(AM[e]),fmt(M(f),1),fmt(w,1)),"Tashev (o'g'itlar)",1)
NOB=[("Geliy eng yengil inert gaz",True),("Argon havoning hajmi bo'yicha eng ko'p uchraydigan inert gazi",True),("Neon atomida 8 ta tashqi elektron bor",True),("Geliyda 8 ta tashqi elektron bor",False),("Nodir gazlar odatiy sharoitda ko'p atomli molekulalar hosil qiladi",False),("Argon elektr lampalarida ishlatiladi",True),("Nodir gazlar kimyoviy jihatdan juda faol",False),("Neon reklama naylarida ishlatiladi",True)]
def t_nob(r):
    ans,ws,it=stm(r,NOB)
    return Q("Nodir gazlar haqida qaysi fikrlar to'g'ri? "+'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(it)),ans,ws,'; '.join('%d) %s'%(i+1,'to\'g\'ri' if x[1] else 'noto\'g\'ri') for i,x in enumerate(it)),"Tashev (nodir gazlar); 8-sinf",'theory')
def t_nitrate_prod(r):
    pool=[('KNO3','KNO2 va O2'),('Cu(NO3)2','CuO, NO2 va O2'),('AgNO3','Ag, NO2 va O2'),('NaNO3','NaNO2 va O2'),('Zn(NO3)2','ZnO, NO2 va O2'),('NH4NO3','N2O va H2O')]
    f,p=pick(r,pool); ws=[x[1] for x in pool if x[1]!=p]; r.shuffle(ws)
    return Q("%s qizdirilganda qanday moddalar hosil bo'ladi?"%f,p,ws[:3],"Nitratlar parchalanishi: K gacha – nitrit + O2; Mg–Cu oralig'ida – oksid + NO2 + O2; Cu dan keyin – metall + NO2 + O2","Tashev (nitratlar)",'theory')
def t_genetic(r):
    chain=[('Ca → CaO → Ca(OH)2 → CaCO3','Ca → CaO → Ca(OH)2 → CaCO3'),]
    ch=pick(r,[(['Ca','O2','H2O','CO2'],['CaO','Ca(OH)2','CaCO3']),(['S','O2','H2O','NaOH'],['SO2','H2SO3','Na2SO3']),(['Na','O2','H2O','HCl'],['Na2O','NaOH','NaCl']),(['P','O2','H2O','KOH'],['P2O5','H3PO4','K3PO4']),(['Cu','O2','H2SO4','NaOH'],['CuO','CuSO4','Cu(OH)2'])])
    reag,prods=ch; k=r.choice([0,1,2]);
    ws=[p for x in [['CaO','Ca(OH)2','CaCO3'],['SO2','H2SO3','Na2SO3'],['Na2O','NaOH','NaCl'],['P2O5','H3PO4','K3PO4'],['CuO','CuSO4','Cu(OH)2']] for p in x if p not in prods]; r.shuffle(ws)
    return Q("%s o'zgarishlar zanjirida (reagentlar: %s) %d-bosqichda hosil bo'ladigan modda formulasini toping."%(' → '.join([reag[0]]+['?']*3),', '.join(reag[1:]),k+1),prods[k],ws[:3],"%s: %s"%(reag[0],' → '.join([reag[0]]+prods)),"8-sinf; 9-sinf (genetik bog'lanish)",'theory')
