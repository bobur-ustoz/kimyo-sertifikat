import re, random
from fractions import Fraction
AM={'H':1,'C':12,'N':14,'O':16,'F':19,'Na':23,'Mg':24,'Al':27,'Si':28,'P':31,'S':32,'Cl':35.5,'K':39,'Ca':40,'Cr':52,'Mn':55,'Fe':56,'Cu':64,'Zn':65,'Br':80,'Ag':108,'I':127,'Ba':137,'Pb':207,'Li':7,'Hg':201}
def parse(f):
    f=f.replace('·','.')
    def rec(s):
        i=0;cnt={}
        while i<len(s):
            if s[i]=='(':
                d=1;j=i+1
                while d:
                    d+= (s[j]=='(')-(s[j]==')'); j+=1
                inner=rec(s[i+1:j-1]); k=re.match(r'\d*',s[j:]).group(0); n=int(k) if k else 1; i=j+len(k)
                for e,c in inner.items(): cnt[e]=cnt.get(e,0)+c*n
            else:
                m=re.match(r'([A-Z][a-z]?)(\d*)',s[i:]); e=m.group(1); n=int(m.group(2)) if m.group(2) else 1
                cnt[e]=cnt.get(e,0)+n; i+=len(m.group(0))
        return cnt
    if '.' in f:
        tot={}
        for part in f.split('.'):
            m=re.match(r'(\d*)(.*)',part); k=int(m.group(1)) if m.group(1) else 1
            for e,c in rec(m.group(2)).items(): tot[e]=tot.get(e,0)+c*k
        return tot
    return rec(f)
def M(f): return sum(AM[e]*c for e,c in parse(f).items())
def balance(eq):
    L,R=eq.split('->'); strip=lambda s:re.sub(r'^\d+','',s.strip()); sp=[(strip(s),1) for s in L.split(' + ')]+[(strip(s),-1) for s in R.split(' + ')]
    els=sorted({e for s,_ in sp for e in parse(s)})
    rows=[[Fraction(sg*parse(s).get(e,0)) for s,sg in sp] for e in els]
    n=len(sp); piv=[];r=0
    for c in range(n):
        p=None
        for i in range(r,len(rows)):
            if rows[i][c]!=0: p=i;break
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        rows[r]=[x/rows[r][c] for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]!=0:
                f=rows[i][c]; rows[i]=[a-f*b for a,b in zip(rows[i],rows[r])]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]
    assert len(free)==1,eq
    fc=free[0]; v=[Fraction(0)]*n; v[fc]=Fraction(1)
    for i,c in enumerate(piv): v[c]=-rows[i][fc]
    from math import gcd
    den=1
    for x in v: den=den*x.denominator//gcd(den,x.denominator)
    iv=[int(x*den) for x in v]; g=0
    for x in iv: g=gcd(g,abs(x))
    iv=[x//g for x in iv]
    if iv[0]<0: iv=[-x for x in iv]
    assert all(x>0 for x in iv),eq
    return [(s,c) for (s,_),c in zip(sp,iv)]
def fmt(x,nd=None):
    if nd is None:
        s=('%.4f'%x).rstrip('0').rstrip('.')
    else:
        s='%.*f'%(nd,x)
        if nd>0 and '.' in s: s=s.rstrip('0').rstrip('.')
    return s.replace('.',',')
def sub(f):
    return f  # formulas stay plain; renderers add subscripts
class Q:
    def __init__(s,text,ans,dis,sol,src,kind='calc',tag=''):
        s.text=text;s.ans=ans;s.dis=dis;s.sol=sol;s.src=src;s.kind=kind;s.tag=tag
def numq(text,ans,wrongs,sol,src,nd=None,kind='calc',rng=None,unit=''):
    a=fmt(ans,nd)
    ws=[]
    for w in wrongs:
        t=fmt(round(w,3 if abs(w)<1 else 2),nd) if nd is None else fmt(w,nd)
        if t!=a and t not in ws and w>0: ws.append(t)
    k=1
    base=[ans*2,ans/2,ans*1.5,ans*0.75,ans+ (1 if ans>=5 else 0.1),ans*3,ans/3,ans*1.25]
    for b in base:
        if len(ws)>=3: break
        t=fmt(round(b,nd if nd is not None else 4),nd)
        if t!=a and t not in ws and b>0: ws.append(t)
    return Q(text,a,ws[:3],sol,src,kind)
def pick(rng,seq): return seq[rng.randrange(len(seq))]
