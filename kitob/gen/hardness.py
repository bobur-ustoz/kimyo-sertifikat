import re
def diff(s,q):
    n=len(re.findall(r'\d+[,.]?\d*',s)); L=len(s)
    th = not re.search(r'hisoblang|aniqlang|toping|nechaga|necha|qancha|massasini|hajmini|miqdorini|sonini',s,re.I) or (n<=1 and L<140 and not re.search(r'g\b|mol|l\b|%',s))
    if re.search(r'o‘zgarishlar asosida',s): return 'qiyin'
    if th: return 'oson'
    if L>=260 or n>=6 or (L>=200 and re.search(r'aralashma|ketma-ket|unum|ekvimolar|teng ikki|bir qismi|ma’lum qismi|1/\d|\d/\d',s)): return 'qiyin'
    if L<130 and n<=3: return 'oson'
    return 'o‘rta'
AP=str.maketrans({"'":'‘','’':'‘','ʻ':'‘','`':'‘','´':'‘'})
def level(text):
    s=re.sub(r'\s+',' ',text.translate(AP)).strip()
    return diff(s,{})
