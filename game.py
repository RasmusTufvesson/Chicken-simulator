import pygame
import random
import time
from datetime import datetime
#import sys

def di(inp: dict):
    return random.choice(list(inp))

def round_up(inp: float):
    l=str(inp).split('.')
    l=[int(l[0]), int(l[1])]
    if l[1]!=0:
        l[0]+=1
    return l[0]

random.dict_choice=di

dis_x=800
dis_y=600

mid_pos=[dis_x//2, dis_y//2]#round(dis_x/2)-round(dis_x/4), round(dis_y/2)-round(dis_y/4)]

background=(117, 149, 31)
white=(255, 255, 255)
black=(0, 0, 0)
red=(171, 17, 17)

#make the pygame window
pygame.init()
screen=pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption('Chicken-Simulator')
pygame.display.set_icon(pygame.image.load('art/icon.png'))

#setting up pygame things
clock=pygame.time.Clock()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=300)
pygame.mixer.init()
pygame.joystick.init()
js=[pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for j in range(len(js)):
    js[j].init()

#load everything that does not fit into any special group
textbox=pygame.image.load('art/textbox.png')
empty=pygame.image.load('art/empty.png')

#load sounds
crack_sound=pygame.mixer.Sound('sound/crack.wav')
chicken_sound=pygame.mixer.Sound('sound/chicken.wav')

#load chicken hats n' stuff
chicken_hats=(pygame.image.load('art/chick_wiz.png'), pygame.image.load('art/chick_hat.png'), pygame.image.load('art/chick_hat_2.png'), pygame.image.load('art/chick_tophat.png'), pygame.image.load('art/chick_head.png'), pygame.image.load('art/chick_mu.png'), pygame.image.load('art/chick_tophat_2.png'))

#load all the eggs
egg_1=pygame.image.load('art/egg_light.png')
egg_crack_2=(pygame.image.load('art/crack_l_1_egg_dark.png'), pygame.image.load('art/crack_l_2_egg_dark.png'), pygame.image.load('art/crack_l_3_egg_dark.png'), pygame.image.load('art/crack_l_4_egg_dark.png'), pygame.image.load('art/crack_l_5_egg_dark.png'))
egg_2=pygame.image.load('art/egg_dark.png')
egg_crack_1=(pygame.image.load('art/crack_r_1_egg_light.png'), pygame.image.load('art/crack_r_2_egg_light.png'), pygame.image.load('art/crack_r_3_egg_light.png'), pygame.image.load('art/crack_r_4_egg_light.png'), pygame.image.load('art/crack_r_5_egg_light.png'))
egg_gold=pygame.image.load('art/egg_golden.png')
egg_crack_gold=(pygame.image.load('art/crack_r_1_egg_golden.png'), pygame.image.load('art/crack_r_2_egg_golden.png'), pygame.image.load('art/crack_r_3_egg_golden.png'), pygame.image.load('art/crack_r_4_egg_golden.png'), pygame.image.load('art/crack_r_5_egg_golden.png'))

eggs={}

#load all the chickens
chicken_1_1=pygame.image.load('art/chicken_l_1.png')
chicken_1_2=pygame.image.load('art/chicken_l_2.png')
chicken_1_3=pygame.image.load('art/chicken_l_3.png')
chicken_1_4=pygame.image.load('art/chicken_l_4.png')
chicken_1_5=pygame.image.load('art/chicken_l_5.png')
chicken_1_6=pygame.image.load('art/chicken_l_6.png')
chicken_1_7=pygame.image.load('art/chicken_l_7.png')
chicken_1_8=pygame.image.load('art/chicken_l_8.png')
chicken_2_1=pygame.image.load('art/chicken_r_1.png')
chicken_2_2=pygame.image.load('art/chicken_r_2.png')
chicken_2_3=pygame.image.load('art/chicken_r_3.png')
chicken_2_4=pygame.image.load('art/chicken_r_4.png')
chicken_2_5=pygame.image.load('art/chicken_r_5.png')
chicken_2_6=pygame.image.load('art/chicken_r_6.png')
chicken_2_7=pygame.image.load('art/chicken_r_7.png')
chicken_2_8=pygame.image.load('art/chicken_r_8.png')

chicken_gold_1=pygame.image.load('art/chicken_l_golden.png')
chicken_gold_2=pygame.image.load('art/chicken_r_golden.png')

chickens={}

#load all the player sprites
player_1=pygame.image.load('art/player.png')
player_1_walk=(pygame.image.load('art/walk_r_1.png'), pygame.image.load('art/walk_r_2.png'), pygame.image.load('art/walk_r_3.png'), pygame.image.load('art/walk_r_4.png'))
player_1_idle=(pygame.image.load('art/idle_r_1.png'), pygame.image.load('art/idle_r_2.png'))
player_1_egg_1=(pygame.image.load('art/walk_r_1_egg_light.png'), pygame.image.load('art/walk_r_2_egg_light.png'), pygame.image.load('art/walk_r_3_egg_light.png'), pygame.image.load('art/walk_r_4_egg_light.png'))#pygame.image.load('art/player_r_egg_light.png')
player_1_egg_2=(pygame.image.load('art/walk_r_1_egg_dark.png'), pygame.image.load('art/walk_r_2_egg_dark.png'), pygame.image.load('art/walk_r_3_egg_dark.png'), pygame.image.load('art/walk_r_4_egg_dark.png'))#pygame.image.load('art/player_r_egg_dark.png'),)
player_1_egg_gold=(pygame.image.load('art/walk_r_1_egg_golden.png'), pygame.image.load('art/walk_r_2_egg_golden.png'), pygame.image.load('art/walk_r_3_egg_golden.png'), pygame.image.load('art/walk_r_4_egg_golden.png'))
player_1_idle_egg_1=(pygame.image.load('art/idle_r_1_egg_light.png'), pygame.image.load('art/idle_r_2_egg_light.png'))
player_1_idle_egg_2=(pygame.image.load('art/idle_r_1_egg_dark.png'), pygame.image.load('art/idle_r_2_egg_dark.png'))
player_1_idle_egg_gold=(pygame.image.load('art/idle_r_1_egg_golden.png'), pygame.image.load('art/idle_r_2_egg_golden.png'))
player_2=pygame.image.load('art/player_west.png')
player_2_walk=(pygame.image.load('art/walk_l_1.png'), pygame.image.load('art/walk_l_2.png'), pygame.image.load('art/walk_l_3.png'), pygame.image.load('art/walk_l_4.png'))
player_2_idle=(pygame.image.load('art/idle_l_1.png'), pygame.image.load('art/idle_l_2.png'))
player_2_egg_1=(pygame.image.load('art/walk_l_1_egg_light.png'), pygame.image.load('art/walk_l_2_egg_light.png'), pygame.image.load('art/walk_l_3_egg_light.png'), pygame.image.load('art/walk_l_4_egg_light.png'))
player_2_egg_2=(pygame.image.load('art/walk_l_1_egg_dark.png'), pygame.image.load('art/walk_l_2_egg_dark.png'), pygame.image.load('art/walk_l_3_egg_dark.png'), pygame.image.load('art/walk_l_4_egg_dark.png'))
player_2_egg_gold=(pygame.image.load('art/walk_l_1_egg_golden.png'), pygame.image.load('art/walk_l_2_egg_golden.png'), pygame.image.load('art/walk_l_3_egg_golden.png'), pygame.image.load('art/walk_l_4_egg_golden.png'))
player_2_idle_egg_1=(pygame.image.load('art/idle_l_1_egg_light.png'), pygame.image.load('art/idle_l_2_egg_light.png'))
player_2_idle_egg_2=(pygame.image.load('art/idle_l_1_egg_dark.png'), pygame.image.load('art/idle_l_2_egg_dark.png'))
player_2_idle_egg_gold=(pygame.image.load('art/idle_l_1_egg_golden.png'), pygame.image.load('art/idle_l_2_egg_golden.png'))
#player_2_egg_1=(pygame.image.load('art/player_l_egg_light.png'),)
#player_2_egg_2=(pygame.image.load('art/player_l_egg_dark.png'),)

player=player_1
animation=(player_1,)
#print (type(animation))
holding=(False, None)
pos=mid_pos
speed=1
default_speed=5
achivements=[]
avatar=1

#show the player
def show_player():
    global pos
    p=player.get_rect()
    p.center=(round(pos[0]), round(pos[1]))
    screen.blit(player, p)

#move the player
dir_r=True
def move(ev):
    global dir_r, js, an_speed, controls, dis_x, dis_y, pos, speed, default_speed, player, player_1, player_2, chicken_1_7, chicken_1_8, chicken_2_7, chicken_2_8, chicken_gold_1, chicken_gold_2, animation, player_1_idle_egg_gold, player_2_idle_egg_gold, player_1_egg_gold, player_1_idle_egg_1, player_1_idle_egg_2, player_2_idle_egg_1, player_2_idle_egg_2, player_1_walk, player_2_walk, player_1_idle, player_2_idle, holding, player_1_egg_1, player_1_egg_2, player_2_egg_1, player_2_egg_2
    #pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_e, pygame.K_q
    walk=True
    is_walk=False
    if ev[controls[0]]:#pygame.K_w]:
        past=pos[1]
        pos[1]-=default_speed*speed
        walk=True
        is_walk=True
        if pos[1]<0:
            pos[1]=past
    elif ev[controls[2]]:#pygame.K_s]:
        past=pos[1]
        pos[1]+=default_speed*speed
        walk=True
        is_walk=True
        if pos[1]>dis_y:
            pos[1]=past
    else:
        walk=False
    if ev[controls[1]]:#pygame.K_a]:
        if dir_r:#player==player_1:
            player=player_2
            animation=(player_2,)
            dir_r=False
        past=pos[0]
        pos[0]-=default_speed*speed
        walk=True
        if pos[0]<0:
            pos[0]=past
    elif ev[controls[3]]:#pygame.K_d]:
        if not dir_r:#player==player_2:
            player=player_1
            animation=(player_1,)
            dir_r=True
        past=pos[0]
        pos[0]+=default_speed*speed
        if pos[0]>dis_x:
            pos[0]=past
        walk=True
    elif not is_walk:
        walk=False
    if not walk:
        #print ('im in!')
        if len(js)!=0:
            for j in js:
                h=j.get_hat(0)
                #print ('got buttons')
                if h[0]!=0 or h[1]!=0:
                    #print ('passed')
                    pos[0]+=h[0]*default_speed*speed
                    pos[1]-=h[1]*default_speed*speed
                    if h[0]!=0:
                        if h[0]==1:
                            dir_r=True
                        else:
                            dir_r=False
                    walk=True
                    break
                #else:
                    #print (h)
    #print (str((player, player_1)))#(player==player_1)
    if walk:
        if dir_r:#player==player_1:#animation==(player_1,):# or animation==player_1_walk:# or animation==player_1_idle:
            if avatar==1:
                if not holding[0]:
                    animation=player_1_walk
                else:
                    if holding[1][2]==1:
                        animation=player_1_egg_1
                    elif holding[1][2]==2:
                        animation=player_1_egg_2
                    else:
                        animation=player_1_egg_gold
                an_speed=8
            elif avatar==2:
                animation=(chicken_gold_2,)
            elif avatar==3:
                animation=(chicken_2_7,)
            elif avatar==4:
                animation=(chicken_2_8,)
        else:
            if avatar==1:
                if not holding[0]:
                    animation=player_2_walk
                else:
                    if holding[1][2]==1:
                        animation=player_2_egg_1
                    elif holding[1][2]==2:
                        animation=player_2_egg_2
                    else:
                        animation=player_2_egg_gold
                #animation=player_2_walk
                an_speed=8
            elif avatar==2:
                animation=(chicken_gold_1,)
            elif avatar==3:
                animation=(chicken_1_7,)
            elif avatar==4:
                animation=(chicken_1_8,)
    else:
        if dir_r:#player==player_1:#animation==player_1_walk or animation==(player_1,):# or animation==player_1_idle:
            if avatar==1:
                if not holding[0]:
                    animation=player_1_idle
                else:
                    if holding[1][2]==1:
                        animation=player_1_idle_egg_1#(player_1_egg_1[0],)
                    elif holding[1][2]==2:
                        animation=player_1_idle_egg_2#(player_1_egg_2[0],)
                    else:
                        animation=player_1_idle_egg_gold
                #animation=player_1_idle#(player_1,)
                an_speed=16
            elif avatar==2:
                animation=(chicken_gold_2,)
            elif avatar==3:
                animation=(chicken_2_7,)
            elif avatar==4:
                animation=(chicken_2_8,)
        else:
            if avatar==1:
                if not holding[0]:
                    animation=player_2_idle
                else:
                    if holding[1][2]==1:
                        animation=player_2_idle_egg_1#(player_2_egg_1[0],)
                    elif holding[1][2]==2:
                        animation=player_2_idle_egg_2#(player_2_egg_2[0],)
                    else:
                        animation=player_2_idle_egg_gold
                #animation=player_2_idle#(player_2,)
                an_speed=16
            elif avatar==2:
                animation=(chicken_gold_1,)
            elif avatar==3:
                animation=(chicken_1_7,)
            elif avatar==4:
                animation=(chicken_1_8,)

#animate the player
step=0
rel_step=0
an_speed=8
def animate():
    global player, animation, step, rel_step, an_speed
    step+=1
    rel_step=round(step/an_speed)
    #print (rel_step)
    #print (type(animation))
    if rel_step>len(animation)-1:
        step=0
        rel_step=0
    player=animation[rel_step]

#create a random egg
egg_num=0
def new_egg(pos: tuple=None, gold=False):#(random.randint(0, dis_x), random.randint(0, dis_y))):
    global dis_x, dis_y, eggs, egg_1, egg_2, egg_gold, egg_num, egg_crack_1, egg_crack_2, egg_crack_gold
    if pos==None:
        pos=(random.randint(0, dis_x), random.randint(0, dis_y))
    if not gold:
        ty=random.choice([egg_1, egg_2])
    else:
        ty=random.choice([egg_1, egg_2, egg_1, egg_2, egg_gold])
    ty2={egg_1:1, egg_2:2, egg_gold:3}#random.choice([1, 2])
    ani={egg_1:(egg_crack_1[0],), egg_2:(egg_crack_2[0],), egg_gold:(egg_crack_gold[0],)}
    eggs[egg_num]=[ty, pos, ty2[ty], ani, 0]
    egg_num+=1

#show all the eggs
def show_eggs():
    global eggs
    for egg in eggs:
        try:
            e=eggs[egg][0].get_rect()
            e.center=eggs[egg][1]
            screen.blit(eggs[egg][0], e)
        except:
            pass#print (eggs)

#old function, this is needed
def get_mid_egg(pos):
    #egg dim=80x85     40x60
    #new_pos=(pos[0]+40, pos[1]+43)
    return pos

#check if you are inside an eggs radius
def inside_egg_radius(pos):
    global eggs
    yes=(False, None)
    for egg in eggs:
        egg_mid=get_mid_egg(eggs[egg][1])
        if pos[0]>egg_mid[0]-70 and pos[0]<egg_mid[0]+70 and pos[1]>egg_mid[1]-70 and pos[1]<egg_mid[1]+70:
            yes=(True, egg)
            break
    return yes

#pickup/drop
def pickup_egg(pos):
    global holding, eggs, egg_num, dir_r
    if not holding[0]:
        rad=inside_egg_radius(get_mid_player(pos))
        if rad[0]:
            holding=(True, eggs[rad[1]])
            del eggs[rad[1]]
            #egg_num-=1
    else:
        if dir_r:
            new_pos=get_mid_player(pos)
            eggs[egg_num]=[holding[1][0], (new_pos[0]+50, new_pos[1]+40), holding[1][2], holding[1][3], holding[1][4]]
            #print (eggs[egg_num])
            #pygame.draw.circle(screen, black, get_mid_player(pos), 10, 5)
        else:
            new_pos=get_mid_player(pos)
            eggs[egg_num]=[holding[1][0], (new_pos[0]-50, new_pos[1]+40), holding[1][2], holding[1][3], holding[1][4]]
            #print (eggs[egg_num])
        holding=(False, None)
        egg_num+=1

#crack an egg
def crack_egg(pos):
    global eggs, use_sound, crack_sound, egg_crack_1, egg_crack_2, egg_crack_gold
    rad=inside_egg_radius(get_mid_player(pos))
    if rad[0]:
        if eggs[rad[1]][2]==1:
            eggs[rad[1]][3]=egg_crack_1
        elif eggs[rad[1]][2]==2:
            eggs[rad[1]][3]=egg_crack_2
        else:
            eggs[rad[1]][3]=egg_crack_gold
        if use_sound:
            crack_sound.play()
        #holding=(True, eggs[rad[1]])
        #del eggs[rad[1]]
        #egg_num-=1

#old function, this is needed
def get_mid_player(pos):
    #80x170
    return pos#(pos[0]+40, pos[1]+85)

def get_if(i, out1, out2):
    if i:
        return random.choice(out1)
    else:
        return out2

#create a new random chicken
chicken_num=0
def new_chicken(gold=False, load=False):
    global dis_x, dis_y, use_sound, chicken_sound, gen_ac, empty, chicken_hats, achivements, chickens, chicken_gold_1, chicken_gold_2, chicken_1_1, chicken_1_2, chicken_2_1, chicken_2_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8, chicken_num
    pos=[random.randint(0, dis_x), random.randint(0, dis_y)]
    ty=random.choice([chicken_1_1, chicken_2_1, chicken_2_2, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8, chicken_2_3, chicken_2_4])
    ty2={chicken_gold_1:3, chicken_gold_2:3, chicken_1_1:1, chicken_1_2:2, chicken_2_1:1, chicken_2_2:2, chicken_1_3:1, chicken_1_4:2, chicken_2_3:1, chicken_2_4:2, chicken_1_5:1, chicken_1_6:2, chicken_1_7:1, chicken_1_8:2, chicken_2_5:1, chicken_2_6:2, chicken_2_7:1, chicken_2_8:2}#egg_1:1, egg_2:2}#random.choice([1, 2])
    if not gold:
        chickens[chicken_num]=[ty, pos, ty2[ty], randpos(), get_if(gen_ac, chicken_hats, empty), datetime.now()]
    else:
        ty=random.choice([chicken_gold_1, chicken_gold_2])
        chickens[chicken_num]=[ty, pos, 3, randpos(), get_if(gen_ac, chicken_hats, empty), datetime.now()]#{chicken_gold_1:1, chicken_gold_2:2}[t]
    chicken_num+=1
    #ad={1:}#chicken_gold_1:3, chicken_gold_2:3, chicken_1_1:1, chicken_1_2:1, chicken_2_1:2, chicken_2_2:2, chicken_1_3:1, chicken_1_4:2, chicken_2_3:2, chicken_2_4:2, chicken_1_5:1, chicken_1_6:1, chicken_1_7:1, chicken_1_8:1, chicken_2_5:2, chicken_2_6:2, chicken_2_7:2, chicken_2_8:2}#{1:'got'}
    ad2={1:'Normal Chicken!', 2:'Brown Chicken!', 3:'Golden Chicken!'}
    #adl=['Normal Chicken!', 'Brown Chicken!', 'Golden Chicken!']
    #i=False
    #for a in achivements:
    #    if a in adl:
    #        i=True
    #        break
    #if not i:
    if ad2[ty2[ty]] not in achivements:#ad2[ad[ty]]
        if not gold:
            advance(ad2[ty2[ty]])#ad2[ad[ty]])
        else:
            advance('Golden Chicken!')
    if use_sound and not load:
        chicken_sound.play()
    #else:
    #    print (ad2[ty2[ty]])#ad[ty]])
    #    print (ad2[ad[ty]])
    #else:
    #    print (ad2[ad[ty]])#('no!', achivements)

#show all chickens
def show_chickens():
    global chickens, show_ac, show_time, font, black
    for egg in chickens:
        try:
            c=chickens[egg][0].get_rect()
            c.center=chickens[egg][1]
            screen.blit(chickens[egg][0], c)#chickens[egg][1])
            if show_ac:
                ca=chickens[egg][4].get_rect()
                ca.center=(chickens[egg][1][0], chickens[egg][1][1]-30)
                screen.blit(chickens[egg][4], ca)
            if show_time:
                #print ('Yeah!')
                n=datetime.now()-chickens[egg][5]
                t=font.render(str(n.days)+'  '+str(n.seconds), False, black)
                r=t.get_rect()
                r.center=(chickens[egg][1][0], chickens[egg][1][1]+50)
                screen.blit(t, r)
        except Exception as er:
            pass

#confusing function
def if_not(i, inp1, inp2, out1, out2, inp3, out3):
    if i in inp1:
        return out1
    elif i in inp2:
        return out2
    else:
        return inp3[out3]

#confusing function
def if_not_2(i, inp1, inp2, out1, out2):
    if i in inp1:
        return out1
    elif i in inp2:
        return out2

#animate all the eggs
egg_timer=0
rel_egg_timer=0
prev_time=0
def animate_eggs():
    global chickens, prev_time, gen_ac, chicken_hats, empty, chicken_num, eggs, egg_timer, rel_egg_timer, chicken_gold_1, chicken_gold_2, chicken_1_1, chicken_2_1, chicken_2_2, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8#, egg_crack_1_1, egg_crack_1_2, egg_crack_2_1, egg_crack_2_2
    egg_timer+=1
    rel_egg_timer=round(egg_timer/15)
    if rel_egg_timer>5-1:
        egg_timer=0
        rel_egg_timer=0
    dels=[]
    for egg in eggs:
        try:
            if rel_egg_timer!=prev_time:
                eggs[egg][4]+=1
            if eggs[egg][4]>4:
                eggs[egg][4]=0
            eggs[egg][0]=eggs[egg][3][eggs[egg][4]]
            if eggs[egg][4]==5-1:
                save=eggs[egg]
                dels.append(egg)
                if save[2]==1:# or save[2]==3:
                    th=random.choice([chicken_1_1, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8])
                    l1=[chicken_1_1, chicken_1_3, chicken_1_5, chicken_1_7]
                    l2=[chicken_2_2, chicken_2_4, chicken_2_6, chicken_2_8]
                    chickens[chicken_num]=[th, list(save[1]), if_not_2(th, l1, l2, 1, 2), randpos(), get_if(gen_ac, chicken_hats, empty), datetime.now()]#[th, list(save[1]), save[2], randpos()]
                elif save[2]==2:# or save[2]==4:
                    th=random.choice([chicken_2_1, chicken_2_2, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8])
                    l1=[chicken_1_1, chicken_1_3, chicken_1_5, chicken_1_7]
                    l2=[chicken_2_2, chicken_2_4, chicken_2_6, chicken_2_8]
                    chickens[chicken_num]=[th, list(save[1]), if_not_2(th, l1, l2, 1, 2), randpos(), get_if(gen_ac, chicken_hats, empty), datetime.now()]
                else:#if save[2]==3:
                    th=random.choice([chicken_gold_1, chicken_gold_2])#random.choice([chicken_1_1, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8, chicken_gold_1, chicken_2_1, chicken_2_2, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8, chicken_gold_2])
                    #l1=[chicken_1_1, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8]
                    #l2=[chicken_2_1, chicken_2_2, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8]
                    #l3={chicken_gold_1:3, chicken_gold_2:4}
                    #l1=[chicken_gold_1]
                    #l2=[chicken_gold_2]
                    chickens[chicken_num]=[th, list(save[1]), 3, randpos(), get_if(gen_ac, chicken_hats, empty), datetime.now()]#if_not(th, l1, l2, 1, 2, l3, 1)
                chicken_num+=1
                #crack_sound.play()#pygame.mixer.Sound.play(crack_sound)
        except:# Exception as er:
            pass#print (sys.exc_info())#er)
    prev_time=rel_egg_timer
    for d in dels:
        del eggs[d]

#get a specific chicken to lay an egg
def lay_egg(chi):
    global chickens
    if chickens[chi][2]==3 and random.randint(1,100)==1:
        new_egg(chickens[chi][1], True)
    else:
        new_egg(chickens[chi][1])

#calculate a specific chickens ai
def chicken_ai(chi):
    global chickens
    pos=chickens[chi][1]
    target=chickens[chi][3]
    if pos==target:
        target=randpos()
        chickens[chi][3]=target
    if target[0]>pos[0]:
        pos[0]+=1
    elif target[0]<pos[0]:
        pos[0]-=1
    if target[1]>pos[1]:
        pos[1]+=1
    elif target[1]<pos[1]:
        pos[1]-=1
    chickens[chi][1]=pos

#get a random position
def randpos():
    global dis_x, dis_y
    return [random.randint(0, dis_x), random.randint(0, dis_y)]

def advance(name):
    global achivements, event_text
    achivements.append(name)
    event_text=name

def wait_for_key():
    global on
    key=False
    while not key:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                on=False
                key=True
            elif ev.type==pygame.KEYDOWN:
                return ev.key

def key_name(key):
    return pygame.key.name(key)

vol=10
def volume(new):
    global crack_sound, chicken_sound, vol
    new=float(new)
    crack_sound.set_volume(new)
    chicken_sound.set_volume(new/2)
    vol=new*10

def warning(text):
    global font, black, dis_x, dis_y
    t=font.render(text, False, black)
    p=t.get_rect()
    p.center=(dis_x//2, dis_y//2)
    screen.blit(t, p)
    pygame.display.update()
    time.sleep(3)

def get_num(cent):
    global textbox
    re=pygame.K_RETURN
    val_keys=[pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
    t=font.render('Waiting...', False, black)
    p=t.get_rect()
    p.center=cent#o[0].center
    p2=textbox.get_rect()
    p2.center=cent
    screen.blit(textbox, p2)
    screen.blit(t, p)
    pygame.display.update()
    num=''
    k=None
    while k!=re:
        k=wait_for_key()
        if k==re:
            break
        elif k in val_keys:
            num+=key_name(k)
            t=font.render(num, False, black)
            p=t.get_rect()
            p.center=cent#o[0].center
            p2=textbox.get_rect()
            p2.center=cent
            screen.blit(textbox, p2)
            screen.blit(t, p)
            pygame.display.update()
    return num

def get_controller():
    global js
    con=[False for a in range(12)]
    tfton={0:False, 1:True, '0':False, '1':True}
    for j in js:
        but=[tfton[j.get_button(b)] for b in range(j.get_numbuttons())]
        if but!=con:
            con=but
            break
    return con

def wait_for_con(wait=True, use_nums=True):
    global on
    key=False
    defa=[False for a in range(12)]
    while not key:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                on=False
                key=True
        con=get_controller()
        if con!=defa:
            if use_nums:
                return get_nums(con)
            else:
                return con
        if not wait:
            key=True
    return defa

def get_nums(l):
    nums=[]
    for a in range(len(l)):
        if l[a]:
            nums.append(a)
    return nums

"""
step=0
rel_step=0
an_speed=8
def animate():
    global player, animation, step, rel_step, an_speed
    step+=1
    rel_step=round(step/an_speed)
    #print (rel_step)
    #print (type(animation))
    if rel_step>len(animation)-1:
        step=0
        rel_step=0
    player=animation[rel_step]
"""

#def show_holding():
#    global pos
#    

def set_dev():
    global dev_mode, used_keys, used_buttons
    dev_mode=not dev_mode
    if dev_mode:
        used_buttons=[7, 6, 3, 8, 4, 5, 9]
        used_keys=[pygame.K_ESCAPE, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n]
    else:
        used_buttons=[9]#[7, 6, 3, 2, 4, 5, 9]
        used_keys=[pygame.K_ESCAPE]

cooldown=0
eggdown=random.randint(1, 1000)
shopdown=0
production_speed=1
money=0
instart=True
inmenu=False
inshot=False
event_text=''
inad=False
insettings=False
setmove=False
setgen=False
setcon=False
button_names={0: 'x', 1: 'a', 2: 'b', 3: 'y', 4: 'LB', 5: 'RB', 6: 'LT', 7: 'RT', 8: 'back', 9: 'start', 10: 'LS', 11: 'RS'}
con_pos=[dis_x//2, dis_y//2]
before_con_pos=(0, 0)
con_fix_timer=10

#settings
controls=[pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_e, pygame.K_q]
used_keys=[pygame.K_ESCAPE]#, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n]
free_bind=False
show_ac=False#True
gen_ac=False#True
#chicken_sound.set_volume(0.5)
text_size=20
use_sound=True
dev_mode=False
show_time=False
cont_controls=[1, 0, 2]
used_buttons=[9]
use_con=False
mouse_fix=False
mouse_fix_time=50

start_image=pygame.image.load('art/start.png')
start_image_pos=start_image.get_rect()
start_image_pos.center=(dis_x//2, dis_y//4)

#get all text
font=pygame.font.Font('freesansbold.ttf', 20)
if random.randint(1, 100)!=1:
    exit_text=font.render('Exit', False, black)
else:
    exit_text=font.render('Eggsit', False, black)
exit_text_cords=exit_text.get_rect()
exit_text_cords.center=(dis_x//2, dis_y//2)
shop_text=font.render('Shop', False, black)
shop_text_cords=shop_text.get_rect()
shop_text_cords.center=(dis_x//2, dis_y//4)
pro_text=font.render('Production speed: $5', False, black)
pro_text_pos=pro_text.get_rect()
pro_text_pos.center=(dis_x//2, dis_y//2)
chi_text=font.render('Chicken: $15', False, black)
chi_pos=chi_text.get_rect()
chi_pos.center=(dis_x//2, dis_y//4)
play_text=font.render('Start', False, black)
play_text_pos=play_text.get_rect()
play_text_pos.center=(dis_x//2, dis_y//2)
main_text=font.render('Back to main menu', False, black)
main_text_pos=main_text.get_rect()
main_text_pos.center=(dis_x//2, (dis_y//4)*3)
#main_exit_text=font.render('Exit', False, black)
main_exit_text_cords=exit_text.get_rect()
main_exit_text_cords.center=(dis_x//2, (dis_y//4)*3)
ad_text=font.render('Advancements', False, black)
ad_text_pos=ad_text.get_rect()
ad_text_pos.center=(dis_x//2, (dis_y//4)//2)
set_text=font.render('Settings', False, black)
set_post=set_text.get_rect()
set_post.center=(dis_x//2, dis_y-((dis_y//4)//2))
set_pos=textbox.get_rect()
set_pos.center=set_post.center

#pygame function replacements
def get_mouse():
    global use_con, con_pos
    if use_con:
        return con_pos
    else:
        return pygame.mouse.get_pos()

def get_click():
    global use_con, cont_controls
    if use_con:
        return wait_for_con(False, False)[cont_controls[0]]
    else:
        return pygame.mouse.get_pressed()[0]

def con_mouse():#pos1, pos2):
    global con_pos, js, default_speed, mouse_fix, before_con_pos
    if len(js)!=0:
        for j in js:
            h=(round_float(j.get_axis(2)), round_float(j.get_axis(3)))#.get_hat(0)
            #print ('got buttons')
            if h[0]!=0 or h[1]!=0:
                #print ('passed')
                #print (type(con_pos))
                do=True
                if mouse_fix:
                    if not mouse_move_check(h):
                        do=False
                if do:
                    con_pos[0]+=h[0]*default_speed*2
                    con_pos[1]+=h[1]*default_speed*2
                    before_con_pos=h
                    break

def mouse_move_check(h):
    global before_con_pos, con_fix_timer, mouse_fix_time
    if con_fix_timer>0:
        con_fix_timer-=1
        return True#before_con_pos!=h
    else:
        if before_con_pos!=h:
            con_fix_timer=mouse_fix_time
            return True
        else:
            return False
        #return before_con_pos!=h
    #t=False
    #for event in pygame.event.get():
    #    if event.type==pygame.JOYBALLMOTION
    #        t=True
    #        break
    #return t

def round_float(f):
    return float('{:>6.3f}'.format(f))

def round_tuple(t):
    r=[]
    for item in t:
        r.append(round(item))
    return tuple(r)

#mainloop
on=True
while on:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            on=False
        #else:
            #print (event)
    screen.fill(background)
    #check if not in start menu
    if not instart:
        text=font.render('Money: '+str(money), False, black, background)
        re=text.get_rect()
        re.center=(-dis_x+(dis_x+len(list('Money: '+str(money)))*7), -dis_y+(dis_y+20))
        screen.blit(text, re)
        if not inmenu:
            ev_text=font.render(event_text, False, black)
            evt_box=ev_text.get_rect()
            evt_box.center=(dis_x//2, dis_y-30)
            ev_box=textbox.get_rect()
            ev_box.center=evt_box.center
            screen.blit(textbox, ev_box)
            screen.blit(ev_text, evt_box)
            animate_eggs()
            show_eggs()
            for chi in chickens:
                chicken_ai(chi)
            show_chickens()
            animate()
            show_player()
        else:
            #check if not in the shop
            if inshop:
                if not inad:
                    pro_box=textbox
                    pro_pos=pro_box.get_rect()
                    pro_pos.center=(dis_x//2, dis_y//2)
                    screen.blit(pro_box, pro_pos)
                    screen.blit(pro_text, pro_text_pos)
                    chi_box=textbox
                    chib_pos=chi_box.get_rect()
                    chib_pos.center=(dis_x//2, dis_y//4)
                    screen.blit(chi_box, chib_pos)
                    screen.blit(chi_text, chi_pos)
                    #check if player bought anything
                    if shopdown<=0:
                        if get_click():#pygame.mouse.get_pressed()[0]:
                            mouse=get_mouse()#pygame.mouse.get_pos()
                            if pro_pos.collidepoint(*mouse):
                                if money>=5:
                                    money-=5
                                    production_speed+=1
                                    shopdown=5
                            if chib_pos.collidepoint(*mouse):
                                if money>=15:
                                    money-=15
                                    if random.randint(1, 30):
                                        new_chicken(True)
                                    else:
                                        new_chicken()
                                    shopdown=5
                    else:
                        shopdown-=1
                else:
                    #po=(dis_x//2, (dis_y//4)//2)
                    po=[dis_x//2, 40]
                    #show advacements
                    for ad in achivements:
                        #get advancement
                        t=font.render(ad, False, black)
                        r=t.get_rect()
                        r.center=tuple(po)
                        r2=textbox.get_rect()
                        r2.center=r.center
                        #draw advancement
                        screen.blit(textbox, r2)
                        screen.blit(t, r)
                        #add to y poition
                        po[1]+=80
            elif insettings:
                if setmove:
                    for_text=font.render('Forward: '+key_name(controls[0]), False, black)
                    back_text=font.render('Backward: '+key_name(controls[2]), False, black)
                    ri_text=font.render('Right: '+key_name(controls[3]), False, black)
                    le_text=font.render('Left: '+key_name(controls[1]), False, black)
                    in_text=font.render('Pickup: '+key_name(controls[4]), False, black)
                    cr_text=font.render('Crack: '+key_name(controls[5]), False, black)
                    tftof={True:'On', False:'Off'}
                    du_text=font.render('Free bind: '+tftof[free_bind], False, black)
                    con=[for_text, back_text, ri_text, le_text, in_text, cr_text]
                    li={}
                    po=[dis_x//2, 40]
                    for t in con:
                        #make text position
                        r=t.get_rect()
                        r.center=tuple(po)
                        r2=textbox.get_rect()
                        r2.center=r.center
                        #print (type(li))
                        li[len(li)]=r2, tuple(po)
                        #print (type(li))
                        #draw control
                        screen.blit(textbox, r2)
                        screen.blit(t, r)
                        #add to y poition
                        po[1]+=80
                    r=du_text.get_rect()
                    r.center=tuple(po)
                    du_box=textbox.get_rect()
                    du_box.center=r.center
                    screen.blit(textbox, du_box)
                    screen.blit(du_text, r)
                    if get_click():#pygame.mouse.get_pressed()[0]:
                        poo=get_mouse()#pygame.mouse.get_pos()
                        do=True
                        if cooldown<=0:
                            if du_box.collidepoint(*poo):
                                do=False
                                cooldown=5
                                free_bind=not free_bind
                        #else:
                        #    cooldown-=1
                        if do:
                            rel_con={0:0, 1:2, 2:3, 3:1, 4:4, 5:5}
                            for c in li:
                                if li[c][0].collidepoint(*poo):
                                    t=font.render('Waiting...', False, black)
                                    p=t.get_rect()
                                    p.center=li[c][1]
                                    p2=textbox.get_rect()
                                    p2.center=p.center
                                    screen.blit(textbox, p2)
                                    screen.blit(t, p)
                                    pygame.display.update()
                                    k=wait_for_key()
                                    if not free_bind:
                                        if k not in used_keys and k not in controls:
                                            controls[rel_con[c]]=k
                                    else:
                                        controls[rel_con[c]]=k
                elif setgen:
                    #vo_text=font.render('Volume: '+str(int(vol)), False, black)
                    ts_text=font.render('Text size: '+str(text_size), False, black)
                    oof={True:'On', False:'Off'}
                    sa_text=font.render('Show accessories: '+oof[show_ac], False, black)
                    so_text=font.render('Sound: '+oof[use_sound], False, black)
                    dm_text=font.render('Developer mode: '+oof[dev_mode], False, black)
                    st_text=font.render('Show chicken lifetime: '+oof[show_time], False, black)
                    op=(ts_text, sa_text, so_text, dm_text, st_text)#tuple([])#(vo_text,)
                    l=[]
                    po=[(dis_x//2)-170, dis_y//4]
                    dow=((dis_x//2)-170)+340+340
                    st=(dis_x//2)-170
                    thi=0
                    for t in op:
                        if po[0]==dow:
                            po[0]=st
                            po[1]+=80
                        r=t.get_rect()
                        r.center=tuple(po)
                        r2=textbox.get_rect()
                        r2.center=r.center
                        screen.blit(textbox, r2)
                        screen.blit(t, r)
                        po[0]+=340
                        l.append([r2, thi])
                        thi+=1
                    #tts={0:setmo}
                    if get_click():#pygame.mouse.get_pressed()[0]:
                        mo=get_mouse()#pygame.mouse.get_pos()
                        for o in l:
                            if o[0].collidepoint(mo):
                                if o[1]==0:
                                    num=get_num(o[0].center)
                                    if num!='':
                                        if int(num)<=25:
                                            font=pygame.font.Font('freesansbold.ttf', int(num))
                                            text_size=int(num)
                                        else:
                                            warning('The max size of text is 25')
                                elif o[1]==1:
                                    if cooldown<=0:
                                        show_ac=not show_ac
                                        cooldown=10
                                elif o[1]==2:
                                    if cooldown<=0:
                                        use_sound=not use_sound
                                        cooldown=10
                                elif o[1]==3:
                                    if cooldown<=0:
                                        set_dev()
                                        cooldown=10
                                elif o[1]==4:
                                    if cooldown<=0:
                                        show_time=not show_time
                                        cooldown=10
##                                if o[1]==0:
##                                    re=pygame.K_RETURN
##                                    val_keys=[pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
##                                    t=font.render('Waiting...', False, black)
##                                    p=t.get_rect()
##                                    p.center=o[0].center
##                                    screen.blit(textbox, o[0])
##                                    screen.blit(t, p)
##                                    pygame.display.update()
##                                    num=''
##                                    k=None
##                                    while k!=re:
##                                        k=wait_for_key()
##                                        if k==re:
##                                            break
##                                        elif k in val_keys:
##                                            num+=key_name(k)
##                                            t=font.render(num, False, black)
##                                            p=t.get_rect()
##                                            p.center=o[0].center
##                                            screen.blit(textbox, o[0])
##                                            screen.blit(t, p)
##                                            pygame.display.update()
##                                    if num!='':
##                                        if int(num)<=100.0:
##                                            volume(int(num)/10)
##                                        else:
##                                            warning('The max volume is 100')
                elif setcon:
                    in_text=font.render('Pickup/Interact: '+button_names[cont_controls[0]], False, black)
                    cr_text=font.render('Crack: '+button_names[cont_controls[1]], False, black)
                    mc_text=font.render('Return to center(menu): '+button_names[cont_controls[2]], False, black)
                    tftof={True:'On', False:'Off'}
                    mf_text=font.render('Mouse fix: '+tftof[mouse_fix], False, black)
                    mt_text=font.render('Mouse fix time: '+str(mouse_fix_time), False, black)
                    du_text=font.render('Free bind: '+tftof[free_bind], False, black)
                    con=[in_text, cr_text, mc_text]
                    li={}
                    po=[dis_x//2, 40]
                    for t in con:
                        #make text position
                        r=t.get_rect()
                        r.center=tuple(po)
                        r2=textbox.get_rect()
                        r2.center=r.center
                        #print (type(li))
                        li[len(li)]=r2, tuple(po)
                        #print (type(li))
                        #draw control
                        screen.blit(textbox, r2)
                        screen.blit(t, r)
                        #add to y poition
                        po[1]+=80
                    r=mf_text.get_rect()
                    r.center=tuple(po)
                    mf_box=textbox.get_rect()
                    mf_box.center=r.center
                    screen.blit(textbox, mf_box)
                    screen.blit(mf_text, r)
                    po[1]+=80
                    r=mt_text.get_rect()
                    r.center=tuple(po)
                    mt_box=textbox.get_rect()
                    mt_box.center=r.center
                    if mouse_fix:
                        screen.blit(textbox, mt_box)
                        screen.blit(mt_text, r)
                        po[1]+=80
                    r=du_text.get_rect()
                    r.center=tuple(po)
                    du_box=textbox.get_rect()
                    du_box.center=r.center
                    screen.blit(textbox, du_box)
                    screen.blit(du_text, r)
                    if get_click():#pygame.mouse.get_pressed()[0]:
                        poo=get_mouse()#pygame.mouse.get_pos()
                        do=True
                        if cooldown<=0:
                            if du_box.collidepoint(*poo):
                                do=False
                                cooldown=5
                                free_bind=not free_bind
                            elif mf_box.collidepoint(*poo):
                                do=False
                                cooldown=5
                                mouse_fix=not mouse_fix
                            elif mt_box.collidepoint(*poo):
                                num=get_num(mt_box.center)
                                if num!='':
                                    if int(num)<=500:
                                        #font=pygame.font.Font('freesansbold.ttf', int(num))
                                        #text_size=int(num)
                                        mouse_fix_time=int(num)
                                    else:
                                        warning('The max fix timer time is 500')
                        #else:
                        #    cooldown-=1
                        if do:
                            #rel_con={0:0, 1:2, 2:3, 3:1, 4:4, 5:5}
                            for c in li:
                                if li[c][0].collidepoint(*poo):
                                    t=font.render('Waiting...', False, black)
                                    p=t.get_rect()
                                    p.center=li[c][1]
                                    p2=textbox.get_rect()
                                    p2.center=p.center
                                    screen.blit(textbox, p2)
                                    screen.blit(t, p)
                                    pygame.display.update()
                                    if use_con:
                                        time.sleep(0.5)
                                    k=wait_for_con()[0]
                                    if not free_bind:
                                        if k not in used_buttons and k not in cont_controls:
                                            cont_controls[c]=k
                                    else:
                                        cont_controls[c]=k
                else:
                    mo_text=font.render('Keyboard', False, black)
                    ge_text=font.render('General', False, black)
                    co_text=font.render('Controller', False, black)
                    #te_text=font.render('test', False, black)
                    op=(mo_text, ge_text, co_text)#, te_text)
                    #320x60
                    l=[]
                    po=[(dis_x//2)-170, dis_y//4]
                    dow=((dis_x//2)-170)+340+340
                    st=(dis_x//2)-170
                    thi=0
                    for t in op:
                        if po[0]==dow:
                            po[0]=st
                            po[1]+=80
                        r=t.get_rect()
                        r.center=tuple(po)
                        r2=textbox.get_rect()
                        r2.center=r.center
                        screen.blit(textbox, r2)
                        screen.blit(t, r)
                        po[0]+=340
                        l.append([r2, thi])
                        thi+=1
                    #tts={0:setmo}
                    if get_click():#pygame.mouse.get_pressed()[0]:
                        mo=get_mouse()#pygame.mouse.get_pos()
                        for o in l:
                            if o[0].collidepoint(mo):
                                if o[1]==0:
                                    setmove=True
                                elif o[1]==1:
                                    setgen=True
                                    cooldown=10
                                elif o[1]==2:
                                    setcon=True
            else:
                exit_box=textbox
                box_pos=exit_box.get_rect()#pygame.Rect((dis_x//2)-160, (dis_y//2)-30, (dis_x//2)+160, (dis_y//2)+30)
                box_pos.center=(dis_x//2, dis_y//2)
                screen.blit(exit_box, box_pos)
                screen.blit(exit_text, exit_text_cords)
                shop_box=textbox
                shop_pos=shop_box.get_rect()
                shop_pos.center=(dis_x//2, dis_y//4)
                screen.blit(shop_box, shop_pos)
                screen.blit(shop_text, shop_text_cords)
                main_box=textbox
                main_pos=main_box.get_rect()
                main_pos.center=(dis_x//2, (dis_y//4)*3)
                screen.blit(main_box, main_pos)
                screen.blit(main_text, main_text_pos)
                ad_pos=textbox.get_rect()
                ad_pos.center=ad_text_pos.center
                screen.blit(textbox, ad_pos)
                screen.blit(ad_text, ad_text_pos)
                screen.blit(textbox, set_pos)
                screen.blit(set_text, set_post)
                #print (type(box.get_rect()))
                #check if player clicked anything
                if get_click():#pygame.mouse.get_pressed()[0]:
                    mouse=get_mouse()#pygame.mouse.get_pos()
                    if box_pos.collidepoint(*mouse):
                        on=False
                    elif shop_pos.collidepoint(*mouse):
                        inad=False
                        inshop=True
                    elif main_pos.collidepoint(*mouse):
                        instart=True
                        cooldown=15
                    elif ad_pos.collidepoint(*mouse):
                        inad=True
                        inshop=True
                    elif set_pos.collidepoint(*mouse):
                        insettings=True
                        inshop=False
                        setmove=False
                        setgen=False
                        setcon=False
                        cooldown=10
                
            #draw cursor
            p=get_mouse()#pygame.mouse.get_pos()
            p=round_tuple(p)
            pygame.draw.circle(screen, white, p, 30, 3)
            pygame.draw.circle(screen, black, p, 10, 2)
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(screen, red, p , 40, 5)
                #print ('off!')
            #b=box.get_rect()
            #print (b)#b.center(dis_x//2, dis_y//2)
            #b)
        #if not inmenu:
        press=pygame.key.get_pressed()
        controller=get_controller()
        if cooldown<=0:
            if press[pygame.K_ESCAPE] or controller[9]:
                inmenu=not inmenu
                inshop=False
                inad=False
                insettings=False
                cooldown=10
                if controller[9]:
                    use_con=True
                    con_pos=[dis_x//2, dis_y//2]
                else:
                    use_con=False
        #else:
        #    cooldown-=1
        if not inmenu:
            move(press)
            if dev_mode==True:
                if press[pygame.K_z] or controller[7]:
                    new_egg(None, True)
                if press[pygame.K_x] or controller[6]:
                    new_chicken(random.choice([False, False, True]))
                if press[pygame.K_c] or controller[3]:
                    event_text=random.choice(['got a meme!', 'Yay! you unlocked a meme channel!', '[incert text here]', 'this is text'])
            if cooldown<=0:
                if press[controls[4]] or controller[cont_controls[0]]:#pygame.K_e]:
                    pickup_egg(pos)
                    cooldown=10
                if press[controls[5]] or controller[cont_controls[1]]:#pygame.K_q]:
                    crack_egg(pos)
                    cooldown=10
                if dev_mode==True:
                    if press[pygame.K_v] or controller[2]:
                        avatar+=1
                        if avatar==5:
                            avatar=1
                        cooldown=10
                    if press[pygame.K_b] or controller[4]:
                        show_ac=not show_ac
                        cooldown=10
                    if press[pygame.K_n] or controller[5]:
                        gen_ac=not gen_ac
                        cooldown=10
            if len(chickens)>0:
                if eggdown<=0:
                    lay_egg(random.dict_choice(chickens))
                    eggdown=random.randint(0, round(1000/(production_speed/2))//round_up(len(chickens)/5))#(len(chickens)/3)))
                else:
                    eggdown-=1
    else:
        screen.blit(start_image, start_image_pos)
        play_box=textbox
        play_pos=play_box.get_rect()
        play_pos.center=(dis_x//2, dis_y//2)
        screen.blit(play_box, play_pos)
        screen.blit(play_text, play_text_pos)
        exit_box=textbox
        box_pos=exit_box.get_rect()#pygame.Rect((dis_x//2)-160, (dis_y//2)-30, (dis_x//2)+160, (dis_y//2)+30)
        box_pos.center=(dis_x//2, (dis_y//4)*3)
        screen.blit(exit_box, box_pos)
        screen.blit(exit_text, main_exit_text_cords)
        p=pygame.mouse.get_pos()
        pygame.draw.circle(screen, white, p, 30, 3)
        pygame.draw.circle(screen, black, p, 10, 2)
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, red, p , 40, 5)
            if play_pos.collidepoint(*p):
                instart=False
                inmenu=False
                inshop=False
                inad=False
                insettings=False
        if cooldown<=0:
            if pygame.mouse.get_pressed()[0]:
                if box_pos.collidepoint(*p):
                    on=False
        #else:
        #    cooldown-=1
    #show_eggs()
    #update display and wait
    cooldown-=1
    if use_con:
        controller=get_controller()
        if inmenu or instart:
            con_mouse()
        if controller[cont_controls[2]]:
            con_pos=[dis_x//2, dis_y//2]
    pygame.display.update()
    clock.tick(30)

#close the pygame window
pygame.quit()
