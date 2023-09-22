from random import randint
b = 20 #размер списка
a = []
for i in range(b):
    a.append(randint(1, 999999))
for i in range(len(a)): #выводим список в столбик
    print(a[i])

def shaker_sort(a): 
    length = len(a) 
    swapped = True
    start_index = 0
    end_index = length - 1
    
    while (swapped == True): 
        
        swapped = False
          
        # проход слева направо
        for i in range(start_index, end_index): 
            if (a[i] > a[i + 1]) : 
                # обмен элементов
                a[i], a[i + 1] = a[i + 1], a[i] 
                swapped = True
  
        # если не было обменов прерываем цикл
        if (not(swapped)): 
            break

        swapped = False

        end_index = end_index - 1
  
        #проход справа налево
        for i in range(end_index - 1, start_index - 1, -1): 
            if (a[i] > a[i + 1]): 
                # обмен элементов
                a[i], a[i + 1] = a[i + 1], a[i] 
                swapped = True
 
        start_index = start_index + 1
                 
  
        
print("After sort")
for i in range(len(a)): #выводим список в столбик
        print(a[i])