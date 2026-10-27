import re
from PIL import Image,ImageDraw,ImageFont
FP='/System/Library/Fonts/Supplemental/Arial.ttf'
def formula(d,xy,text,size=44,fill='#222',anchor='l'):
    """Indekslarni (raqamlar) pastga tushirib yozadi. xy = chap-markaz (anchor='l') yoki o'ng-markaz ('r')."""
    F=ImageFont.truetype(FP,size); S=ImageFont.truetype(FP,int(size*0.62))
    parts=[]; prev=''
    for ch in text:
        parts.append((ch, ch.isdigit() and (prev.isalpha() or prev==')'))); prev=ch
    w=sum(d.textlength(c,font=S if s else F) for c,s in parts)
    x,y=xy
    if anchor=='r': x-=w
    for c,s in parts:
        if s: d.text((x,y+size*0.28),c,font=S,fill=fill,anchor='lm'); x+=d.textlength(c,font=S)
        else: d.text((x,y),c,font=F,fill=fill,anchor='lm'); x+=d.textlength(c,font=F)
    return w
def line(d,a,b,w=4,fill='#222'): d.line([a,b],fill=fill,width=w)
