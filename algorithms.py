
def bubble_sort(array):
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

def insertion_sort(array,counter):
    for i in range(0,counter):
        if(array[i] < array[counter]):
            temp = array[counter]
            array.pop(counter)            
            array.insert(i,temp)
    if(counter == 599):
        return True
    return False
