import re,glob,statistics
def cx(t): return len(re.findall(r'[=→]',t))+0.5*len(re.findall(r'\d+[,.]?\d*',t))/10
res={n:[] for n in range(36,41)}; qlen={n:[] for n in range(36,41)}
for f in sorted(glob.glob('gen/out_variant_*.md')):
    md=open(f,encoding='utf8').read(); ans=md[md.index('# JAVOBLAR'):]
    a=ans[ans.index('## 36–40'):]; a=a[:a.index('\n---')]
    for m in re.finditer(r'\*\*(\d+)\.\*\* (.*)',a): res[int(m.group(1))].append(cx(m.group(2)))
    q=md[md.index('## III QISM'):md.index('## IV QISM')]
    for m in re.finditer(r'\*\*(\d+)\.\*\* (.*)',q): qlen[int(m.group(1))].append(len(m.group(2)))
for n in res: print(n,'yechim',round(statistics.mean(res[n]),2),'matn uzunligi',round(statistics.mean(qlen[n])))
print('jami yechim',round(sum(statistics.mean(v) for v in res.values()),2))
