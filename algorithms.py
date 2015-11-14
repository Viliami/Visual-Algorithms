
def bubble_sort(array):
    global finished_sort;
    swaps = 0
    for i in range(0,len(array)-1):
        if(array[i] < array[i+1]):
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            swaps+=1
    if(swaps == 0):
        return True
    return False
