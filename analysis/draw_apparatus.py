
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from html import escape
import math
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"figures"
OUT.mkdir(exist_ok=True)
W,H=1800,1640
im=Image.new("RGB",(W,H),"#f2f5f8"); d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',f'<rect width="{W}" height="{H}" fill="#f2f5f8"/>']
ink="#182b45"; blue="#2675b8"; orange="#d97b22"; green="#18876e"; gray="#8191a2"
fonts={}
def font(size):
    if size not in fonts: fonts[size]=ImageFont.truetype("C:/Windows/Fonts/msyh.ttc",size)
    return fonts[size]
def text(x,y,s,size=24,color=ink):
    d.text((x,y),s,font=font(size),fill=color)
    svg.append(f'<text x="{x}" y="{y+size}" font-family="Microsoft YaHei, sans-serif" font-size="{size}" fill="{color}">{escape(s)}</text>')
def line(pts,color=ink,width=3):
    d.line(pts,fill=color,width=width)
    coords=" ".join(f"{x},{y}" for x,y in pts)
    svg.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}"/>')
def rect(x,y,w,h,fill="#e1e8ef",stroke=ink):
    d.rectangle((x,y,x+w,y+h),fill=fill,outline=stroke,width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def circle(x,y,r,fill="white",stroke=ink):
    d.ellipse((x-r,y-r,x+r,y+r),fill=fill,outline=stroke,width=3)
    svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
def arrow(x1,y1,x2,y2,color=blue,width=4):
    line([(x1,y1),(x2,y2)],color,width)
    a=math.atan2(y2-y1,x2-x1)
    for t in [-0.5,0.5]:
        line([(x2,y2),(x2-14*math.cos(a+t),y2-14*math.sin(a+t))],color,width)
def spring(x1,y1,x2,y2,color=orange):
    dx=x2-x1;dy=y2-y1;l=math.hypot(dx,dy); ux=dx/l;uy=dy/l
    pts=[(x1,y1),(x1+dx*.1,y1+dy*.1)]
    for i in range(1,15):
        t=.1+.8*i/15; a=7*(-1)**i
        pts.append((x1+dx*t-uy*a,y1+dy*t+ux*a))
    pts.extend([(x1+dx*.9,y1+dy*.9),(x2,y2)])
    line(pts,color,3)
def panel(x,y,title):
    rect(x,y,850,450,"white","#ced8e2");text(x+20,y+12,title,28)
text(35,18,"粉笔虚线实验 · 双自由度机械握持器",38)
text(35,72,"水平板面｜轴心只升降，粉笔绕单轴转动｜设计示意，不按比例；2026-09-20",23)
panel(30,125,"A  侧视 X–z：运动与受力")
# side board
rect(75,494,670,20,"#344658")
text(90,522,"移动黑板＋载板",23)
arrow(575,545,735,545);text(585,517,"v →",22)
# fixed rail
rect(617,204,26,270,"#dae4ed")
rect(574,315,83,67,"#bfd9ed")
line([(590,204),(685,204),(685,474),(590,474)],gray,4)
spring(682,204,682,328);spring(682,370,682,474)
line([(657,328),(682,328)],blue,4);line([(657,370),(682,370)],blue,4)
text(703,252,"上簧",21,orange);text(703,411,"下簧",21,orange)
line([(575,348),(468,348)],blue,12)
circle(468,348,12,blue)
line([(455,361),(400,410)],green,27)
line([(400,410),(303,494)],"#c5b49c",16)
circle(303,492,5)
text(395,290,"P 固定X，可升降",22)
text(324,372,"可拆笔套",20,green)
text(199,415,"Q 尖端",22)
arrow(554,320,554,275);arrow(554,375,554,417)
text(597,169,"导轨",21,blue)
text(95,195,"竖直弹簧连：固定架 / 滑台",23,orange)
text(95,232,"转动弹簧连：滑台 / 转子（见D）",22)
line([(303,491),(393,491)],gray,2)
text(340,465,"θ",23)
arrow(100,465,100,382);text(105,374,"z",20)
arrow(100,465,175,465);text(180,454,"X",20)
panel(920,125,"B  正视 y–z：轴承与侧置立架")
rect(955,496,750,18,"#344658")
rect(978,209,38,273)
rect(996,325,66,65,"#bfd9ed")
line([(1060,355),(1170,355)],blue,9)
rect(1165,302,22,120,"#dae4ed")
rect(1335,302,22,120,"#dae4ed")
circle(1176,355,15,"#a8c7e2")
circle(1346,355,15,"#a8c7e2")
line([(1145,355),(1380,355)],ink,6)
rect(1243,337,40,37,"#b5dbc9")
line([(1263,374),(1263,493)],"#c5b49c",15)
text(1212,269,"两轴承跨距20–30 mm",23)
text(1398,332,"轴沿y",22)
text(1125,427,"夹头在两支撑之间",22)
text(945,531,"立架在板边，短横向连接避开运动路径",23)
arrow(1540,472,1660,472);text(1652,440,"y",22)
text(950,195,"固定立架",22)
text(1430,220,"光轴Ø3 mm",23)
text(1430,255,"F623ZZ ×2",23)
panel(30,605,"C  俯视 X–y：相机与移动路径")
rect(295,710,460,190,"#e6ecef")
text(520,718,"黑板移动区域",22)
line([(325,811),(718,811)],green,3)
text(513,836,"粉笔轨迹",22,green)
arrow(566,879,720,879);text(635,845,"v / X",22)
rect(418,669,73,29)
text(82,666,"立架/导轨在板侧",22)
line([(455,698),(455,784)],blue,9)
line([(455,784),(455,837)],ink,7)
line([(455,811),(348,811)],"#b4a793",12)
circle(455,811,7,green)
circle(348,811,6,green)
text(370,755,"粉笔",21)
rect(309,952,78,43,"#c8d5e1")
arrow(348,944,348,832,gray,3)
text(420,943,"相机沿y看X–z平面",22)
text(420,978,"转轴沿y；尖端在轴心左侧",22)
text(76,1020,"板下另装导向/滚轮；机架不随板运动",22)
panel(920,605,"D  转动回复：可调锚架随滑台升降")
# frame trapezoid
line([(1000,918),(1000,755),(1670,755),(1670,918)],blue,5)
text(1075,668,"蓝框固定在滑台；可调角后锁紧",23,blue)
# spring neutral point at center, top
spring(1040,782,1324,782)
spring(1324,782,1635,782)
circle(1040,782,7,blue);circle(1635,782,7,blue)
circle(1324,782,8,green)
line([(1324,782),(1324,900)],green,9)
circle(1324,900,16,green)
text(1270,925,"P转轴",23)
text(1348,832,"r",24)
text(1030,814,"B",23);text(1628,814,"C",23)
text(1309,738,"A",23)
text(1010,968,"对拉：一伸一缩。γ ≈ 2 k_s r²（小角估算）",23)
text(1005,1012,"工作点可预紧；两根弹簧全程保持拉紧",22,orange)
panel(30,1085,"E  可换粉笔夹：不用粘粉笔")
# section v block
rect(106,1207,235,100,"#e1c69c")
rect(106,1160,235,38,"#e1c69c")
rect(106,1198,235,9,"#89bfae")
rect(106,1230,235,9,"#89bfae")
line([(135,1219),(493,1219)],"#b4a793",21)
# bolts
line([(124,1139),(124,1324)],ink,5)
line([(320,1139),(320,1324)],ink,5)
rect(111,1145,27,12);rect(307,1145,27,12)
text(379,1143,"两颗螺钉对称夹紧",23)
text(380,1260,"粉笔伸出Lc",23)
text(83,1350,"替代结构：V槽木块＋薄橡胶＋蝶形螺母",23)
text(83,1392,"首选：旋紧笔套；两管夹固定笔套外壳",23,green)
text(83,1432,"换笔后重设L / Lc、θ0与N0，检查滑移",23)
text(83,1476,"侧面投影：螺钉在粉笔两侧，不穿过粉笔",21,gray)
panel(920,1085,"F  装配与标定顺序")
for i,s in enumerate([
"1  导轨＋滑台 → 先测寄生摩擦",
"2  两轴承＋转轴 → 确认可自由转动",
"3  装可拆笔夹 → 记录L、Lc与质量",
"4  上下簧 → 调竖直预紧并测k",
"5  转臂对拉簧 → 调预力矩并测γ",
"6  反复匹配N0和θ0 → 拍摄与测速",
"7  手拉复现通过 → 再装电机",
"实线：机械连接；橙色：弹簧；蓝色：导向"
]):
    text(948,1146+i*44,s,23,orange if i==7 else ink)
text(35,1560,"完整尺寸、购件词、500元分配和误差验收：实验装置设计.md  |  设计尚未实物验证",24)
svg.append("</svg>")
im.save(OUT/"机械握持器设计.png")
(OUT/"机械握持器设计.svg").write_text("\n".join(svg),encoding="utf-8")
print("Saved schematic PNG and SVG.")
