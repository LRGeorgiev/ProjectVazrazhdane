# Generates starter villager textures for every vanilla profession.
# Run from anywhere:  python3 tools/gen_textures.py
# Needs Pillow:       pip install pillow
from PIL import Image, ImageDraw
import os

SKIN=(217,169,122,255); SKIN_D=(185,133,88,255); EYE=(45,107,58,255); BROW=(58,42,26,255)
RED=(179,32,42,255); BLACK=(28,28,34,255); WHITE=(244,239,226,255); GOLD=(224,165,38,255)
GREEN=(45,107,58,255); NAVY=(34,48,74,255); DKRED=(122,31,31,255)
def C(r,g,b): return (r,g,b,255)

def faces(u,v,w,h,d):
    return {'top':(u+d,v,w,d),'bottom':(u+d+w,v,w,d),'right':(u,v+d,d,h),
            'front':(u+d,v+d,w,h),'left':(u+d+w,v+d,d,h),'back':(u+2*d+w,v+d,w,h)}

def R(dr,x,y,w,h,c):
    dr.rectangle([x,y,x+w-1,y+h-1],fill=c)

def fill_box(dr,box,c,which=None):
    for k,(x,y,w,h) in faces(*box).items():
        if which is None or k in which: R(dr,x,y,w,h,c)

HEAD=(0,0,8,10,8); HAT=(32,0,8,10,8); BODY=(16,20,8,12,6); JACKET=(0,38,8,20,6)
ARM=(44,22,4,8,4); ARM2=(40,38,8,4,4); LEG=(0,22,4,12,4); NOSE=(24,0,2,4,2)

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

def make_profession(cfg):
    im=Image.new('RGBA',(64,64),(0,0,0,0)); dr=ImageDraw.Draw(im)
    hat=cfg.get('hat')
    if hat:
        for k,(x,y,w,h) in faces(*HAT).items():
            if k=='top': R(dr,x,y,w,h,hat['color'])
            elif k!='bottom':
                R(dr,x,y,w,hat['rows'],hat['color'])
                if hat.get('band'): R(dr,x,y+hat['rows'],w,1,hat['band'])
        if hat.get('feather'):
            x,y,w,h=faces(*HAT)['right']
            R(dr,x+2,y-1+1,1,3,hat['feather']); R(dr,x+3,y+1,1,2,hat['feather'])
    jc=cfg['jacket']; collar=cfg.get('collar',WHITE)
    for k,(x,y,w,h) in faces(*JACKET).items():
        if k=='top': R(dr,x,y,w,h,collar); continue
        if k=='bottom': R(dr,x,y,w,h,jc); continue
        R(dr,x,y,w,h,jc)
        R(dr,x,y,w,2,collar)
        if cfg.get('sash'):
            R(dr,x,y+11,w,2,cfg['sash'])
            for i in range(0,w,2): R(dr,x+i,y+11,1,1,GOLD)
        hem=cfg.get('hem',(GOLD,RED))
        R(dr,x,y+h-2,w,1,hem[0]); R(dr,x,y+h-1,w,1,hem[1])
        if cfg.get('wool'):
            for yy in range(3,11,2):
                for xx in range((yy//2)%2,w,2): R(dr,x+xx,y+yy,1,1,cfg['wool'])
        if k=='front':
            ap=cfg.get('apron')
            if ap:
                R(dr,x+2,y+13,4,5,ap)
                if cfg.get('stripes'):
                    R(dr,x+2,y+14,4,1,cfg['stripes'][0]); R(dr,x+2,y+16,4,1,cfg['stripes'][1])
                    R(dr,x+3,y+15,2,1,GOLD)
                for (px,py,pc) in cfg.get('apron_dots',[]): R(dr,x+px,y+py,1,1,pc)
            if cfg.get('cross'):
                R(dr,x+3,y+3,2,5,GOLD); R(dr,x+2,y+4,4,1,GOLD)
            if cfg.get('scroll'):
                R(dr,x+5,y+13,2,4,C(222,205,160)); R(dr,x+5,y+13,2,1,C(160,120,70))
    for k,(x,y,w,h) in faces(*ARM2).items():
        if k in('front','back','top','bottom'):
            R(dr,x,y,w,h,WHITE)
            if k in('front','back'):
                for i in range(0,w,2): R(dr,x+i,y+h-1,1,1,cfg.get('cuff',RED))
        else: R(dr,x,y,w,h,SKIN)
    return im

PROFS={
 'none':        dict(jacket=BLACK, sash=RED),
 'nitwit':      dict(jacket=GREEN, sash=GOLD, hem=(GOLD,GOLD)),
 'farmer':      dict(jacket=BLACK, sash=RED, apron=RED, stripes=(WHITE,BLACK),
                     hat=dict(color=BLACK,rows=3,band=DKRED)),
 'shepherd':    dict(jacket=C(205,198,184), wool=C(150,140,125), sash=C(110,75,45),
                     hem=(C(110,75,45),C(80,55,35)), cuff=C(110,75,45),
                     hat=dict(color=C(120,115,110),rows=4,band=None)),
 'cleric':      dict(jacket=BLACK, sash=GOLD, cross=True, hem=(GOLD,GOLD), cuff=GOLD,
                     hat=dict(color=BLACK,rows=4,band=None)),
 'armorer':     dict(jacket=BLACK, sash=C(90,60,35), apron=C(110,110,118),
                     apron_dots=[(2,14,C(190,190,200)),(5,14,C(190,190,200)),(3,16,C(190,190,200)),(4,16,C(190,190,200))],
                     hat=dict(color=C(95,95,105),rows=3,band=C(60,60,68))),
 'toolsmith':   dict(jacket=BLACK, sash=C(90,60,35), apron=C(125,85,50),
                     apron_dots=[(2,14,GOLD),(5,14,GOLD),(3,16,GOLD),(4,16,GOLD)],
                     hat=dict(color=C(80,55,35),rows=3,band=GOLD)),
 'weaponsmith': dict(jacket=BLACK, sash=C(90,60,35), apron=DKRED,
                     apron_dots=[(2,14,C(190,190,200)),(5,14,C(190,190,200)),(3,16,C(190,190,200)),(4,16,C(190,190,200))],
                     hat=dict(color=C(55,55,62),rows=3,band=C(120,120,128))),
 'butcher':     dict(jacket=BLACK, sash=RED, apron=WHITE,
                     apron_dots=[(2,15,RED),(4,14,RED),(5,17,RED),(3,17,DKRED)],
                     hat=dict(color=WHITE,rows=3,band=C(200,195,180))),
 'cartographer':dict(jacket=C(36,84,70), sash=GOLD, scroll=True, cuff=GOLD,
                     hat=dict(color=BLACK,rows=3,band=GOLD)),
 'fisherman':   dict(jacket=C(58,90,120), sash=WHITE, hem=(WHITE,C(40,60,95)), cuff=C(40,60,95),
                     hat=dict(color=C(40,60,95),rows=4,band=WHITE)),
 'fletcher':    dict(jacket=C(60,100,50), sash=RED,
                     hat=dict(color=BLACK,rows=3,band=RED,feather=RED)),
 'leatherworker':dict(jacket=BLACK, sash=C(90,60,35), apron=C(120,80,48),
                     apron_dots=[(2,13,GOLD),(3,13,GOLD),(4,13,GOLD),(5,13,GOLD)],
                     hat=dict(color=C(95,65,40),rows=3,band=C(70,48,30))),
 'librarian':   dict(jacket=NAVY, sash=GOLD, collar=WHITE, cuff=GOLD, hem=(GOLD,GOLD),
                     hat=dict(color=BLACK,rows=2,band=GOLD)),
 'mason':       dict(jacket=BLACK, sash=C(90,60,35), apron=C(170,170,170),
                     apron_dots=[(2,15,C(120,120,120)),(4,14,C(120,120,120)),(5,16,C(120,120,120)),(3,17,C(120,120,120))],
                     hat=dict(color=C(140,140,145),rows=3,band=C(100,100,105))),
}

ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
base=os.path.join(ROOT,'resourcepack','assets','minecraft','textures','entity','villager')
os.makedirs(os.path.join(base,'type'),exist_ok=True)
os.makedirs(os.path.join(base,'profession'),exist_ok=True)

t=make_type(); t.save(os.path.join(base,'type','plains.png'))
imgs={}
for name,cfg in PROFS.items():
    im=make_profession(cfg); imgs[name]=im
    im.save(os.path.join(base,'profession',name+'.png'))

# contact sheet: each profession over the plains type layer
S=3; cols=5; cell=64*S+8
rows=(len(imgs)+cols-1)//cols
sheet=Image.new('RGBA',(cols*cell,rows*(64*S+14)),(40,40,46,255))
d=ImageDraw.Draw(sheet)
for i,(name,im) in enumerate(imgs.items()):
    comp=Image.new('RGBA',(64,64),(70,70,78,255)); comp.alpha_composite(t); comp.alpha_composite(im)
    x=(i%cols)*cell; y=(i//cols)*(64*S+14)
    sheet.paste(comp.resize((64*S,64*S),Image.NEAREST),(x,y+12))
    d.text((x+2,y),name,fill=(230,230,230,255))
os.makedirs(os.path.join(ROOT,'docs'),exist_ok=True)
sheet.save(os.path.join(ROOT,'docs','preview_professions.png'))
os.remove(os.path.join(ROOT,'docs','preview_plains_farmer.png')) if os.path.exists(os.path.join(ROOT,'docs','preview_plains_farmer.png')) else None
print(len(imgs),'profession textures written')
