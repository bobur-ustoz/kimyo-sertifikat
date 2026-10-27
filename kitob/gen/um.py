from core import *
import re
SYM=['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr']
NAME={'Li':'litiy','Be':'berilliy','B':'bor','C':'uglerod','N':'azot','O':'kislorod','F':'ftor','Ne':'neon','Na':'natriy','Mg':'magniy','Al':'alyuminiy','Si':'kremniy','P':'fosfor','S':'oltingugurt','Cl':'xlor','Ar':'argon','K':'kaliy','Ca':'kalsiy','Ti':'titan','V':'vanadiy','Cr':'xrom','Mn':'marganes','Fe':'temir','Co':'kobalt','Ni':'nikel','Cu':'mis','Zn':'rux','Br':'brom','Ga':'galliy','As':'mishyak','Se':'selen'}
ORDER=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1)]
def config(Z):
    occ={};left=Z
    for n,l in ORDER:
        cap=2*(2*l+1); e=min(cap,left); occ[(n,l)]=e; left-=e
        if left==0: break
    if Z==24: occ[(4,0)]=1; occ[(3,2)]=5
    if Z==29: occ[(4,0)]=1; occ[(3,2)]=10
    return {k:v for k,v in occ.items() if v}
def electrons(Z):
    out=[]
    for (n,l),e in config(Z).items():
        orbs=list(range(-l,l+1)); up=min(e,len(orbs))
        for i in range(e):
            if i<len(orbs): out.append((n,l,orbs[i],0.5))
            else: out.append((n,l,orbs[i-len(orbs)],-0.5))
    return out
def conf_str(Z):
    names='spdf'; return ' '.join('%d%s%d'%(n,names[l],e) for (n,l),e in sorted(config(Z).items(),key=lambda kv:(kv[0][0]+kv[0][1],kv[0][0])))
def unpaired(Z):
    c=0
    for (n,l),e in config(Z).items():
        o=2*l+1; c+= e if e<=o else 2*o-e
    return c
# ---------------- TUSHUNCHA ----------------
def t_jism(r):
    subs=['shakar','mis','osh tuzi','suv','kislorod','oltingugurt','alyuminiy','temir','etanol','grafit']
    jism=['probirka','qalam','tanga','qaychi','stakan','mix']
    a=r.sample(subs,r.randint(2,4)); b=r.sample(jism,r.randint(2,3)); lst=a+b; r.shuffle(lst)
    k=len(a)
    return numq("Quyidagilarni jism va moddalarga ajrating: %s. Ulardan nechtasi modda?"%', '.join(lst),k,[k+1,k-1 if k>1 else k+3,len(b),k+2],"Moddalar: %s (%d ta); jismlar: %s."%(', '.join(a),k,', '.join(b)),"7-sinf (jism va modda)",0,kind='theory')
VAL=[('Fe2O3','temir',3),('P2O5','fosfor',5),('SO3','oltingugurt',6),('Cl2O7','xlor',7),('MnO2','marganes',4),('N2O3','azot',3),('CrO3','xrom',6),('CO2','uglerod',4),('Al2O3','alyuminiy',3),('SiO2','kremniy',4),('N2O5','azot',5),('Mn2O7','marganes',7)]
ROM={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII'}
def t_valent(r):
    f,e,v=pick(r,VAL)
    ws=[ROM[x] for x in r.sample([x for x in range(2,8) if x!=v],3)]
    return Q("%s tarkibida %s ning valentligini aniqlang."%(f,e),ROM[v],ws,"Kislorod II valentli: %s da %s ning valentligi %s."%(f,e,ROM[v]),"7-sinf (valentlik)",'theory')
def c_hydrate(r):
    sets=[('CuSO4.5H2O',250,90),('Na2CO3.10H2O',286,180),('FeSO4.7H2O',278,126),('Na2SO4.10H2O',322,180),('MgSO4.7H2O',246,126)]
    f,m,w=pick(r,sets); p=w/m*100
    return numq("%s kristallogidratida kristallizatsion suvning massa ulushini (%%) aniqlang."%f.replace('.','·'),p,[100-p,p/2,w/(m-w)*100],"M(%s) = %d; suv %d g: %d/%d = %s %%"%(f.replace('.','·'),m,w,w,m,fmt(p,1)),"7-sinf; Tirkashev (kristallogidrat)",1)
# ---------------- MOL ----------------
CMP=['CH4','NH3','H2O','CO2','C2H6','SO3','C3H8','H2SO4']
def c_atoms(r):
    f=pick(r,CMP); n=r.choice([0.5,1,1.5,2,2.5]); tot=sum(parse(f).values()); at=n*tot
    return numq("%s mol %s tarkibida necha mol atom bor?"%(fmt(n),f),at,[at-n,n*(tot+1),n,2*at],"%s molekulasida %d atom: %s · %d = %s mol"%(f,tot,fmt(n),tot,fmt(at)),"7-sinf (mol)",None)
def c_Natoms(r):
    f=pick(r,['CH4','NH3','H2O','CO2','C2H6','C3H8']); n=r.choice([0.1,0.2,0.5,1,2]); tot=sum(parse(f).values())
    N=n*tot*6.02
    return numq("%s mol %s tarkibidagi atomlar sonini toping (N_A = 6,02·10²³). Javobni 10²³ birligida yozing."%(fmt(n),f),N/10,[N/10*2,N/10/2,n*6.02/10],"N = n · atomlar soni · N_A = %s · %d · 6,02·10²³ = %s·10²³"%(fmt(n),tot,fmt(N/10,3)),"7-sinf (Avogadro)",3)
GMIX=[('CO',28,'CO2',44),('N2',28,'CO2',44),('H2',2,'CH4',16),('CH4',16,'C2H6',30),('O2',32,'CO2',44),('He',4,'O2',32)]
def c_gasmix(r):
    f1,m1,f2,m2=pick(r,GMIX)
    x=r.choice([0.1,0.2,0.25,0.3]); y=r.choice([0.2,0.25,0.3,0.4])
    V=(x+y)*22.4; m=x*m1+y*m2
    return numq("%s va %s dan iborat %s l (n.sh.) aralashmaning massasi %s g. Aralashmadagi %s ning massasini (g) aniqlang."%(f1,f2,fmt(V,2),fmt(m,2),f1),x*m1,[y*m1,x*m2,y*m2,(x+y)*m1],"x + y = %s; %d x + %d y = %s → x = %s mol %s → %s g"%(fmt(x+y,2),m1,m2,fmt(m,2),fmt(x),f1,fmt(x*m1,2)),"11-sinf (gaz aralashmalar)",2)
def c_density(r):
    f1,m1,f2,m2=pick(r,GMIX); a=r.choice([1,2,3]); b=r.choice([1,2,3])
    if a==b: b=a+1
    M_=(a*m1+b*m2)/(a+b)
    return numq("%s va %s gazlari %d : %d hajmiy nisbatda aralashtirildi. Aralashmaning vodorodga nisbatan zichligini aniqlang."%(f1,f2,a,b),M_/2,[M_,M_/2+1,(m1+m2)/4,M_/4],"M = (%d·%d + %d·%d)/%d = %s; D = M/2 = %s"%(a,m1,b,m2,a+b,fmt(M_,2),fmt(M_/2,2)),"11-sinf (D)",2)
RX=[('CaCO3 + 2HCl -> CaCl2 + CO2 + H2O','CaCO3','CO2'),('Zn + 2HCl -> ZnCl2 + H2','Zn','H2'),('Na2CO3 + 2HCl -> 2NaCl + CO2 + H2O','Na2CO3','CO2'),('2Al + 6HCl -> 2AlCl3 + 3H2','Al','H2'),('Mg + H2SO4 -> MgSO4 + H2','Mg','H2'),('2KClO3 -> 2KCl + 3O2','KClO3','O2'),('2H2O2 -> 2H2O + O2','H2O2','O2'),('Fe + 2HCl -> FeCl2 + H2','Fe','H2')]
def c_gasvol(r):
    eq,a,g=pick(r,RX); co=dict(balance(eq)); n=r.choice([0.1,0.2,0.25,0.5]); m=n*M(a)
    mol_g=n*co[g]/co[a]; y=r.choice([80,75,90,100]); V=mol_g*22.4*y/100
    t="%s g %s reaksiyaga kirishdi (%s). Ajralgan %s hajmini (l, n.sh.) hisoblang%s."%(fmt(m,2),a,eq.replace('->','→'),g,(" (unum %d %%)"%y if y<100 else ""))
    return numq(t,V,[mol_g*22.4,V*2,V/2,n*22.4*y/100],"n(%s) = %s mol → n(%s) = %s mol; V = %s l"%(a,fmt(n),g,fmt(mol_g),fmt(V,2)),"8-sinf; 9-sinf (stexiometriya)",2)
EX=[('Zn + S -> ZnS','Zn','S','ZnS'),('Fe + S -> FeS','Fe','S','FeS'),('2Na + Cl2 -> 2NaCl','Na','Cl2','NaCl'),('Mg + 2HCl -> MgCl2 + H2','Mg','HCl','MgCl2'),('NaOH + HCl -> NaCl + H2O','NaOH','HCl','NaCl'),('CaO + H2O -> Ca(OH)2','CaO','H2O','Ca(OH)2')]
def c_excess(r):
    eq,a,b,p=pick(r,EX); co=dict(balance(eq)); na=r.choice([0.2,0.3,0.4]); nb=na*co[b]/co[a]*r.choice([0.5,0.75,1.5])
    lim=min(na/co[a],nb/co[b]); mp=lim*co[p]*M(p)
    return numq("%s g %s va %s g %s aralashtirilib, reaksiya o'tkazildi (%s). Hosil bo'lgan %s massasini (g) aniqlang."%(fmt(na*M(a),2),a,fmt(nb*M(b),2),b,eq.replace('->','→'),p),mp,[na*co[p]/co[a]*M(p),nb*co[p]/co[b]*M(p),mp*2,mp/2],"n(%s) = %s, n(%s) = %s; kam miqdordagi modda bo'yicha: %s g"%(a,fmt(na),b,fmt(nb),fmt(mp,2)),"8-sinf (ortiqcha modda masalasi)",2)
# ---------------- QONUN/GAZ ----------------
def c_pv(r):
    for _ in range(50):
        T=r.choice([0,27,127]); P=r.choice([1,2,0.5]); n=r.choice([0.25,0.4,0.5,1]); Mx=r.choice([20,28,32,44,16]); V=n*0.082*(273+T)/P
        if abs(V*100-round(V*100))<1e-6: break
    return numq("%d °C va %s atm bosimda hajmi %s l bo'lgan gazning massasi %s g. Gazning molyar massasini (g/mol) aniqlang. (R = 0,082 l·atm/(mol·K))"%(T,fmt(P),fmt(V,2),fmt(n*Mx,2)),Mx,[Mx*2,Mx/2,Mx*1.5],"n = PV/RT = %s mol; M = m/n = %d"%(fmt(n),Mx),"11-sinf (Mendeleyev–Klapeyron)",None)
def c_ekv(r):
    me,E=r.choice([('Al',9),('Mg',12),('Ca',20)]); m=r.choice([2.4,4.8,10.8]) if me!='Al' else r.choice([5.4,2.7,10.8])
    if me=='Ca': m=r.choice([4,8,10])
    if me=='Mg': m=r.choice([2.4,4.8,7.2])
    mo=m*8/E; ox=m+mo
    return numq("%s g metall oksidlanganda %s g oksid hosil bo'ldi. Metallning ekvivalent massasini (g/mol) aniqlang."%(fmt(m,2),fmt(ox,2)),E,[E*2,E/2,E*1.5,m*8],"m(O) = %s g; E = m·8/m(O) = %s"%(fmt(mo,2),fmt(E)),"11-sinf (ekvivalentlar qonuni)",None)
def c_vol(r):
    rx=[('N2 + 3H2 -> 2NH3',1,3,2,'N2','H2'),('2H2 + O2 -> 2H2O',2,1,2,'H2','O2'),('2CO + O2 -> 2CO2',2,1,2,'CO','O2'),('2SO2 + O2 -> 2SO3',2,1,2,'SO2','O2')]
    eq,a,b,c,f1,f2=pick(r,rx); Va=r.choice([10,20,30,40]); Vb=Va*b/a*r.choice([1.5,2]); lim=min(Va/a,Vb/b)
    vp=lim*c; rest=(Va-lim*a)+(Vb-lim*b); tot=rest+vp
    note=", suv bug' holida" if 'H2O' in eq else ""
    return numq("%s l %s va %s l %s aralashmasi reaksiyaga kirishdi (%s, hamma moddalar bir xil sharoitda gaz holida%s). Reaksiyadan keyingi gaz aralashmasining hajmini (l) aniqlang."%(fmt(Va),f1,fmt(Vb),f2,eq.replace('->','→'),note),tot,[Va+Vb,vp,rest,tot*2],"Hajmiy nisbat bo'yicha: qolgan %s l + hosil %s l = %s l"%(fmt(rest),fmt(vp),fmt(tot)),"8-sinf (Gey-Lyussak, Avogadro)",None)
# ---------------- ATOM ----------------
def t_config(r):
    for _ in range(20):
        Z=r.choice([7,8,13,14,15,16,17,24,25,26,29,30,33,34,35]); e=SYM[Z]; kind=r.choice(['unp','d','out','n3l2']); el=electrons(Z)
        if kind=='unp': k=unpaired(Z); t="%s (Z = %d) atomida nechta juftlashmagan elektron bor?"%(NAME[e].capitalize(),Z)
        elif kind=='d': k=sum(1 for x in el if x[1]==2); t="%s atomida d-pog'onachadagi elektronlar sonini aniqlang (Z = %d)."%(NAME[e].capitalize(),Z)
        elif kind=='out': mx=max(x[0] for x in el); k=sum(1 for x in el if x[0]==mx); t="%s (Z = %d) atomining tashqi energetik pog'onasidagi elektronlar sonini aniqlang."%(NAME[e].capitalize(),Z)
        else: k=sum(1 for x in el if x[0]==3 and x[1]==2); t="%d-tartib raqamli element atomida n = 3 va l = 2 bo'lgan elektronlar sonini aniqlang."%Z
        if k>0: break
    return numq(t,k,[k+1,k-1,k+2,max(k*2,1)],"Konfiguratsiya: %s"%conf_str(Z),"Tirkashev I bob; 8-sinf (elektron konfiguratsiya)",0,'theory')
def t_qnum(r):
    Z=r.choice([15,17,26,28,33,35]); el=electrons(Z)
    ml=r.choice([0,1,-1]); ms=r.choice([0.5,-0.5])
    a=sum(1 for x in el if x[2]==ml and x[3]==ms); b=sum(1 for x in el if x[2]==ml and x[3]==-ms)
    sg=lambda s:'+½' if s>0 else '−½'
    ans='%d va %d'%(a,b)
    ws=['%d va %d'%x for x in [(b,a),(a+1,b),(a,b+1),(a+2,b),(a,b+2)] if '%d va %d'%x!=ans]
    return Q("%d-tartib raqamli element atomida magnit kvant soni m_l = %d bo'lgan elektronlardan nechtasining spin kvant soni m_s = %s ga, nechtasiniki m_s = %s ga teng?"%(Z,ml,sg(ms),sg(-ms)),ans,list(dict.fromkeys(ws))[:3],"Elektronlar to'ldirilishi (Gund qoidasi): m_l = %d, m_s = %s: %d ta; m_s = %s: %d ta"%(ml,sg(ms),a,sg(-ms),b),"Tirkashev I bob (kvant sonlari)",'theory')
DEC=[('238','92','Pb','206','82',8,6),('232','90','Pb','208','82',6,4),('235','92','Pb','207','82',7,4),('226','88','Pb','206','82',5,4)]
def t_decay(r):
    A,Z,sy,A2,Z2,a,b=pick(r,DEC); mode=r.choice(['ab','alpha','beta'])
    assert int(A)-4*a==int(A2) and int(Z)-2*a+b==int(Z2)
    sol="ΔA = %d → %d α-zarra; zaryad: %s − 2·%d + β = %s → β = %d"%(int(A)-int(A2),a,Z,a,Z2,b)
    src="11-sinf 1-bob (yadro reaksiyalari)"
    if mode=='alpha': return numq("Massa soni %s, zaryadi %s bo'lgan yadro massa soni %s, zaryadi %s bo'lgan yadroga aylandi (α va β⁻ parchalanish). Nechta α-zarra chiqarilgan?"%(A,Z,A2,Z2),a,[a+1,a-1,a+2,b],sol,src,0,'theory')
    if mode=='beta': return numq("Massa soni %s, zaryadi %s bo'lgan yadro massa soni %s, zaryadi %s bo'lgan yadroga aylandi (α va β⁻ parchalanish). Nechta β⁻-zarra chiqarilgan?"%(A,Z,A2,Z2),b,[b+1,b-1 if b>1 else b+3,b+2,a],sol,src,0,'theory')
    ans="%dα va %dβ"%(a,b)
    return Q("Massa soni %s va zaryadi %s bo'lgan yadro massa soni %s, zaryadi %s bo'lgan yadroga aylanishida nechta α- va β⁻-zarra chiqaradi?"%(A,Z,A2,Z2),ans,["%dα va %dβ"%(a+1,b),"%dα va %dβ"%(a,b+2),"%dα va %dβ"%(b,a)],sol,src,'theory')
def c_isotope(r):
    sets=[('³⁵Cl',35,75,'³⁷Cl',37),('¹⁰B',10,20,'¹¹B',11),('⁶³Cu',63,70,'⁶⁵Cu',65),('⁷⁹Br',79,50,'⁸¹Br',81),('²⁴Mg',24,80,'²⁶Mg',26)]
    a,ma,pa,b,mb=pick(r,sets); avg=(ma*pa+mb*(100-pa))/100
    return numq("Tabiiy elementning ikki izotopi: %s (%d %%) va %s (%d %%). Elementning o'rtacha nisbiy atom massasini aniqlang."%(a,pa,b,100-pa),avg,[(ma+mb)/2,ma*(100-pa)/100+mb*pa/100,ma,mb],"Ar = (%d·%d + %d·%d)/100 = %s"%(ma,pa,mb,100-pa,fmt(avg,2)),"8-sinf (izotoplar)",2)
def c_ion(r):
    Z=r.choice([12,13,20,26]); ch={12:2,13:3,20:2,26:r.choice([2,3])}[Z]; A=2*Z+r.choice([0,1,2,3,4])
    ne=Z-ch; n=A-Z
    sup=''.join('⁰¹²³⁴⁵⁶⁷⁸⁹'[int(d)] for d in str(ch))+'⁺'
    return numq("X%s ionida %d ta elektron va %d ta neytron bor. X atomining nisbiy atom massasini aniqlang."%(sup,ne,n),A,[A+ch,A-ch,Z,2*n],"Z = %d + %d = %d; A = Z + N = %d"%(ne,ch,Z,A),"8-sinf (atom tuzilishi)",0)
def t_isoel(r):
    ng=r.choice(['Ne','Ar']); n={'Ne':10,'Ar':18}[ng]
    allz=[('Na⁺',10),('Mg²⁺',10),('F⁻',10),('O²⁻',10),('Al³⁺',10),('Cl⁻',18),('K⁺',18),('Li⁺',2),('S²⁻',18),('Ca²⁺',18),('N³⁻',10)]
    good=[x for x in allz if x[1]==n]; bad=[x for x in allz if x[1]!=n]
    k=r.randint(2,3); lst=r.sample(good,k)+r.sample(bad,4-k); r.shuffle(lst)
    nums=[i+1 for i,x in enumerate(lst) if x[1]==n]; ans=', '.join(map(str,nums))
    allc=['1, 2','1, 3','2, 3','1, 2, 3','2, 4','1, 4','3, 4','1, 3, 4','2, 3, 4','1, 2, 4']
    ws=[c for c in allc if c!=ans and len(c.split(', '))in(len(nums),len(nums)+1,len(nums)-1)]
    r.shuffle(ws)
    return Q("Quyidagi zarrachalardan qaysilari %s atomi bilan izoelektron? %s"%(NAME[ng],'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(lst))),ans,ws[:3],"%s: %d e⁻; zarrachalardagi elektronlar: %s"%(ng,n,', '.join('%s – %d'%x for x in lst)),"Tirkashev I bob; 8-sinf (izoelektron)",'theory')
