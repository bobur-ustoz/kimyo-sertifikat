from core import *
from um import electrons, SYM, NAME, config
import random
SALTS=[('NaCl',58.5),('KNO3',101),('Na2SO4',142),('KCl',74.5),('NaNO3',85),('K2SO4',174),('CuSO4',160),('BaCl2',208),('MgSO4',120),('NaOH',40),('KOH',56),('NH4NO3',80),('Na2CO3',106),('KBr',119)]
def _tab(rows,head): return "| "+" | ".join(head)+" |\n|"+"---|"*len(head)+"\n"+"\n".join("| "+" | ".join(str(c) for c in row)+" |" for row in rows)
def tbl_mix2(r):
    s,_=r.choice(SALTS); m1=r.choice([50,100,150,200,250]); m2=r.choice([100,200,300,150]); w1=r.choice([5,10,12,15,20]); w2=r.choice([25,30,35,40]); water=r.choice([0,0,50,100])
    w=(m1*w1+m2*w2)/(m1+m2+water)
    form=r.choice([0,1,2]); wtxt=" Eritmalar aralashtirilib, ustiga %s g suv qo'shildi."%water if water else " Eritmalar aralashtirildi."
    if form==0:
        t="Jadvalda %s ning ikki eritmasi haqida ma'lumot berilgan:\n\n%s\n\n%s Hosil bo'lgan eritmaning massa ulushini (%%) aniqlang."%(s,_tab([(1,m1,w1),(2,m2,w2)],['Eritma','Massasi, g','Massa ulushi, %']),wtxt.strip())
    elif form==1:
        t="Laboratoriyada %s eritmalari quyidagicha tayyorlangan:\n\n%s\n\nBu ikki eritma bir idishga quyilib%s, yangi eritmadagi %s ning massa ulushi (%%) qancha bo'ladi?"%(s,_tab([('A',m1,w1),('B',m2,w2)],['Idish','Eritma massasi, g','ω(%s), %%'%s]),(" va ustiga %s g suv qo'shilsa"%water if water else ''),s)
    else:
        t="Quyidagi jadvalda %s tuzining eritmalari keltirilgan:\n\n%s\n\n%s Oxirgi eritmadagi tuzning massa ulushini (%%) toping."%(s,_tab([('I',m1,w1),('II',m2,w2)],['№','m(eritma), g','ω, %']),wtxt.strip())
    q=numq(t,w,[(w1+w2)/2,w1+w2,(m1*w2+m2*w1)/(m1+m2),w*0.9,(m1*w1+m2*w2)/(m1+m2)],"m(%s) = %s g; m(eritma) = %d g; ω = %s %%"%(s,fmt((m1*w1+m2*w2)/100,2),m1+m2+water,fmt(w,2)),"Tirkashev III bob (eritmalar, jadval)",2)
    q.kind='table'; return q
EQB=[('N2 + 3H2 ⇌ 2NH3',[('N2',1),('H2',3)],('NH3',2)),('H2 + I2 ⇌ 2HI',[('H2',1),('I2',1)],('HI',2)),('2SO2 + O2 ⇌ 2SO3',[('SO2',2),('O2',1)],('SO3',2)),('CO + H2O ⇌ CO2 + H2',[('CO',1),('H2O',1)],('CO2',1)),('N2O4 ⇌ 2NO2',[('N2O4',1)],('NO2',2)),('2NO + O2 ⇌ 2NO2',[('NO',2),('O2',1)],('NO2',2)),('PCl5 ⇌ PCl3 + Cl2',[('PCl5',1)],('PCl3',1)),('CO + Cl2 ⇌ COCl2',[('CO',1),('Cl2',1)],('COCl2',1))]
def tbl_eq2(r):
    for _ in range(100):
        eq,rs,(pn,pc)=r.choice(EQB); V=r.choice([1,2,4,5]); x=r.choice([1,2,0.5,1.5])
        init=[r.choice([2,3,4,6]) for _ in rs]
        # reactant sarfi: x mol of "reaction extent"; products formed x*pc
        eqm=[a-x*c for a,(n,c) in zip(init,rs)]; pm=x*pc
        if all(e>0 for e in eqm): break
    else: raise RuntimeError
    if eq=='CO + H2O ⇌ CO2 + H2': K=(pm/V)**2/((eqm[0]/V)*(eqm[1]/V))
    elif eq=='PCl5 ⇌ PCl3 + Cl2': K=(pm/V)**2/(eqm[0]/V)
    else:
        num=(pm/V)**pc; den=1
        for e,(n,c) in zip(eqm,rs): den*=(e/V)**c
        K=num/den
    head=['Modda']+[n for n,_ in rs]+[pn]
    rows=[["Boshlang'ich, mol"]+[fmt(a) for a in init]+['0'],['Muvozanatda, mol']+['—']*len(rs)+[fmt(pm)]]
    t="%s reaksiyasi %d l hajmli idishda o'tkazildi. Ma'lumotlar jadvalda berilgan:\n\n%s\n\n"%(eq,V,_tab(rows,head))
    if r.random()<0.5:
        a0=init[0]; conv=x*rs[0][1]/a0*100
        q=numq(t+"%s ning necha foizi reaksiyaga kirishganini aniqlang."%rs[0][0],conv,[conv/2,conv*1.5,x/a0*100,100-conv],"%s sarfi %s mol; α = %s/%s = %s %%"%(rs[0][0],fmt(x*rs[0][1]),fmt(x*rs[0][1]),fmt(a0),fmt(conv,1)),"Tirkashev VI bob (muvozanat, jadval)",1)
    else:
        q=numq(t+"Muvozanat konstantasini (K) hisoblang.",K,[K*2,K/2,K*V,K/V,1/K],"Muvozanat miqdorlari: %s; %s = %s mol; K = %s"%(', '.join('%s %s'%(n,fmt(e)) for e,(n,c) in zip(eqm,rs)),pn,fmt(pm),fmt(K,3)),"Tirkashev VI bob (muvozanat, jadval)",3)
    q.kind='table'; return q
def tbl_rate(r):
    for _ in range(60):
        c0=r.choice([2.0,1.6,1.2,2.4]); k=r.choice([0.1,0.15,0.2,0.25])
        t=[0,2,4,6]; cs=[round(c0-k*ti*c0/2,2) for ti in t]
        if min(cs)>0: break
    i,j=r.choice([(0,1),(1,3),(0,3),(0,2)])
    v=(cs[i]-cs[j])/(t[j]-t[i]); sub=r.choice(['A','X','N2O5','H2O2'])
    q=numq("%s moddaning parchalanish reaksiyasida konsentratsiyaning vaqt bo'yicha o'zgarishi jadvalda berilgan:\n\n%s\n\n%d-minutdan %d-minutgacha o'rtacha tezlikni mol/(l·min) hisoblang."%(sub,_tab([(a,b) for a,b in zip(t,[fmt(c,2) for c in cs])],['t, min','c, mol/l']),t[i],t[j]),v,[v*2,v/2,cs[i]-cs[j],cs[i]/(t[j]-t[i])],"v = (%s − %s)/%d = %s"%(fmt(cs[i],2),fmt(cs[j],2),t[j]-t[i],fmt(v,3)),"Tirkashev VI bob (tezlik, jadval)",3)
    q.kind='table'; return q
def tbl_solub(r):
    salt="noma'lum X"
    base=r.choice([(13,32,64,110),(30,36,40,46),(15,24,38,60),(22,30,40,55)]); T=[0,20,40,60]
    t1,t2=r.choice([(60,20),(60,0),(40,20),(40,0)]); s1=base[T.index(t1)]; s2=base[T.index(t2)]
    m=round(r.choice([100,150,200,250,300])*(100+s1)/100,2)
    salt_m=m*s1/(100+s1); water=m-salt_m; dep=salt_m-water*s2/100
    q=numq("%s tuzining eruvchanligi (g/100 g suv) haroratga bog'liq jadvalda keltirilgan:\n\n%s\n\n%d °C da tayyorlangan to'yingan %s g eritma %d °C gacha sovitildi. Cho'kmaga tushgan tuz massasini (g) aniqlang."%(salt,_tab([['S, g/100 g suv']+list(base)],['t, °C']+[str(x) for x in T]),t1,fmt(m,2),t2),dep,[salt_m,water*s2/100,dep*2,dep/2],"%d °C: tuz %s g, suv %s g; %d °C da %s g eriydi → cho'kma %s g"%(t1,fmt(salt_m,2),fmt(water,2),t2,fmt(water*s2/100,2),fmt(dep,2)),"Tirkashev III bob (eruvchanlik, jadval)",2)
    q.kind='table'; return q
def tbl_atoms(r):
    Z=r.choice([11,12,13,16,17,19,20,26,29,30]); A=2*Z+r.choice([0,1,2,3,4,5]); ch=r.choice([0,0,1,-1])
    p=Z; n=A-Z; e=Z-ch
    q=numq("Zarracha haqida ma'lumot jadvalda berilgan:\n\n%s\n\nShu zarrachaning massa sonini aniqlang."%_tab([('proton',p),('neytron',n),('elektron',e)],['Zarracha tarkibi','Soni']),A,[A+1,p+e,2*p,A-ch+1],"A = p + n = %d + %d = %d"%(p,n,A),"8-sinf (atom tuzilishi, jadval)",0)
    q.kind='table'; return q
def tbl_gas(r):
    g=r.sample([('H2',2),('He',4),('CH4',16),('N2',28),('O2',32),('CO2',44),('Cl2',71),('SO2',64),('NH3',17)],3)
    vols=[r.choice([1,2,3]) for _ in g]; M_=sum(v*m for v,(_,m) in zip(vols,g))/sum(vols); D=M_/29
    q=numq("Gazlar aralashmasi tarkibi jadvalda berilgan (n.sh.):\n\n%s\n\nAralashmaning havoga nisbatan zichligini aniqlang (M(havo) = 29 g/mol)."%_tab([(n,v) for (n,_),v in zip(g,vols)],['Gaz','Hajmi, l']),D,[D*2,D/2,M_,M_/2],"M(o'rt.) = %s g/mol; D = %s/29 = %s"%(fmt(M_,2),fmt(M_,2),fmt(D,2)),"11-sinf (gaz aralashmalar, jadval)",2)
    q.kind='table'; return q
def c_ekv2(r):
    k=r.choice(['h2','ox','acid'])
    if k=='h2':
        me,E=r.choice([('Zn',32.5),('Mg',12),('Al',9),('Fe',28),('Ca',20)]); V=r.choice([1.12,2.24,3.36,4.48,5.6]); m=V*E/11.2
        return numq("%s g metall kislotada eritilganda %s l (n.sh.) vodorod ajraldi. Metallning ekvivalent massasini (g/mol) aniqlang (V_E(H2) = 11,2 l/mol)."%(fmt(m,2),fmt(V,2)),E,[E*2,E/2,m*11.2,E*1.5],"E = m·11,2/V = %s"%fmt(E),"11-sinf (ekvivalentlar qonuni)",None)
    if k=='ox':
        me,E=r.choice([('Al',9),('Mg',12),('Ca',20),('Zn',32.5),('Fe',28),('Cu',32)]); m=r.choice([2,4,6,8,10]); mo=m*8/E; ox=m+mo
        return numq("Metall oksidida kislorodning massa ulushi %s %%. Metallning ekvivalent massasini (g/mol) aniqlang."%fmt(mo/ox*100,2),E,[E*2,E/2,E*1.5,16],"ω(O) = %s %% → E(Me) = ω(Me)·8/ω(O) = %s"%(fmt(mo/ox*100,2),fmt(E)),"11-sinf (ekvivalentlar qonuni)",None)
    a,E=r.choice([('HCl',36.5),('HNO3',63),('CH3COOH',60),('H2SO4',49)]); b=r.choice([4,8,12]); m=b/40*E
    t="%s g NaOH ni to'liq neytrallash uchun %s g %s sarflandi. %s ning ekvivalent massasini (g/mol) aniqlang."%(fmt(b),fmt(m,2),a,a)
    if a=='H2SO4': t="%s g NaOH ni to'liq neytrallash uchun %s g H2SO4 sarflandi (ikkala H almashinadi). H2SO4 ning ekvivalent massasini (g/mol) aniqlang."%(fmt(b),fmt(m,2))
    return numq(t,E,[E*2,E/2,m,E*1.5],"E(kislota) = m·E(NaOH)/m(NaOH) = %s·40/%s = %s"%(fmt(m,2),fmt(b),fmt(E,2)),"11-sinf (ekvivalentlar qonuni)",None)
def c_vol2(r):
    rx=[('CH4 + 2O2 -> CO2 + 2H2O','CH4','O2','CO2',1,2,1),('C2H4 + 3O2 -> 2CO2 + 2H2O','C2H4','O2','CO2',1,3,2),('2H2S + 3O2 -> 2SO2 + 2H2O','H2S','O2','SO2',2,3,2),('2NO + O2 -> 2NO2','NO','O2','NO2',2,1,2),('H2 + Cl2 -> 2HCl','H2','Cl2','HCl',1,1,2),('2CO + O2 -> 2CO2','CO','O2','CO2',2,1,2),('N2 + O2 -> 2NO','N2','O2','NO',1,1,2),('C2H2 + 2H2 -> C2H6','C2H2','H2','C2H6',1,2,1)]
    eq,f1,f2,fp,a,b,c=r.choice(rx); Va=r.choice([10,20,30,40,50]); k=r.choice([1.5,2,3])
    Vb=Va*b/a*k; rest_b=Vb-Va*b/a; vp=Va*c/a; tot=rest_b+vp
    note=" (reaksiyadan so'ng suv suyuq holatda; gazlar bir xil sharoitda o'lchandi)" if 'H2O' in eq else " (barcha gazlar bir xil sharoitda o'lchandi)"
    base="%s l %s va %s l %s aralashmasi %s tenglama bo'yicha to'liq reaksiyaga kirishdi%s. "%(fmt(Va),f1,fmt(Vb),f2,eq.replace('->','→'),note)
    ask=r.choice(['tot','contr','rest'])
    if ask=='contr' and abs(Va+Vb-tot)<1e-9: ask='tot'
    if ask=='tot': return numq(base+"Reaksiyadan so'ng hosil bo'lgan gazlar aralashmasining umumiy hajmini (l) aniqlang.",tot,[Va+Vb,vp,rest_b,tot*2],"Qoldiq %s %s l + %s %s l = %s l"%(f2,fmt(rest_b),fp,fmt(vp),fmt(tot)),"8-sinf (Gey-Lyussak qonuni)",None)
    if ask=='contr': return numq(base+"Aralashma hajmi necha litrga o'zgargan (modul bo'yicha)?",abs(Va+Vb-tot),[Va+Vb,tot,vp,abs(Va+Vb-tot)*2+1],"Boshida %s l, oxirida %s l; farq %s l"%(fmt(Va+Vb),fmt(tot),fmt(abs(Va+Vb-tot))),"8-sinf (Gey-Lyussak qonuni)",None)
    return numq(base+"Reaksiyadan so'ng ortib qolgan %s ning hajmini (l) aniqlang."%f2,rest_b,[Vb,rest_b*2,vp,Vb-Va],"%s sarfi %s l; ortgani %s − %s = %s l"%(f2,fmt(Va*b/a),fmt(Vb),fmt(Va*b/a),fmt(rest_b)),"8-sinf (Gey-Lyussak qonuni)",None)
def c_pv2(r):
    k=r.choice(['V','m','D','rho'])
    for _ in range(80):
        T=r.choice([0,27,127,-23]); P=r.choice([1,2,0.5,4]); n=r.choice([0.25,0.4,0.5,1,2]); Mx=r.choice([2,4,16,28,32,44,64,71])
        V=n*0.082*(273+T)/P
        if abs(V*100-round(V*100))<1e-6: break
    R="(R = 0,082 l·atm/(mol·K))"; gas={2:'H2',4:'He',16:'CH4',28:'N2',32:'O2',44:'CO2',64:'SO2',71:'Cl2'}[Mx]
    if k=='V': return numq("%s g %s %d °C va %s atm bosimda qancha hajm (l) egallaydi? %s"%(fmt(n*Mx,2),gas,T,fmt(P),R),V,[V*2,V/2,n*22.4,V*1.5],"n = %s mol; V = nRT/P = %s l"%(fmt(n),fmt(V,2)),"11-sinf (Mendeleyev–Klapeyron)",2)
    if k=='m': return numq("%s l %s %d °C va %s atm bosimda necha gramm keladi? %s"%(fmt(V,2),gas,T,fmt(P),R),n*Mx,[n*Mx*2,n*Mx/2,V*Mx/22.4,n*Mx*1.5],"n = PV/RT = %s mol; m = nM = %s g"%(fmt(n),fmt(n*Mx,2)),"11-sinf (Mendeleyev–Klapeyron)",2)
    if k=='D': return numq("Massasi %s g bo'lgan gaz %d °C va %s atm bosimda %s l hajm egallaydi. Gazning vodorodga nisbatan zichligini aniqlang. %s"%(fmt(n*Mx,2),T,fmt(P),fmt(V,2),R),Mx/2,[Mx,Mx/4,Mx*2,Mx/2+2],"M = mRT/(PV) = %s; D(H2) = M/2 = %s"%(fmt(Mx),fmt(Mx/2,2)),"11-sinf (Mendeleyev–Klapeyron)",2)
    rho=n*Mx/V
    return numq("%s gazining %d °C va %s atm bosimdagi zichligini (g/l) aniqlang. %s"%(gas,T,fmt(P),R),rho,[rho*2,rho/2,Mx/22.4,rho*1.5],"ρ = PM/(RT) = %s g/l"%fmt(rho,3),"11-sinf (Mendeleyev–Klapeyron)",2)
def t_qnum2(r):
    Z=r.choice([7,8,13,15,16,17,24,26,28,29,33,35]); el=electrons(Z); kind=r.choice(['nl','mlpos','pair','spin','maxn'])
    if kind=='nl':
        n=r.choice([2,3]); l=r.choice([0,1]); k=sum(1 for x in el if x[0]==n and x[1]==l)
        t="%d-tartib raqamli element atomida bosh kvant soni n = %d, orbital kvant soni l = %d bo'lgan elektronlar soni nechta?"%(Z,n,l)
    elif kind=='mlpos':
        ml=r.choice([-1,0,1]); k=sum(1 for x in el if x[2]==ml and x[1]>0)
        t="%s atomining p- va d- pog'onachalaridagi elektronlardan nechtasining magnit kvant soni m_l = %d ga teng? (Z = %d)"%(NAME[SYM[Z]].capitalize(),ml,Z)
    elif kind=='pair':
        k=0
        for (n,l),e in config(Z).items():
            o=2*l+1; k+= (e-o)*2 if e>o else 0
        t="%s (Z = %d) atomi elektron konfiguratsiyasida jami nechta juftlashgan elektron bor?"%(NAME[SYM[Z]].capitalize(),Z)
    elif kind=='spin':
        k=sum(1 for x in el if x[3]==0.5)
        t="%d-tartib raqamli elementning barcha elektronlaridan nechtasining spin kvant soni m_s = +½ ga teng (Hund qoidasi bo'yicha to'ldirilgan holat)?"%Z
    else:
        mx=max(x[0] for x in el); k=sum(1 for x in el if x[0]==mx and x[1]==1)
        t="%s (Z = %d) atomining eng tashqi pog'onasidagi p-elektronlar sonini aniqlang."%(NAME[SYM[Z]].capitalize(),Z)
    if k==0: return t_qnum2(r)
    return numq(t,k,[k+1,k-1 if k>1 else k+3,k+2,2*k],"Konfiguratsiya bo'yicha hisoblash: %d"%k,"Tirkashev I bob (kvant sonlari)",0,'theory')
def c_prep2(r):
    s,Ms=r.choice(SALTS[:10]); k=r.choice(['dil','add','evap','mixw'])
    if k=='dil':
        m=r.choice([200,300,400,500]); w0=r.choice([20,25,40,50]); w1=r.choice([5,10,8]); x=m*w1/w0
        return numq("%s ning %d %% li eritmasidan %s g %d %% li eritma tayyorlash uchun necha gramm suv kerak?"%(s,w0,m,w1),m-x,[x,m,(m-x)*2,m*w1/100],"Eritma massasi: %s·%d/%d = %s g; suv %s − %s = %s g"%(m,w1,w0,fmt(x,2),m,fmt(x,2),fmt(m-x,2)),"Tirkashev III bob (eritmalar)",2)
    if k=='add':
        m=r.choice([100,200,300,400]); w0=r.choice([5,10,15,20]); add=r.choice([10,20,25,50]); w=(m*w0/100+add)/(m+add)*100
        return numq("%d g %d %% li %s eritmasiga %d g shu tuzning o'zi qo'shilib eritildi. Hosil bo'lgan eritmaning massa ulushini (%%) aniqlang."%(m,w0,s,add),w,[w0+add/m*100,(w0+100*add/m)/2,w*0.8,w*1.2],"m(tuz) = %s + %d = %s g; m(eritma) = %d g; ω = %s %%"%(fmt(m*w0/100,2),add,fmt(m*w0/100+add,2),m+add,fmt(w,2)),"Tirkashev III bob (eritmalar)",2)
    if k=='evap':
        m=r.choice([200,300,400,500,250]); w0=r.choice([10,15,20,12]); ev=r.choice([50,100,80]); w=m*w0/(m-ev)
        return numq("%d g %d %% li %s eritmasidan %d g suv bug'latildi. Qolgan eritmadagi tuzning massa ulushini (%%) toping."%(m,w0,s,ev),w,[w0*m/(m+ev),w0*ev/m,w*0.8,w+10],"m(tuz) = %s g; m(eritma) = %d g; ω = %s %%"%(fmt(m*w0/100,2),m-ev,fmt(w,2)),"Tirkashev III bob (eritmalar)",2)
    m1=r.choice([100,200,300]); m2=r.choice([100,200]); w1=r.choice([10,20,30]); w2=r.choice([40,50,60]); w=(m1*w1+m2*w2)/(m1+m2)
    return numq("%d g %d %% li va %d g %d %% li %s eritmalari aralashtirildi. Yangi eritmaning massa ulushini (%%) toping."%(m1,w1,m2,w2,s),w,[(w1+w2)/2,w1+w2,w*0.9,w*1.1],"ω = (%d·%d + %d·%d)/%d = %s %%"%(m1,w1,m2,w2,m1+m2,fmt(w,2)),"Tirkashev III bob (eritmalar)",2)
# ---------------- qo'shimcha jadvalli savollar (OQR, kuchlanish qatori, bog', yadro)
OXS={'N':[('NH3',-3),('N2',0),('N2O',1),('NO',2),('NO2',4),('HNO3',5),('NaNO2',3)],'S':[('H2S',-2),('S',0),('SO2',4),('SO3',6),('H2SO4',6),('Na2SO3',4),('Na2S',-2)],'Cl':[('HCl',-1),('Cl2',0),('HClO',1),('KClO3',5),('HClO4',7),('NaCl',-1)],'Mn':[('MnO2',4),('KMnO4',7),('MnSO4',2),('K2MnO4',6),('Mn',0)],'Cr':[('Cr',0),('Cr2O3',3),('CrO3',6),('K2Cr2O7',6),('CrCl2',2)]}
def tbl_oqr(r):
    el=r.choice(list(OXS)); items=r.sample(OXS[el],4); vals={'N':(-3,5),'S':(-2,6),'Cl':(-1,7),'Mn':(0,7),'Cr':(0,6)}[el]
    lo,hi=vals; kind=r.choice(['ox','red','both'])
    def ok(s):
        if kind=='ox': return s==hi
        if kind=='red': return s==lo
        return lo<s<hi
    ans=sum(1 for _,s in items if ok(s))
    what={'ox':"faqat oksidlovchi bo'la oladigan",'red':"faqat qaytaruvchi bo'la oladigan",'both':"ham oksidlovchi, ham qaytaruvchi bo'la oladigan"}[kind]
    q=numq("Jadvalda %s elementining birikmalaridagi oksidlanish darajasi berilgan:\n\n%s\n\nShu birikmalardan nechtasida %s element %s bo'la oladi? (%s ning eng past oksidlanish darajasi %s, eng yuqorisi +%d)"%(el,_tab(items,['Modda','Oksidlanish darajasi']),el,what.replace("bo'la oladigan",'').strip() or 'element',"",'','') if False else "Jadvalda %s elementining birikmalaridagi oksidlanish darajasi berilgan:\n\n%s\n\nUshbu moddalardan nechtasida %s elementi %s xossani namoyon qiladi? (%s uchun eng past oksidlanish darajasi %s, eng yuqorisi %+d)"%(el,_tab([(a,('%+d'%s if s else '0')) for a,s in items],['Modda','Oksidlanish darajasi']),el,what.replace(" bo'la oladigan",''),el,('%+d'%lo if lo else '0'),hi),ans,[ans+1,max(ans-1,0)+3,ans+2,4-ans if 4-ans!=ans else ans+3],"Eng past (%s) – faqat qaytaruvchi, eng yuqori (%+d) – faqat oksidlovchi, oraliq – ikkala xossa. Natija %d"%(('%+d'%lo if lo else '0'),hi,ans),"Tirkashev V bob (OQR, jadval)",0)
    q.kind='table'; return q
ACT=['Mg','Zn','Fe','Cu','Ag']
def tbl_series(r):
    ms=r.sample(ACT,3); sal={'Mg':'MgSO4','Zn':'ZnSO4','Fe':'FeSO4','Cu':'CuSO4','Ag':'AgNO3'}; sel=r.sample(ACT,3)
    rows=[]
    for m in ms:
        rows.append([m]+['+' if ACT.index(m)<ACT.index(s) else '−' for s in sel])
    head=['Metall']+[sal[s]+' eritmasi' for s in sel]
    ans=max(ms,key=lambda m:-ACT.index(m)); 
    cnt=lambda m:sum(1 for x in rows[ms.index(m)][1:] if x=='+')
    best=max(ms,key=cnt)
    if sorted(cnt(m) for m in ms)[-1]==sorted(cnt(m) for m in ms)[-2]: return tbl_series(r)
    q=Q("Jadvalda metall plastinkalarning tuz eritmalariga tushirilishidagi kuzatuvlar berilgan («+» – metall ajraladi, reaksiya boradi; «−» – reaksiya bormaydi):\n\n%s\n\nUshbu metallardan qaysi biri eng faol?"%_tab(rows,head),best,[m for m in ms if m!=best]+[x for x in ACT if x not in ms][:1],"Eng ko'p tuzdan metallni siqib chiqargan metall – eng faol: %s"%best,"Tirkashev V bob (kuchlanish qatori, jadval)",'table')
    q.kind='table'; return q
ENV={'H':2.1,'C':2.5,'N':3.0,'O':3.5,'F':4.0,'Cl':3.0,'Na':0.9,'S':2.5,'Br':2.8,'K':0.8,'Ca':1.0,'Mg':1.2,'Al':1.5,'Si':1.8,'P':2.1}
def tbl_bond(r):
    prs=r.sample([('H','F'),('H','Cl'),('H','O'),('H','N'),('C','O'),('Na','Cl'),('K','Br'),('C','H'),('Mg','O'),('Al','Cl'),('N','H'),('Si','O')],4)
    rows=[('%s–%s'%(a,b),ENV[a],ENV[b],round(abs(ENV[a]-ENV[b]),1)) for a,b in prs]
    best=max(rows,key=lambda x:x[3])
    if sorted(x[3] for x in rows)[-1]==sorted(x[3] for x in rows)[-2]: return tbl_bond(r)
    q=Q("Jadvalda bog'lar hosil qiluvchi atomlarning elektrmanfiyliklari berilgan:\n\n%s\n\nQaysi bog' eng qutbli (eng ko'p ionli xarakterga ega)?"%_tab([(a,fmt(b,1),fmt(c,1)) for a,b,c,d in rows],['Bog\'','EM (1-atom)','EM (2-atom)']),best[0],[x[0] for x in rows if x[0]!=best[0]],"Elektrmanfiylik farqi eng katta: %s (Δ = %s)"%(best[0],fmt(best[3],1)),"8-sinf (kimyoviy bog'lanish turlari, jadval)",'table')
    q.kind='table'; return q
def tbl_nuclide(r):
    base=r.choice([(6,12),(8,16),(11,23),(17,35),(20,40),(26,56)]); Z,A=base
    sp=[('I',Z,A+2),('II',Z+1,A),('III',Z+1,A+1+0),('IV',Z,A)]
    rows=[('X',Z,A)]+[(n,z,a) for n,z,a in [('Y',Z,A+r.choice([1,2])),('T',Z+1,A),('U',Z+1,A+1),('V',Z,A+r.choice([1,2]))]]
    isot=sum(1 for n,z,a in rows[1:] if z==Z and a!=A); isob=sum(1 for n,z,a in rows[1:] if a==A and z!=Z)
    kind=r.choice(['isot','isob'])
    q=numq("Jadvalda nuklidlarning proton soni (Z) va massa soni (A) berilgan:\n\n%s\n\nX nuklidning nechta %s jadvalda keltirilgan?"%(_tab(rows,['Nuklid','Z','A']),'izotopi' if kind=='isot' else 'izobari'),isot if kind=='isot' else isob,[ (isot if kind=='isot' else isob)+1,(isot if kind=='isot' else isob)+2,max((isot if kind=='isot' else isob)-1,0)+3,4],"Izotoplar – Z bir xil, A har xil; izobarlar – A bir xil, Z har xil","8-sinf (izotoplar, izobarlar, jadval)",0)
    q.kind='table'; return q
