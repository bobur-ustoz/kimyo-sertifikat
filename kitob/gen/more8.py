import random
from core import *
# Samarqand darajasidagi organik masalalar: ikki noma'lumli aralashmalar, "tuzoq" reaksiyalar (HCHO → 4Ag, HCOOH → 2Ag),
# unum + zichlik, ketma-ket jarayonlar. Hammasi 10-sinf darsligi doirasida.
V=22.4
def _f(x,nd=2): return fmt(x,nd)
def _pickmix(r,A,B,opts=(0.1,0.2,0.3,0.4,0.5)):
    for _ in range(40):
        a=r.choice(opts); b=r.choice(opts)
        if a!=b: return a,b
    return 0.2,0.1

# 1) Krekking/degidrogenlanish unumi va zichlik (vodorodga nisbatan)
DEC=[('etan','C2H6',30,'C2H6 → C2H4 + H2'),('propan','C3H8',44,'C3H8 → C3H6 + H2'),('butan','C4H10',58,'C4H10 → C2H6 + C2H4'),('izobutan','C4H10',58,'C4H10 → C3H6 + CH4')]
def c_decomp(r):
    for _ in range(200):
        nm,f,M0,eq=r.choice(DEC); eta=r.choice([0.2,0.25,0.4,0.5,0.6,0.75,0.8,1.0])
        D=M0/(2*(1+eta))
        if abs(D*10-round(D*10))<1e-9: break
    ask=r.choice(['eta','D'])
    if ask=='eta':
        ans=eta*100
        t="%s qizdirilib, quyidagi sxema bo'yicha parchalandi: %s. Hosil bo'lgan gazlar aralashmasining vodorodga nisbatan zichligi %s bo'lsa, %sning parchalanish unumini (%%) aniqlang."%(nm[0].upper()+nm[1:],eq,_f(D,1),nm.split()[0])
        return numq(t,ans,[ans/2,100-ans,ans*2 if ans*2<=100 else ans*0.8,(M0/(2*D)-1)*50],"1 mol %s olsak, reaksiyada %s mol hosil bo'ladi: n(jami) = 1 + η = %s mol; M(o'rt) = %d/(1+η) = %s → η = %s %%"%(f,_f(eta),_f(1+eta),M0,_f(2*D,1),_f(ans,0)),"10-sinf (alkanlarning krekingi va degidrogenlanishi)",0)
    t="%s %s %% unum bilan quyidagi sxema bo'yicha parchalandi: %s. Hosil bo'lgan gazlar aralashmasining vodorodga nisbatan zichligini aniqlang."%(nm[0].upper()+nm[1:],_f(eta*100,0),eq)
    return numq(t,D,[M0/2,M0/(2*(1+eta/2)),M0/(2*(1-eta)) if eta<1 else M0,D*2],"1 mol olsak: n(jami) = 1 + %s = %s mol; M(o'rt) = %d/%s = %s; D(H2) = %s"%(_f(eta),_f(1+eta),M0,_f(1+eta),_f(2*D,2),_f(D,2)),"10-sinf (alkanlarning krekingi va degidrogenlanishi)",1)

# 2) Alken + alkan aralashmasi: brom suvidan o'tkazish va qolganini yondirish
def c_alkene_alkane(r):
    pairs=[('propen','propan',42,44,3,'C3H6','C3H8'),('etilen','etan',28,30,2,'C2H4','C2H6'),('buten-1','butan',56,58,4,'C4H8','C4H10'),('etilen','propan',28,44,3,'C2H4','C3H8')]
    nA,nB,MA,MB,cB,fA,fB=r.choice(pairs)
    a=r.choice([0.1,0.2,0.25,0.3,0.4]); b=r.choice([0.1,0.2,0.25,0.3,0.4])
    dm=a*MA; co2=b*cB*V
    ans=MA*a/(MA*a+MB*b)*100
    t="%s va %s aralashmasi mo'l bromli suvdan o'tkazilganda idish massasi %s g ortdi. Qolgan gaz to'liq yondirilganda %s l (n.sh.) CO2 hosil bo'ldi. Boshlang'ich aralashmadagi %s ning massa ulushini (%%) toping."%(nA[0].upper()+nA[1:],nB,_f(dm),_f(co2),nA)
    return numq(t,ans,[a/(a+b)*100,100-ans,MA/(MA+MB)*100,b*MB/(MA*a+MB*b)*100],"Brom faqat %s ni yutadi: n(%s) = %s/%d = %s mol; %s dan CO2: n(%s) = %s/22,4/%d = %s mol; ω = %s %%"%(nA,fA,_f(dm),MA,_f(a),nB,fB,_f(co2),cB,_f(b),_f(ans,1)),"10-sinf (alken va alkanlarning xossalari)",1)

# 3) Benzol + toluol aralashmasi: CO2 va H2O dan tarkibni topish
def c_arene_mix(r):
    a,b=_pickmix(r,0,0,(0.1,0.2,0.3,0.4)); co2=6*a+7*b; h2o=3*a+4*b
    ask=r.choice(['frac','mass'])
    if ask=='frac':
        ans=a/(a+b)*100
        t="Benzol va toluol aralashmasi yondirilganda %s mol CO2 va %s mol suv hosil bo'ldi. Aralashmadagi benzolning mol ulushini (%%) aniqlang."%(_f(co2),_f(h2o))
        return numq(t,ans,[b/(a+b)*100,a*78/(a*78+b*92)*100,50,(6*a)/(6*a+7*b)*100],"Benzol x, toluol y: 6x + 7y = %s; 3x + 4y = %s → x = %s, y = %s; mol ulushi = %s %%"%(_f(co2),_f(h2o),_f(a),_f(b),_f(ans,1)),"10-sinf (arenlar; yonish)",1)
    m=78*a+92*b
    t="Benzol va toluol aralashmasi yondirilganda %s mol CO2 va %s mol suv hosil bo'ldi. Dastlabki aralashmaning massasini (g) toping."%(_f(co2),_f(h2o))
    return numq(t,m,[m*2,78*(a+b),92*(a+b),m/2],"6x + 7y = %s; 3x + 4y = %s → x = %s, y = %s; m = 78x + 92y = %s g"%(_f(co2),_f(h2o),_f(a),_f(b),_f(m,1)),"10-sinf (arenlar; yonish)",1)

# 4) Spirtlar aralashmasi + natriy
def c_alcohol_mix(r):
    A=[('metanol','CH3OH',32),('etanol','C2H5OH',46),('propanol-1','C3H7OH',60)]
    (n1,f1,M1),(n2,f2,M2)=r.sample(A,2)
    a,b=_pickmix(r,0,0); m=a*M1+b*M2; h2=(a+b)/2*V
    ask=r.choice(['m2','w'])
    if ask=='m2':
        ans=b*M2
        t="%s va %s aralashmasi (%s g) natriy bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi. Aralashmadagi %sning massasini (g) aniqlang."%(n1[0].upper()+n1[1:],n2,_f(m),_f(h2),n2)
        return numq(t,ans,[a*M2,b*M1,ans*2,(m/2)],"n(H2) = %s/22,4 = %s mol → x + y = %s; %d x + %d y = %s → y = %s mol; m = %s g"%(_f(h2),_f(h2/V),_f(a+b),M1,M2,_f(m),_f(b),_f(ans)),"10-sinf (spirtlarning xossalari)",1)
    ans=a*M1/m*100
    t="%s va %s aralashmasi (%s g) natriy bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi. Aralashmadagi %sning massa ulushini (%%) toping."%(n1[0].upper()+n1[1:],n2,_f(m),_f(h2),n1)
    return numq(t,ans,[100-ans,a/(a+b)*100,b/(a+b)*100,50],"x + y = %s; %d x + %d y = %s → x = %s, y = %s; ω = %s %%"%(_f(a+b),M1,M2,_f(m),_f(a),_f(b),_f(ans,1)),"10-sinf (spirtlarning xossalari)",1)

# 5) HCHO + aldegid aralashmasi: "tuzoq" — formaldegid 4 Ag beradi
ALD=[('etanal','CH3CHO',44),('propanal','C2H5CHO',58),('butanal','C3H7CHO',72)]
def c_ald_ag(r):
    nm,f,M2=r.choice(ALD); a,b=_pickmix(r,0,0,(0.05,0.1,0.15,0.2,0.25)); m=30*a+M2*b; ag=(4*a+2*b)*108
    ask=r.choice(['m2','m1','frac','h2'])
    head="Formaldegid va %s aralashmasi (%s g) mo'l ammiakli kumush oksid eritmasi bilan qizdirilganda %s g kumush ajraldi. "%(nm,_f(m),_f(ag))
    sol="HCHO → 4Ag, %s → 2Ag. 30x + %d y = %s; 4x + 2y = %s/108 = %s → x = %s, y = %s; "%(f,M2,_f(m),_f(ag),_f(ag/108),_f(a),_f(b))
    src="10-sinf (aldegidlarning kumush ko'zgu reaksiyasi)"
    if ask=='m2': return numq(head+"Aralashmadagi %sning massasini (g) aniqlang."%nm,M2*b,[30*a,M2*b*2,m/2,ag/108*M2/2],sol+"m = %s g"%_f(M2*b),src,1)
    if ask=='m1': return numq(head+"Aralashmadagi formaldegidning massasini (g) aniqlang."%(),30*a,[M2*b,30*a*2,m/2,a*M2],sol+"m = %s g"%_f(30*a),src,1)
    if ask=='frac': return numq(head+"Aralashmadagi formaldegidning mol ulushini (%) aniqlang.",a/(a+b)*100,[b/(a+b)*100,30*a/m*100,50,a*100],sol+"mol ulushi = %s %%"%_f(a/(a+b)*100,1),src,1)
    return numq(head+"Shu aralashmani to'liq gidrogenlash uchun zarur vodorod hajmini (l, n.sh.) hisoblang.",(a+b)*V,[a*V,b*V,(a+b)*V*2,(a+b)*V/2],sol+"V(H2) = (x + y)·22,4 = %s l"%_f((a+b)*V),src,2)

# 6) Chumoli kislota + boshqa kislota aralashmasi
ACS=[('sirka','CH3COOH',60),('propion','C2H5COOH',74),('akril','CH2=CHCOOH',72)]
def c_acid_mix(r):
    nm,f,M2=r.choice(ACS); a,b=_pickmix(r,0,0,(0.1,0.2,0.3,0.4)); co2=(a+b)*V; ag=2*a*108
    ask=r.choice(['w','nahco3','m2'])
    head="Chumoli va %s kislota aralashmasi mo'l NaHCO3 eritmasi bilan ta'sirlashganda %s l (n.sh.) gaz ajraldi. Shu miqdordagi aralashma ammiakli kumush oksid bilan qizdirilganda %s g kumush hosil bo'ldi. "%(nm,_f(co2),_f(ag))
    sol="Ikkala kislota ham NaHCO3 bilan CO2 beradi: x + y = %s mol; faqat HCOOH 2Ag beradi: x = %s/216 = %s mol → y = %s; "%(_f(a+b),_f(ag),_f(a),_f(b))
    src="10-sinf (karbon kislotalar; chumoli kislotaning o'ziga xosligi)"
    if ask=='w':
        ans=M2*b/(46*a+M2*b)*100
        return numq(head+"Aralashmadagi %s kislotaning massa ulushini (%%) toping."%nm,ans,[100-ans,b/(a+b)*100,a/(a+b)*100,ans/2],sol+"ω = %s %%"%_f(ans,1),src,1)
    if ask=='nahco3':
        ans=(a+b)*84
        return numq(head+"Reaksiyaga sarflangan NaHCO3 massasini (g) hisoblang.",ans,[a*84,b*84,ans*2,ans/2],sol+"m(NaHCO3) = (x + y)·84 = %s g"%_f(ans),src,1)
    ans=M2*b
    return numq(head+"Aralashmadagi %s kislotaning massasini (g) toping."%nm,ans,[46*a,ans*2,ans/2,46*a+M2*b],sol+"m = %s g"%_f(ans),src,1)

# 7) Murakkab efirlar aralashmasi gidrolizi
EST=[(('metilformiat',60,'CH3OH',32,'HCOONa',68),('etilatsetat',88,'C2H5OH',46,'CH3COONa',82)),
     (('metilformiat',60,'CH3OH',32,'HCOONa',68),('metilatsetat',74,'CH3OH',32,'CH3COONa',82)),
     (('etilformiat',74,'C2H5OH',46,'HCOONa',68),('propilatsetat',102,'C3H7OH',60,'CH3COONa',82))]
def c_ester_mix(r):
    for _ in range(40):
        E1,E2=r.choice(EST); a,b=_pickmix(r,0,0,(0.1,0.2,0.3,0.4))
        if E1[3]!=E2[3] or True: break
    m=E1[1]*a+E2[1]*b; n=a+b
    ask=r.choice(['alc','salt','m2'])
    head="%s va %s aralashmasi (%s g) mo'l NaOH eritmasi bilan to'liq gidrolizlandi. Aralashmaning mol miqdori %s mol. "%(E1[0][0].upper()+E1[0][1:],E2[0],_f(m),_f(n))
    sol="x + y = %s; %d x + %d y = %s → x = %s, y = %s; "%(_f(n),E1[1],E2[1],_f(m),_f(a),_f(b))
    src="10-sinf (murakkab efirlarning gidrolizi)"
    if ask=='alc':
        ans=E1[3]*a+E2[3]*b
        return numq(head+"Hosil bo'lgan spirtlar massasini (g) aniqlang.",ans,[ans*2,m-ans,(E1[3]+E2[3])*n/2,E2[3]*n],sol+"m(spirt) = %s g"%_f(ans),src,1)
    if ask=='salt':
        ans=E1[5]*a+E2[5]*b
        return numq(head+"Hosil bo'lgan tuzlar massasini (g) aniqlang.",ans,[ans*2,m,(E1[5]+E2[5])*n/2,E2[5]*n],sol+"m(tuz) = %s g"%_f(ans),src,1)
    ans=E2[1]*b
    return numq(head+"Aralashmadagi %s massasini (g) toping."%E2[0],ans,[E1[1]*a,ans*2,m/2,ans+E1[1]*a*0.5],sol+"m = %s g"%_f(ans),src,1)

# 8) Anilin + alifatik amin: faqat anilin brom bilan cho'kma beradi
AMS=[('metilamin','CH3NH2',31),('etilamin','C2H5NH2',45),('propilamin','C3H7NH2',59)]
def c_amine_mix(r):
    nm,f,M2=r.choice(AMS); a,b=_pickmix(r,0,0,(0.05,0.1,0.15,0.2)); m=93*a+M2*b; ppt=330*a
    ask=r.choice(['hcl','m2'])
    head="Anilin va %s aralashmasi (%s g) mo'l bromli suv bilan ta'sirlashganda %s g cho'kma tushdi. "%(nm,_f(m),_f(ppt))
    sol="Cho'kma – 2,4,6-tribromanilin (330 g/mol): x = %s/330 = %s mol; 93x + %d y = %s → y = %s mol; "%(_f(ppt),_f(a),M2,_f(m),_f(b))
    src="10-sinf (aminlar va anilin xossalari)"
    if ask=='hcl':
        ans=(a+b)*36.5
        return numq(head+"Shu aralashmani neytrallash uchun zarur HCl ning massasini (g) hisoblang.",ans,[a*36.5,b*36.5,ans*2,m/2],sol+"HCl: (x + y)·36,5 = %s g"%_f(ans),src,2)
    ans=M2*b
    return numq(head+"Aralashmadagi %sning massasini (g) toping."%nm,ans,[93*a,ans*2,m/2,ans+10],sol+"m = %s g"%_f(ans),src,2)

# 9) Glukoza: bijg'ish (unum) -> CO2 -> CaCO3 yoki etanol
def c_glucose_chain(r):
    eta=r.choice([0.6,0.75,0.8,0.9]); n=r.choice([0.5,1,1.5,2,2.5]); m=n*180
    ask='caco3'
    head="%s g glukoza spirtli bijg'ishga uchradi (unum %s %%). "%(_f(m,0),_f(eta*100,0))
    src="10-sinf (uglevodlar; glukozaning bijg'ishi)"
    if ask=='caco3':
        ans=2*n*eta*100
        return numq(head+"Ajralgan gaz mo'l ohakli suvdan o'tkazilganda necha gramm cho'kma hosil bo'ladi?",ans,[n*2*100,ans/2,n*eta*100,ans*2],"C6H12O6 → 2C2H5OH + 2CO2; n(CO2) = 2·%s·%s = %s mol; CO2 + Ca(OH)2 → CaCO3↓ + H2O; m = %s g"%(_f(n),_f(eta),_f(2*n*eta),_f(ans,1)),src,1)
    if ask=='etoh':
        ans=2*n*eta*46
        return numq(head+"Hosil bo'lgan etanol massasini (g) aniqlang.",ans,[n*2*46,ans/2,ans*2,n*eta*46],"n(C2H5OH) = 2·%s·%s = %s mol; m = %s g"%(_f(n),_f(eta),_f(2*n*eta),_f(ans,1)),src,1)
    co2=2*n*eta*V
    return numq("Glukozaning spirtli bijg'ishidan (unum %s %%) %s l (n.sh.) CO2 ajraldi. Bijg'ishga olingan glukoza massasini (g) toping."%(_f(eta*100,0),_f(co2)),m,[m*eta,m/2,m*2,m/eta*0.5],"n(CO2) = %s/22,4 = %s mol → nazariy n(glukoza) = %s mol; amalda %s/%s = %s mol → %s g"%(_f(co2),_f(co2/V),_f(co2/V/2),_f(co2/V/2),_f(eta),_f(n),_f(m,0)),src,0)

# 10) Atsetilen -> aldegid -> kumush yoki kislota (ketma-ket, unum bilan)
def c_chain_alkyne(r):
    n=r.choice([0.5,1,2,2.5]); e1=r.choice([0.8,0.9,0.75]); e2=r.choice([0.8,0.5,0.6]); ask=r.choice(['ag','acid'])
    head="%s mol atsetilen Kucherov reaksiyasi bo'yicha gidratlandi (unum %s %%). Hosil bo'lgan aldegidning %s %% i "%(_f(n),_f(e1*100,0),_f(e2*100,0))
    if ask=='ag':
        ag=n*e1*e2*2*108
        return numq(head+"ammiakli kumush oksid bilan reaksiyaga kirishdi. Necha gramm kumush ajraladi?",ag,[ag/2,ag*2,n*e1*2*108,n*2*108],"C2H2 + H2O → CH3CHO: %s mol; reaksiyaga kirishgani: %s mol; CH3CHO → 2Ag: %s mol → %s g"%(_f(n*e1),_f(n*e1*e2),_f(2*n*e1*e2),_f(ag,1)),"10-sinf (alkinlar, aldegidlar)",1)
    ac=n*e1*e2*60
    return numq(head+"oksidlanib sirka kislotaga aylandi. Hosil bo'lgan sirka kislota massasini (g) toping.",ac,[ac/2,ac*2,n*e1*60,n*60],"C2H2 + H2O → CH3CHO: %s mol; oksidlangani: %s mol; CH3CHO → CH3COOH: %s g"%(_f(n*e1),_f(n*e1*e2),_f(ac,1)),"10-sinf (alkinlar, aldegidlar, karbon kislotalar)",1)


# 11) Galogenli hosila: massa ulushidan uglevodorodni aniqlash
def c_halo_formula(r):
    kind=r.choice([('alkan','xlor','Cl',35.5,lambda n:14*n+36.5,'CnH2n+1Cl','alkanning monoxlorlanishidan'),('alkan','brom','Br',80,lambda n:14*n+81,'CnH2n+1Br','alkanning monobromlanishidan'),('alken','xlor','Cl',35.5,lambda n:14*n+36.5,'CnH2n+1Cl','alkenga HCl birikishidan'),('alken','brom','Br',80,lambda n:14*n+81,'CnH2n+1Br','alkenga HBr birikishidan')])
    cls,hn,sym,Ah,Mf,gen,how=kind; n=r.choice([2,3,4,5,6]); w=Ah/Mf(n)*100
    ask=r.choice(['M','C'])
    t="%s hosil bo'lgan galogenli hosilada %s massa ulushi %s %% ga teng. "%(how[0].upper()+how[1:],hn,_f(w,1))
    if ask=='M':
        Mu=14*n+(2 if cls=='alkan' else 0)
        return numq(t+"Dastlabki %sning molyar massasini (g/mol) aniqlang."%cls,Mu,[Mu+14,Mu-14,Mu*2,Mf(n)],"Hosila %s: ω = %s/(14n + %s) = %s → n = %d; %s M = %d g/mol"%(gen,_f(Ah),_f(Mf(n)-14*n),_f(w/100,3),n,cls,Mu),"10-sinf (alkan va alkenlarning galogenli hosilalari)",0)
    return numq(t+"Dastlabki %s molekulasidagi uglerod atomlari sonini toping."%cls,n,[n+1,n-1 if n>1 else n+2,n+2,2*n],"Hosila %s: ω = %s/(14n + %s) = %s → n = %d"%(gen,_f(Ah),_f(Mf(n)-14*n),_f(w/100,3),n),"10-sinf (alkan va alkenlarning galogenli hosilalari)",0)

# 12) Alken + vodorod aralashmasi: gidrogenlash, hajm kamayishi va zichlik
def c_hydrogenation(r):
    nm,f,MA=r.choice([('etilen','C2H4',28),('propen','C3H6',42),('buten-1','C4H8',56)])
    a,b=r.choice([(1,2),(1,3),(2,3),(2,5),(1,4)]); a2=a/b
    ask=r.choice(['dec','D'])
    mass0=MA*a+2*b; M0=mass0/(a+b); D0=M0/2
    nf=a+(b-a); Mf_=mass0/b
    if ask=='dec':
        ans=a/(a+b)*100
        return numq("%s va vodorod aralashmasining (mol nisbati %d : %d) vodorodga nisbatan zichligi %s. Aralashma Ni katalizatori ustida to'liq gidrogenlandi. Gaz hajmi necha foizga kamayadi?"%(nm[0].upper()+nm[1:],a,b,_f(D0,2)),ans,[ans*2,100-ans,b/(a+b)*100,a/b*100],"%s %d mol, H2 %d mol: CnH2n + H2 → CnH2n+2; %d mol H2 sarflanadi, hajm %d mol ga kamayadi: %d/%d = %s %%"%(nm,a,b,a,a,a,a+b,_f(ans,1)),"10-sinf (alkenlarni gidrogenlash)",1)
    D1=Mf_/2
    return numq("%s va vodorod aralashmasi (mol nisbati %d : %d) Ni katalizatori ustida to'liq gidrogenlandi. Reaksiyadan so'ng hosil bo'lgan gazlar aralashmasining vodorodga nisbatan zichligini aniqlang."%(nm[0].upper()+nm[1:],a,b),D1,[D0,D1*2,D1/2,(MA+2)/2],"%d mol %s + %d mol H2 → %d mol alkan + %d mol H2 qoladi; m = %s g, n = %d mol; M = %s; D = %s"%(a,nm,b,a,b-a,_f(mass0),b,_f(Mf_,2),_f(D1,2)),"10-sinf (alkenlarni gidrogenlash)",1)

# 13) Benzol -> nitrobenzol -> anilin (ikki bosqichli unum)
def c_nitro_chain(r):
    n=r.choice([0.5,1,2]); e1=r.choice([0.8,0.9,0.75]); e2=r.choice([0.8,0.5,0.6,0.9])
    m=n*78; ans=n*e1*e2*93
    tgt='aniline'
    if tgt=='aniline':
        return numq("%s g benzol nitrolandi (unum %s %%), hosil bo'lgan nitrobenzol Zinin reaksiyasi bo'yicha qaytarildi (unum %s %%). Olingan anilin massasini (g) hisoblang."%(_f(m,0),_f(e1*100,0),_f(e2*100,0)),ans,[ans*2,ans/2,n*93,n*e1*93],"C6H6 → C6H5NO2: %s mol; → C6H5NH2: %s mol; m = %s g"%(_f(n*e1),_f(n*e1*e2),_f(ans,1)),"10-sinf (arenlar, anilin olinishi)",1)
    ans=n*e1*123
    return numq("%s g benzol nitrolandi (unum %s %%). Hosil bo'lgan nitrobenzolning massasini (g) toping."%(_f(m,0),_f(e1*100,0)),ans,[n*123,ans/2,ans*2,n*e1*93],"n(C6H6) = %s mol; n(C6H5NO2) = %s mol; m = %s g"%(_f(n),_f(n*e1),_f(ans,1)),"10-sinf (arenlar, nitrolash)",1)

# 14) Etanol: etilen va dietil efir (parallel jarayonlar)
def c_ethanol_parallel(r):
    n=r.choice([0.2,0.4,0.5,1]); p=r.choice([0.4,0.5,0.6,0.8]); ask=r.choice(['water','ether'])
    m=n*46
    head="%s g etanol sulfat kislota ishtirokida qizdirilganda uning %s %% i etilenga, qolgani dietil efirga aylandi. "%(_f(m,1),_f(p*100,0))
    h2o=n*p+n*(1-p)/2
    if ask=='water':
        return numq(head+"Barcha jarayonlarda hosil bo'lgan suv massasini (g) aniqlang.",h2o*18,[n*18,n*p*18,h2o*18*2,n*(1-p)*18],"C2H5OH → C2H4 + H2O: %s mol H2O; 2C2H5OH → (C2H5)2O + H2O: %s mol H2O; jami %s mol = %s g"%(_f(n*p),_f(n*(1-p)/2),_f(h2o),_f(h2o*18,2)),"10-sinf (spirtlarning degidratlanishi)",2)
    ans=n*(1-p)/2*74
    return numq(head+"Hosil bo'lgan dietil efir massasini (g) toping.",ans,[n*(1-p)*74,ans*2,n*p*28,ans/2],"Efirga ketgan etanol %s mol → efir %s mol → %s g"%(_f(n*(1-p)),_f(n*(1-p)/2),_f(ans,2)),"10-sinf (spirtlarning degidratlanishi)",2)

# 15) Kraxmal -> glukoza -> etanol (ikki unumli zanjir)
def c_starch_chain(r):
    m=r.choice([162,324,486,810]); e1=r.choice([0.8,0.9,0.75]); e2=r.choice([0.8,0.5,0.6,0.9]); n=m/162
    ans=n*e1*e2*2*46
    return numq("%s g kraxmal gidrolizlanib (unum %s %%) glukoza olindi, glukoza esa spirtli bijg'ishga uchradi (unum %s %%). Hosil bo'lgan etanol massasini (g) toping."%(_f(m,0),_f(e1*100,0),_f(e2*100,0)),ans,[ans/2,ans*2,n*e1*2*46,n*2*46],"(C6H10O5)n → nC6H12O6: n(glukoza) = %s mol; → 2C2H5OH: %s mol; m = %s g"%(_f(n*e1),_f(n*e1*e2*2),_f(ans,1)),"10-sinf (uglevodlar: kraxmal, glukoza)",1)

# 16) Birlamchi amin yonishi: CO2 : N2 nisbatidan formula
def c_amine_comb(r):
    n=r.choice([1,2,3,4,5]); ask=r.choice(['M','H2O'])
    names={1:'metilamin',2:'etilamin',3:'propilamin',4:'butilamin',5:'pentilamin'}
    t="To'yingan alifatik birlamchi amin yondirilganda hosil bo'lgan CO2 hajmi azot hajmidan %d marta ko'p bo'lsa, "%(2*n)
    if ask=='M':
        Mu=14*n+17
        return numq(t+"aminning molyar massasini (g/mol) toping.",Mu,[Mu+14,Mu-14,Mu+17,Mu*2],"CnH2n+3N → nCO2 + (2n+3)/2 H2O + 1/2 N2: n : 0,5 = %d → n = %d; M = 14n + 17 = %d"%(2*n,n,Mu),"10-sinf (aminlar yonishi)",0)
    ans=(2*n+3)/2/0.5
    return numq(t+"suv bug'lari hajmi azot hajmidan necha marta ko'p bo'ladi?",ans,[ans+1,ans-1,ans*2,2*n],"CnH2n+3N: n = %d; V(H2O) : V(N2) = (2n+3)/2 : 0,5 = %s"%(n,_f(ans,0)),"10-sinf (aminlar yonishi)",0)

HARD_ORG={0:[c_decomp,c_halo_formula],1:[c_alkene_alkane,c_chain_alkyne,c_hydrogenation,c_halo_formula],2:[c_arene_mix,c_nitro_chain],3:[c_alcohol_mix,c_ethanol_parallel],4:[c_ald_ag],5:[c_acid_mix],6:[c_ester_mix],7:[c_glucose_chain,c_starch_chain],8:[c_amine_mix,c_amine_comb]}
