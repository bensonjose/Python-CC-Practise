# LINEAR SEARCH.*********************************************LINEAR SEARCH**********************************LINEAR SEARCH******
'''
def linear(lis,n,target): 
    for i in range(n):
        if(lis[i]==target):
            print("Your Target element is found at the Index ",i,"!")
        else:
            print("Target element not found!")
            
                   
n=int(input("Enter the size of list: "))
target=int(input("Target element: "))
lis=[]
for i in range(n):
    element=int(input(f"enter the {i} element-->"))
    lis.append(element)

# print(lis)
linear(lis,n,target)
print(lis)
# print(lis.append(element))
'''
# **********************************XXXXX***LINEAR SEARCH***XXXXX******************************************************





# INSERTION SORT.********************INSERTION SORT**************************INSERTION SORT********************************

def insertion_sort(list_a):
    # indexing_length=range(1,len(list_a))   #----->You can create a variable to assign range if needed.
    for i in range(1,len(list_a)):
        # value_to_sort=list_a[i]  #------->You can assign list_a[i] into value_to_sort if required.
        
        while list_a[i-1]>list_a[i] and i>0:   #we take (i>0) because the first left index,
            # we are assuming it to be sorted and to the right of that is the unsorted list.
            # Also the condition----(list_a[i-1]>list_a[i]) means that if value to the left i.e a[i-1] is greater 
            # than the value to the right i.e a[i] then swapping takes place.
            list_a[i],list_a[i-1]=list_a[i-1],list_a[i]
            i-=1   # i=i-1           
    return list_a

# Taking user input.
n=int(input("Size of list: "))                                      #    |
list_a=[]                                                           #    |
i=1                                                                 #    |
for i in range(i,n+1):                                              #    |------->>>(Taking User Input)
    element=int(input(f"enter the element {i}-->"))                 #    |
    list_a.append(element)                                          #    |
                                                                    #    |
print("The Sorted List by Insertion Sort--->",insertion_sort(list_a))              

# print(insertion_sort([5,6,2,3,8,1,9]))   #Here we are passing input as an argument

# print("The Sorted list by Insertion Sort-->",insertion_sort([2,3,4,1,6,8,5,15,12,20,17,24]))  #Here we are passing input as an argument

# ***************************************XXXXXX******INSERTION SORT******XXXXXX*****************************************



# *****************BUBBLE SORT*******************BUBBLE SORT***********************************************************
'''
def bubble(list_a):
    for i in range(len(list_a)-1,0,-1):
    # for i in range(len(list_a)-1,0,-1):
        for j in range (i):
            if list_a[j]>list_a[j+1]:
                # temp=list_a[j]
                # list_a[j]=list_a[j+1]
                # list_a[j+1]=temp
                list_a[j],list_a[j+1]=list_a[j+1],list_a[j]
                
        
# list_a=[2,3,4,15,1,0,9,12,18,651,99]
# bubble(list_a)
# print(list_a)
n=int(input("Size of list: "))                                      
list_a=[]                                                               
i=1                                                                     
for i in range(i,n+1):                                                  
    element=int(input(f"enter the element {i}-->"))                     
    list_a.append(element) 
bubble(list_a)
print("Sorted list by Bubble sort is",list_a)
'''
# *********************************************xxxxxxxx*****Bubble sort**xxxxxxx***************************************



# ******************SELECTION SORT**************SELECTION SORT******************SELECTION SORT***************************
'''
def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]: 
                min_value = j


        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

# print(selection_sort([2,5,1,0,12,15,24,9,7,3,6]))   #Passing list as an argument

n=int(input("Size of list: "))                                      
list_a=[]                                                           
i=1                                                                     
for i in range(i,n+1):                                                                                                   
    element=int(input(f"enter the element {i}-->"))                 
    list_a.append(element)                                      
                                                        
print("The Sorted List by Selection Sort is--->",selection_sort(list_a))
'''

# *********************************XXXXXXX******SELECTION SORT******XXXXXXX**********************************************************
