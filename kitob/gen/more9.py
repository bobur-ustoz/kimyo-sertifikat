import itertools
from core import *
# Samarqand darajasidagi anorganik masalalar: reagent yetishmasi (cheklovchi modda), aralashmalar, plastinka massasi o'zgarishi,
# nitratlarning parchalanishi, ko'p bosqichli unum. 8-9-sinf darsliklari doirasida.
V=22.4
def _f(x,nd=2): return fmt(x,nd)
def _pick2(r,opts):
    for _ in range(40):
        a=r.choice(opts); b=r.choice(opts)
        if a!=b: return a,b
    return opts[0],opts[1]

# 1) Metallar aralashmasi + kislota (H2 hajmidan tarkib)
MET=[('Mg',24,1),('Al',27,1.5),('Zn',65,1),('Fe',56,1)]
def c_metal_mix(r):
    (n1,M1,k1),(n2,M2,k2)=r.sample(MET,2); a,b=_pick2(r,[0.1,0.2,0.3,0.4]); acid=r.choice(['HCl','H2SO4 (suyultirilgan)'])
    m=a*M1+b*M2; h2=(a*k1+b*k2)*V; ask=r.choice(['m1','w2'])
    head="%s va %s aralashmasi (%s g) mo'l %s bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi. "%(n1,n2,_f(m),acid,_f(h2))
    sol="%s: x mol (H2 %s·x), %s: y mol (H2 %s·y); %d x + %d y = %s; %s x + %s y = %s → x = %s, y = %s; "%(n1,_f(k1),n2,_f(k2),M1,M2,_f(m),_f(k1),_f(k2),_f(h2/V),_f(a),_f(b))
    src="9-sinf (metallarning kislotalar bilan reaksiyasi)"
    if ask=='m1':
        return numq(head+"Aralashmadagi %s ning massasini (g) toping."%n1,a*M1,[b*M2,a*M1*2,m/2,a*M1/2],sol+"m(%s) = %s g"%(n1,_f(a*M1)),src,1)
    ans=b*M2/m*100
    return numq(head+"Aralashmadagi %s ning massa ulushini (%%) aniqlang."%n2,ans,[100-ans,b/(a+b)*100,a/(a+b)*100,50],sol+"ω = %s %%"%_f(ans,1),src,1)

# 2) Cu/Ag bilan aralashma: faqat faol metall reaksiyaga kirishadi
def c_metal_inert(r):
    act=r.choice([('Zn',65,1),('Mg',24,1),('Al',27,1.5),('Fe',56,1)]); inert=r.choice([('Cu',64),('Ag',108)])
    a=r.choice([0.1,0.2,0.3,0.4]); b=r.choice([0.1,0.2,0.3,0.5]); m=a*act[1]+b*inert[1]; h2=a*act[2]*V
    ask=r.choice(['res','w'])
    head="%s va %s aralashmasi (%s g) mo'l xlorid kislota bilan ta'sirlashganda %s l (n.sh.) gaz ajraldi. "%(act[0],inert[0],_f(m),_f(h2))
    sol="%s xlorid kislotada erimaydi; H2 faqat %s dan: x = %s/(22,4·%s) = %s mol → m(%s) = %s g; "%(inert[0],act[0],_f(h2),_f(act[2]),_f(a),act[0],_f(a*act[1]))
    src="9-sinf (metallarning kuchlanish qatori)"
    if ask=='res': return numq(head+"Erimay qolgan qoldiq massasini (g) aniqlang.",b*inert[1],[a*act[1],m/2,b*inert[1]*2,m-b*inert[1]*0.5],sol+"qoldiq = %s g"%_f(b*inert[1]),src,1)
    ans=a*act[1]/m*100
    return numq(head+"Aralashmadagi %s ning massa ulushini (%%) toping."%act[0],ans,[100-ans,50,a/(a+b)*100,ans/2],sol+"ω = %s %%"%_f(ans,1),src,1)

# 3) Nitratlarning termik parchalanishi: massa kamayishi
NIT=[('Cu(NO3)2',187.5,108,'CuO',79.5,'NO2 va O2'),('Zn(NO3)2',189,108,'ZnO',81,'NO2 va O2'),('Pb(NO3)2',331,108,'PbO',223,'NO2 va O2'),('AgNO3',170,62,'Ag',108,'NO2 va O2'),('KNO3',101,16,'KNO2',85,'O2'),('NaNO3',85,16,'NaNO2',69,'O2')]
def c_nitrate_loss(r):
    f,M0,dm,prod,Mp,gas=r.choice(NIT); n=r.choice([0.1,0.2,0.25,0.4,0.5]); loss=n*dm
    ask=r.choice(['salt','solid'])
    head="%s qizdirilganda qattiq qoldiq massasi dastlabki massadan %s g ga kamaydi. "%(f,_f(loss))
    sol="%s → %s + %s: 1 mol tuzda massa %s g ga kamayadi; n(tuz) = %s/%s = %s mol; "%(f,prod,gas,_f(dm,1),_f(loss),_f(dm,1),_f(n))
    src="9-sinf (nitratlarning termik parchalanishi)"
    if ask=='salt': return numq(head+"Parchalangan tuz massasini (g) toping.",n*M0,[loss,n*M0*2,n*M0/2,n*Mp],sol+"m = %s g"%_f(n*M0),src,1)
    return numq(head+"Hosil bo'lgan %s massasini (g) aniqlang."%prod,n*Mp,[n*M0,loss,n*Mp*2,n*Mp/2],sol+"m(%s) = %s g"%(prod,_f(n*Mp)),src,1)

# 4) H2S va SO2 (cheklovchi modda)
def c_h2s_so2(r):
    a=r.choice([0.2,0.3,0.4,0.5,0.6]); b=r.choice([0.1,0.2,0.3]); ask=r.choice(['S','rest'])
    if abs(a/2-b)<1e-9: b=b+0.1
    nS=min(a/2,b)*3
    left_H2S=max(a-2*b,0); left_SO2=max(b-a/2,0)
    head="%s l (n.sh.) H2S va %s l (n.sh.) SO2 aralashtirilib, reaksiya oxirigacha olib borildi. "%(_f(a*V),_f(b*V))
    sol="2H2S + SO2 → 3S + 2H2O: H2S %s mol, SO2 %s mol → %s yetishmaydi; S: %s mol; "%(_f(a),_f(b),"H2S" if a/2<b else "SO2",_f(nS))
    src="9-sinf (oltingugurt birikmalari; cheklovchi modda)"
    if ask=='S': return numq(head+"Hosil bo'lgan oltingugurt massasini (g) hisoblang.",nS*32,[a*32,b*32*3,nS*32*2,nS*16],sol+"m(S) = %s g"%_f(nS*32),src,1)
    rest=(left_H2S if left_H2S>0 else left_SO2)*V; gname='H2S' if left_H2S>0 else 'SO2'
    return numq(head+"Reaksiyadan so'ng ortib qolgan gaz hajmini (l, n.sh.) toping.",rest,[a*V,b*V,rest*2,(a+b)*V-rest],sol+"ortgan gaz: %s = %s l"%(gname,_f(rest)),src,2)

# 5) CO2 + NaOH (nisbatga qarab tuz turi)
def c_co2_naoh(r):
    a=r.choice([0.2,0.4,0.5]); ratio=r.choice([1.25,1.5,1.75]); b=a*ratio; reag=r.choice([('CO2','NaOH','Na2CO3','NaHCO3',106,84),('SO2','KOH','K2SO3','KHSO3',158,120)])
    ga,gb,ns,ac,Mn,Ma=reag
    x=b-a; y=a-x   # x mol o'rta tuz, y mol nordon tuz (2x+y=b, x+y=a)
    ask=r.choice(['tot','neutral'])
    head="%s mol %s %s mol %s eritmasidan o'tkazildi (reaksiya oxirigacha). "%(_f(a),ga,_f(b),gb)
    sol="n(%s)/n(%s) = %s: ham o'rta, ham nordon tuz hosil bo'ladi. x + y = %s; 2x + y = %s → o'rta tuz x = %s, nordon tuz y = %s; "%(gb,ga,_f(ratio),_f(a),_f(b),_f(x),_f(y))
    src="9-sinf (kislotali oksidlarning ishqor bilan reaksiyasi)"
    if ask=='tot': return numq(head+"Hosil bo'lgan tuzlar umumiy massasini (g) aniqlang.",x*Mn+y*Ma,[a*Mn,a*Ma,(x*Mn+y*Ma)*2,x*Mn],sol+"m = %s g"%_f(x*Mn+y*Ma),src,1)
    return numq(head+"Hosil bo'lgan o'rta tuz massasini (g) toping.",x*Mn,[y*Ma,a*Mn,x*Mn*2,x*Ma],sol+"m(%s) = %s g"%(ns,_f(x*Mn)),src,1)

# 6) H3PO4 + NaOH nisbatlari
def c_h3po4(r):
    a=r.choice([0.2,0.4]); ratio=r.choice([1.5,2.5]); b=a*ratio
    if ratio==1.5: s1,s2,M1,M2=('NaH2PO4','Na2HPO4',120,142)
    else: s1,s2,M1,M2=('Na2HPO4','Na3PO4',142,164)
    # s1 x mol, s2 y mol ; x+y=a ; (k)x+(k+1)y=b
    k=1 if ratio==1.5 else 2
    y=b-k*a; x=a-y
    ask=r.choice(['tot','s2'])
    head="%s mol fosfat kislota %s mol NaOH bilan ta'sirlashtirildi (reagentlar to'liq sarflandi). "%(_f(a),_f(b))
    sol="n(NaOH)/n(H3PO4) = %s: %s (x) va %s (y) aralashmasi. x + y = %s; %dx + %dy = %s → x = %s, y = %s; "%(_f(ratio),s1,s2,_f(a),k,k+1,_f(b),_f(x),_f(y))
    src="9-sinf (ko'p negizli kislotalar, nordon tuzlar)"
    if ask=='tot': return numq(head+"Hosil bo'lgan tuzlar massasini (g) hisoblang.",x*M1+y*M2,[a*M1,a*M2,(x*M1+y*M2)*2,y*M2],sol+"m = %s g"%_f(x*M1+y*M2),src,1)
    return numq(head+"Hosil bo'lgan %s massasini (g) aniqlang."%s2,y*M2,[x*M1,a*M2,y*M2*2,y*M1],sol+"m(%s) = %s g"%(s2,_f(y*M2)),src,1)

# 7) Plastinka massasining o'zgarishi
PLT=[('Fe','CuSO4','Cu',56,64,1,'mis'),('Zn','CuSO4','Cu',65,64,1,'mis'),('Fe','AgNO3','Ag',56,108,2,'kumush'),('Cu','AgNO3','Ag',64,108,2,'kumush'),('Zn','Pb(NO3)2','Pb',65,207,1,'qo\'rg\'oshin'),('Mg','CuSO4','Cu',24,64,1,'mis')]
def c_plate(r):
    A,salt,B,MA,MB,k,bn=r.choice(PLT); n=r.choice([0.05,0.1,0.2,0.25]); dm=n*(k*MB-MA)
    sign='ortdi' if dm>0 else 'kamaydi'
    ask=r.choice(['dep','salt'])
    head="%s plastinka %s eritmasiga tushirildi. Reaksiya tugagach, plastinka massasi %s g ga %s. "%(A,salt,_f(abs(dm)),sign)
    sol="%s + %s → ...: 1 mol %s erishida %d g %s ajraladi, plastinka massasi 1 mol uchun %s g ga o'zgaradi; n = %s mol; "%(A,salt,A,k*MB,B,_f(k*MB-MA,1),_f(n))
    src="9-sinf (metallarning kuchlanish qatori; plastinka massasi o'zgarishi)"
    if ask=='dep': return numq(head+"Plastinkada ajralgan %s massasini (g) hisoblang."%bn,n*k*MB,[n*MB,abs(dm),n*k*MB*2,n*MA],sol+"m(%s) = %s g"%(B,_f(n*k*MB)),src,1)
    return numq(head+"Erigan %s plastinka massasini (g) aniqlang."%A,n*MA,[n*k*MB,abs(dm),n*MA*2,n*MA/2],sol+"m(%s) = %s g"%(A,_f(n*MA)),src,1)

# 8) Temir oksidlari aralashmasi CO bilan qaytarilishi
def c_fe_oxides(r):
    a,b=_pick2(r,[0.05,0.1,0.15,0.2]); m=160*a+232*b; co2=(3*a+4*b)*V; ask=r.choice(['Fe','o3'])
    head="Fe2O3 va Fe3O4 aralashmasi (%s g) CO bilan to'liq qaytarilganda %s l (n.sh.) CO2 hosil bo'ldi. "%(_f(m),_f(co2))
    sol="Fe2O3 + 3CO → 2Fe + 3CO2; Fe3O4 + 4CO → 3Fe + 4CO2. 160x + 232y = %s; 3x + 4y = %s → x = %s, y = %s; "%(_f(m),_f(co2/V),_f(a),_f(b))
    src="9-sinf (temir va uning oksidlari)"
    if ask=='Fe':
        ans=(2*a+3*b)*56
        return numq(head+"Hosil bo'lgan temir massasini (g) hisoblang.",ans,[a*2*56,b*3*56,ans*2,m*0.7],sol+"m(Fe) = (2x + 3y)·56 = %s g"%_f(ans),src,1)
    ans=160*a/m*100
    return numq(head+"Aralashmadagi Fe2O3 ning massa ulushini (%) toping.",ans,[100-ans,a/(a+b)*100,50,ans/2],sol+"ω = %s %%"%_f(ans,1),src,1)

# 9) NaBr + NaI aralashmasiga Cl2 ta'siri (massa o'zgarishi)
def c_halide_mix(r):
    a,b=_pick2(r,[0.1,0.2,0.3,0.4]); m=103*a+150*b; mf=58.5*(a+b)
    ask=r.choice(['NaI','Cl2'])
    head="NaBr va NaI aralashmasi (%s g) eritmasidan mo'l xlor o'tkazilib, eritma quritildi. Quruq qoldiq massasi %s g bo'ldi. "%(_f(m),_f(mf))
    sol="Qoldiq – faqat NaCl: n(NaCl) = %s/58,5 = %s mol = x + y; 103x + 150y = %s → x = %s, y = %s; "%(_f(mf),_f(a+b),_f(m),_f(a),_f(b))
    src="9-sinf (galogenlar; siqib chiqarish reaksiyalari)"
    if ask=='NaI': return numq(head+"Aralashmadagi NaI massasini (g) aniqlang.",150*b,[103*a,150*b*2,m/2,150*b/2],sol+"m(NaI) = %s g"%_f(150*b),src,1)
    ans=(a/2+b/2)*V
    return numq(head+"Sarflangan xlor hajmini (l, n.sh.) hisoblang.",ans,[(a+b)*V,a*V,ans*2,b*V],sol+"n(Cl2) = (x + y)/2 = %s mol → %s l"%(_f((a+b)/2),_f(ans)),src,2)

# 10) Karbonatlar aralashmasi + kislota
CARB=[('CaCO3',100),('MgCO3',84),('BaCO3',197),('Na2CO3',106)]
def c_carbonates(r):
    (n1,M1),(n2,M2)=r.sample(CARB,2); a,b=_pick2(r,[0.1,0.2,0.3,0.4]); m=a*M1+b*M2; co2=(a+b)*V
    ask=r.choice(['m1','HCl'])
    head="%s va %s aralashmasi (%s g) mo'l xlorid kislota bilan ta'sirlashganda %s l (n.sh.) gaz ajraldi. "%(n1,n2,_f(m),_f(co2))
    sol="Har biri 1 mol CO2 beradi: x + y = %s; %d x + %d y = %s → x = %s, y = %s; "%(_f(a+b),M1,M2,_f(m),_f(a),_f(b))
    src="8-9-sinf (karbonatlar; kislotalar bilan reaksiya)"
    if ask=='m1': return numq(head+"Aralashmadagi %s massasini (g) toping."%n1,a*M1,[b*M2,a*M1*2,m/2,a*M1/2],sol+"m = %s g"%_f(a*M1),src,1)
    ans=2*(a+b)*36.5
    return numq(head+"Sarflangan HCl massasini (g) hisoblang.",ans,[(a+b)*36.5,ans*2,a*73,b*73],sol+"n(HCl) = 2(x + y) = %s mol → %s g"%(_f(2*(a+b)),_f(ans)),src,1)

# 11) Cu + konsentrlangan H2SO4 (cheklovchi modda)
def c_cu_h2so4(r):
    nCu=r.choice([0.2,0.3,0.4,0.5]); nA=r.choice([0.2,0.4,0.6,1.0])
    if abs(nA-2*nCu)<1e-9: nA+=0.2
    nSO2=min(nCu,nA/2); lim='Cu' if nCu<nA/2 else 'H2SO4'
    t="%s g mis %s mol konsentrlangan sulfat kislota bilan qizdirildi. Ajralgan gaz hajmini (l, n.sh.) hisoblang."%(_f(nCu*64,1),_f(nA))
    return numq(t,nSO2*V,[nCu*V,nA*V,nA/2*V if lim=='Cu' else nCu*V*2,nSO2*V*2],"Cu + 2H2SO4(kons.) → CuSO4 + SO2↑ + 2H2O: Cu %s mol, kislota %s mol; %s yetishmaydi → SO2 %s mol = %s l"%(_f(nCu),_f(nA),lim,_f(nSO2),_f(nSO2*V)),"9-sinf (sulfat kislotaning xossalari; cheklovchi modda)",2)

# 12) Ammiakdan nitrat kislota (ketma-ket unum)
def c_hno3_chain(r):
    n=r.choice([2,4,5,10]); e=r.choice([[0.9,0.8],[0.8,0.75],[0.9,0.6],[0.75,0.8]]); m=n*17
    tgt=r.choice(['hno3','nh4no3'])
    pr=n*e[0]*e[1]
    if tgt=='hno3':
        return numq("%s g ammiak katalitik oksidlanib NO ga (unum %s %%), so'ng NO2 va HNO3 gacha (umumiy unum %s %%) aylantirildi. Hosil bo'lgan nitrat kislota massasini (g) hisoblang."%(_f(m,0),_f(e[0]*100,0),_f(e[1]*100,0)),pr*63,[n*63,pr*63*2,n*e[0]*63,pr*17],"n(NH3) = %s mol; NH3 → HNO3 (1:1): %s·%s·%s = %s mol; m = %s g"%(_f(n),_f(n),_f(e[0]),_f(e[1]),_f(pr),_f(pr*63,1)),"9-sinf (azotning birikmalari; ammiak va HNO3 olinishi)",1)
    return numq("%s g ammiakning %s %% i HNO3 ga aylantirildi, qolgan ammiak shu kislota bilan neytrallandi. Hosil bo'lgan NH4NO3 massasini (g) toping."%(_f(m,0),_f(e[0]*100,0)),min(n*(1-e[0]),n*e[0])*80,[n*80*e[0],n*80*(1-e[0]),n*80,n*80*0.5],"HNO3: %s mol; NH3 qoldi: %s mol; NH3 + HNO3 → NH4NO3: tuz = min = %s mol → %s g"%(_f(n*e[0]),_f(n*(1-e[0])),_f(min(n*(1-e[0]),n*e[0])),_f(min(n*(1-e[0]),n*e[0])*80)),"9-sinf (ammiak va HNO3, ammoniy nitrat)",1)

# 13) Al2(SO4)3 va Na2CO3 (qo'shma gidroliz)
def c_joint_hydrolysis(r):
    salt=r.choice([('Al2(SO4)3',342,'Na2CO3',3,'CO2',V),('Al2(SO4)3',342,'Na2S',3,'H2S',V),('AlCl3',133.5,'Na2CO3',1.5,'CO2',V)])
    s,Ms,reag,k,gas,Vg=salt; n=r.choice([0.1,0.2,0.4]); m=n*Ms
    ask=r.choice(['gas','ppt'])
    nAl=n*(2 if s=='Al2(SO4)3' else 1)
    head="%s g %s eritmasiga mo'l %s eritmasi qo'shildi (qo'shma gidroliz). "%(_f(m,1),s,reag)
    sol="2Al³⁺ + 3%s²⁻ + 6H2O → 2Al(OH)3↓ + 3%s↑: n(Al³⁺) = %s mol; "%("CO3" if "CO3" in reag else "S","CO2" if gas=='CO2' else "H2S",_f(nAl))
    src="9-sinf; 10-sinf (tuzlar gidrolizi, qo'shma gidroliz)"
    if ask=='gas': return numq(head+"Ajralgan gaz hajmini (l, n.sh.) hisoblang.",1.5*nAl*V,[nAl*V,3*nAl*V,1.5*nAl*V*2,n*V],sol+"V(%s) = 1,5·%s·22,4 = %s l"%(gas,_f(nAl),_f(1.5*nAl*V)),src,2)
    return numq(head+"Hosil bo'lgan cho'kma massasini (g) toping.",nAl*78,[n*78,nAl*78*2,nAl*78/2,m],sol+"m(Al(OH)3) = %s·78 = %s g"%(_f(nAl),_f(nAl*78)),src,1)

# 14) Suvni yumshatish: Ca(HCO3)2
def c_hardness(r):
    c=r.choice([0.162,0.324,0.486,0.81]); Vw=r.choice([100,200,500,1000]); n=c*Vw/162; reag=r.choice([('Ca(OH)2',74,1),('Na2CO3',106,1)])
    nm,Mr,k=reag
    t="1 litr suvda %s g Ca(HCO3)2 bor. %s l shu suvni to'liq yumshatish uchun zarur %s massasini (g) hisoblang."%(_f(c,3),_f(Vw,0),nm)
    return numq(t,n*Mr,[n*Mr*2,n*Mr/2,n*162,c*Vw],"n(Ca(HCO3)2) = %s·%s/162 = %s mol; %s bilan 1:1 → m = %s g"%(_f(c,3),_f(Vw,0),_f(n),nm,_f(n*Mr)),"9-sinf (suvning qattiqligi va uni yumshatish)",2)

HARD_INORG={'S/SO2/H2SO4':[c_h2s_so2,c_cu_h2so4],'N/NH3/HNO3':[c_hno3_chain,c_nitrate_loss],'P/C/Si':[c_h3po4,c_co2_naoh],'galogenlar':[c_halide_mix],'IA metallar':[c_co2_naoh,c_nitrate_loss],
 'IIA/IIIA metallar (Ca,Mg,Al)':[c_metal_mix,c_joint_hydrolysis,c_carbonates],'d-metallar (Fe,Cu,Zn,Cr)':[c_plate,c_fe_oxides,c_metal_inert],'suv qattiqligi':[c_hardness,c_carbonates],
 'oksid/asos/kislota/tuz':[c_metal_inert,c_carbonates],'genetik zanjir/reaksiya turlari':[c_plate,c_metal_mix],"mineral o'g'itlar/nodir gazlar":[c_hno3_chain],'tuzlarning termik parchalanishi':[c_nitrate_loss]}
