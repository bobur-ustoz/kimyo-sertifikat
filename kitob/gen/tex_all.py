import re,sys
sys.argv=[sys.argv[0]]
import tex_build as T
_o=r'\fancyhead[R]{\hdrpill{VARIANT-VAR}}'
pre=T.PRE.replace(_o,r'\newcommand{\curvar}{}'+r'\fancyhead[R]{\hdrpill{\curvar}}',1).replace(_o,r'\fancyhead[R]{\hdrpill{\curvar}}')
assert r'\curvar' in pre
qs=[];ks=[]
for v in range(1,21):
    t=T.build(str(v),T.K+'gen/out_variant_%02d.md'%v)
    a=t.index(r'\thispagestyle{first}'); b=t.index('\\newpage\n\\noindent\\textbf{\\fontsize{13}{15}\\selectfont %d-variant}'%v); c=t.rindex(r'\end{document}')
    qs.append(('\\newpage\n' if v>1 else '')+'\\renewcommand{\\curvar}{%d-variant}\n'%v+t[a:b])
    ks.append('\\renewcommand{\\curvar}{Javoblar}\n'+t[b:c])
sep=r'''\newpage\renewcommand{\curvar}{}\thispagestyle{first}
\vspace*{6cm}\begin{center}{\color{ygreen}\rule{0.6\linewidth}{1.6pt}}\\[14pt]{\fontsize{34}{38}\selectfont\bfseries JAVOBLAR}\\[10pt]{\large 1--20-variantlar javoblar kaliti}\\[14pt]{\color{ygreen}\rule{0.6\linewidth}{1.6pt}}\end{center}
'''
doc=pre+''.join(qs)+sep+''.join(ks)+'\\end{document}\n'
open(T.OUT+'Kimyo_MS_20_variant_bitta.tex','w',encoding='utf8').write(doc); print(len(doc))
