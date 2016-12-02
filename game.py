#!/usr/bin/env python
import csv
import pygame
import time
import random

pygame.init()

display_width = 700
display_height = 650

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

bg=pygame.image.load('tlo.png') 

def Best_Score(count):
        plik = open("score.txt")
        with plik as pl:
            liczba = plik.readline()
    
        plik.close()
        if liczba!='':
            liczba=int(liczba)
            if(count>liczba):
                liczba=count
                plik = open("score.txt", "w")
                with plik as pl:
                    plik.write(str(liczba))
                plik.close()
        else:
            liczba=count
            plik = open("score.txt", "w")
            with plik as pl:
                plik.write(str(liczba))
            plik.close()

def Show_Score():
        plik = open("score.txt")
        with plik as pl:
            liczba = plik.readline()
    
        plik.close()
        if liczba!='':
            message_display1(liczba) 
            
        else:
            liczba=0
            message_display1(str(liczba)) 
 





def save_music(music):
      plik = open("music.txt", "w")
      with plik as pl:
          plik.write(music)
      plik.close()



def animacja(a,skrzydlo,b,c,b1,c1,b11,c11,t1,t11,h1,h2,h11,h22,h111,h222,floor,floor1,count,music):
    a.image=pygame.transform.rotate(a.image,-90)
    plik = open("music.txt")
    with plik as pl:
        music0 = plik.readline()
    plik.close()
    if(music0=="ON"):
        music.play()
    while a.rect.y+a.h<display_height-30:
        a.rect.y+=4
        skrzydlo.rect.y+=4
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(a.image,(a.rect.x,a.rect.y))
        gameDisplay.blit(skrzydlo.image,(skrzydlo.rect.x,skrzydlo.rect.y))
        
        
        gameDisplay.blit(b.image,(b.rect.x,display_height-h1))
        gameDisplay.blit(c.image,(c.rect.x,-(c.rect.h-h2)))   
        if(t1==1):
            gameDisplay.blit(b1.image,(b1.rect.x,display_height-h11))
            gameDisplay.blit(c1.image,(c1.rect.x,-(c1.rect.h-h22)))   
        if(t11==1):
            gameDisplay.blit(b11.image,(b11.rect.x,display_height-h111))
            gameDisplay.blit(c11.image,(c11.rect.x,-(c1.rect.h-h222))) 
        gameDisplay.blit(floor.image,(floor.rect.x,floor.rect.y))
        if(floor.rect.x<0 or floor1.rect.x<=0):
             gameDisplay.blit(floor1.image,(floor1.rect.x,floor1.rect.y))
        
        wynik(count,200,100)
        pygame.display.update()
        
        
       
    message_display('Game Over')  

    time.sleep(3)
    game_loop()
    
    
def paused(pause=True):

    k=0
    col1=red
    col2=black
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
               if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN: 
                   if(col1==red):
                       pause=False
                
               if event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT :
                   k+=1
               if event.key==pygame.K_ESCAPE:
                   pause=False
                   
               if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN: 
                   if(col2==red):
                       pause=False
                       game_intro()
                   

        if k%2==0:
            col1=red
            col2=black
        if k%2==1:
            col1=black
            col2=red
        
        #gameDisplay.fill(white)
        font = pygame.font.SysFont("comicsansms", 72)
        #largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Continue", font,col1)
        TextRect.center = ((display_width/2-150),(display_height/2+200))
        TextSurf1, TextRect1 = text_objects("Menu", font,col2)
        TextRect1.center = ((display_width/2+150),(display_height/2+200))
        
        TextSurf2, TextRect2 = text_objects("PAUSE", font,black)
        TextRect2.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf1, TextRect1)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        pygame.display.update()
        clock.tick(15)
        



music1=pygame.mixer.Sound("Batman1.wav")

music2=pygame.mixer.Sound("crush.wav")

music3=pygame.mixer.Sound("bonus.wav")

music4=pygame.mixer.Sound("level_up.wav")

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()


def text_objects(text, font,trans=black):
    textSurface = font.render(text, True, trans)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2-100))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

    
def message_display1(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2-100))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    
def wynik(count,h,k):
    text=str(count)
    largeText = pygame.font.Font('freesansbold.ttf',k)
    TextSurf, TextRect = text_objects(text, largeText) 
    TextRect.center = ((display_width/2),(display_height/2-h))
    gameDisplay.blit(TextSurf, TextRect) 

def crash():
    plik = open("music.txt")
    with plik as pl:
        music0 = plik.readline()
    plik.close()
    if(music0=="ON"):
        music2.play()
    message_display('Game Over')

class ptak(pygame.sprite.Sprite):

	def __init__(self):
         super().__init__()
         self.image = pygame.image.load('11.png') 
         self.rect = self.image.get_rect()
         self.w ,self.h=self.image.get_size()
         self.mask = pygame.mask.from_surface(self.image)
         #self.x=60
         #self.y=(display_height * 0.4)


class slupek(pygame.sprite.Sprite):

	def __init__(self):
         super().__init__()
         self.image = pygame.image.load('slupek_dl.png') 
         self.rect = self.image.get_rect()
         self.w,self.h=self.image.get_size()
         self.mask = pygame.mask.from_surface(self.image)
         self.rect.x=1000
         #self.y=-100
   
def game_loop():
    
    x = 60
    y = (display_height * 1/2)
    
    x0=display_width
    x1=display_width
    x11=display_width
    
    y_change = 0
    y_change1=0
    znak=0
    count=0
    a=0.05
    gameExit = False
    
    tt=0
    t1=0
    t11=0
    t=0
    k=0
    kk=0
    g=0
    ptaszek=ptak()
    ptaszek.rect.x=70
    ptaszek.rect.y=y
    pred=0
    skrzydlo=ptak()
    skrzydlo.image=pygame.image.load('skrzydlo.png') 
    skrzydlo.rect=skrzydlo.image.get_rect()
    floor=ptak()
    floor.image=pygame.image.load('floor.png') 
    floor.rect=floor.image.get_rect()
    floor.rect.x=0
    floor.rect.y=display_height-floor.h
    floor1=ptak()
    floor1.image=pygame.image.load('floor.png') 
    floor1.rect=floor1.image.get_rect()
    floor.w,floor.h=floor.image.get_size()
    floor1.w,floor.h=floor1.image.get_size()
    floor1.rect.x=display_width
    floor1.rect.y=display_height-floor1.h
    
    plik = open("music.txt")
    with plik as pl:
        music0 = plik.readline()
    plik.close()
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if k==0:
                        y_change=-10
                        k=1
                        znak=1
                        pred=1
                        if(music0=="ON"):
                            music1.play()
                        
                        
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused(pause)
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_change = 0
                    znak=-1
                    k=0
                    kk=0
                    
                 
       # gameDisplay.fill((0, 0, 255))
        gameDisplay.blit(bg, (0, 0))
        
        
        if(pred==0):
            wynik("Press SPACE to FLY",-100,50)
      
        if count>=6:
            pred=2
            if(music0=="ON"):
                 music4.play()
        if count>9:
            pred=3
            if(music0=="ON"):
                music4.play()
        if count>15:
            pred=4
            if(music0=="ON"):
                music4.play()
        
        if(k==1 and kk==0):
            y_change1=y_change
            kk=1
       
        ptaszek.rect.y += y_change1
        
        if(znak==1 and y_change1 <0):
            t=0
            y_change1 = min(y_change1+2,0)
            
                
           
        if(znak==-1 or kk==1):
            t+=1
            y_change1 = y_change1 + a*t
        
        g+=1
        if(g%15==0):
           skrzydlo.image= pygame.transform.flip(skrzydlo.image,False,True)
            
        if(znak==0 and g%20==0):
            y_change1=-5
            g=0
            
         
           
        if(znak==0 and g%20==10):
            y_change1=5
        
        if(znak==0):
            if(y_change1<0):
                y_change1+=0.5
            if(y_change1>0):
                y_change1-=0.5
           
        
        
        if(tt==0):
            h1=random.randrange(100, 400)
            b=slupek()
            c=slupek()
            b.rect.x=x0
            h2=500-h1
            c.rect.x=x0
            c.image=pygame.transform.flip(c.image,True, True)
            tt=1
            
        if(b.rect.x<=-b.w):
            h1=random.randrange(100, 400)
            b=slupek()
            c=slupek()
            b.rect.x=x0
            h2=500-h1
            c.rect.x=x0
            c.image=pygame.transform.flip(c.image,True, True)

        if(b.rect.x<=(2*display_width/3-b.w) or x1<(2*display_width/3)):
            if (t1==0):
                #h11=250
                h11=random.randrange(100, 400)
                t1=1
          
            b1=slupek()
            c1=slupek()
            b1.rect.x=x1
            h22=500-h11
            c1.rect.x=x1
            c1.image=pygame.transform.flip(c1.image,True, True)
            x1=x1-pred
            c1.rect.x=c1.rect.x-pred
            b1.rect.x=b1.rect.x-pred
            b1.rect.y=display_height-h11
            c1.rect.y=-(c1.rect.h-h22)
            gameDisplay.blit(b1.image,(b1.rect.x,display_height-h11))
            gameDisplay.blit(c1.image,(c1.rect.x,-(c1.rect.h-h22)))
        
            if(x1<=-b1.w):
                x1=display_width
        
        if(b.rect.x<=(display_width/3-b.w) or x1<=(2*display_width/3-b.w)  or ( b.rect.x>=(2*display_width/3-b.w) and x1<=(display_width/3-b.w)) or x11<=(display_width/3)):
            if (t11==0):
                #h111=250
                h111=random.randrange(100,400)
                t11=1
            b11=slupek()
            c11=slupek()
            b11.rect.x=x11
            h222=500-h111
            c11.rect.x=x11
            c11.image=pygame.transform.flip(c11.image,True, True)
            x11=x11-pred
            c11.rect.x=c11.rect.x-pred
            b11.rect.x=b11.rect.x-pred
            b11.rect.y=display_height-h111
            c11.rect.y=-(c11.rect.h-h222)
            gameDisplay.blit(b11.image,(b11.rect.x,display_height-h111))
            gameDisplay.blit(c11.image,(c11.rect.x,-(c11.rect.h-h222)))
         

            if(x11<=-b11.w):
                x11=display_width
                
        gameDisplay.blit(b.image,(b.rect.x,display_height-h1))
        gameDisplay.blit(c.image,(c.rect.x,-(c.rect.h-h2)))

        gameDisplay.blit(ptaszek.image,(ptaszek.rect.x,ptaszek.rect.y))
        skrzydlo.rect.x=ptaszek.rect.x+4
        skrzydlo.rect.y=ptaszek.rect.y+7
        
        gameDisplay.blit(skrzydlo.image,(skrzydlo.rect.x,skrzydlo.rect.y))
        
        gameDisplay.blit(floor.image,(floor.rect.x,floor.rect.y))
        floor.rect.x-=5
        
        if floor.rect.x<0 or floor1.rect.x<=0 :
            gameDisplay.blit(floor1.image,(floor1.rect.x,floor1.rect.y))
            floor1.rect.x-=5
        
        if floor.rect.x==-floor.w:
            floor.rect.x=display_width
        if floor1.rect.x==-floor1.w:
            floor1.rect.x=display_width
        
        
        b.rect.x=b.rect.x-pred
        c.rect.x=c.rect.x-pred
        b.rect.y=display_height-h1
        c.rect.y=-(c.rect.h-h2)
       
        wynik(count,200,100)
        if ptaszek.rect.y+ptaszek.h/2 >= display_height-floor.h:
            crash()

        if pygame.sprite.collide_rect(ptaszek, b) or pygame.sprite.collide_rect(ptaszek, c):
            animacja(ptaszek,skrzydlo,b,c,b1,c1,b11,c11,t1,t11,h1,h2,h11,h22,h111,h222,floor,floor1,count,music2)
            #crash()
        
        
        if ptaszek.rect.y<=0 :
            if ptaszek.rect.x+ptaszek.w>=c.rect.x or  ptaszek.rect.x+ptaszek.w>=x1 or ptaszek.rect.x+ptaszek.w>=x11:  
                #crash()
                animacja(ptaszek,skrzydlo,b,c,b1,c1,b11,c11,t1,t11,h1,h2,h11,h22,h111,h222,floor,floor1,count,music2)

#                
#    
        if t1==1:
           if pygame.sprite.collide_rect(ptaszek, b1) or pygame.sprite.collide_rect(ptaszek, c1) : 
               animacja(ptaszek,skrzydlo,b,c,b1,c1,b11,c11,t1,t11,h1,h2,h11,h22,h111,h222,floor,floor1,count,music2)

#                    
#            
        if t11==1:
            if pygame.sprite.collide_rect(ptaszek, b11) or pygame.sprite.collide_rect(ptaszek, c11):
                animacja(ptaszek,skrzydlo,b,c,b1,c1,b11,c11,t1,t11,h1,h2,h11,h22,h111,h222,floor,floor1,count,music2)
 
#                    
#            
        if  ptaszek.rect.x==(b.rect.x+b.w):
            count+=1   
            if(music0=="ON"):
                music3.play()
        
        if t1==1:
            if ptaszek.rect.x==(b1.rect.x+b.w):
                count+=1
                if(music0=="ON"):
                    music3.play()
        
        if t11==1:
            if ptaszek.rect.x==(b11.rect.x+b.w):
                count+=1
                if(music0=="ON"):
                    music3.play()
#      
       
       
        
       
        Best_Score(count)
        
        pygame.display.update()
        clock.tick(60)

def game_intro():
    g=0
    intro = True
    k=0
    y_change1=0
    col1=red
    col2=black
    col3=black
    floor=ptak()
    floor.image=pygame.image.load('floor.png') 
    floor.rect=floor.image.get_rect()
    floor.rect.x=0
    floor.rect.y=display_height-floor.h
    floor1=ptak()
    floor1.image=pygame.image.load('floor.png') 
    floor1.rect=floor1.image.get_rect()
    floor.w,floor.h=floor.image.get_size()
    floor1.w,floor.h=floor1.image.get_size()
    floor1.rect.x=display_width
    floor1.rect.y=display_height-floor1.h
    y = (display_height * 1/2)
    ptaszek=ptak()
    ptaszek.rect.x=70
    ptaszek.rect.y=y
    skrzydlo=ptak()
    skrzydlo.image=pygame.image.load('skrzydlo.png') 
    skrzydlo.rect=skrzydlo.image.get_rect()
    opcja=0
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
               if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN: 
                   if(col1==red):
                       intro=False
                       game_loop()
                   if(col2==red):
                       score()
                       intro=True
                   if(col3==red):
                       musicc()
                       
               if event.key==pygame.K_UP:
                   k-=1
               if event.key==pygame.K_DOWN:
                   k+=1
               if event.key==pygame.K_ESCAPE:
                   pygame.quit()
                   quit()
            if event.type == pygame.KEYUP:
                                    
               if event.key==pygame.K_UP or pygame.K_DOWN :
                   k=0
              
                   
        opcja=(opcja+k)%3
        if opcja==0:
            col1=red
            col2=black
            col3=black
        if opcja==1:
            col1=black
            col2=red
            col3=black
        if opcja==2:
            col1=black
            col2=black
            col3=red
            
        
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(floor.image,(floor.rect.x,floor.rect.y))
        floor.rect.x-=5
        if floor.rect.x<0 or floor1.rect.x<=0 :
            gameDisplay.blit(floor1.image,(floor1.rect.x,floor1.rect.y))
            floor1.rect.x-=5
        
        if floor.rect.x==-floor.w:
            floor.rect.x=display_width
        if floor1.rect.x==-floor1.w:
            floor1.rect.x=display_width
        
       
        g+=1
        if( g%20==0):
            y_change1=-5
        
        
        if( g%20==10):
            y_change1=5
      
        ptaszek.rect.y += y_change1
        
        skrzydlo.rect.x=ptaszek.rect.x+4
        skrzydlo.rect.y=ptaszek.rect.y+7
        if(g%5==0):
           skrzydlo.image= pygame.transform.flip(skrzydlo.image,False,True) 
        
        gameDisplay.blit(ptaszek.image,(ptaszek.rect.x,ptaszek.rect.y))  
        gameDisplay.blit(skrzydlo.image,(skrzydlo.rect.x,skrzydlo.rect.y))
        font = pygame.font.SysFont("comicsansms", 72)
        #largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Start", font,col1)
        TextRect.center = ((display_width/2),(display_height/2-100))
        TextSurf1, TextRect1 = text_objects("Best score", font,col2)
        TextRect1.center = ((display_width/2),(display_height/2))
        TextSurf2, TextRect2 = text_objects("Sounds", font,col3)
        TextRect2.center = ((display_width/2),(display_height/2+100))
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf1, TextRect1)
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
        



def score():
    g=0
    intro1= True
    k=0
    y_change1=0
    col1=red
    floor=ptak()
    floor.image=pygame.image.load('floor.png') 
    floor.rect=floor.image.get_rect()
    floor.rect.x=0
    floor.rect.y=display_height-floor.h
    floor1=ptak()
    floor1.image=pygame.image.load('floor.png') 
    floor1.rect=floor1.image.get_rect()
    floor.w,floor.h=floor.image.get_size()
    floor1.w,floor.h=floor1.image.get_size()
    floor1.rect.x=display_width
    floor1.rect.y=display_height-floor1.h
    y = (display_height * 1/2)
    ptaszek=ptak()
    ptaszek.rect.x=70
    ptaszek.rect.y=y
    skrzydlo=ptak()
    skrzydlo.image=pygame.image.load('skrzydlo.png') 
    skrzydlo.rect=skrzydlo.image.get_rect()
    
    while intro1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
               if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN: 
                       game_intro()
               if event.key==pygame.K_ESCAPE:
                   pygame.quit()
                   quit()
                   

     
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(floor.image,(floor.rect.x,floor.rect.y))
        floor.rect.x-=5
        if floor.rect.x<0 or floor1.rect.x<=0 :
            gameDisplay.blit(floor1.image,(floor1.rect.x,floor1.rect.y))
            floor1.rect.x-=5
        
        if floor.rect.x==-floor.w:
            floor.rect.x=display_width
        if floor1.rect.x==-floor1.w:
            floor1.rect.x=display_width
        
       
        g+=1
        if( g%20==0):
            y_change1=-5
        
        
        if( g%20==10):
            y_change1=5
      
        ptaszek.rect.y += y_change1
        
        skrzydlo.rect.x=ptaszek.rect.x+4
        skrzydlo.rect.y=ptaszek.rect.y+7
        if(g%5==0):
           skrzydlo.image= pygame.transform.flip(skrzydlo.image,False,True) 
        
        gameDisplay.blit(ptaszek.image,(ptaszek.rect.x,ptaszek.rect.y))  
        gameDisplay.blit(skrzydlo.image,(skrzydlo.rect.x,skrzydlo.rect.y))
        font = pygame.font.SysFont("comicsansms", 72)
        #largeText = pygame.font.Font('freesansbold.ttf',100)
        
        TextSurf1, TextRect1 = text_objects("Back", font,red)
        TextRect1.center = ((display_width/2),(display_height/2+200))
        gameDisplay.blit(TextSurf1, TextRect1)
        Show_Score()
        pygame.display.update()
        clock.tick(15)
        


def musicc():
    g=0
    intro = True
    k=0
    y_change1=0
    col1=red
    col2=black
    col3=black
    floor=ptak()
    floor.image=pygame.image.load('floor.png') 
    floor.rect=floor.image.get_rect()
    floor.rect.x=0
    floor.rect.y=display_height-floor.h
    floor1=ptak()
    floor1.image=pygame.image.load('floor.png') 
    floor1.rect=floor1.image.get_rect()
    floor.w,floor.h=floor.image.get_size()
    floor1.w,floor.h=floor1.image.get_size()
    floor1.rect.x=display_width
    floor1.rect.y=display_height-floor1.h
    y = (display_height * 1/2)
    ptaszek=ptak()
    ptaszek.rect.x=70
    ptaszek.rect.y=y
    skrzydlo=ptak()
    skrzydlo.image=pygame.image.load('skrzydlo.png') 
    skrzydlo.rect=skrzydlo.image.get_rect()
    opcja=0
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
               if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN: 
                   if(col1==red):
                       music="ON"
                       save_music(music)
                       game_intro()
                   if(col2==red):
                       music="OFF"
                       save_music(music)
                       game_intro()
                       
               if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                   k+=1
             
               if event.key==pygame.K_ESCAPE:
                   pygame.quit()
                   quit()
           
            
                   
        
        if k%2==0:
            col1=red
            col2=black
           
        if k%2==1:
            col1=black
            col2=red
        
            
        
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(floor.image,(floor.rect.x,floor.rect.y))
        floor.rect.x-=5
        if floor.rect.x<0 or floor1.rect.x<=0 :
            gameDisplay.blit(floor1.image,(floor1.rect.x,floor1.rect.y))
            floor1.rect.x-=5
        
        if floor.rect.x==-floor.w:
            floor.rect.x=display_width
        if floor1.rect.x==-floor1.w:
            floor1.rect.x=display_width
        
       
        g+=1
        if( g%20==0):
            y_change1=-5
        
        
        if( g%20==10):
            y_change1=5
      
        ptaszek.rect.y += y_change1
        
        skrzydlo.rect.x=ptaszek.rect.x+4
        skrzydlo.rect.y=ptaszek.rect.y+7
        if(g%5==0):
           skrzydlo.image= pygame.transform.flip(skrzydlo.image,False,True) 
        
        gameDisplay.blit(ptaszek.image,(ptaszek.rect.x,ptaszek.rect.y))  
        gameDisplay.blit(skrzydlo.image,(skrzydlo.rect.x,skrzydlo.rect.y))
        font = pygame.font.SysFont("comicsansms", 72)
        #largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("ON", font,col1)
        TextRect.center = ((display_width/2),(display_height/2-100))
       
        TextSurf2, TextRect2 = text_objects("OFF", font,col2)
        TextRect2.center = ((display_width/2),(display_height/2+100))
        gameDisplay.blit(TextSurf2, TextRect2)

        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
        

#example of use:

game_intro()
game_loop()
pygame.quit()
quit()

         
         
         
         
