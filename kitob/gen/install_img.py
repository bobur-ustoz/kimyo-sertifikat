import sys
from PIL import Image
import PIL.ImageChops as C
src,name=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB')
bb=C.difference(im,Image.new('RGB',im.size,(255,255,255))).point(lambda p:255 if p>25 else 0).getbbox()
m=40; bb=(max(bb[0]-m,0),max(bb[1]-m,0),min(bb[2]+m,im.width),min(bb[3]+m,im.height)); im=im.crop(bb)
im.thumbnail((1100,1100)); im.save('/Users/macbook/kimyo-sertifikat/kitob/rasmlar/darslik/%s.png'%name); print(name,im.size)
