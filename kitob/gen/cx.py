import re,statistics,glob,sys
def parts(md):
    a=md.index('# JAVOBLAR')
    ans=md[a:]
    s3=ans[ans.index('## 33–35'):ans.index('## 36–40')]
    def top(n):
        m=re.search(r'## %d-topshiriq — yechim.*?\n(.*?)(?=\n---|\Z)'%n,ans,re.S); return m.group(1)
    return s3,top(41),top(43)
def cx(t): return len(re.findall(r'[=→]',t))+0.5*len(re.findall(r'\d+[,.]?\d*',t))/10
res={'33–35':[], '41':[], '43':[], 'bands43':[], 'bands41':[]}
for f in sorted(glob.glob('gen/out_variant_*.md')):
    md=open(f,encoding='utf8').read(); s3,a,b=parts(md)
    res['33–35'].append(cx(s3)); res['41'].append(cx(a)); res['43'].append(cx(b))
    res['bands41'].append(len(re.findall(r'\*\*\d-band',a))); res['bands43'].append(len(re.findall(r'\*\*\d-band',b)))
for k,v in res.items(): print(k,round(statistics.mean(v),2))
