import re,collections,sys
def prep(p):
    p=re.sub(r'^\*\*\d+(?:–\d+)?\.\*\*\s*','',p)
    p=re.sub(r'\n\*\*3[345]\.\*\*','',p); p=re.sub(r'!\[[^\]]*\]\([^)]*\)','',p); p=re.split(r'\n\s*A\)',p)[0]
    p=re.sub(r'\d+(?:[.,]\d+)?','#',p.lower()); p=re.sub(r'[^a-z# ]',' ',p); p=re.sub(r'\s+',' ',p).strip()
    return p
def questions(path):
    md=open(path,encoding='utf8').read(); md=md[:md.index('# JAVOBLAR')]
    parts=re.split(r'\n(?=\*\*\d+(?:–\d+)?\.\*\* )',md)
    ps=[p for p in parts if re.match(r'\*\*\d',p)]
    out=[];i=0
    while i<len(ps):
        if ps[i].startswith('**33–35.**'): out.append(' '.join(ps[i:i+4])); i+=4
        else: out.append(ps[i]); i+=1
    return out
files={}
for v in range(1,21): files[v]='gen/out_variant_%02d.md'%v
cnt=collections.defaultdict(set);Q={}
for v,p in files.items():
    Q[v]=[(i,prep(q)) for i,q in enumerate(questions(p))]
    for i,q in Q[v]: cnt[q].add(v)
tot=sum(map(len,Q.values())); rep=sum(1 for v in Q for i,q in Q[v] if len(cnt[q])>1)
print('full stem',tot,rep,'%.1f%%'%(rep/tot*100))
byslot=collections.Counter(i for v in Q for i,q in Q[v] if len(cnt[q])>1)
print(sorted(byslot.items()))
c=collections.Counter({q:len(s) for q,s in cnt.items() if len(s)>1})
for q,n in c.most_common(int(sys.argv[1]) if len(sys.argv)>1 else 5): print(n,q[:100])
