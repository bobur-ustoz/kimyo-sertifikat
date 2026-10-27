import re,sys,os
K='/Users/macbook/kimyo-sertifikat/kitob/'
OUT=K+'tex/'
os.makedirs(OUT,exist_ok=True)
# ------------------------------------------------------------------ matn -> LaTeX
SUPM=dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻','0123456789+-')); SUBM=dict(zip('₀₁₂₃₄₅₆₇₈₉','0123456789'))
GREEK={'α':'\\alpha','β':'\\beta','γ':'\\gamma','σ':'\\sigma','π':'\\pi','ω':'\\omega','η':'\\eta','Δ':'\\Delta','φ':'\\varphi','λ':'\\lambda','μ':'\\mu','ρ':'\\rho','ν':'\\nu','Σ':'\\Sigma','θ':'\\theta'}
def esc(s):
    s=s.replace('\\','\x00BS\x00')
    for a,b in [('&','\\&'),('%','\\%'),('#','\\#'),('_','\\_'),('{','\\{'),('}','\\}'),('$','\\$'),('~','\\textasciitilde{}'),('^','\\textasciicircum{}')]: s=s.replace(a,b)
    return s.replace('\x00BS\x00','\\textbackslash{}')
def chem(s):
    # eskirgan: faqat matn rejimida ishlaydi; s allaqachon escape qilingan
    s=re.sub(r'N\\_A',r'N\\textsubscript{A}',s)
    s=re.sub('[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+',lambda m:'\\textsuperscript{%s}'%''.join(SUPM[c] for c in m.group(0)).replace('-','$-$'),s)
    s=re.sub('[₀₁₂₃₄₅₆₇₈₉]+',lambda m:'\\textsubscript{%s}'%''.join(SUBM[c] for c in m.group(0)),s)
    # formulalardagi raqamlar -> pastki indeks (bosh harf yoki ")" dan keyin kelgan raqamlar)
    def sub_tok(m):
        lead,t=m.group(1),m.group(2)
        if not re.search(r'[A-Z]',t) or re.fullmatch(r'[A-Za-z]{1,2}',t): return lead+t
        return lead+re.sub(r'(?<=[A-Za-z\)\]])(\d+)',lambda x:'\\textsubscript{%s}'%x.group(1),t)
    s=re.sub(r'(?<![A-Za-z0-9\\{,])(\d{0,2})([A-Z\(][A-Za-z0-9\(\)\[\]]*[A-Za-z0-9\)])',sub_tok,s)
    s=re.sub(r'\bsp(\d)\b',r'sp\\textsuperscript{\1}',s)
    return s
UMAP=[('⇄','$\\rightleftarrows$'),('⇌','$\\rightleftarrows$'),('⇆','$\\rightleftarrows$'),('→','$\\to$'),('←','$\\leftarrow$'),('↑','$\\uparrow$'),('↓','$\\downarrow$'),('≈','$\\approx$'),('≥','$\\geq$'),('≤','$\\leq$'),('·','$\\cdot$'),('×','$\\times$'),('−','$-$'),('—','---'),('–','--'),('°C','\\textdegree{}C'),('°','\\textdegree{}'),('½','$\\frac{1}{2}$'),('’',"'"),('‘','`'),('“','``'),('”',"''"),('Δ','$\\Delta$'),('∑','$\\Sigma$'),('√','$\\surd$'),('≠','$\\neq$'),('⁰',''),('§','\\S{}'),('№','No.'),('«',"``"),('»',"''"),('≡','$\\equiv$'),('…','\\ldots{}'),('∝','$\\propto$'),('⇔','$\\Leftrightarrow$'),('●','$\\bullet$')]
def conv(s,math_ok=True):
    s=s.replace('\u00a0',' ')
    _R={v:k for k,v in SUPM.items()}
    s=re.sub(r'\^(\d*[+\-])',lambda m:''.join(_R[c] for c in m.group(1)),s)
    s=re.sub(r'\^\(([^)]*)\)',lambda m:'\x06'+m.group(1)+'\x07',s)
    s=re.sub(r'\^(-?\d+)',lambda m:'\x06'+m.group(1)+'\x07',s)
    s=re.sub(r'(\d)\s*%',r'\1%',s)
    s=esc(s)
    s=re.sub(r"([oOgG])'",r"\1`",s)
    s=chem(s)
    for a,b in UMAP: s=s.replace(a,b)
    for a,b in GREEK.items(): s=s.replace(a,'$%s$'%b)
    s=re.sub(r'\b([XYZUV])\b(?![a-z])',r'\\textit{\1}',s)
    s=re.sub(r'(\d)\s*\\%',r'\1\\%',s)
    # qolgan ASCII bo'lmagan belgilarni olib tashlash
    s=re.sub('\x06(.*?)\x07',lambda m:'\\textsuperscript{%s}'%m.group(1),s)
    s=re.sub(r'[^\x00-\x7f]','?',s)
    return s
def bold_task(s):
    """savoldagi asosiy talab qismini qalin qilish"""
    verbs=r"(?:hisoblang|aniqlang|toping|belgilang|ko'rsating|tanlang|nomlang|tenglang|yozing)"
    m=None
    for mm in re.finditer(r"(\S*ni(?:\s\([^)]*\))?\s%s[.?]?)"%verbs,s): m=mm
    if not m:
        for mm in re.finditer(r"(%s[.?]?)"%verbs,s): m=mm
    out=s
    if m: out=s[:m.start()]+'\x01'+m.group(1)+'\x02'+s[m.end():]
    out=re.sub(r"(to'g'ri bo'lmagan|noto'g'ri)",lambda x:'\x01'+x.group(1)+'\x02',out)
    return out
def inline(s,bold=False,ital=False,boldtask=False):
    """**qalin** belgilarini ham qayta ishlaydi"""
    if boldtask: s=bold_task(s)
    parts=re.split(r'(\*\*[^*]+\*\*|\x01[^\x02]*\x02)',s); out=''
    for p in parts:
        if not p: continue
        if p.startswith('**'): out+='\\textbf{%s}'%conv(p[2:-2])
        elif p.startswith('\x01'): out+='\\textbf{%s}'%conv(p[1:-1])
        else: out+=conv(p)
    # —reagent→ sxemalari
    out=re.sub(r'---(.*?)\$\\to\$',lambda m:'$\\xrightarrow{\\text{%s}}$'%m.group(1).strip(),out)
    if ital: out='\\textsl{%s}'%out
    return out
# ------------------------------------------------------------------ jadval va rasm
def table_tex(lines,full,fit=False):
    rows=[[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if not re.match(r'^\|[-| :]+\|$',l.strip())]
    n=len(rows[0]); spec='|'+'c|'*n
    t='\\begin{center}\n\\renewcommand{\\arraystretch}{1.15}\n'+('\\fitbox{' if fit else '')+'\\begin{tabular}{%s}\\hline\n'%spec
    for i,r in enumerate(rows):
        cells=[('\\textbf{%s}'%conv(c)) if i==0 else conv(c) for c in r]
        t+=' & '.join(cells)+' \\\\ \\hline\n'
    return t+'\\end{tabular}'+('}' if fit else '')+'\n\\end{center}\n'
def para_tex(text,boldtask=False):
    out=''; buf=[]; tb=[]
    def flush():
        nonlocal out,buf,tb
        if buf: out+=inline(' '.join(buf),boldtask=boldtask)+'\n'; buf=[]
        if tb: out+=table_tex(tb,False); tb=[]
    for l in text.split('\n'):
        if l.strip().startswith('|'): 
            if buf: out+=inline(' '.join(buf),boldtask=boldtask)+'\n'; buf=[]
            tb.append(l)
        elif not l.strip():
            flush()
        else:
            if tb: out+=table_tex(tb,False); tb=[]
            buf.append(l.strip())
    flush(); return out
def img_tex(path,width):
    return '\\begin{center}\\includegraphics[width=%s]{%s}\\end{center}\n'%(width,path)
def is_wide(lines):
    rows=[[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if not re.match(r'^\|[-| :]+\|$',l.strip())]
    return len(rows[0])>=5 or max(len(c) for r in rows for c in r)>22
# ------------------------------------------------------------------ parslash
def parse(md):
    q=md[:md.index('# JAVOBLAR')] if '# JAVOBLAR' in md else md
    ans=md[md.index('# JAVOBLAR'):]
    return q,ans
def blocks(text):
    d={}
    for m in re.finditer(r'\*\*(\d+)\.\*\*\s*(.*?)(?=\n\*\*\d+(?:–\d+)?\.\*\*|\n### |\n## |\Z)',text,re.S): d[int(m.group(1))]=m.group(2).strip()
    return d
def split_opts(body,n=4):
    lines=body.split('\n'); stem=[];opts=[]
    i=0
    while i<len(lines):
        l=lines[i]
        if re.match(r'^[A-F]\) ',l): break
        stem.append(l); i+=1
    rest=' '.join(lines[i:])
    parts=re.split(r'\s{2,}(?=[A-F]\) )|\s(?=[B-F]\) )',rest.strip())
    parts=[p.strip() for p in parts if p.strip()]
    return '\n'.join(stem).strip(),[re.sub(r'^[A-F]\) ','',p) for p in parts]
def render_q(n,body,opts_n=4):
    stem,opts=split_opts(body)
    flows=[];  # (kind,content)
    paras=re.split(r'\n\s*\n',stem); tex=''
    full=False
    for p in paras:
        lines=[l for l in p.split('\n') if l.strip()]
        if not lines: continue
        if lines[0].startswith('|'):
            tex+=table_tex(lines,False,fit=True); continue
        m=re.match(r'!\[[^\]]*\]\(([^)]+)\)',lines[0])
        if m: tex+=img_tex(m.group(1),'0.86\\linewidth'); continue
        txt=' '.join(lines)
        txt=re.sub(r'!\[[^\]]*\]\(([^)]+)\)',lambda x:'\x03%s\x03'%x.group(1),txt)
        if '\x03' in txt:
            a,pth,b=txt.split('\x03')[:3]; tex+=inline(a,boldtask=False)+'\n'+img_tex(pth,'0.86\\linewidth')+inline(b,boldtask=True)+'\n'
        else: tex+=inline(txt,boldtask=True)+'\n'
    head='\\noindent\\qn{%d.} '%n
    # birinchi matn paragrafi bilan birga
    tex=head+tex
    # variantlar
    L=['A)','B)','C)','D)','E)','F)']
    if opts:
        o=[inline(x,ital=True) for x in opts]
        mx=max(len(re.sub(r'[\\${}]','',x)) for x in o)
        if len(opts)<=4 and max(len(x) for x in opts)<=9:
            row=' \\hfill '.join('%s~%s'%(L[i],o[i]) for i in range(len(o)))
            tex+='\n\\noindent '+row+'\\par\n'
        elif len(opts)<=4 and max(len(x) for x in opts)<=22:
            tex+='\n\\noindent\\begin{tabular}{@{}p{0.47\\linewidth}@{}p{0.47\\linewidth}@{}}\n'
            for i in range(0,len(o),2):
                tex+='%s~%s & %s~%s \\\\\n'%(L[i],o[i],L[i+1],o[i+1] if i+1<len(o) else '')
            tex+='\\end{tabular}\\par\n'
        else:
            for i in range(len(o)): tex+='\\noindent %s~%s\\par\n'%(L[i],o[i])
    return tex+'\\qsep\n',full
# ------------------------------------------------------------------ preambula
PRE=r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{textcomp}
\usepackage[left=1.8cm,right=1.8cm,top=3.0cm,bottom=2.2cm,headheight=36pt,headsep=12pt]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{fancyhdr}\usepackage{tikz}
\usepackage{graphicx}
\usepackage{array}
\usepackage{amsmath,amssymb}
\usepackage{setspace}
\usepackage{longtable}
\graphicspath{{../}}
\definecolor{ygreen}{RGB}{46,139,87}\definecolor{dgreen}{RGB}{28,90,56}
\renewcommand{\normalsize}{\fontsize{10.9}{13.4}\selectfont}
\renewcommand{\familydefault}{\rmdefault}
\setlength{\parindent}{0pt}
\setlength{\columnsep}{0.8cm}
\setlength{\columnseprule}{0.4pt}
\setlength{\multicolsep}{3pt plus 1pt minus 1pt}
\renewcommand{\textsubscript}[1]{\ensuremath{_{\text{\fontsize{8}{8}\selectfont #1}}}}
\renewcommand{\textsuperscript}[1]{\ensuremath{^{\text{\fontsize{8}{8}\selectfont #1}}}}
\newcommand{\qn}[1]{\textbf{\fontsize{11.5}{13}\selectfont #1}}
\newcommand{\qsep}{\par\vspace{13pt}}
\newcommand{\fwrule}{\par\vspace{5pt}\noindent\rule{\linewidth}{1.4pt}\par\vspace{7pt}}
\newsavebox{\fitb}
\newcommand{\fitbox}[1]{\sbox{\fitb}{#1}\ifdim\wd\fitb>\linewidth\resizebox{\linewidth}{!}{\usebox{\fitb}}\else\usebox{\fitb}\fi}
\newcommand{\diqqat}[1]{\par\smallskip\noindent\textbf{Diqqat!} #1\par\medskip}
\newcommand{\javob}{\par\nopagebreak[4]\smallskip\noindent\textbf{Javob:} \rule[-2pt]{7.5cm}{0.4pt}\par\smallskip\noindent\textbf{Diqqat!} Javobingizni javoblar varaqasiga ko`chirib yozing.\par\medskip}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{1.6pt}\renewcommand{\headrule}{{\color{ygreen}\hrule height 1.6pt width\headwidth}}
\newcommand{\hdrlogo}{\begin{tikzpicture}[baseline=0pt]\fill[ygreen,rounded corners=3pt] (0,0) rectangle (0.95,0.95);\node[white,font=\fontsize{24}{26}\bfseries\selectfont] at (0.475,0.47){K};\node[anchor=west,font=\fontsize{16}{18}\bfseries\selectfont,text=dgreen] at (1.15,0.66){KIMYO};\node[anchor=west,font=\footnotesize\scshape,text=gray] at (1.15,0.2){Milliy sertifikat\ \ 2026};\end{tikzpicture}}
\newcommand{\hdrpill}[1]{\begin{tikzpicture}[baseline=0pt]\node[fill=ygreen,text=white,rounded corners=8pt,inner xsep=10pt,inner ysep=5pt,font=\fontsize{13}{15}\bfseries\selectfont] at (0,0.475){#1};\end{tikzpicture}}
\fancyhead[L]{\hdrlogo}
\fancyhead[R]{\hdrpill{VARIANT-VAR}}

\fancyfoot[C]{\thepage}
\fancypagestyle{first}{\fancyhf{}\renewcommand{\headrulewidth}{1.6pt}\renewcommand{\headrule}{{\color{ygreen}\hrule height 1.6pt width\headwidth}}\fancyhead[L]{\hdrlogo}\fancyhead[R]{\hdrpill{VARIANT-VAR}}\fancyfoot[C]{\thepage}}
\begin{document}
\normalsize
'''
def title(vn):
    return r'''\thispagestyle{first}
\noindent\textit{Davriy jadvaldan foydalanish mumkin.}
\par\smallskip
'''
# ------------------------------------------------------------------ variant
def build(vn,path):
    md=open(path,encoding='utf8').read(); q,ans=parse(md)
    p1=q[q.index('## I QISM'):q.index('## II QISM')]
    p2=q[q.index('## II QISM'):q.index('## III QISM')]
    p3=q[q.index('## III QISM'):q.index('## IV QISM')]
    p4=q[q.index('## IV QISM'):]
    B1=blocks(p1)
    tex=PRE.replace('VARIANT-VAR','%s-variant'%vn)+title(vn)
    tex+='\\begin{multicols}{2}\n'
    for n in range(1,33):
        t,full=render_q(n,B1[n])
        if False: tex+='\\end{multicols}\n\\fwrule\n'+t.replace('\\qsep\n','')+'\\fwrule\n\\begin{multicols}{2}\n'
        else: tex+=t
    tex+='\\end{multicols}\n'
    # 33–35 ramka
    m=re.search(r'\*\*33–35\.\*\* [^\n]*\n(.*?)\n\n\*\*33\.\*\* (.*?)\n\*\*34\.\*\* (.*?)\n\*\*35\.\*\* (.*?)\n\n(A\).*?)\n',p2,re.S)
    story=m.group(1).strip(); qs=[m.group(2).strip(),m.group(3).strip(),m.group(4).strip()]
    opts=[re.sub(r'^[A-F]\) ','',x) for x in re.split(r'\s{2,}(?=[A-F]\) )',m.group(5).strip())]
    optcol='\\\\[3pt]\n'.join('%s~%s'%('ABCDEF'[i],inline(o,ital=True)) for i,o in enumerate(opts))
    tex+='\\medskip\n\\noindent\\setlength{\\fboxsep}{0pt}\\fbox{\\begin{tabular}{p{0.74\\linewidth}|p{0.2\\linewidth}}\n'
    tex+='\\parbox[t]{0.72\\linewidth}{\\vspace{3pt}\\textbf{Topshiriqlar (33--35) va javob variant (A--F)larini o`zaro to`g`ri moslashtiring.} '+para_tex(story)+'\\vspace{3pt}} & \\multirow{1}{*}{}'
    tex=tex.replace(' & \\multirow{1}{*}{}',' & \\parbox[t]{0.19\\linewidth}{\\vspace{3pt}%s}'%optcol)
    tex+='\\\\ \\hline\n'
    for i,x in enumerate(qs):
        tex+='\\parbox[t]{0.72\\linewidth}{\\vspace{2pt}\\textbf{%d. %s}\\vspace{2pt}} & \\\\ \\hline\n'%(33+i,inline(x))
    tex=tex.rstrip()
    tex=re.sub(r'\\\\ \\hline\n?$','',tex)
    tex+='\n\\end{tabular}}\n\\par\\bigskip\n'
    # 36–40
    B3=blocks(p3)
    for n in range(36,41):
        body=B3[n]; body=re.sub(r'\n?---\s*$','',body).strip()
        paras=re.split(r'\n\s*\n',body); tt='\\noindent\\qn{%d.} '%n
        for pr in paras:
            ls=[l for l in pr.split('\n') if l.strip()]
            if ls and ls[0].startswith('|'): tt+=table_tex(ls,True)
            else: tt+=inline(' '.join(ls),boldtask=True)+'\n'
        tex+=tt+'\\javob\\qsep\n'
    # 41–43
    tex+='\\par\\bigskip\\begin{center}\\textbf{\\fontsize{13}{15}\\selectfont YOZMA ISH}\\end{center}\n'
    ins=r'\textbf{Topshiriqni bajarish jarayonida barcha reaksiya tenglamalarini yozing. Miqdoriy va arifmetik hisoblashlarni (unga asos bo`lgan usul yoki formulani ko`rsatgan holda) uzviy ketma-ketlikda bajaring.}'
    for num in (41,42,43):
        mm=re.search(r'### %d-topshiriq[^\n]*\n(.*?)(?=\n### |\Z)'%num,p4,re.S)
        lines=[l for l in mm.group(1).split('\n') if l.strip() and not re.match(r'^-{3,}$',l.strip())]
        stm=[l for l in lines if not re.match(r'^\d\) ',l)]; bnd=[l for l in lines if re.match(r'^\d\) ',l)]
        tex+='\\noindent\\qn{%d.} '%num
        if num!=42: tex+=ins+'\\par\\smallskip\n'
        i_=0
        while i_<len(stm):
            l=stm[i_]
            if l.strip().startswith('|'):
                run=[]
                while i_<len(stm) and stm[i_].strip().startswith('|'): run.append(stm[i_]); i_+=1
                tex+=table_tex(run,False); continue
            i_+=1
            if re.search(r'---|—[^—]*→',l) and num==42 and len(l)>20 and ('—' in l):
                s=l; s=re.sub(r'—([^—→]*)→',lambda x:'\x04%s\x05'%x.group(1).strip(),s)
                segs=re.split(r'(\x04[^\x05]*\x05)',s); disp=''
                for sg in segs:
                    if sg.startswith('\x04'): disp+='\\xrightarrow{\\text{%s}}'%conv(sg[1:-1])
                    elif sg.strip(): disp+='\\text{%s}'%conv(sg.strip())
                tex+='\\[\\setlength{\\fboxsep}{0pt}%s\\]\n'%disp
            else: tex+=inline(l)+'\\par\n'
        for l in bnd:
            k=int(l[0]); body=l[3:]
            if num==42:
                s=re.sub(r'—([^—→]*)→',lambda x:'\x04%s\x05'%x.group(1).strip(),body)
                segs=re.split(r'(\x04[^\x05]*\x05)',s); disp=''
                for sg in segs:
                    if sg.startswith('\x04'): disp+='$\\xrightarrow{\\text{%s}}$'%conv(sg[1:-1])
                    else: disp+=conv(sg)
                tex+='\\noindent %d)\\ %s\\par\n'%(k,disp)
            else: tex+='\\noindent %d)\\ %s\\par\n'%(k,inline(body))
        tex+='\\diqqat{Mazkur topshiriq kengaytirilgan javobni talab etib, uning yechilish usuli va shu usul asosidagi barcha hisoblash amallari javoblar varaqasida aks etishi lozim.}\\qsep\n'
    # ---------------- javoblar kaliti
    tex+='\\newpage\n\\noindent\\textbf{\\fontsize{13}{15}\\selectfont %s-variant}\\hfill \\textbf{Javoblar kaliti}\\par\\smallskip\\hrule\\smallskip\n\\textit{Faqat o`qituvchi uchun.}\\par\\medskip\n'%vn
    keys={}
    for m in re.finditer(r'\|\s*((?:\d+\s*\|\s*)+)\n\|[-| ]+\|\n\|\s*((?:[A-D]\s*\|\s*)+)',ans):
        ns=[int(x) for x in re.findall(r'\d+',m.group(1))]; ks=re.findall(r'[A-D]',m.group(2)); keys.update(dict(zip(ns,ks)))
    k3=re.search(r'33 → \*\*(\w)\*\* \(([^)]*)\); 34 → \*\*(\w)\*\* \(([^)]*)\); 35 → \*\*(\w)\*\* \(([^)]*)\)',ans)
    k5=re.search(r'36 → \*\*([^*]*)\*\*; 37 → \*\*([^*]*)\*\*; 38 → \*\*([^*]*)\*\*; 39 → \*\*([^*]*)\*\*; 40 → \*\*([^*]*)\*\*',ans)
    tex+='\\noindent\\textbf{1--32-savollar}\\par\\smallskip\n\\noindent\\begin{tabular}{|'+'c|'*16+'}\\hline\n'
    for lo in (1,17):
        tex+=' & '.join('\\textbf{%d}'%n for n in range(lo,lo+16))+'\\\\\\hline\n'+' & '.join('\\textsl{%s}'%keys.get(n,'?') for n in range(lo,lo+16))+'\\\\\\hline\n'
    tex+='\\end{tabular}\\par\\medskip\n'
    if k3:
        tex+='\\noindent\\textbf{33--35-savollar}\\par\\smallskip\n\\noindent\\begin{tabular}{|c|c|c|}\\hline \\textbf{No} & \\textbf{Javob} & \\textbf{Qiymat}\\\\\\hline\n'
        for i,n in enumerate((33,34,35)): tex+='%d & \\textsl{%s} & %s\\\\\\hline\n'%(n,k3.group(1+2*i),conv(k3.group(2+2*i)))
        tex+='\\end{tabular}\\par\\medskip\n'
    if k5:
        tex+='\\noindent\\textbf{36--40-savollar}\\par\\smallskip\n\\noindent\\begin{tabular}{|c|c|}\\hline \\textbf{No} & \\textbf{To`g`ri javob}\\\\\\hline\n'
        for i,n in enumerate(range(36,41)): tex+='%d & %s\\\\\\hline\n'%(n,conv(k5.group(1+i)))
        tex+='\\end{tabular}\\par\\medskip\n'
    tex+='\\noindent\\textbf{41--43-topshiriqlar: javoblar}\\par\\smallskip\n'
    for num in (41,42,43):
        mm=re.search(r'## %d-topshiriq — yechim[^\n]*\n(.*?)(?=\n---|\n## |\Z)'%num,ans,re.S)
        tex+='\\noindent\\textbf{%d-topshiriq.}\\par\n'%num
        lines=[l for l in mm.group(1).strip().split('\n') if l.strip()]
        if num==42:
            for l in lines:
                if l.startswith(('Jami','Baholash')): continue
                tex+='\\noindent '+inline(l)+'\\par\n'
        else:
            items={}
            for l in lines:
                m2=re.match(r'\*\*(\d)-band[^*]*\*\*\s*(.*)',l)
                if not m2: continue
                body=m2.group(2); bolds=re.findall(r'\*\*([^*]+)\*\*',body)
                items[int(m2.group(1))]='; '.join(bolds) if bolds else body[:120]
            for k in sorted(items): tex+='\\noindent %d) %s\\par\n'%(k,conv(items[k]))
    # mavzular taqsimoti
    rows=re.findall(r'^\| (\d+) \| ([^|]+) \| ([A-D]) \| (.*?) \| ([^|]+) \|$',ans,re.M)
    skill={'hisob':"Hisoblash va masala yechish",'nazariy':"Bilim va tushunish",'grafik':"Grafik tahlili",'jadval':"Jadval tahlili",'rasm':"Rasm bo`yicha tahlil"}
    if rows:
        tex+='\\par\\bigskip\\noindent\\textbf{Mavzular taqsimoti}\\par\\smallskip\n{\\small\\noindent\\begin{longtable}{|c|p{7.2cm}|p{5.4cm}|c|}\\hline \\textbf{No} & \\textbf{Mavzu} & \\textbf{Tekshiriladigan ko`nikma} & \\textbf{Ball}\\\\\\hline\n'
        for n,tur,jv,yech,man in rows:
            tex+='%s & %s & %s & 1\\\\\\hline\n'%(n,conv(man.strip()),skill.get(tur.strip(),conv(tur)))
        tex+='33--35 & Aralash masala (moslashtirish) & Ko`p bosqichli hisob & 3\\\\\\hline\n36--40 & Qisqa javobli masalalar & Hisoblash & 5\\\\\\hline\n41--43 & Yozma ish & Usul va hisob (M, A) & 75\\\\\\hline\n\\end{longtable}}\n'
    tex+='\\end{document}\n'
    return tex
if __name__=='__main__':
    which=[int(x) for x in sys.argv[1:]] or list(range(1,21))
    for v in which:
        p=K+'gen/out_variant_%02d.md'%v
        t=build(str(v),p)
        open(OUT+'Kimyo_MS_%02d_variant.tex'%v,'w',encoding='utf8').write(t)
        # sintaksis tekshiruvi: figurali qavslar muvozanati
        depth=0
        for ch in re.sub(r'\\[{}]','',t):
            depth+= (ch=='{')-(ch=='}')
            if depth<0: break
        print(v,len(t),'qavs balansi:',depth, 'ASCII emas:',len(re.findall(r'[^\x00-\x7f]',t)))
