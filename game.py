import pygame
import random
import sys

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

clock=pygame.time.Clock()

#load everything that does not fit into any special group
textbox=pygame.image.load('art/textbox.png')

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

#show the player
def show_player():
    global pos
    p=player.get_rect()
    p.center=(pos)
    screen.blit(player, p)

#move the player
dir_r=True
def move(ev):
    global dir_r, an_speed, pos, speed, default_speed, player, player_1, player_2, animation, player_1_idle_egg_gold, player_2_idle_egg_gold, player_1_egg_gold, player_1_idle_egg_1, player_1_idle_egg_2, player_2_idle_egg_1, player_2_idle_egg_2, player_1_walk, player_2_walk, player_1_idle, player_2_idle, holding, player_1_egg_1, player_1_egg_2, player_2_egg_1, player_2_egg_2
    walk=True
    is_walk=False
    if ev[pygame.K_w]:
        pos[1]-=default_speed*speed
        walk=True
        is_walk=True
    elif ev[pygame.K_s]:
        pos[1]+=default_speed*speed
        walk=True
        is_walk=True
    else:
        walk=False
    if ev[pygame.K_a]:
        if dir_r:#player==player_1:
            player=player_2
            animation=(player_2,)
            dir_r=False
        pos[0]-=default_speed*speed
        walk=True
    elif ev[pygame.K_d]:
        if not dir_r:#player==player_2:
            player=player_1
            animation=(player_1,)
            dir_r=True
        pos[0]+=default_speed*speed
        walk=True
    elif not is_walk:
        walk=False
    #print (str((player, player_1)))#(player==player_1)
    if walk:
        if dir_r:#player==player_1:#animation==(player_1,):# or animation==player_1_walk:# or animation==player_1_idle:
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
        else:
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
    else:
        if dir_r:#player==player_1:#animation==player_1_walk or animation==(player_1,):# or animation==player_1_idle:
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
        else:
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
    global eggs, egg_crack_1, egg_crack_2, egg_crack_gold
    rad=inside_egg_radius(get_mid_player(pos))
    if rad[0]:
        if eggs[rad[1]][2]==1:
            eggs[rad[1]][3]=egg_crack_1
        elif eggs[rad[1]][2]==2:
            eggs[rad[1]][3]=egg_crack_2
        else:
            eggs[rad[1]][3]=egg_crack_gold
        #holding=(True, eggs[rad[1]])
        #del eggs[rad[1]]
        #egg_num-=1

#old function, this is needed
def get_mid_player(pos):
    #80x170
    return pos#(pos[0]+40, pos[1]+85)

#create a new random chicken
chicken_num=0
def new_chicken(gold=False):
    global dis_x, dis_y, achivements, chickens, chicken_gold_1, chicken_gold_2, chicken_1_1, chicken_1_2, chicken_2_1, chicken_2_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8, chicken_num
    pos=[random.randint(0, dis_x), random.randint(0, dis_y)]
    ty=random.choice([chicken_1_1, chicken_2_1, chicken_2_2, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8, chicken_2_3, chicken_2_4])
    ty2={chicken_1_1:1, chicken_1_2:2, chicken_2_1:1, chicken_2_2:2, chicken_1_3:1, chicken_1_4:2, chicken_2_3:1, chicken_2_4:3, chicken_1_5:1, chicken_1_6:2, chicken_1_7:1, chicken_1_8:2, chicken_2_5:1, chicken_2_6:2, chicken_2_7:1, chicken_2_8:2}#egg_1:1, egg_2:2}#random.choice([1, 2])
    if not gold:
        chickens[chicken_num]=[ty, pos, ty2[ty], randpos()]
    else:
        t=random.choice([chicken_gold_1, chicken_gold_2])
        chickens[chicken_num]=[t, pos, {chicken_gold_1:1, chicken_gold_2:2}[t], randpos()]
    chicken_num+=1
    ad={chicken_gold_1:3, chicken_gold_2:3, chicken_1_1:1, chicken_1_2:1, chicken_2_1:2, chicken_2_2:2, chicken_1_3:1, chicken_1_4:2, chicken_2_3:2, chicken_2_4:2, chicken_1_5:1, chicken_1_6:1, chicken_1_7:1, chicken_1_8:1, chicken_2_5:2, chicken_2_6:2, chicken_2_7:2, chicken_2_8:2}#{1:'got'}
    ad2={1:'Normal Chicken!', 2:'Brown Chicken!', 3:'Golden Chicken!'}
    #adl=['Normal Chicken!', 'Brown Chicken!', 'Golden Chicken!']
    #i=False
    #for a in achivements:
    #    if a in adl:
    #        i=True
    #        break
    #if not i:
    if ad2[ad[ty]] not in achivements:
        advance(ad2[ad[ty]])
    #    print (ad2[ad[ty]])
    #else:
    #    print (ad2[ad[ty]])#('no!', achivements)

#show all chickens
def show_chickens():
    global chickens
    for egg in chickens:
        try:
            c=chickens[egg][0].get_rect()
            c.center=chickens[egg][1]
            screen.blit(chickens[egg][0], c)#chickens[egg][1])
        except:
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
    global chickens, prev_time, chicken_num, eggs, egg_timer, rel_egg_timer, chicken_gold_1, chicken_gold_2, chicken_1_1, chicken_2_1, chicken_2_2, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8#, egg_crack_1_1, egg_crack_1_2, egg_crack_2_1, egg_crack_2_2
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
                    chickens[chicken_num]=[th, list(save[1]), if_not_2(th, l1, l2, 1, 2), randpos()]#[th, list(save[1]), save[2], randpos()]
                elif save[2]==2:# or save[2]==4:
                    th=random.choice([chicken_2_1, chicken_2_2, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8])
                    l1=[chicken_1_1, chicken_1_3, chicken_1_5, chicken_1_7]
                    l2=[chicken_2_2, chicken_2_4, chicken_2_6, chicken_2_8]
                    chickens[chicken_num]=[th, list(save[1]), if_not_2(th, l1, l2, 1, 2), randpos()]
                else:#if save[2]==3:
                    th=random.choice([chicken_1_1, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8, chicken_gold_1, chicken_2_1, chicken_2_2, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8, chicken_gold_2])
                    l1=[chicken_1_1, chicken_1_2, chicken_1_3, chicken_1_4, chicken_1_5, chicken_1_6, chicken_1_7, chicken_1_8]
                    l2=[chicken_2_1, chicken_2_2, chicken_2_3, chicken_2_4, chicken_2_5, chicken_2_6, chicken_2_7, chicken_2_8]
                    l3={chicken_gold_1:3, chicken_gold_2:4}
                    chickens[chicken_num]=[th, list(save[1]), if_not(th, l1, l2, 1, 2, l3, 1), randpos()]
                chicken_num+=1
        except:# Exception as er:
            pass#print (sys.exc_info())#er)
    prev_time=rel_egg_timer
    for d in dels:
        del eggs[d]

#get a specific chicken to lay an egg
def lay_egg(chi):
    global chickens
    if chickens[chi][2]==3 and random.randint(1,10)==1:
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

cooldown=0
eggdown=random.randint(1, 1000)
shopdown=0
production_speed=1
money=0
instart=True
inmenu=False
inshot=False
event_text=''

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
            if not inshop:
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
                #print (type(box.get_rect()))
                #check if player clicked anything
                if pygame.mouse.get_pressed()[0]:
                    mouse=pygame.mouse.get_pos()
                    if box_pos.collidepoint(*mouse):
                        on=False
                    elif shop_pos.collidepoint(*mouse):
                        inshop=True
                    elif main_pos.collidepoint(*mouse):
                        instart=True
                        cooldown=15
            else:
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
                    if pygame.mouse.get_pressed()[0]:
                        mouse=pygame.mouse.get_pos()
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
            #draw cursor
            p=pygame.mouse.get_pos()
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
        if cooldown<=0:
            if press[pygame.K_ESCAPE]:
                inmenu=not inmenu
                inshop=False
                cooldown=10
        else:
            cooldown-=1
        if not inmenu:
            move(press)
            if press[pygame.K_z]:
                new_egg(None, True)
            if press[pygame.K_x]:
                new_chicken(random.choice([False, False, True]))
            if cooldown<=0:
                if press[pygame.K_e]:
                    pickup_egg(pos)
                    cooldown=10
                if press[pygame.K_q]:
                    crack_egg(pos)
                    cooldown=10
                if press[pygame.K_c]:
                    event_text=random.choice(['got a meme!', 'Yay! you unlocked a meme channel!', '[incert text here]', 'this is text'])
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
        if cooldown<=0:
            if pygame.mouse.get_pressed()[0]:
                if box_pos.collidepoint(*p):
                    on=False
        else:
            cooldown-=1
    #show_eggs()
    #update display and wait
    pygame.display.update()
    clock.tick(30)

#close the pygame window
pygame.quit()
