# Generates starter villager textures. Run from anywhere.
from PIL import Image, ImageDraw
import os

SKIN=(217,169,122,255); SKIN_D=(185,133,88,255); EYE=(45,107,58,255); BROW=(58,42,26,255)
RED=(179,32,42,255); BLACK=(28,28,34,255); WHITE=(244,239,226,255); GOLD=(224,165,38,255)
GREEN=(45,107,58,255); NAVY=(34,48,74,255); DKRED=(122,31,31,255); GREY=(205,198,184,255)

def faces(u,v,w,h,d):
    return {'top':(u+d,v,w,d),'bottom':(u+d+w,v,w,d),'right':(u,v+d,d,h),
            'front':(u+d,v+d,w,h),'left':(u+d+w,v+d,d,h),'back':(u+2*d+w,v+d,w,h)}

def R(dr,x,y,w,h,c):
    dr.rectangle([x,y,x+w-1,y+h-1],fill=c)

def fill_box(dr,box,c,which=None):
    for k,(x,y,w,h) in faces(*box).items():
        if which is None or k in which: R(dr,x,y,w,h,c)

HEAD=(0,0,8,10,8); HAT=(32,0,8,10,8); BODY=(16,20,8,12,6); JACKET=(0,38,8,20,6)
ARM=(44,22,4,8,4); ARM2=(40,38,8,4,4); LEG=(0,22,4,12,4)
NOSE=(24,0,2,4,2)

def make_type():
    im=Image.new('RGBA',(64,64),(0,0,0,0)); dr=ImageDraw.Draw(im)
    fill_box(dr,HEAD,SKIN)
    fx,fy,fw,fh=faces(*HEAD)['front']
    R(dr,fx+1,fy+3,2,1,BROW); R(dr,fx+5,fy+3,2,1,BROW)
    R(dr,fx+1,fy+4,2,1,WHITE); R(dr,fx+5,fy+4,2,1,WHITE)
    R(dr,fx+2,fy+4,1,1,EYE); R(dr,fx+5,fy+4,1,1,EYE)
    R(dr,fx+2,fy+8,4,1,BROW)
    fill_box(dr,NOSE,SKIN_D)
    fill_box(dr,BODY,WHITE)
    bx,by,bw,bh=faces(*BODY)['front']
    R(dr,bx+3,by,2,3,GOLD)
    fill_box(dr,ARM,WHITE)
    for k,(x,y,w,h) in faces(*ARM).items():
        if k in('front','back','left','right'): R(dr,x,y+h-2,w,1,GOLD)
    fill_box(dr,ARM2,WHITE)
    for k in('left','right'):
        x,y,w,h=faces(*ARM2)[k]; R(dr,x,y,w,h,SKIN)
    fill_box(dr,LEG,NAVY)
    for k in('front','back','left','right'):
        x,y,w,h=faces(*LEG)[k]; R(dr,x,y+h-3,w,3,WHITE); R(dr,x,y+h-4,w,1,RED)
    return im

def make_farmer():
    im=Image.new('RGBA',(64,64),(0,0,0,0)); dr=ImageDraw.Draw(im)
    for k,(x,y,w,h) in faces(*HAT).items():
        if k=='top': R(dr,x,y,w,h,BLACK)
        elif k!='bottom':
            R(dr,x,y,w,3,BLACK); R(dr,x,y+3,w,1,DKRED)
    for k,(x,y,w,h) in faces(*JACKET).items():
        if k in('top','bottom'):
            R(dr,x,y,w,h,BLACK if k=='bottom' else WHITE); continue
        R(dr,x,y,w,h,BLACK)
        R(dr,x,y,w,2,WHITE)
        R(dr,x,y+11,w,2,RED)
        for i in range(0,w,2): R(dr,x+i,y+11,1,1,GOLD)
        R(dr,x,y+h-2,w,1,GOLD); R(dr,x,y+h-1,w,1,RED)
        if k=='front':
            R(dr,x+2,y+13,4,5,RED)
            R(dr,x+2,y+14,4,1,WHITE); R(dr,x+2,y+16,4,1,BLACK)
            R(dr,x+3,y+15,2,1,GOLD)
            R(dr,x+3,y+2,2,1,GOLD)
    for k,(x,y,w,h) in faces(*ARM2).items():
        if k in('front','back','top','bottom'):
            R(dr,x,y,w,h,WHITE)
            if k in('front','back'):
                for i in range(0,w,2): R(dr,x+i,y+h-1,1,1,RED)
        else:
            R(dr,x,y,w,h,SKIN)
    return im


ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
base=os.path.join(ROOT,'resourcepack','assets','minecraft','textures','entity','villager')
os.makedirs(os.path.join(base,'type'),exist_ok=True)
os.makedirs(os.path.join(base,'profession'),exist_ok=True)
t=make_type(); f=make_farmer()
t.save(os.path.join(base,'type','plains.png'))
f.save(os.path.join(base,'profession','farmer.png'))
S=8
sheet=Image.new('RGBA',(64*S*2+24,64*S),(40,40,46,255))
bg=Image.new('RGBA',(64*S,64*S),(70,70,78,255))
for i,im in enumerate((t,f)):
    sheet.paste(bg,(i*(64*S+24),0))
    sheet.alpha_composite(im.resize((64*S,64*S),Image.NEAREST),(i*(64*S+24),0))
os.makedirs(os.path.join(ROOT,'docs'),exist_ok=True)
sheet.save(os.path.join(ROOT,'docs','preview_plains_farmer.png'))
print('textures written')
