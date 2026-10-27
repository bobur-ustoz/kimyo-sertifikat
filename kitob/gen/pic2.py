from core import *
from pic import _save
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, itertools, math
# =================================================================== structural formulas
STEM={1:'met',2:'et',3:'prop',4:'but',5:'pent',6:'geks',7:'gept',8:'okt',9:'non',10:'dek'}
MULT={1:'',2:'di',3:'tri'}
def make_mol(r):
    n=r.choice([5,6,7]); kind=r.choice(['alkan','alkan','alken','alkin'])
    bonds=[1]*(n-1)
    if kind=='alken': bonds[r.randrange(1,n-2)]=2 if n>3 else 2
    if kind=='alkin': bonds[r.randrange(1,n-2)]=3
    # substituents: dict pos(1..n)->list of lengths
    sub={}
    for _ in range(r.choice([1,2,2,3])):
        p=r.randrange(2,n); L=r.choice([1,1,1,2])
        if p in sub: continue
        # carbon valence check on chain carbon: bonds on both sides + branches <=4
        b=(bonds[p-2] if p>=2 else 0)+(bonds[p-1] if p<=n-1 else 0)
        if b+1>4: continue
        sub[p]=[L]
    if not sub: return make_mol(r)
    return n,bonds,sub,kind
def graph(n,bonds,sub):
    adj={}; order={}; nid=0
    def add():
        nonlocal nid; adj[nid]=[]; nid+=1; return nid-1
    ch=[add() for _ in range(n)]
    for i in range(n-1):
        adj[ch[i]].append((ch[i+1],bonds[i])); adj[ch[i+1]].append((ch[i],bonds[i]))
    for p,ls in sub.items():
        for L in ls:
            prev=ch[p-1]
            for _ in range(L):
                c=add(); adj[prev].append((c,1)); adj[c].append((prev,1)); prev=c
    return adj
def all_chains(adj):
    leaves=[v for v in adj if len(adj[v])==1]
    ch=[]
    def dfs(v,path):
        if len(adj[v])==1 and len(path)>1: ch.append(list(path));
        for w,_ in adj[v]:
            if w not in path: dfs(w,path+[w])
    for l in leaves: dfs(l,[l])
    return ch
def name_of(n,bonds,sub,kind):
    adj=graph(n,bonds,sub); chains=all_chains(adj)
    def bo(a,b): return [o for w,o in adj[a] if w==b][0]
    def mult(ch): return sum(1 for i in range(len(ch)-1) if bo(ch[i],ch[i+1])>1)
    best=None
    cand=[]
    for ch in chains:
        if kind!='alkan' and mult(ch)==0: continue
        subs=[]
        cs=set(ch)
        for i,v in enumerate(ch):
            for w,o in adj[v]:
                if w in cs: continue
                # size of branch
                sz=0; stack=[(w,v)]
                while stack:
                    x,pv=stack.pop(); sz+=1
                    for y,_ in adj[x]:
                        if y!=pv: stack.append((y,x))
                subs.append((i+1,sz))
        db=[i+1 for i in range(len(ch)-1) if bo(ch[i],ch[i+1])>1]
        cand.append((len(ch),len(subs),ch,subs,db))
    mx=max(c[0] for c in cand); cand=[c for c in cand if c[0]==mx]
    mxs=max(c[1] for c in cand); cand=[c for c in cand if c[1]==mxs]
    res=[]
    for L,ns,ch,subs,db in cand:
        for rev in (False,True):
            s_=[(L+1-p,sz) for p,sz in subs] if rev else subs
            d_=[L-p for p in db] if rev else db
            res.append((d_[0] if d_ else 0,sorted(p for p,_ in s_),L,s_,d_[0] if d_ else 0))
    res.sort(key=lambda x:(x[0],x[1],[('etil' if sz==2 else 'metil') for _,sz in sorted(x[3])]))
    best=res[0]; L=best[2]; s_=best[3]; d=best[4]
    groups={}
    for p,sz in s_: groups.setdefault('etil' if sz==2 else 'metil',[]).append(p)
    parts=[]
    for nm in sorted(groups):
        ps=sorted(groups[nm]); parts.append('%s-%s%s'%(','.join(map(str,ps)),MULT[len(ps)],nm))
    pre='-'.join(parts)
    base=STEM[L]+{'alkan':'an','alken':'en','alkin':'in'}[kind]
    if kind!='alkan': base+='-%d'%d
    return pre+base if pre else base
def draw_mol(n,bonds,sub,fname):
    fig,ax=plt.subplots(figsize=(5.6,2.6)); ax.axis('off')
    pos={}; lab={}
    xs=lambda i:i*1.7
    # chain carbons
    deg={}
    for i in range(n):
        h=4-((bonds[i-1] if i>0 else 0)+(bonds[i] if i<n-1 else 0))-len(sub.get(i+1,[]))
        pos[('c',i)]=(xs(i),0); deg[('c',i)]=h
    edges=[]
    for i in range(n-1): edges.append((('c',i),('c',i+1),bonds[i]))
    side=1
    for p,ls in sorted(sub.items()):
        for L in ls:
            prev=('c',p-1)
            for k in range(L):
                key=('s',p,k); pos[key]=(xs(p-1),side*1.25*(k+1)); h=3 if k==L-1 else 2; deg[key]=h
                edges.append((prev,key,1)); prev=key
        side=-side
    for a,b,o in edges:
        (x1,y1),(x2,y2)=pos[a],pos[b]
        if y1==y2:
            offs={1:[0],2:[-0.045,0.045],3:[-0.08,0,0.08]}[o]
            for d in offs: ax.plot([x1,x2],[y1+d,y2+d],'k',lw=1.4,zorder=1)
        else: ax.plot([x1,x2],[y1,y2],'k',lw=1.4,zorder=1)
    for k,(x,y) in pos.items():
        h=deg[k]; t='C' if h==0 else ('CH' if h==1 else 'CH'+('₂' if h==2 else '₃'))
        ax.text(x,y,t,ha='center',va='center',fontsize=15,zorder=3,bbox=dict(fc='white',ec='none',pad=2.2))
    ax.set_xlim(-0.6,xs(n-1)+0.6); ys=[p[1] for p in pos.values()]; ax.set_ylim(min(ys)-0.5,max(ys)+0.5)
    return _save(fig,fname)
def mol_formula(n,bonds,sub,kind):
    c=n+sum(sum(v) for v in sub.values()); h={'alkan':2*c+2,'alken':2*c,'alkin':2*c-2}[kind]
    return c,h
def wrong_names(n,bonds,sub,kind,right,r):
    ws=set()
    chain=lambda s:s
    import re
    # locant perturbations
    nums=re.findall(r'\d+',right)
    for _ in range(40):
        if len(ws)>=6: break
        new=right
        k=r.choice(['loc','swap','stem','mult'])
        if k=='loc' and nums:
            i=r.randrange(len(nums)); nv=int(nums[i])+r.choice([-1,1,2])
            if nv>=1:
                parts=re.split(r'(\d+)',right); idx=[j for j,p in enumerate(parts) if p.isdigit()][i]; parts[idx]=str(nv); new=''.join(parts)
        elif k=='swap' and 'metil' in right and 'etil' in right.replace('metil',''):
            new=right.replace('metil','XX').replace('etil','metil').replace('XX','etil')
        elif k=='stem':
            for L,s in STEM.items():
                if right.find(s+'an')>=0 or right.find(s+'en')>=0 or right.find(s+'in')>=0:
                    L2=max(3,min(8,L+r.choice([-1,1]))); new=right.replace(s,STEM[L2],1); break
        elif k=='mult':
            new=right.replace('dimetil','metil') if 'dimetil' in right else right.replace('trimetil','dimetil')
        if new!=right and new not in ws: ws.add(new)
    return list(ws)
def p_struct(r):
    for _ in range(50):
        n,bonds,sub,kind=make_mol(r)
        nm=name_of(n,bonds,sub,kind)
        ws=wrong_names(n,bonds,sub,kind,nm,r)
        if len(ws)>=3: break
    tag='%s_%d'%(abs(hash(nm))%10**8,r.randrange(1000)); img=draw_mol(n,bonds,sub,'struct_%s.png'%tag)
    c,h=mol_formula(n,bonds,sub,kind)
    qk=r.choice(['name','name2','sigma','sp','formula','mass','prim','class'])
    adj=graph(n,bonds,sub)
    pi=sum(o-1 for v in adj for w,o in adj[v])//2
    tot=c+h-1+0
    sigma=(c-1)+h
    head="![Tuzilish formulasi](rasmlar/gen/struct_%s.png)"%tag
    if qk in('name','name2'):
        T=("Rasmda tasvirlangan birikmaning sistematik nomi qaysi qatorda to'g'ri ko'rsatilgan?" if qk=='name' else "Tuzilish formulasi keltirilgan uglevodorodni xalqaro nomenklatura bo'yicha nomlang.")
        q=Q("%s\n\n%s"%(T,head),nm,ws[:3],"Eng uzun zanjir tanlanadi va raqamlash karrali bog'ga (yoki o'rinbosarlarga) eng kichik raqam berilishi bilan olib boriladi: %s"%nm,"10-sinf (nomenklatura)",'picture')
    elif qk=='sigma':
        q=numq("Rasmdagi birikma molekulasida nechta σ-bog' bor?\n\n%s"%head,sigma,[sigma+1,sigma-1,sigma+2,c+h],"C%dH%d: C–C %d ta, C–H %d ta → σ = %d (π = %d)"%(c,h,c-1,h,sigma,pi),"10-sinf (kovalent bog'lar)",0,'picture')
    elif qk=='sp':
        sp2=sum(1 for v in adj if len(adj[v])>0 and any(o==2 for _,o in adj[v])); spc=sum(1 for v in adj if any(o==3 for _,o in adj[v]))
        sp3=len(adj)-sp2-spc
        q=numq("Rasmda tasvirlangan molekuladagi sp³-gibridlangan uglerod atomlari sonini aniqlang.\n\n%s"%head,sp3,[sp3+1,sp3-1 if sp3>1 else sp3+3,c,sp3+2],"Karrali bog'dagi ugleroddan boshqa C atomlari sp³: %d ta"%sp3,"10-sinf (gibridlanish)",0,'picture')
    elif qk=='formula':
        q=Q("Rasmda tasvirlangan birikmaning molekulyar formulasini aniqlang.\n\n%s"%head,"C%dH%d"%(c,h),["C%dH%d"%(c,h+2),"C%dH%d"%(c+1,h),"C%dH%d"%(c-1,h-2)],"C = %d, H = %d"%(c,h),"10-sinf (uglevodorodlar)",'picture')
    elif qk=='mass':
        Mr=12*c+h
        q=numq("Rasmda tasvirlangan birikmaning molyar massasini (g/mol) hisoblang.\n\n%s"%head,Mr,[Mr+2,Mr-2,Mr+14,Mr*2],"C%dH%d: 12·%d + %d = %d"%(c,h,c,h,Mr),"10-sinf (uglevodorodlar)",0,'picture')
    elif qk=='prim':
        prim=sum(1 for v in adj if len(adj[v])==1); tert=sum(1 for v in adj if len([w for w,o in adj[v] if o==1])>=3 and all(o==1 for _,o in adj[v]))
        q=numq("Rasmdagi molekulada faqat bitta uglerod atomi bilan bog'langan (birlamchi) uglerod atomlari nechta?\n\n%s"%head,prim,[prim+1,prim-1 if prim>1 else prim+3,prim+2,c-prim],"Birlamchi C: boshqa bitta C ga bog'langan atomlar = %d"%prim,"10-sinf (uglerod atomlari turlari)",0,'picture')
    else:
        cl={'alkan':'alkanlar','alken':'alkenlar','alkin':'alkinlar'}[kind]; allc=['alkanlar','alkenlar','alkinlar','arenlar']
        q=Q("Rasmda tasvirlangan birikma qaysi uglevodorodlar sinfiga kiradi?\n\n%s"%head,cl,[x for x in allc if x!=cl][:3],"CnH2n+2 — alkan, CnH2n — alken, CnH2n−2 — alkin; bu yerda C%dH%d"%(c,h),"10-sinf (uglevodorodlar)",'picture')
    q.kind='picture'; return q
# =================================================================== atom model pictures
SYMB=['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca']
def shells(Z):
    out=[];left=Z
    for cap in (2,8,8,2):
        e=min(cap,left); out.append(e); left-=e
        if left==0: break
    return out
def draw_atom(Z,fname):
    sh=shells(Z); fig,ax=plt.subplots(figsize=(3.2,3.2)); ax.set_aspect('equal'); ax.axis('off')
    for i,e in enumerate(sh):
        R=1+0.8*i; ax.add_patch(plt.Circle((0,0),R,fill=False,ec='gray',lw=1))
        for k in range(e):
            a=2*math.pi*k/e+0.3*i; ax.plot(R*math.cos(a),R*math.sin(a),'o',ms=6,c='#3aa63a',mec='#1f6b1f')
    ax.text(0,0,'A',ha='center',va='center',fontsize=22,fontweight='bold'); ax.set_xlim(-3.1,3.1); ax.set_ylim(-3.1,3.1)
    return _save(fig,fname)
def p_atom(r):
    Z=r.choice([3,4,5,6,7,8,9,11,12,13,14,15,16,17,19,20]); sh=shells(Z); per=len(sh); val=sh[-1]
    grp={1:'IA',2:'IIA',3:'IIIA',4:'IVA',5:'VA',6:'VIA',7:'VIIA'}[val]
    img=draw_atom(Z,'atom_%d_%d.png'%(Z,r.randrange(10**5))); head="![Atom modeli](rasmlar/gen/%s)"%img.split('/')[-1]
    kinds=['group','period','Z','oxide','hyd','ecount','nature']
    k=r.choice(kinds)
    if k=='hyd' and val<4: k='oxide'
    if k=='group':
        allg=['IA','IIA','IIIA','IVA','VA','VIA','VIIA']; ws=[g for g in allg if g!=grp]; r.shuffle(ws)
        q=Q("Rasmda A elementining atom modeli (elektron qavatlar) tasvirlangan. Element Mendeleyev jadvalining qaysi guruhida joylashgan?\n\n%s"%head,grp+" guruh",[w+" guruh" for w in ws[:3]],"Tashqi qavatda %d e⁻ → %s guruh"%(val,grp),"8-sinf (davriy qonun)",'picture')
    elif k=='period':
        ws=[str(x) for x in (1,2,3,4) if x!=per]; q=Q("Rasmda tasvirlangan A atomining elektron qavatlari soniga qarab uning davr raqamini aniqlang.\n\n%s"%head,"%d-davr"%per,["%s-davr"%w for w in ws[:3]],"Qavatlar soni = %d → %d-davr"%(per,per),"8-sinf (davriy qonun)",'picture')
    elif k=='Z':
        q=numq("Rasmda A atomining modeli berilgan. Atom yadrosining zaryadini aniqlang.\n\n%s"%head,Z,[Z+1,Z-1,Z+2,val],"Elektronlar soni = %d → Z = %d"%(Z,Z),"8-sinf (atom tuzilishi)",0,'picture')
    elif k=='oxide':
        if val==1: ox='A2O'
        elif val==2: ox='AO'
        elif val==3: ox='A2O3'
        else: ox={4:'AO2',5:'A2O5',6:'AO3',7:'A2O7'}[val]
        allo=['A2O','AO','A2O3','AO2','A2O5','AO3','A2O7']; ws=[o for o in allo if o!=ox]; r.shuffle(ws)
        q=Q("Rasmda A elementi atomining modeli tasvirlangan. Uning eng yuqori oksidi formulasini aniqlang.\n\n%s"%head,ox,ws[:3],"Valentlik = tashqi qavatdagi elektronlar = %d → %s"%(val,ox),"8-sinf (oksidlar)",'picture')
    elif k=='hyd':
        h={4:'AH4',5:'AH3',6:'H2A',7:'HA'}[val]; allh=['AH4','AH3','H2A','HA','AH']; ws=[x for x in allh if x!=h]; r.shuffle(ws)
        q=Q("Rasmda tasvirlangan A elementi metallmas. Uning vodorodli birikmasining formulasini aniqlang.\n\n%s"%head,h,ws[:3],"Vodorod bo'yicha valentlik = 8 − %d"%val,"8-sinf (vodorodli birikmalar)",'picture')
    elif k=='ecount':
        q=numq("Rasmdagi atomning tashqi (oxirgi) qavatida nechta elektron joylashgan?\n\n%s"%head,val,[val+1,val-1 if val>1 else val+3,val+2,per],"Tashqi qavatdagi elektronlar: %d"%val,"8-sinf (atom tuzilishi)",0,'picture')
    else:
        met=(val<=3 and Z>2 and not (Z in (5,)))
        q=Q("Rasmda tasvirlangan A elementi haqida qaysi fikr to'g'ri?\n\n%s"%head,("Metall, oksidi asosli yoki amfoter xossali" if met else "Metallmas, oksidi kislotali xossali"),(["Metallmas, oksidi asosli xossali","Metall, oksidi kislotali xossali","Inert gaz, birikmalar hosil qilmaydi"] if met else ["Metall, oksidi asosli xossali","Metall, vodorodli birikma hosil qilmaydi","Inert gaz, birikmalar hosil qilmaydi"]),"Tashqi qavatda %d e⁻ (davr %d): %s"%(val,per,"metall" if met else "metallmas"),"8-sinf (metallar va metallmaslar)",'picture')
    q.kind='picture'; return q
# =================================================================== yangi grafiklar
def g_gasv(r,tag):
    Vmax=r.choice([60,80,100,120,50]); k=r.choice([0.35,0.45,0.3]); t1,t2=r.choice([(0,2),(2,4),(0,4),(1,3)])
    f=lambda t:Vmax*(1-math.exp(-k*t))
    v1=round(f(t1)); v2=round(f(t2)); tt=np.linspace(0,8,200)
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(tt,[f(x) for x in tt],'b')
    for x,y in ((t1,v1),(t2,v2)): ax.plot(x,y,'ro',ms=4); ax.plot([x,x],[0,y],'k:',lw=.8); ax.plot([0,x],[y,y],'k:',lw=.8)
    ax.set_xlabel('vaqt, min'); ax.set_ylabel('V(H₂), ml (n.sh.)'); ax.set_xticks(sorted({0,t1,t2,8})); ax.set_yticks(sorted({0,v1,v2,Vmax})); ax.grid(alpha=.25); ax.set_xlim(0,8); ax.set_ylim(0,Vmax*1.08)
    name=_save(fig,'gv_%s.png'%tag); img="![Grafik: gaz hajmi](%s)"%name
    me=r.choice([('Zn',65),('Mg',24),('Fe',56)]); head="Kislotada %s bo'lagi eritilganda ajralgan vodorod hajmining vaqtga bog'liqligi grafikda berilgan.\n\n%s\n\n"%(me[0],img)
    ask=r.choice(['rate','mass','n'])
    dv=v2-v1
    if ask=='rate': q=numq(head+"%d-minutdan %d-minutgacha vodorod ajralishining o'rtacha tezligini (ml/min) hisoblang."%(t1,t2),dv/(t2-t1),[dv,(dv/(t2-t1))*2,v2/(t2-t1),dv/2],"Δ V = %d − %d = %d ml; v = %d/%d = %s"%(v2,v1,dv,dv,t2-t1,fmt(dv/(t2-t1),2)),"Tirkashev VI bob (reaksiya tezligi, grafik)",2)
    elif ask=='mass':
        m=v2/22400*me[1]; q=numq(head+"%d-minutgacha reaksiyaga kirishgan %s massasini (mg) hisoblang (1 mol gaz = 22400 ml)."%(t2,me[0]),m*1000,[m*500,m*2000,m*1000/2*3,v1/22400*me[1]*1000],"n(H2) = %d/22400 = %s mol; m = n·%d = %s g = %s mg"%(v2,fmt(v2/22400,5),me[1],fmt(m,4),fmt(m*1000,1)),"Tirkashev VI bob (reaksiya tezligi, grafik)",1)
    else: q=numq(head+"%d-minutda ajralgan vodorodning miqdorini (mmol) toping (1 mmol gaz = 22,4 ml)."%t2,v2/22.4,[v2/22.4*2,v2/22.4/2,v2,v1/22.4],"n = %d/22,4 = %s mmol"%(v2,fmt(v2/22.4,2)),"Tirkashev VI bob (reaksiya tezligi, grafik)",2)
    q.kind='graph'; return q
def g_titr(r,tag):
    for _ in range(50):
        ca=r.choice([0.1,0.05,0.2]); Va=r.choice([20,25,10]); cb=r.choice([0.1,0.2,0.05])
        Veq=ca*Va/cb
        if abs(Veq-round(Veq))<1e-9 and 5<=Veq<=40: break
    V=np.linspace(0,Veq*1.6,300); pH=[]
    for v in V:
        na=ca*Va; nb=cb*v; tot=(Va+v)
        if abs(na-nb)<1e-12: pH.append(7)
        elif na>nb: pH.append(-math.log10((na-nb)/tot))
        else: pH.append(14+math.log10((nb-na)/tot))
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(V,pH,'b'); ax.axvline(Veq,ls=':',c='k',lw=.8); ax.axhline(7,ls=':',c='gray',lw=.8)
    ax.set_xlabel('V(NaOH), ml'); ax.set_ylabel('pH'); ax.set_xticks(sorted({0,round(Veq),round(Veq*1.6)})); ax.set_yticks(range(0,15,2)); ax.grid(alpha=.25)
    name=_save(fig,'ti_%s.png'%tag); img="![Grafik: titrlash](%s)"%name
    head="%d ml HCl eritmasi %s mol/l li NaOH eritmasi bilan titrlandi. Titrlash egri chizig'i grafikda berilgan (ekvivalent nuqta %d ml da).\n\n%s\n\n"%(Va,fmt(cb),Veq,img)
    ask=r.choice(['c','m','ph'])
    if ask=='c': q=numq(head+"Dastlabki HCl eritmasining konsentratsiyasini (mol/l) aniqlang.",ca,[ca*2,ca/2,cb,Veq/Va],"c(HCl)·%d = %s·%d → c = %s"%(Va,fmt(cb),Veq,fmt(ca)),"Tirkashev V bob (pH, neytrallash, grafik)",None)
    elif ask=='m': q=numq(head+"Ekvivalent nuqtagacha sarflangan NaOH ning massasini (g) hisoblang.",cb*Veq/1000*40,[cb*Veq*40,cb*Veq/1000*40*2,ca*Va/1000*36.5,cb*Veq/1000],"n(NaOH) = %s·%d/1000 = %s mol; m = %s g"%(fmt(cb),Veq,fmt(cb*Veq/1000,4),fmt(cb*Veq/1000*40,3)),"Tirkashev V bob (neytrallash, grafik)",3)
    else: q=numq(head+"Grafikning boshlang'ich nuqtasi (V = 0) pH ining qiymatiga mos keluvchi HCl eritmasidagi H⁺ konsentratsiyasini (mol/l) toping.",ca,[ca*10,ca/10,ca*2,ca/2],"[H⁺] = c(HCl) = %s mol/l (pH = %s)"%(fmt(ca),fmt(-math.log10(ca),2)),"Tirkashev V bob (pH, grafik)",None)
    q.kind='graph'; return q
def g_ppt(r,tag):
    for _ in range(100):
        n=r.choice([0.01,0.02,0.025,0.04,0.05]); c=r.choice([0.5,1,0.25,0.2,0.1]); Vb=n/c*1000
        if Vb<=400: break
    m=n*233; Vs=np.linspace(0,Vb*1.7,200); ms=[min(v*c/1000*233,m) for v in Vs]
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(Vs,ms,'b'); ax.axvline(Vb,ls=':',c='k',lw=.8)
    ax.set_xlabel('V(BaCl₂ eritmasi), ml'); ax.set_ylabel('m(cho\'kma), g'); ax.set_xticks(sorted({0,round(Vb),round(Vb*1.7)})); ax.set_yticks(sorted({0,round(m,2)})); ax.grid(alpha=.25); ax.set_ylim(0,m*1.15)
    name=_save(fig,'pp_%s.png'%tag); img="![Grafik: cho'kma massasi](%s)"%name
    head="Na2SO4 eritmasiga %s mol/l li BaCl2 eritmasi oz-ozdan qo'shilganda hosil bo'lgan cho'kma massasining qo'shilgan hajmga bog'liqligi grafikda keltirilgan.\n\n%s\n\n"%(fmt(c),img)
    ask=r.choice(['salt','n','c'])
    if ask=='salt': q=numq(head+"Dastlabki eritmadagi Na2SO4 ning massasini (g) hisoblang.",n*142,[n*233,n*208,n*142*2,m/2],"n(BaSO4) = %s/233 = %s mol = n(Na2SO4); m = %s g"%(fmt(m,2),fmt(n,3),fmt(n*142,2)),"Tirkashev V bob (almashinish reaksiyalari, grafik)",2)
    elif ask=='n': q=numq(head+"Eritmada nechta mol sulfat ioni bo'lgan?",n,[n*2,n/2,m/233*2,n*10],"n(SO4²⁻) = n(BaSO4) = %s/233 = %s mol"%(fmt(m,2),fmt(n,3)),"Tirkashev V bob (almashinish reaksiyalari, grafik)",3)
    else: q=numq(head+"Grafikdagi cho'kma massasi %s g da to'xtagan. Egri chiziq to'xtagan nuqtagacha qo'shilgan BaCl2 ning massasini (g) toping."%fmt(m,2),n*208,[n*233,n*142,n*208*2,n*208/2],"n(BaCl2) = n(BaSO4) = %s mol; m = %s g"%(fmt(n,3),fmt(n*208,2)),"Tirkashev V bob (almashinish reaksiyalari, grafik)",2)
    q.kind='graph'; return q
def g_hyd(r,tag):
    H=r.choice([('CuSO4·5H2O',[250,214,178,160],'CuSO4'),('Na2CO3·10H2O',[286,124,106],'Na2CO3')]); Ms=H[1]; m0=r.choice([25,28.6,50]) if H[0].startswith('Na2') else r.choice([25,50,12.5])
    n=m0/Ms[0]; masses=[n*x for x in Ms]
    fig,ax=plt.subplots(figsize=(5,3.2)); T=[20]
    xs=[0];ys=[masses[0]]
    for i in range(1,len(masses)):
        xs+= [i*100,i*100+1,i*100+60]; ys+=[masses[i-1],masses[i],masses[i]]
    ax.plot(xs,ys,'b'); ax.set_xlabel('harorat, °C'); ax.set_ylabel('namuna massasi, g'); ax.set_yticks(sorted({round(x,2) for x in masses})); ax.set_xticks([]); ax.grid(alpha=.25); ax.set_ylim(0,masses[0]*1.1)
    name=_save(fig,'hy_%s.png'%tag); img="![Grafik: qizdirish](%s)"%name
    head="%s kristallogidrat namunasi (%s g) bosqichma-bosqich qizdirilganda uning massasi o'zgarishi grafikda keltirilgan.\n\n%s\n\n"%(H[0],fmt(m0,2),img)
    ask=r.choice(['step1','final','water'])
    if ask=='step1':
        w=(Ms[0]-Ms[1])/18; q=numq(head+"1-bosqichda 1 mol kristallogidratdan necha mol suv ajraladi?",w,[w+1,w-1 if w>1 else w+2,w*2,Ms[1]/18],"Δm = %s − %s = %s g/mol → %s mol H2O"%(fmt(Ms[0]),fmt(Ms[1]),fmt(Ms[0]-Ms[1]),fmt(w)),"7-sinf (kristallogidratlar)",0)
    elif ask=='final': q=numq(head+"To'liq suvsizlangandan keyin qolgan %s ning massasini (g) toping."%H[2],masses[-1],[masses[0]-masses[-1],masses[-2],masses[-1]*2,masses[-1]/2],"%s mol · %s = %s g"%(fmt(n,4),fmt(Ms[-1]),fmt(masses[-1],2)),"7-sinf (kristallogidratlar)",2)
    else: q=numq(head+"Qizdirish natijasida ajralgan suvning umumiy massasini (g) hisoblang.",masses[0]-masses[-1],[masses[-1],masses[0],(masses[0]-masses[-1])*2,(masses[0]-masses[-1])/2],"Δm = %s − %s = %s g"%(fmt(masses[0],2),fmt(masses[-1],2),fmt(masses[0]-masses[-1],2)),"7-sinf (kristallogidratlar)",2)
    q.kind='graph'; return q
def g_vant(r,tag):
    g=r.choice([2,3,4]); v0=r.choice([1,2,0.5,3]); T=[20,30,40,50,60]; vs=[v0*g**i for i in range(5)]
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.bar([str(t) for t in T],vs,color='#4a7fc1'); ax.set_xlabel('harorat, °C'); ax.set_ylabel('reaksiya tezligi, mol/(l·min)')
    for i,v in enumerate(vs): ax.text(i,v,fmt(v),ha='center',va='bottom',fontsize=8)
    ax.set_yticks([])
    name=_save(fig,'vh_%s.png'%tag); img="![Diagramma: tezlik va harorat](%s)"%name
    head="Reaksiya tezligining haroratga bog'liqligi diagrammada ko'rsatilgan.\n\n%s\n\n"%img
    ask=r.choice(['gamma','v70','dT'])
    if ask=='gamma': q=numq(head+"Reaksiyaning temperatura koeffitsiyentini (γ) aniqlang.",g,[g+1,g-1 if g>2 else g+2,g*2,vs[1]],"γ = v(30)/v(20) = %s/%s = %d"%(fmt(vs[1]),fmt(vs[0]),g),"Tirkashev VI bob (Vant-Goff qoidasi, grafik)",0)
    elif ask=='v70': q=numq(head+"Diagrammadagi qonuniyat 70 °C gacha davom etsa, shu haroratdagi tezlik (mol/(l·min)) necha bo'ladi?",vs[0]*g**5,[vs[0]*g**4,vs[0]*g**6,vs[0]*g**5/g,vs[0]*5*g],"v = %s·%d⁵ = %s"%(fmt(vs[0]),g,fmt(vs[0]*g**5)),"Tirkashev VI bob (Vant-Goff qoidasi, grafik)",None)
    else:
        k=r.choice([2,3,4]); q=numq(head+"Haroratni 20 °C dan %d °C gacha ko'tarilganda tezlik necha marta ortadi?"%(20+10*k),g**k,[g*k,g**(k+1),g**k/2,k**g],"%d^%d = %d marta"%(g,k,g**k),"Tirkashev VI bob (Vant-Goff qoidasi, grafik)",0)
    q.kind='graph'; return q
def g_far(r,tag):
    me=r.choice([('Cu',64,2),('Ag',108,1),('Zn',65,2),('Ni',59,2)]) if False else r.choice([('Cu',64,2),('Ag',108,1)])
    I=r.choice([2,5,10,4]); tt=np.linspace(0,1800,50); mf=lambda t:I*t*me[1]/(me[2]*96500)
    T1=r.choice([600,900,1200,1800]); m1=mf(T1)
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(tt,[mf(x) for x in tt],'b'); ax.plot(T1,m1,'ro'); ax.plot([T1,T1],[0,m1],'k:',lw=.8); ax.plot([0,T1],[m1,m1],'k:',lw=.8)
    ax.set_xlabel('vaqt, s'); ax.set_ylabel('katodda ajralgan metall massasi, g'); ax.set_xticks([0,T1,1800]); ax.set_yticks([0,round(m1,3)]); ax.grid(alpha=.25)
    name=_save(fig,'fa_%s.png'%tag); img="![Grafik: elektroliz](%s)"%name
    head="Doimiy tok kuchida %s tuzining eritmasi elektroliz qilinganda katodda ajralgan metall massasining vaqtga bog'liqligi grafikda berilgan (M(%s) = %d g/mol, valentlik %d).\n\n%s\n\n"%(me[0],me[0],me[1],me[2],img)
    ask=r.choice(['I','m2','t'])
    if ask=='I': q=numq(head+"Elektroliz vaqtida tok kuchini (A) aniqlang (F = 96500 C/mol).",I,[I*2,I/2,I+1,m1*96500/T1],"I = m·z·F/(M·t) = %s·%d·96500/(%d·%d) = %d A"%(fmt(m1,3),me[2],me[1],T1,I),"11-sinf (Faradey qonuni, grafik)",None)
    elif ask=='m2': q=numq(head+"Xuddi shu sharoitda 1800 s da ajralgan metall massasini (g) toping.",mf(1800),[mf(1800)*2,mf(1800)/2,m1*2,mf(1800)+m1],"m ∝ t: m = %s·1800/%d = %s g"%(fmt(m1,3),T1,fmt(mf(1800),3)),"11-sinf (Faradey qonuni, grafik)",3)
    else: q=numq(head+"Grafikdagi nuqtaga mos kelgan jarayonda elektrodlardan o'tgan zaryad miqdorini (C) hisoblang.",I*T1,[I*T1*2,I*T1/2,m1*96500,I*T1/96500],"Q = I·t = %d·%d = %d C"%(I,T1,I*T1),"11-sinf (Faradey qonuni, grafik)",None)
    q.kind='graph'; return q
def g_ie(r,tag):
    val=r.choice([1,2,3,4,5]); base=r.choice([5,7,9,12]); vals=[]
    cur=base
    for i in range(1,7):
        cur=cur*r.choice([1.5,1.7,1.9]) if i>1 else cur
        if i==val+1: cur*=r.choice([4,5,6])
        vals.append(round(cur,1))
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.bar(['I₁','I₂','I₃','I₄','I₅','I₆'],vals,color='#c1704a'); ax.set_ylabel('ionlanish energiyasi, eV'); ax.grid(axis='y',alpha=.25)
    name=_save(fig,'ie_%s.png'%tag); img="![Diagramma: ionlanish energiyalari](%s)"%name
    head="A elementi atomining ketma-ket ionlanish energiyalari diagrammada berilgan.\n\n%s\n\n"%img
    ask=r.choice(['val','grp','ox'])
    grpn=['IA','IIA','IIIA','IVA','VA'][val-1]
    if ask=='val': q=numq(head+"A atomining tashqi qavatidagi elektronlar sonini aniqlang.",val,[val+1,val-1 if val>1 else val+3,val+2,6-val],"Energiya keskin ortgan joy: I%d → I%d, demak %d valent elektron"%(val,val+1,val),"8-sinf (ionlanish energiyasi, grafik)",0)
    elif ask=='grp': q=Q(head+"A elementi davriy jadvalning qaysi guruhida joylashgan?",grpn+" guruh",[g+" guruh" for g in ['IA','IIA','IIIA','IVA','VA','VIA'] if g!=grpn][:3],"Valent elektronlar %d ta → %s guruh"%(val,grpn),"8-sinf (ionlanish energiyasi, grafik)",'graph')
    else:
        ox={1:'A2O',2:'AO',3:'A2O3',4:'AO2',5:'A2O5'}[val]; ws=[o for o in ['A2O','AO','A2O3','AO2','A2O5','AO3'] if o!=ox][:3]
        q=Q(head+"A elementining eng yuqori oksidi formulasini toping.",ox,ws,"Valentlik %d → %s"%(val,ox),"8-sinf (ionlanish energiyasi, grafik)",'graph')
    q.kind='graph'; return q
GRAPHS2=[g_gasv,g_titr,g_ppt,g_hyd,g_vant,g_far,g_ie]
PICS2=[p_struct,p_struct,p_struct,p_atom,p_atom,p_atom]
