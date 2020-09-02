import pygame;
import random,time,keyboard,datetime;
pygame.init();
gd = pygame.display.set_mode((600,600))
pygame.display.set_caption('Pong');
def score(number1,number2):
    font = pygame.font.SysFont(None,40);
    text = font.render(str(number1),True,(255,255,255))
    gd.blit(text,(200,0));
    text = font.render(str(number2),True,(255,255,255))
    gd.blit(text,(400,0));
def pong(x1,y1,x2,y2,bx,by):
    pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
    pygame.draw.rect(gd,(255,255,255),[(x1),(y1),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x1),(y1-10),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x1),(y1-20),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x1),(y1-30),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x1),(y1-40),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x1),(y1-50),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x1),(y1-60),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x2),(y2),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x2),(y2-10),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x2),(y2-20),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x2),(y2-30),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x2),(y2-40),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x2),(y2-50),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(x2),(y2-60),10,10]);
    pygame.draw.rect(gd,(255,255,255),[(bx),(by),10,10]);
def text_objects(text,font,renk):
    textS=font.render(text,True,renk)
    return(textS)
def pprint(text):
    LT = pygame.font.Font('freesansbold.ttf',40);
    Text = text_objects(text,LT,(255,255,255))
    gd.blit(Text,(180,80))
    pygame.display.update();
def pprint2(text,x,y,renk):
    LT = pygame.font.Font('freesansbold.ttf',15);
    Text = text_objects(text,LT,renk)
    gd.blit(Text,(x,y))
    pygame.display.update();
def game_loop():
    while True:
        pause=1;
        robo=0;
        sayi1=0;
        sayi2=0;
        x1 = 20;
        y1 = 330;
        x2 = 570;
        y2 = 330;
        bx = 290
        by = 290
        yonx=1;
        yony=1;
        Dur=0;
        gd.fill((0,0,0))
        pygame.display.update();
        pprint('Pong');
        time.sleep(1);
        gd.fill((0,0,0))
        pprint('by Can ER')
        time.sleep(1);
        gd.fill((0,0,0))
        pygame.draw.rect(gd,(255,255,255),[200,200,200,50]);
        pygame.draw.rect(gd,(0,0,0),[205,205,190,40]);
        pprint2("Bilgisayara Karsi",210,220,(255,255,255))
        pygame.draw.rect(gd,(255,255,255),[200,260,200,50]);
        pygame.draw.rect(gd,(0,0,0),[205,265,190,40]);
        pprint2("2 Oyunculu",210,280,(255,255,255))
        pygame.display.update();
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            mouse = pygame.mouse.get_pos();
            click = pygame.mouse.get_pressed();
            if (200<mouse[0]<400) and (200<mouse[1]<250) and (click[0]==1):
                robo=1;
                break;
            if (200<mouse[0]<400) and (260<mouse[1]<310) and (click[0]==1):
                robo=0;
                break;
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pong(x1,y1,x2,y2,bx,by);
            score(sayi1,sayi2);
            pygame.display.update();
            key = pygame.key.get_pressed();
            if key[pygame.K_UP]:
                if (y2-10)>=50:
                    y2=y2-10;
                    pause=0;
                time.sleep(0.001);
            if key[pygame.K_DOWN]:
                if (y2+10)<=590:
                    y2=y2+10;
                    pause=0;
                time.sleep(0.001);
            if robo==0:
                if key[pygame.K_w]:
                    if (y1-10)>=50:
                        y1=y1-10;
                        pause=0;
                    time.sleep(0.001);
                if key[pygame.K_s]:
                    if (y1+10)<=590:
                        y1=y1+10;
                        pause=0;
                    time.sleep(0.001);
            else:
                if (y1-30)>by:
                    if (y1-10)>=50:
                        y1=y1-10;
                    time.sleep(0.001);
                if (y1-30)<by:
                    if (y1+10)<=590:
                        y1=y1+10;
                    time.sleep(0.001);
            if pause==0:
                if bx>=590:
                    sayi1+=1;
                    pong(x1,y1,x2,y2,bx,by);
                    score(sayi1,sayi2);
                    pygame.display.update();
                    time.sleep(1);
                    bx = 290
                    by = 290
                    yonx=1;
                    yony=1;
                    x1 = 20;
                    y1 = 330;
                    x2 = 570;
                    y2 = 330;
                if bx<=0:
                    sayi2+=1;
                    pong(x1,y1,x2,y2,bx,by);
                    score(sayi1,sayi2);
                    pygame.display.update();
                    time.sleep(1);
                    bx = 290
                    by = 290
                    yonx=2;
                    yony=2;
                    x1 = 20;
                    y1 = 330;
                    x2 = 570;
                    y2 = 330;
                if by>=590:
                    yony=2
                if by<=0:
                    yony=1
                if yony==1:
                    by=by+6;
                if yony==2:
                    by=by-6;
                if (by<=y1 and by>=(y1-60)) and bx<=20:
                    yonx=2
                if (by<=y2 and by>=(y2-60)) and bx>=570:
                    yonx=1
                if yonx==1:
                    bx=bx-10;
                if yonx==2:
                    bx=bx+10;
                if key[pygame.K_0]:
                    break;
                if sayi1==10:
                    gd.fill((0,0,0))
                    pprint2("Player1 Wins",210,220,(255,255,255))
                    pprint2("Score: "+str(sayi1)+" - "+str(sayi2),220,280,(255,255,255))
                    pygame.display.update();
                    time.sleep(5)
                    break;
                if sayi2==10:
                    gd.fill((0,0,0))
                    pprint2("Player2 Wins",210,220,(255,255,255))
                    pprint2("Score: "+str(sayi1)+" - "+str(sayi2),210,280,(255,255,255))
                    pygame.display.update();
                    time.sleep(5)
                    break;
                pygame.display.update();
                time.sleep(0.025);
game_loop();
