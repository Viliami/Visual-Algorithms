import pygame,random
from algorithms import *;

pygame.init()
screen = pygame.display.set_mode((600,600));
clock = pygame.time.Clock()
pygame.display.set_caption("Algorithms")
finished_sort = False
insertion_counter = 0

def draw_array(array):
    for i in range(0,len(array)):
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
    #clock.tick(120)

    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

    if(not finished_sort):
        finished_sort_x = insertion_sort(x_array,insertion_counter)
        finished_sort_y = insertion_sort(y_array,insertion_counter)
        if(finished_sort_x and finished_sort_y):
            finished_sort = True
            print("Done")
    #if(insertion_counter <= 598):
    insertion_counter+=1

    screen.fill((200,220,220)) #clear screen

    draw_array(x_array)

    pygame.display.flip() #update screen

