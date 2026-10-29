import random, math
from core import *
# 1-19 uchun Tongotarov/Samarqand darajasidagi (2-3 bosqichli, fikrlashni talab qiladigan) masalalar. Mazmun asl.
V=22.4; F=96500; R=8.314
def _f(x,nd=2): return fmt(x,nd)
def _o(x): return x  # yordamchi

# ================= UMUMIY KIMYO =================
OXIDES={'Fe':(56,[('FeO',1,1),('Fe2O3',2,3),('Fe3O4',3,4)]),'Cu':(64,[('CuO',1,1),('Cu2O',2,1)]),'Mn':(55,[('MnO',1,1),('Mn2O3',2,3),('MnO2',1,2),('Mn2O7',2,7)]),'Cr':(52,[('CrO',1,1),('Cr2O3',2,3),('CrO3',1,3)]),'Pb':(207,[('PbO',1,1),('PbO2',1,2),('Pb3O4',3,4)])}
def u_oxide_formula(r):
    me=r.choice(list(OXIDES)); Ar,ox=OXIDES[me]; f,x,y=r.choice(ox)
    w=16*y/(Ar*x+16*y)*100
    ws=[o[0] for o in ox if o[0]!=f]
    for extra in (me+'2O',me+'O2',me+'2O5',me+'O3'):
        if len(ws)>=3: break
        if extra!=f and extra not in ws and extra not in [o[0] for o in ox]: ws.append(extra)
    return Q("%s (Ar = %d) ning oksidida kislorodning massa ulushi %s %% ga teng. Oksidning formulasini aniqlang."%(me,Ar,_f(w,1)),f,ws[:3],"x : y = (100 − ω(O))/Ar : ω(O)/16 = %s : %s → %s"%(_f((100-w)/Ar,3),_f(w/16,3),f),"8-sinf (oksidlar tarkibi; massa ulushi)",'calc')
def u_dilute_chain(r):
    m1=r.choice([100,200,300]); p1=r.choice([10,20,30]); s=r.choice([10,20,25,50]); w=r.choice([50,100,150])
    ans=(m1*p1/100+s)/(m1+s+w)*100
    t="%d g %d %% li NaCl eritmasiga %d g NaCl qo'shib eritildi, so'ngra eritma %d g suv bilan suyultirildi. Hosil bo'lgan eritmadagi tuzning massa ulushini (%%) aniqlang."%(m1,p1,s,w)
    return numq(t,ans,[(m1*p1/100)/(m1+w)*100,(m1*p1/100+s)/(m1+s)*100,(p1+s)/2,ans*2],"m(tuz) = %s + %d = %s g; m(eritma) = %d + %d + %d = %d g; ω = %s %%"%(_f(m1*p1/100,1),s,_f(m1*p1/100+s,1),m1,s,w,m1+s+w,_f(ans,2)),"8-9-sinf (eritmalar; ketma-ket jarayon)",2)
def u_alpha_particles(r):
    c=r.choice([0.1,0.2,0.5]); Vl=r.choice([1,2,5]); al=r.choice([0.01,0.02,0.05,0.1]); n=c*Vl
    ans=n*(1+al)
    t="%s mol/l li sirka kislota eritmasining %d l ida (dissotsilanish darajasi α = %s) suv molekulalaridan tashqari jami necha mol zarracha (molekula va ionlar) bor?"%(_f(c),Vl,_f(al,2))
    return numq(t,ans,[n,n*(1-al),n*(1+2*al),2*n],"n(CH3COOH) = %s mol; dissotsilangan %s mol → ionlar 2·%s; qolgan molekulalar %s; jami = %s mol"%(_f(n),_f(n*al,3),_f(n*al,3),_f(n*(1-al),3),_f(ans,3)),"9-sinf (elektrolitik dissotsilanish)",3)
SPI=[('C2H4',5,1),('C2H2',3,2),('C6H6',12,3),('HCN',2,2),('CO2',2,2),('C2H6',7,0),('CH3CHO',6,1),('HCHO',3,1),('C3H6',8,1),('C4H6 (butadiyen-1,3)',9,2)]
def u_sigma_pi(r):
    (a_,s1,p1),(b_,s2,p2)=r.sample(SPI,2); x=r.choice([1,2,3]); y=r.choice([1,2,3]); ask=r.choice(['pi','ratio'])
    P=x*p1+y*p2; S=x*s1+y*s2
    if ask=='pi': return numq("%d mol %s va %d mol %s aralashmasidagi π-bog'lar umumiy sonini (N_A birligida) aniqlang."%(x,a_,y,b_),P,[S,P+S,x*p1,y*p2],"%d·%d + %d·%d = %d (σ: %d)"%(x,p1,y,p2,P,S),"8-10-sinf (σ- va π-bog'lar)",0)
    ans=P/S
    return numq("%d mol %s va %d mol %s aralashmasida π-bog'lar sonining σ-bog'lar soniga nisbatini toping."%(x,a_,y,b_),ans,[S/P,P/(P+S),ans*2,ans/2],"π = %d, σ = %d → %s"%(P,S,_f(ans,3)),"8-10-sinf (σ- va π-bog'lar)",3)
ISO=[('B',10,11,0.2),('Cl',35,37,0.75),('Cu',63,65,0.75),('Br',79,81,0.5),('Li',6,7,0.1)]
def u_isotope_mass(r):
    el,a,b,x=r.choice(ISO); Ar=a*x+b*(1-x); m=r.choice([10,20,50]); heavy=b*(1-x)/Ar
    t="%s elementi ikki izotopdan iborat: ³%s%s va ³%s%s. Elementning o'rtacha nisbiy atom massasi %s bo'lsa, shu elementning %d g namunasidagi og'ir izotop massasini (g) aniqlang."%(el,'',el,'',el,_f(Ar,2),m) if False else "%s elementi ikki izotopdan iborat (massa sonlari %d va %d). O'rtacha nisbiy atom massasi %s bo'lsa, %d g namunadagi og'ir izotopning massasini (g) aniqlang."%(el,a,b,_f(Ar,2),m)
    return numq(t,m*heavy,[m*(1-x),m*x,m*(1-x)*b/a,m/2],"Og'ir izotop ulushi: %s·x + %s·(1−x) = %s → 1−x = %s; massa ulushi = %s·%s/%s = %s; m = %s g"%(a,b,_f(Ar,2),_f(1-x,2),b,_f(1-x,2),_f(Ar,2),_f(heavy,3),_f(m*heavy,2)),"8-sinf (izotoplar; o'rtacha atom massa)",2)
DEC=[(238,92,8,6),(235,92,7,4),(232,90,6,4),(226,88,4,2)]
def u_decay(r):
    A,Z,al,be=r.choice(DEC); m=r.choice([0.238,2.38,23.8]) if A==238 else r.choice([A/1000,A/100])
    A2=A-4*al; Z2=Z-2*al+be; n2=A2-Z2; ask=r.choice(['n','alpha'])
    nn=m/A
    if ask=='n':
        return numq("%d_%d yadro ketma-ket %d ta α- va %d ta β⁻-yemirilishga uchradi. Hosil bo'lgan barqaror yadrodagi neytronlar sonini toping."%(A,Z,al,be),n2,[n2+4,n2-2,Z2,A2],"A' = %d − 4·%d = %d; Z' = %d − 2·%d + %d = %d; N = %d − %d = %d"%(A,al,A2,Z,al,be,Z2,A2,Z2,n2),"9-sinf; 11-sinf (radioaktiv yemirilish)",0)
    return numq("%s g massali %d-massa sonli izotop (Z = %d) %d ta α- va %d ta β⁻-yemirilishga uchradi (M ≈ %d g/mol). Chiqarilgan α-zarralar sonini N_A birligida aniqlang."%(_f(m,3),A,Z,al,be,A),nn*al,[nn*be,nn*(al+be),nn,nn*al*2],"n(yadro) = %s/%d = %s mol; α-zarralar = %d·%s = %s mol"%(_f(m,3),A,_f(nn,4),al,_f(nn,4),_f(nn*al,4)),"9-sinf; 11-sinf (radioaktiv yemirilish)",3)
def u_equilibrium(r):
    a,b,x=r.choice([(4,2,0.5),(4,2,0.75),(6,3,0.5),(2,1,0.5),(4,2,0.25)]); Vv=r.choice([1,2])
    so3=a*x; so2=a-so3; o2=b-a*x/2; K=(so3/Vv)**2/((so2/Vv)**2*(o2/Vv))
    ask=r.choice(['K','p'])
    t="%d l hajmli idishga %d mol SO2 va %d mol O2 solindi. 2SO2 + O2 ⇌ 2SO3 muvozanati qaror topganda SO2 ning %s %% i sarflangan bo'ldi. "%(Vv,a,b,_f(x*100,0))
    if ask=='K': return numq(t+"Muvozanat konstantasini (K) hisoblang.",K,[K/2,K*2,so3/(so2*o2),K/Vv],"SO3 = %s, SO2 = %s, O2 = %s mol; [SO3]² / ([SO2]²·[O2]) = %s"%(_f(so3),_f(so2),_f(o2),_f(K,3)),"9-sinf; 11-sinf (kimyoviy muvozanat)",3)
    p=(so3+so2+o2)/(a+b)
    return numq(t+"Muvozanatdagi umumiy bosimning boshlang'ich bosimga nisbatini (T = const) toping.",p,[1/p,p*2,so3/(a+b),1-p],"n(jami) = %s + %s + %s = %s mol; boshlang'ich %d mol → %s"%(_f(so3),_f(so2),_f(o2),_f(so3+so2+o2),a+b,_f(p,3)),"9-sinf; 11-sinf (kimyoviy muvozanat)",3)
def u_rate_comb(r):
    for _ in range(50):
        g=r.choice([2,3]); dT=r.choice([20,30,40]); f=r.choice([2,3]); inc=r.choice(['V','c'])
        if inc=='V' or g**(dT//10)!=f*f: break
    n_temp=dT//10
    if inc=='V':
        t="2NO + O2 → 2NO2 reaksiyasi (v = k·[NO]²·[O2]) harorati %d °C ga oshirilib (γ = %d), idish hajmi %d marta kamaytirildi. Reaksiya tezligi necha marta ortadi?"%(dT,g,f)
        ans=g**n_temp*f**3
        sol="Harorat: γ^(%d/10) = %d; hajm %d marta kamaysa, hamma konsentratsiya %d marta ortadi: %d³ = %d; jami %d·%d = %d"%(dT,g**n_temp,f,f,f,f**3,g**n_temp,f**3,ans)
    else:
        t="2NO + O2 → 2NO2 reaksiyasida (v = k·[NO]²·[O2]) harorat %d °C ga oshirildi (γ = %d), shu bilan birga NO konsentratsiyasi %d marta kamaytirildi. Reaksiya tezligi qanday o'zgaradi (necha marta ortadi/kamayadi)? Tezlikning yangi/eski nisbatini toping."%(dT,g,f)
        ans=g**n_temp/f**2
        sol="Harorat: %d marta ortadi; [NO] %d marta kamayishi tezlikni %d² = %d marta kamaytiradi: %d/%d = %s"%(g**n_temp,f,f,f*f,g**n_temp,f*f,_f(ans,3))
    return numq(t,ans,[ans*2,ans/2,g**n_temp,f**3 if inc=='V' else f*f],sol,"9-sinf; 11-sinf (reaksiya tezligi; Vant-Goff, massalar ta'siri)",3)
def u_titration(r):
    kind=r.choice(['fe','ox'])
    if kind=='fe':
        m=r.choice([2.78,5.56,13.9]); c=r.choice([0.1,0.05,0.02]); n=m/278; v=n/5/c*1000
        return numq("%s g FeSO4·7H2O ni kislotali muhitda oksidlash uchun %s mol/l li KMnO4 eritmasidan necha ml kerak?"%(_f(m,2),_f(c,2)),v,[v*5,v/5,v*2,v/2],"10FeSO4 + 2KMnO4 + 8H2SO4 → 5Fe2(SO4)3 + K2SO4 + 2MnSO4 + 8H2O: n(Fe²⁺) = %s mol → n(KMnO4) = %s mol → V = %s ml"%(_f(n,4),_f(n/5,5),_f(v,1)),"9-sinf; 11-sinf (OQR; titrlash)",3)
    m=r.choice([12.6,25.2,6.3]); n=m/126; co2=n*2*V
    return numq("%s g H2C2O4·2H2O kislotali muhitda mo'l KMnO4 bilan oksidlandi (5H2C2O4 + 2KMnO4 + 3H2SO4 → 10CO2 + 2MnSO4 + K2SO4 + 8H2O). Ajralgan CO2 hajmini (l, n.sh.) hisoblang."%_f(m,1),co2,[co2/2,n*V,co2*2,m/90*2*V],"n(H2C2O4·2H2O) = %s/126 = %s mol; CO2 = 2·%s = %s mol → %s l"%(_f(m,1),_f(n,3),_f(n,3),_f(2*n,3),_f(co2,2)),"9-sinf; 11-sinf (OQR)",2)
def u_koh_electrolysis(r):
    m,p1,p2=r.choice([(240,10,16),(200,10,12.5),(300,5,6),(160,15,20)]); x=m*(1-p1/p2); n=x/18; vol=1.5*n*V
    return numq("%d g %s %% li KOH eritmasi inert elektrodlar bilan elektroliz qilinib, ishqorning massa ulushi %s %% ga yetdi. Elektrolizda ajralgan gazlarning umumiy hajmini (l, n.sh.) hisoblang."%(m,_f(p1,0),_f(p2,1)),vol,[n*V,vol*2,vol/2,x],"KOH massasi o'zgarmaydi: %d·%s = (%d − x)·%s → x = %s g H2O parchalangan; n(H2O) = %s mol; H2 = %s, O2 = %s → %s l"%(m,_f(p1/100,3),m,_f(p2/100,4),_f(x,1),_f(n,3),_f(n,3),_f(n/2,3),_f(vol,2)),"11-sinf (elektroliz; suvning elektrolizi)",1)
def u_gas_law(r):
    n1,n2=r.choice([(0.1,0.3),(0.2,0.2),(0.3,0.1),(0.2,0.4)]); T=300; P=83.14; vm=R*T/P
    n=n1+n2; Vg=n*vm; m=16*n1+44*n2
    t="27 °C va 83,14 kPa da hajmi %s l bo'lgan CH4 va CO2 aralashmasining massasi %s g. Aralashmadagi CO2 ning hajmiy ulushini (%%) hisoblang (R = 8,314 J/(mol·K))."%(_f(Vg,1),_f(m,1))
    ans=n2/n*100
    return numq(t,ans,[n1/n*100,44*n2/m*100,50,ans/2],"n = PV/RT = %s mol; 16x + 44y = %s; x + y = %s → y = %s; φ = %s %%"%(_f(n,3),_f(m,1),_f(n,3),_f(n2,3),_f(ans,1)),"8-10-sinf (gaz qonunlari)",3)
def u_equiv_chain(r):
    me=r.choice([('Mg',12),('Al',9),('Zn',32.5),('Fe',28)]); m=r.choice([2.4,5.4,6.5,5.6,12]); E=me[1]
    if abs(m/E-round(m/E,3))>0.01: m=E*r.choice([0.2,0.4,0.5])
    mo=m/E*8
    t="Metallning %s g massasi oksidlanganda %s g oksid hosil bo'ldi. Shu metallning %s g miqdori kislotadan qancha hajm (l, n.sh.) vodorodni siqib chiqaradi? (Ekvivalent hajm V_E(H2) = 11,2 l/mol)"%(_f(m,2),_f(m+mo,2),_f(m*2,2))
    ans=2*m/E*11.2
    return numq(t,ans,[m/E*11.2,ans*2,ans/2,2*m/E*22.4],"m(O) = %s − %s = %s g; E(M) = m(M)/(m(O)/8) = %s g/mol; V(H2) = (2·%s/%s)·11,2 = %s l"%(_f(m+mo,2),_f(m,2),_f(mo,2),_f(E,1),_f(m,2),_f(E,1),_f(ans,2)),"8-sinf (ekvivalentlar qonuni)",3)
def u_ph_mix(r):
    ratio,k=r.choice([(0.1,3),(0.01,4)]); Vt=r.choice([200,400]); acid_ex=r.choice([True,False]); c=0.01
    V1=Vt*(1+ratio)/2; V2=Vt-V1
    if acid_ex:
        t="pH = 2 bo'lgan HCl eritmasidan %s ml va pH = 12 bo'lgan NaOH eritmasidan %s ml aralashtirildi. Hosil bo'lgan eritmaning pH ini aniqlang."%(_f(V1,0),_f(V2,0)); ans=k
    else:
        t="pH = 2 bo'lgan HCl eritmasidan %s ml va pH = 12 bo'lgan NaOH eritmasidan %s ml aralashtirildi. Hosil bo'lgan eritmaning pH ini aniqlang."%(_f(V2,0),_f(V1,0)); ans=14-k
    return numq(t,ans,[ans+1,ans-1 if ans>1 else ans+2,7,14-ans],"c(HCl) = c(NaOH) = 0,01 mol/l; ortiqcha %s: (%s − %s)·0,01/%d = 10^−%d mol/l → pH = %d"%("kislota" if acid_ex else "ishqor",_f(max(V1,V2),0),_f(min(V1,V2),0),Vt,k,ans),"9-sinf; 11-sinf (pH; neytrallanish)",0)
HYD=[('NH4Cl',[("suyultirish",True),("qizdirish",True),("NaOH eritmasi qo'shish",True),("Na2CO3 eritmasi qo'shish",True),("HCl qo'shish",False),("qattiq NH4Cl qo'shib, konsentratsiyani oshirish",False),("sovitish",False)]),
     ('Na2CO3',[("suyultirish",True),("qizdirish",True),("NH4Cl eritmasi qo'shish",True),("HCl qo'shish",True),("NaOH eritmasi qo'shish",False),("qattiq Na2CO3 qo'shib, konsentratsiyani oshirish",False),("sovitish",False)])]
def t_hydr_shift(r):
    salt,lst=r.choice(HYD)
    for _ in range(50):
        it=r.sample(lst,4); fl=[t for _,t in it]
        if any(fl) and not all(fl): break
    nums=[i+1 for i,t in enumerate(fl) if t]; ans=', '.join(map(str,nums))
    from an import COMB
    ws=[c for c in COMB if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("%s eritmasida gidrolizlanish darajasini oshirish uchun qaysi usullar qo'llanadi? %s"%(salt,'; '.join('%d) %s'%(i+1,x) for i,(x,_) in enumerate(it))),ans,ws[:3],'; '.join('%s – %s'%(x,"oshiradi" if t else "oshirmaydi") for x,t in it),"9-sinf; 11-sinf (tuzlar gidrolizi; Le-Shatelye)",'theory')

# ================= ANORGANIK =================
def i_nitrate_mix(r):
    a,b=r.choice([(0.1,0.2),(0.2,0.1),(0.2,0.2),(0.1,0.3)]); m=187.5*a+101*b; dm=108*a+16*b
    ask=r.choice(['cu','solid'])
    head="Cu(NO3)2 va KNO3 dan iborat %s g aralashma doimiy massagacha qizdirilganda massasi %s g ga kamaydi. "%(_f(m,2),_f(dm,2))
    sol="Cu(NO3)2 → CuO (Δm 108 g/mol), KNO3 → KNO2 (Δm 16 g/mol): 187,5x + 101y = %s; 108x + 16y = %s → x = %s, y = %s; "%(_f(m,2),_f(dm,2),_f(a),_f(b))
    if ask=='cu': return numq(head+"Aralashmadagi Cu(NO3)2 ning massa ulushini (%) toping.",187.5*a/m*100,[100-187.5*a/m*100,a/(a+b)*100,50,101*b/m*100*0.5],sol+"ω = %s %%"%_f(187.5*a/m*100,1),"9-sinf (nitratlarning parchalanishi)",1)
    s=m-dm
    return numq(head+"Qattiq qoldiq massasini (g) aniqlang.",s,[dm,m,s*2,a*80+b*101],sol+"qoldiq = %s − %s = %s g"%(_f(m,2),_f(dm,2),_f(s,2)),"9-sinf (nitratlarning parchalanishi)",2)
def i_mg_air(r):
    u,w=r.choice([(0.14,0.02),(0.1,0.0333333),(0.17,0.01),(0.2,0.02)]); w=round(w,3)
    nMg=u+3*w; mp=40*u+100*w
    t="%s g magniy havoda yondirilganda %s g qattiq mahsulot hosil bo'ldi. Shu mahsulot mo'l suv bilan ishlanganda ajralgan ammiakning hajmini (l, n.sh.) hisoblang."%(_f(nMg*24,2),_f(mp,2))
    ans=2*w*V
    return numq(t,ans,[w*V,3*w*V,ans*2,u*V],"Mg: u mol MgO + w mol Mg3N2: u + 3w = %s; 40u + 100w = %s → w = %s mol; Mg3N2 + 6H2O → 3Mg(OH)2 + 2NH3↑: n(NH3) = %s mol → %s l"%(_f(nMg,3),_f(mp,2),_f(w,3),_f(2*w,3),_f(ans,2)),"9-sinf (magniyning yonishi; nitridlar)",3)
def i_si_sio2(r):
    a,b=r.choice([(0.1,0.2),(0.2,0.1),(0.1,0.1),(0.2,0.3)]); m=28*a+60*b; h2=2*a*V
    ask=r.choice(['w','naoh'])
    head="Si va SiO2 dan iborat %s g aralashma mo'l NaOH eritmasi bilan qizdirilganda %s l (n.sh.) vodorod ajraldi. "%(_f(m,1),_f(h2,2))
    sol="Faqat Si vodorod beradi: Si + 2NaOH + H2O → Na2SiO3 + 2H2: n(Si) = %s/(2·22,4) = %s mol; m(SiO2) = %s − %s = %s g; "%(_f(h2,2),_f(a),_f(m,1),_f(28*a,1),_f(60*b,1))
    if ask=='w': return numq(head+"Aralashmadagi SiO2 ning massa ulushini (%) toping.",60*b/m*100,[100-60*b/m*100,b/(a+b)*100,50,28*a/m*100*0.5],sol+"ω = %s %%"%_f(60*b/m*100,1),"9-sinf (kremniy va uning oksidi)",1)
    return numq(head+"Aralashmani to'liq eritish uchun sarflangan NaOH massasini (g) hisoblang.",(2*a+2*b)*40,[a*2*40,b*2*40,(a+b)*40,(2*a+2*b)*40*2],sol+"NaOH: SiO2 + 2NaOH → Na2SiO3 + H2O; jami 2(%s + %s) = %s mol → %s g"%(_f(a),_f(b),_f(2*a+2*b),_f((2*a+2*b)*40,1)),"9-sinf (kremniy va uning oksidi)",2)
def i_no_o2(r):
    a=r.choice([20,30,40,60]); b=r.choice([20,30,40,60]);
    if b<a/2: b=a
    tot=a+b; after=tot-a/2
    t="NO va O2 dan iborat %d ml aralashma (hajmlar bir xil sharoitda) o'zaro ta'sirlashgandan so'ng hajmi %s ml bo'lib qoldi (NO to'liq reaksiyaga kirishdi, kislorod ortiqcha). Dastlabki aralashmadagi NO ning hajmiy ulushini (%%) aniqlang."%(tot,_f(after,1))
    ans=a/tot*100
    return numq(t,ans,[100-ans,a/after*100,50,(tot-after)/tot*100],"2NO + O2 → 2NO2: hajm kamayishi = NO hajmining yarmi: %d − %s = %s ml = a/2 → a = %s ml NO; φ = %s %%"%(tot,_f(after,1),_f(tot-after,1),_f(a,0),_f(ans,1)),"9-sinf (azot oksidlari; gaz hajmlari)",2)
def i_na_na2o(r):
    a,b=r.choice([(0.2,0.1),(0.1,0.1),(0.3,0.1),(0.2,0.2)]); Wt=r.choice([100,200,300]); m=23*a+62*b; h2=a/2*V
    mass=m+Wt-a; w=40*(a+2*b)/mass*100
    t="Na va Na2O dan iborat %s g aralashma %d g suvda eritilganda %s l (n.sh.) gaz ajraldi. Hosil bo'lgan eritmadagi NaOH ning massa ulushini (%%) aniqlang."%(_f(m,1),Wt,_f(h2,2))
    return numq(t,w,[(a+b)*40/mass*100,40*a/(m+Wt-a)*100,w*2,w/2],"H2 = %s mol → Na = %s mol; m(Na2O) = %s − %s = %s g; NaOH = %s + 2·%s = %s mol = %s g; eritma = %s + %d − %s = %s g → ω = %s %%"%(_f(h2/V,3),_f(a),_f(m,1),_f(23*a,1),_f(62*b,1),_f(a),_f(b),_f(a+2*b),_f(40*(a+2*b),1),_f(m,1),Wt,_f(a,1),_f(mass,1),_f(w,2)),"9-sinf (ishqoriy metallar va ularning oksidlari)",3)
def i_ammofos(r):
    x,y=r.choice([(1,1),(1,2),(2,1),(2,3)]); m=115*x+132*y
    ask=r.choice(['N','P2O5'])
    if ask=='N':
        ans=(14*x+28*y)/m*100
        return numq("Ammofos tarkibida NH4H2PO4 va (NH4)2HPO4 mol nisbati %d : %d. Shu o'g'itdagi azotning massa ulushini (%%) toping."%(x,y),ans,[14*(x+y)/m*100,28*(x+y)/m*100,ans*2,ans/2],"N: (14·%d + 28·%d) = %d; M = 115·%d + 132·%d = %d → %s %%"%(x,y,14*x+28*y,x,y,m,_f(ans,2)),"9-sinf (mineral o'g'itlar)",2)
    ans=71*(x+y)/2/m*100
    return numq("Ammofos tarkibida NH4H2PO4 va (NH4)2HPO4 mol nisbati %d : %d. O'g'it tarkibidagi fosforning P2O5 hisobidagi massa ulushini (%%) aniqlang."%(x,y),ans,[31*(x+y)/m*100,71*(x+y)/m*100,ans*2,ans/2],"n(P) = %d mol → P2O5 = %s mol (142·%s = %s g); M(o'g'it) = %d g → %s %%"%(x+y,_f((x+y)/2,2),_f((x+y)/2,2),_f(71*(x+y),1),m,_f(ans,2)),"9-sinf (mineral o'g'itlar)",2)
def i_so2_equil(r):
    a,b,x=r.choice([(4,2,0.75),(4,2,0.5),(6,3,0.5),(2,1,0.5)]); so3=a*x; so2=a-so3; o2=b-a*x/2; n=so3+so2+o2; M=(a*64+b*32)/n
    ask=r.choice(['M','phi'])
    head="%d mol SO2 va %d mol O2 aralashmasi katalizator ustida qizdirilib, SO2 ning %s %% i SO3 ga aylantirildi. "%(a,b,_f(x*100,0))
    if ask=='M': return numq(head+"Hosil bo'lgan gazlar aralashmasining o'rtacha molyar massasini (g/mol) aniqlang.",M,[(a*64+b*32)/(a+b),M*2,M/2,80],"SO3 = %s, SO2 = %s, O2 = %s mol; n = %s; m = %s g → M = %s"%(_f(so3),_f(so2),_f(o2),_f(n),_f(a*64+b*32),_f(M,2)),"9-sinf (oltingugurt(IV) oksidining oksidlanishi)",2)
    return numq(head+"Aralashmadagi SO3 ning hajmiy ulushini (%) toping.",so3/n*100,[so3/(a+b)*100,so2/n*100,o2/n*100,x*100],"n(jami) = %s mol; φ(SO3) = %s/%s = %s %%"%(_f(n),_f(so3),_f(n),_f(so3/n*100,1)),"9-sinf (oltingugurt(IV) oksidining oksidlanishi)",2)
def i_pyrite_partial(r):
    x=r.choice([0.2,0.4,0.5,0.8]); m0=120*r.choice([1,2,5])
    n0=m0/120; reacted=n0*x; dm=40*reacted
    t="%s g pirit (FeS2) yondirilganda (4FeS2 + 11O2 → 2Fe2O3 + 8SO2) qattiq qoldiq massasi %s g ga kamaydi. Shu jarayonda ajralgan SO2 hajmini (l, n.sh.) hisoblang."%(_f(m0,0),_f(dm,1))
    ans=2*reacted*V
    return numq(t,ans,[reacted*V,ans*2,ans/2,n0*2*V],"4FeS2 (480 g) → 2Fe2O3 (320 g): 4 mol da massa 160 g ga kamayadi, 1 mol FeS2 da 40 g; n(FeS2) = %s/40 = %s mol → SO2 = 2·%s = %s mol → %s l"%(_f(dm,1),_f(reacted,3),_f(reacted,3),_f(2*reacted,3),_f(ans,2)),"9-sinf (oltingugurt birikmalari; pirit)",3)
def i_ca_cac2(r):
    a,b=r.choice([(0.1,0.1),(0.2,0.1),(0.1,0.2),(0.2,0.2)]); n=a+b; M=(2*a+26*b)/n; D=M/2; m=40*a+64*b
    t="Ca va CaC2 dan iborat aralashma suv bilan ta'sirlashganda %s l (n.sh.) gaz aralashmasi ajraldi, uning vodorodga nisbatan zichligi %s. Dastlabki aralashmaning massasini (g) hisoblang."%(_f(n*V,2),_f(D,2))
    return numq(t,m,[m*2,m/2,40*a+64*a,40*b+64*b],"Ca + 2H2O → Ca(OH)2 + H2; CaC2 + 2H2O → Ca(OH)2 + C2H2: x + y = %s; 2x + 26y = %s·%s = %s → x = %s, y = %s; m = 40x + 64y = %s g"%(_f(n,2),_f(D*2,2),_f(n,2),_f(2*a+26*b,2),_f(a),_f(b),_f(m,2)),"9-sinf; 10-sinf (kalsiy; karbidlar)",3)
def i_amph_mix(r):
    a,b=r.choice([(0.1,0.1),(0.1,0.2),(0.2,0.1),(0.2,0.2)]); m=102*a+160*b; res=160*b
    ask=r.choice(['w','hcl'])
    head="Al2O3 va Fe2O3 dan iborat %s g aralashma mo'l konsentrlangan NaOH eritmasi bilan qizdirilganda, erimay qolgan qoldiq massasi %s g bo'ldi. "%(_f(m,1),_f(res,1))
    sol="Al2O3 ishqorda eriydi (amfoter), Fe2O3 erimaydi: m(Fe2O3) = %s g (%s mol); m(Al2O3) = %s g (%s mol); "%(_f(res,1),_f(b),_f(102*a,1),_f(a))
    if ask=='w': return numq(head+"Aralashmadagi Al2O3 ning massa ulushini (%) toping.",102*a/m*100,[100-102*a/m*100,a/(a+b)*100,50,160*b/m*100*0.5],sol+"ω = %s %%"%_f(102*a/m*100,1),"9-sinf (amfoter oksidlar)",1)
    return numq(head+"Xuddi shunday aralashmani to'liq eritish uchun sarflanadigan HCl massasini (g) toping.",6*(a+b)*36.5,[6*a*36.5,6*b*36.5,3*(a+b)*36.5,12*(a+b)*36.5],sol+"HCl: Al2O3 + 6HCl, Fe2O3 + 6HCl → 6(%s + %s) = %s mol → %s g"%(_f(a),_f(b),_f(6*(a+b)),_f(6*(a+b)*36.5,1)),"9-sinf (amfoter oksidlar)",2)
def i_h2s_o2(r):
    a,b=r.choice([(4,4),(4,5),(6,6),(2,2),(6,7)]); s=(3*a-2*b)/2; t_=a-s
    if not (0<s<a): a,b,s=4,4,2; t_=2
    t="%d mol H2S %d mol kislorodda yondirildi (H2S to'liq sarflandi; oltingugurt va SO2 aralashmasi hosil bo'ldi). Hosil bo'lgan oltingugurtning massasini (g) hisoblang."%(a,b)
    return numq(t,32*s,[32*a,32*t_ if t_>0 else 16,32*s*2,64*s],"2H2S + O2 → 2S + 2H2O (s mol H2S); 2H2S + 3O2 → 2SO2 + 2H2O (t mol H2S): s + t = %d; s/2 + 3t/2 = %d → s = %s, t = %s; m(S) = %s g"%(a,b,_f(s,2),_f(t_,2),_f(32*s,2)),"9-sinf (vodorod sulfidning yonishi)",2)
def i_cl2_alkali(r):
    n=r.choice([0.6,1.2,2.4]); cold=n/2; hot=n/2
    kcl=cold+hot*5/3; kclo=cold; kclo3=hot/3
    ask=r.choice(['KCl','KOH'])
    head="%s mol xlorning yarmi sovuq, yarmi qaynoq KOH eritmasidan o'tkazildi (mo'l ishqor; sovuqda xlorid va gipoxlorit, qizdirilganda xlorid va xlorat hosil bo'ladi). "%_f(n)
    sol="Sovuq: Cl2 + 2KOH → KCl + KClO + H2O (%s mol Cl2); issiq: 3Cl2 + 6KOH → 5KCl + KClO3 + 3H2O (%s mol Cl2); "%(_f(cold),_f(hot))
    if ask=='KCl': return numq(head+"Hosil bo'lgan KCl ning umumiy massasini (g) hisoblang.",kcl*74.5,[n*74.5,kclo*74.5,kcl*74.5*2,(cold+hot*5)*74.5],sol+"n(KCl) = %s + %s·5/3 = %s mol → %s g"%(_f(cold),_f(hot),_f(kcl,3),_f(kcl*74.5,2)),"9-sinf (galogenlarning ishqor bilan reaksiyasi)",3)
    koh=2*cold+2*hot
    return numq(head+"Sarflangan KOH massasini (g) aniqlang.",koh*56,[n*56,koh*56*2,koh*56/2,hot*6*56],sol+"n(KOH) = 2·%s + 2·%s = %s mol → %s g"%(_f(cold),_f(hot),_f(koh),_f(koh*56,1)),"9-sinf (galogenlarning ishqor bilan reaksiyasi)",2)

HARD_UM14={"tushuncha/valentlik":[u_oxide_formula],'eritma %/M/eruvchanlik':[u_dilute_chain],'dissotsilanish/pH/gidroliz':[u_alpha_particles,u_ph_mix,t_hydr_shift],"bog'lanish/gibridlanish":[u_sigma_pi],'atom/davriy/izoelektron':[u_isotope_mass],'kvant/yadro':[u_decay],'muvozanat':[u_equilibrium],'tezlik':[u_rate_comb],'OQR':[u_titration],'elektroliz':[u_koh_electrolysis],'qonunlar/gaz/ekvivalent':[u_gas_law,u_equiv_chain]}
HARD_AN14={'tuzlarning termik parchalanishi':[i_nitrate_mix],'N/NH3/HNO3':[i_mg_air,i_no_o2],'P/C/Si':[i_si_sio2],'IA metallar':[i_na_na2o],"mineral o'g'itlar/nodir gazlar":[i_ammofos],'S/SO2/H2SO4':[i_so2_equil,i_pyrite_partial,i_h2s_o2],'IIA/IIIA metallar (Ca,Mg,Al)':[i_ca_cac2,i_amph_mix],'galogenlar':[i_cl2_alkali],'d-metallar (Fe,Cu,Zn,Cr)':[i_amph_mix],'oksid/asos/kislota/tuz':[i_amph_mix],'genetik zanjir/reaksiya turlari':[i_nitrate_mix],'suv qattiqligi':[]}
