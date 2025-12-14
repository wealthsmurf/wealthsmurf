from numpy import polysub
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
app = Ursina()
window.borderless = False
window.color = color.black
camera.orthographic = True
camera.fov = 20

Text.default_font = 'SpoqaHanSansNeo_TTF_original\SpoqaHanSansNeo-Light.ttf'

ground = Entity(
    model='cube',
    texture='clown.png',
    color=color.gray,
    z=0.1,
    y=-8,
    scale=(1500,5,10),
    collider='box'
)

wall1 = Entity(
    model='cube', 
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(-3, 0),
    scale=(5, 1),
    air_time = 3
)
god = []
god_ball = Entity(
    model='cube', 
    texture='godst_ball.png',
    collider = 'box',
    color=color.white,
    position=(random.randint(-10, 10), -5),
    scale=(1)
)
god.append(god_ball)
bad = []
bad_ball = Entity(
    model='cube', 
    texture='bad_ball.png',
    collider = 'box',
    color=color.white,
    position=(random.randint(30, 50), -5),
    scale=(1)
)
bad.append(bad_ball)
player = PlatformerController2d(
    position=(-15, -5),
    texture='gost.png',
    color=color.white,
    scale=(1,1.5),
    max_jumps=2,
    gravity = 0.7,
    walk_speed = 8
)

troll = []
troll_ball = Entity(
    model='cube', 
    texture='troll_ball.png',
    collider = 'box',
    color=color.white,
    position=(random.randint(72, 74), -4),
    scale=(1)
)
troll.append(troll_ball)
speed = []
speed_ball = Entity(
    model='cube', 
    texture='speed_ball.png',
    collider = 'box',
    color=color.white,
    position=(random.randint(-10, 10), -4),
    scale=(1)
)
speed.append(speed_ball)
spiks1 = []

for i in range(10):
    spik1 = Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(-10, 10), -5),
        scale=1
    )
    spiks1.append(spik1)

wall2 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(13, 0),
    scale=(5, 1)
)
spiks2 = []

for i in range(10):
    spik2 = Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(10, 30), -5),
        scale=1
    )
    spiks2.append(spik2)




wall3 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(33, 0),
    scale=(5, 1)
)
spiks3 = []

for i in range(10):
    spik3 = Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(30, 50), -5),
        scale=1
    )
    spiks3.append(spik3)
wall4 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(53, 0),
    scale=(5, 1)
)
spiks4 = []

for i in range(10):
    spik4= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(50, 68), -5),
        scale=1
    )
    spiks4.append(spik4)
spiks0 = []

for i in range(500):
    spik0= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(76,300), -5),
        scale=1
    )
    spiks0.append(spik0)

    
stair = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (73,-5),
    scale=(3.4,1)
)
stair2 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (78,-4),
    scale=(3.4,1)
)
stair3 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (83,-3),
    scale=(3.4,1)
)
stair4 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (88,-2),
    scale=(3.4,1)
)
stair5 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (93,-1),
    scale=(3.4,1)
)
stair6 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (98,0),
    scale=(3.4,1)
)
stair7 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (103,1),
    scale=(3.4,1)
)
stair8 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (108,2),
    scale=(3.4,1)
)
stair9 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (113,3),
    scale=(3.4,1)
)
stair10 = Entity(
    model='cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (118,4),
    scale=(3.4,1)
)

load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (113,12),
    scale=(3.4,1)
)
spiks15 = []
for i in range(2):
    spik15= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(112, 114), 13),
        scale=1
    )
    spiks15.append(spik15)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (108,20),
    scale=(3.4,1)
)
spiks16 = []
for i in range(2):
    spik16= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(107, 109), 21),
        scale=1
    )
    spiks16.append(spik16)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (105,28),
    scale=(3.4,1)
)
spiks17 = []
for i in range(1):
    spik17= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(104, 106), 29),
        scale=1
    )
    spiks17.append(spik17)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (97,25),
    scale=(3.4,1)
)
spiks18 = []
for i in range(2):
    spik18= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(96, 98), 26),
        scale=1
    )
    spiks18.append(spik18)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (115,36),
    scale=(3.4,1)
)
spiks19 = []
for i in range(2):
    spik19= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(114, 116), 37),
        scale=1
    )
    spiks19.append(spik19)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (118,28),
    scale=(3.4,1)
)
spiks20 = []
for i in range(2):
    spik20= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(117, 119), 29),
        scale=1
    )
    spiks20.append(spik20)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (122,32),
    scale=(3.4,1)
)
spiks21 = []
for i in range(2):
    spik21= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(121, 123), 33),
        scale=1
    )
    spiks21.append(spik21)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (128,40),
    scale=(3.4,1)
)
spiks22 = []
for i in range(2):
    spik22= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(127, 129), 41),
        scale=1
    )
    spiks22.append(spik22)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (126,48),
    scale=(3.4,1)
)
spiks23 = []
for i in range(2):
    spik23= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(126, 128), 49),
        scale=1
    )
    spiks23.append(spik23)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (132,45),
    scale=(3.4,1)
)
spiks24 = []
for i in range(2):
    spik24= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(131, 133), 46),
        scale=1
    )
    spiks24.append(spik24)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (145,53),
    scale=(3.4,1)
)
spiks25 = []
for i in range(2):
    spik25= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(144, 146), 54),
        scale=1
    )
    spiks25.append(spik25)



spiks5 = []

for i in range(2):
    spik5= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(72, 74), -4),
        scale=1
    )
    spiks5.append(spik5)
spiks6 = []

for i in range(2):
    spik6= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(77, 79), -3),
        scale=1
    )
    spiks6.append(spik6)
spiks7 = []

for i in range(2):
    spik7= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(82, 84), -2),
        scale=1
    )
    spiks7.append(spik7)
spiks8 = []

for i in range(2):
    spik8= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(87, 89), -1),
        scale=1
    )
    spiks8.append(spik8)
spiks9 = []

for i in range(2):
    spik9= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(92, 94), 0),
        scale=1
    )
    spiks9.append(spik9)
spiks10 = []

for i in range(2):
    spik10= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(97, 99), 1),
        scale=1
    )
    spiks10.append(spik10)
spiks11 = []

for i in range(2):
    spik11= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(102, 104), 2),
        scale=1
    )
    spiks11.append(spik11)
spiks12 = []

for i in range(2):
    spik12= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(107, 109), 3),
        scale=1
    )
    spiks12.append(spik12)
spiks13 = []

for i in range(2):
    spik13= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(112, 114), 4),
        scale=1
    )
    spiks13.append(spik13)
spiks14= []

for i in range(2):
    spik14= Entity(
        model='cube',
        texture='spik.png',
        color=color.white,
        collider='box',
        position=(random.randint(117, 119), 5),
        scale=1
    )
    spiks14.append(spik14)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (148,49),
    scale=(3.4,1)
)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (157,49),
    scale=(3.4,1)
)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (165,53),
    scale=(3.4,1)
)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (170,49),
    scale=(3.4,1)
)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (173,57),
    scale=(3.4,1)
)
load = Entity(
    model = 'cube',
    texture = 'clown.png',
    color = color.white,
    collider='box',
    position = (180,57),
    scale=(3.4,1)
)
spiks26 = []
for i in range(2):
    spik26 = Entity(
        model = 'cube',
        texture = 'spik.png',
        color = color.white,
        collider='box',
        position = (random.randint(148,150),50),
        scale = 1
    )
    spiks26.append(spik26)
for i in range(2):
    spik26 = Entity(
        model = 'cube',
        texture = 'spik.png',
        color = color.white,
        collider='box',
        position = (random.randint(156,158),50),
        scale = 1
    )
    spiks26.append(spik26)
for i in range(2):
    spik26 = Entity(
        model = 'cube',
        texture = 'spik.png',
        color = color.white,
        collider='box',
        position = (random.randint(164,166),54),
        scale = 1
    )
    spiks26.append(spik26)
for i in range(2):
    spik26 = Entity(
        model = 'cube',
        texture = 'spik.png',
        color = color.white,
        collider='box',
        position = (random.randint(169,171),50),
        scale = 1
    )
for i in range(2):
    spik26 = Entity(
        model = 'cube',
        texture = 'spik.png',
        color = color.white,
        collider='box',
        position = (random.randint(172,174),58),
        scale = 1
    )
    spiks26.append(spik26)
for i in range(2):
    spik26 = Entity(
        model = 'cube',
        texture = 'spik.png',
        color = color.white,
        collider='box',
        position = (random.randint(179,181),58),
        scale = 1
    )
    spiks26.append(spik26)
points = []
spawn_point = Entity(
    model = 'cube',
    color=color.green,
    collider='box',
    position = (70,-5)
)
points.append(spawn_point)
end = []
endwall = Entity(
    model='cube',
    color=color.rgb(255,215,0),
    collider='box',
    position=(185,61),
    scale=(5,1)
)
end.append(endwall)

wall1 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(530, 0),
    scale=(5, 1),
    air_time = 3
)

wall1 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(520, 0),
    scale=(5, 1),
    air_time = 3
)
wall_1 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(540, 5),
    scale=(5, 1),
    air_time = 3
)

wall_1 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(530, 9),
    scale=(3.4, 1),
    air_time = 3
)
wall_1 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(540, 13),
    scale=(1, 3),
    air_time = 3
)

pointt = []
spawn_pointt = Entity(
    model = 'cube',
    color=color.green,
    collider='box',
    position = (535,21)
)
pointt.append(spawn_pointt)
wall_2 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(543, 21),
    scale=(1, 1),
    air_time = 3
)


wall_1 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(550, 22),
    scale=(0.5, 1),
    air_time = 3
)
wall_1 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(555, 25),
    scale=(0.5, 1),
    air_time = 3
)
wall_2 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(555, 33),
    scale=(0.5, 0.5),
    air_time = 3
)
point = []
spawn_poin = Entity(
    model = 'cube',
    color=color.green,
    collider='box',
    position = (565,38)
)
wall_2 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(560, 45),
    scale=(0.5, 0.5),
    air_time = 3
)
wall_2 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(565, 48),
    scale=(0.5, 0.5),
    air_time = 3
)
wall_2 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(573, 48),
    scale=(0.5, 0.5),
    air_time = 3
)
wall_2 = Entity(
    model='cube',
    texture='clown.png',
    color=color.white,
    collider='box',
    position=(583, 43),
    scale=(0.5, 0.5),
    air_time = 3
)
point.append(spawn_poin)
life = 24
rule = Text(text="가시를 네 번 밟을 때마다 게이지가 닳고 게이지가 전부 닳으면 죽습니다.",x=-0.04, y=0.49,scale =1, background=True)
L = 24
def hurt():
    global life
    life -= 1
def out():
    quit()
def next():
    global life
    L = life
def update():
    global life
    if life == 30:
        player.texture = 'godst.png'
    if life == 24:
        player.texture = 'gost.png'
        
    if life == 20:
        player.texture = 'gost2.png'
        
    if life == 16:
        player.texture = 'gost3.png'
        
    if life == 12:
        player.texture = 'gost4.png'
        
    if life == 8:
        player.texture = 'gost5.png'
        
    if life == 4:
        player.texture = 'gost6.png'
         
    if life == 0:
        player.texture = 'ghost.png'
    if life == 50:
        player.texture = 'ghost1.png'
        
    hit_info = player.intersects()
    if hit_info.entity in end:
        player.position = (520,-5)
        player.max_jumps = 2
        life = 24
    if hit_info.entity in spiks4: 
        player.position = (-15, -5)
        hurt()
    elif hit_info.entity in god:
        life = 30
        god_ball.collider = ' '
        god_ball.texture = 'black.png'
    elif hit_info.entity in bad:
        life = 4
        bad_ball.collider = ' '
        bad_ball.texture = 'black.png'
    elif hit_info.entity in troll:
        player.walk_speed = 4.5
        troll_ball.collider = ' '
        troll_ball.texture = 'black.png'
    elif hit_info.entity in speed:
        player.walk_speed = 10
        speed_ball.collider = ' '
        speed_ball.texture = 'black.png'
    elif hit_info.entity in spiks3: 
        player.position = (-15, -5)
        hurt()
        
    elif hit_info.entity in spiks2: 
        player.position = (-15, -5)
        hurt()
        
    elif hit_info.entity in spiks1: 
        player.position = (-15, -5)
        hurt()
        
    elif hit_info.entity in spiks5:
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks6: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks7: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks8: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks9: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks10: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks11: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks12: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks13: 
        player.position = (70, -4)
        hurt()
        
    elif hit_info.entity in spiks14: 
        player.position = (70, -4)
        hurt()
        
    if hit_info.entity in points:
        player.max_jumps = 3
    if hit_info.entity in pointt:
        player.max_jumps = 3
    if hit_info.entity in point:
        player.max_jumps = 2
    elif hit_info.entity in spiks0:
        player.position = (-15,-5)
        hurt()
        
        player.max_jumps = 2
    elif hit_info.entity in spiks15:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks16:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks17:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks18:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks19:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks20:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks21:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks22:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks23:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks24:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks25:
        player.position = (70,-4)
        hurt()
        
    elif hit_info.entity in spiks26:
        player.position = (70,-4)
        hurt()
    
    elif hit_info.entity in end:
        player.position = (520,-5)
        player.max_jumps = 2
        player.walk_speed = 8
        life = 50
        rule.text = " "
    '''elif hit_info.entity in end:
        player.position = (-1020, 500)
        player.gravity = 0.1
        Text(text="!!wlecom to HEAVEN!!",scale=3.5,color=color.yellow,background=True)
        window.color = color.white'''
    if life == 0:
        player.position = (-1020,500)
        player.gravity = 0.01
        window.color = color.black
        Text(text="멍청한녀석",scale=3,color=color.red,background=True)
        Text(text="24번이나 죽다니",scale = 2.5,y = 0.2,color = color.red,background=True)          
    





camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))
app.run()           
