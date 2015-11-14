import pygame,random
from algorithms import *;

pygame.init()
screen = pygame.display.set_mode((600,600));
clock = pygame.time.Clock()
pygame.display.set_caption("Bubble sort")
#array = [2,4,1,6,3,5,7,8,9,10,11,12]
finished_sort = False

def draw_array(array):
    for i in range(0,len(array)):
        #pygame.draw.circle(screen,(255-(i//2),0,0),(array[i],array[i]-i+100),10)
        pygame.draw.circle(screen,(255-(i//3),0,0),(x_array[i],y_array[i]),10)
    pass

def gen_array(size):
    array = []
    for i in range(0,size):
        rand_num = random.randint(0,size)
        while(rand_num in array):
            rand_num = random.randint(0,size)
        array.append(rand_num)
    return array

x_array = gen_array(600)
y_array = gen_array(600)

print("Before")
print(x_array)

while(True):
    clock.tick(60)
    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
    if(not finished_sort):
        finished_sort_x = bubble_sort(x_array)
        finished_sort_y = bubble_sort(y_array)
        if(finished_sort_x and finished_sort_y):
            finished_sort = True
            print("Done")
    screen.fill((200,220,220))
    draw_array(x_array)
    pygame.display.flip()
