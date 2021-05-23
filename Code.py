#project DSA
# # KNOWN BUGS:
# CAN ONLY WORK ON MAZES THAT ARE 15X15
# THE MAZE HAS TO START AND STOP AT THE SAME COORDINATES
# YOU NEED TO RERUN THE PROGRAM IF YOU WIN OR LOSE
#global variables can be avoided by adding parameters in functions
import pygame
import sys
import time
fps=30
fpsclock=pygame.time.Clock()


pygame.init()
window=pygame.display.set_mode((600,600))
pygame.display.set_caption("Maze")

def draw(lst):
    x=0
    y=0
    width=40
    height=40
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if lst[row][col]==1:
                pygame.draw.rect(window,(255,0,0),(x,y,width,height))
                
                
            x+=width
        x=0
        y+=height
lev_1=[[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [0,0,1,0,0,0,1,0,1,1,1,1,1,1,1],
        [1,0,1,1,1,1,1,0,1,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,1,1,1,0,1],
        [1,1,1,0,1,1,0,1,1,1,1,0,0,0,1],
        [1,0,0,0,1,0,0,1,0,0,0,0,1,1,1],
        [1,1,1,1,1,1,0,1,0,1,0,1,1,0,1],
        [1,1,0,0,0,0,0,1,0,1,1,1,1,1,1],
        [1,1,0,1,1,1,0,1,0,0,1,0,0,0,1],
        [1,1,0,0,0,1,1,1,1,0,0,0,1,1,1],
        [1,0,0,1,0,0,0,0,1,0,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],

       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1], 
        [0,0,1,1,1,0,1,0,1,0,1,0,0,0,1],
        [1,0,0,0,1,0,1,0,1,0,1,0,1,1,1],
        [1,1,1,1,1,0,1,1,1,0,1,0,0,0,1], 
        [1,0,0,0,0,0,0,0,0,0,1,1,1,0,1], 
        [1,0,1,0,1,0,0,1,1,0,1,0,0,0,1], 
        [1,0,1,0,1,0,0,0,1,0,1,0,1,1,1], 
        [1,0,1,0,1,1,1,0,1,0,1,0,0,0,1], 
        [1,0,1,0,1,0,1,1,1,0,1,1,1,0,1], 
        [1,0,1,0,0,0,0,0,1,0,1,0,1,0,1], 
        [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1], 
        [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0],
        [1,0,0,0,1,0,1,0,1,0,0,0,1,0,1], 
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
 
       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
        [0,0,1,0,1,1,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,1,0,1,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,0,1,1,1,0,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,0,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1,1,1,0,1,0,1,0,0],
        [1,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
 
       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,1,1,1,0,1,0,1],
        [0,0,1,0,1,1,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,0,0,1,1,1,1,1,0,0,0,1],
        [1,0,1,0,1,0,0,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,0,1,0,1,0,0,0,0,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1,0,0,0,1],
        [1,0,1,0,1,0,1,0,0,0,1,0,1,1,1],
        [1,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,0,1,0,0],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]], 

       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [0,0,1,0,0,0,1,0,1,1,1,1,1,1,1],
        [1,0,1,1,1,1,1,0,1,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,1,1,1,0,1],
        [1,1,1,0,1,1,0,1,1,1,1,0,0,0,1],
        [1,0,0,0,1,0,0,1,0,0,0,0,1,1,1],
        [1,1,1,1,1,1,0,1,0,1,0,1,1,0,1],
        [1,1,0,0,0,0,0,1,0,1,1,1,1,1,1],
        [1,1,0,1,1,1,0,1,0,0,1,0,0,0,1],
        [1,1,0,0,0,1,1,1,1,0,0,0,1,1,1],
        [1,0,0,1,0,0,0,0,1,0,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]]
visited=[]
lives=3
font_details=pygame.font.Font(None,32)
back_track =font_details.render("DON'T BAACKTRACK",True,(0,0,0))#takes three parameters, text, antialias, colour 

         
        
        
        
    
# if len(visited)==len(path):
#     lives+=1
dash=pygame.image.load('youwin.jpg')
you_lose=pygame.image.load('youlose.jpg')
back_track=pygame.image.load('back_track.png')
i=lev_1[0]
quitt=False
count=0
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        else:
            if i==lev_1[-1] and winning:
                print(i)
                window.fill((225,225,225))
                time.sleep(5)
                window.blit(dash,(0,0))
                pygame.display.update()
                quitt=True
                run=False
            if winning and count<len(lev_1)-1:
                if len(visited)==len(path[count]):
                     lives+=1
                     print(lives)
                window.fill((0,0,0))
                x1=0
                y1=80
                countx=0
                county=0
                winning=False
                visited=[]
                discovered=[]
                back_tracking=False
                print(visited,path[count])
                
                count+=1
                i=lev_1[count]
            if lives!=0 and not winning:
                draw(i)
                move(i)
            elif lives==0:
                window.fill((225,225,225))
                window.blit(you_lose,(0,0))
                pygame.display.update()
    pygame.display.update()
    
while quitt and not run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             quit()
        else:
            window.blit(dash,(0,0))
            pygame.display.update()
quit()
