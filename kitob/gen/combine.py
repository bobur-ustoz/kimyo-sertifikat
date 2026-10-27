import re,os
K='/Users/macbook/kimyo-sertifikat/kitob/'
def read(p): return open(p,encoding='utf8').read()
src={}
for v in range(1,21): src[v]=K+'gen/out_variant_%02d.md'%v
kir=read(K+'KITOB_reja_va_kirish.md'); kir=kir[kir.index('# KIRISH (qoralama)'):].replace('# KIRISH (qoralama)','# KIRISH').replace('## Milliy sertifikat imtihoni haqida','## Milliy sertifikat imtihoni haqida')
out=['# MILLIY SERTIFIKAT. KIMYO\n\n**Nazariy va hisoblash topshiriqlari — 20 ta namunaviy variant**\n\nHar variant 43 topshiriqdan iborat. Barcha topshiriqlar 7–11-sinf darsliklari va rasmiy test spetsifikatsiyasi asosida tuzilgan.\n\n## Mundarija\n- Kirish\n- 1–20-variantlar (savollar)\n- Javoblar va yechimlar\n\n',kir,'\n']
ans=['# JAVOBLAR VA YECHIMLAR\n']
for v in range(1,21):
    md=read(src[v]); i=md.index('## I QISM'); j=md.index('# JAVOBLAR VA YECHIMLAR')
    q=md[i:j].strip().rstrip('-').strip(); a=md[j+len('# JAVOBLAR VA YECHIMLAR'):].strip()
    out.append('# VARIANT %d\n\n%s\n\n'%(v,q))
    a=re.sub(r'^## ','### ',a,flags=re.M)
    ans.append('## VARIANT %d\n\n%s\n\n'%(v,a))
txt=''.join(out)+''.join(ans)
txt=re.sub(r'\n---\n','\n',txt)
open(K+'Kimyo_MS_20_variant.md','w',encoding='utf8').write(txt); print(len(txt))
