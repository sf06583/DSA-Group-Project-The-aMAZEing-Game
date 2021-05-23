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

         
def shortestPath(lst):
    Source=31
    discovered=[]
    distance={}
    q=[]
    parent={}
    for i in range(1,226):
        distance[i]=float("inf")
        q.append(i)
    distance[Source]=0
    #print(distance)
    while len(q)!=0:
        nbr=[]
        
        S=""
        for i in q:
            if S=="":
                S=i
            if distance[i]<distance[S]:
                S=i
        if S%15==0:
            i=(S-1)//15
        else:
            i=S//15
        j=(S%15)-1
        if S not in discovered:
            q.remove(S)
            discovered.append(S)
        if S>15 and lst[i-1][j]==0:#not top wall
            nbr.append(S-15)
        if S%15!=0 and lst[i][j+1]==0:#not right wall
            nbr.append(S+1)
        
        if S<=15*14 and lst[i+1][j]==0:#not bottom wall
            nbr.append(S+15)
        if S%15!=1 and lst[i][j-1]==0:#not left wall
            nbr.append(S-1)
        for i in nbr:
          if i not in discovered:
            if distance[S]+1<distance[i]:
                distance[i]=distance[S]+1
                parent[i]=S
    path=[]
    i=195
    while i!= 31:
        path.append((parent[i],i))
        i=parent[i]
    return path[::-1]
    #return distance[to]
path=[]
for i in lev_1:
    path.append(shortestPath(i))
    
run=True
x1=0
y1=80
countx=0
county=0
winning=False
back_tracking=False
def move(lst):
    global x1
    global y1
    global run
    global visited
    global lives
    global winning
    global back_tracking
    width=40
    height=40 
    font_details=pygame.font.Font(None,32)
    back_track =font_details.render("DON'T BAACKTRACK",True,(0,0,0))#takes three parameters, text, antialias, colour  
    key_input = pygame.key.get_pressed() 
    try: 
     if key_input[pygame.K_LEFT]:
        if lst[y1//width][(x1-width)//40]==1:
          if lives!=0:
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1
        elif (x1 -width,y1) not in visited:
            x1 = x1 -width
            visited.append((x1,y1))
            print(visited)
        else:
            back_tracking=True
            print("don't backtrack")
     if key_input[pygame.K_DOWN]:
        if lst[(y1+height)//width][x1//40]==1:
          if lives!=0:  
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1 
          else:
              run=False
        elif (x1,y1 + height) not in visited:
            y1 = y1 + height
            visited.append((x1,y1))
            print(visited)
        else:
            back_tracking=True
            print("don't backtrack")
     if key_input[pygame.K_UP]:
        if lst[(y1-height)//width][x1//40]==1:
          if lives!=0:
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1
          else:
              run=False
        elif (x1,y1-height) not in visited:
            y1 = y1-height
            visited.append((x1,y1))
            print(visited)
        else:
            back_tracking=True
            print("don't backtrack")
     if key_input[pygame.K_RIGHT]:
        if lst[y1//width][(x1+width)//40]==1:
          if lives!=0:
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1
          else:
              run=False
        elif (x1 + width,y1) not in visited:
            x1 = x1 + width
            visited.append((x1,y1))
            print(visited)
        else:
            back_tracking=True
            print("don't backtrack")
     pygame.draw.rect(window,(0,225,0),(x1,y1,width,height))
     #pygame.display.update()
     if (x1,y1)==(560, 480):
         winning=True

    except:
         winning=True
         window.fill((225,225,225))
         pygame.display.update()
         window.blit(dash,(0,0))
         
        
        
        
            
        
        
    
# if len(visited)==len(path):
#     lives+=1
dash=pygame.image.load('youwin.jpg')
you_lose=pygame.image.load('youlose.jpg')
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
