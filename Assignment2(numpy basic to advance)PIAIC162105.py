#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x
function1()


# In[40]:


# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    x = np.arange(10,37,dtype=np.float64).reshape(3,3,3)     #wrtie your code here


    return x
function2()


# In[148]:


def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[a%35 == 0] #wrtie your code here
    return x
function3()


# In[74]:


#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    arr[:,[0, 1]] = arr[:,[1, 0]]

    
    return arr #wrtie your code here
function4()


# In[79]:


#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros(20).reshape(4,5)
    return z

function5()


# In[84]:


#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr = np.zeros(10)
    arr[4]=10
    arr[7]= 20
  
    return arr
function6()


# In[89]:


#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.zeros(4, dtype=np.int64)
    
    return x

function7()


# In[95]:


#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = np.ones(10, dtype=np.int32).reshape(2,5)*6
  
    return x
function8()


# In[98]:


#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    
    a = np.arange(1,101)
    a = a[a%2 == 0]
  
    return a
function9()


# In[100]:


#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr-np.vstack(brr)
    return subt
function10()


# In[101]:


#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[1::2] = -1
    ans = arr  
    return ans
function11()


# In[104]:


#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = np.hstack((np.repeat(arr,3),arr,arr,arr))
  
    return ans
function12()


# In[113]:


#Task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr>5)&(arr<10)] 
  
    return ans
function13()


# In[115]:


#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    
    arr = np.arange(10, 34, 1) #write reshape code
    ans = np.split(arr,4)
  
    return ans
function14()


# In[132]:


#task15
def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[-4,  1,  7],[ 8,  2, -2],[ 6,  3,  9]])
    arr[0:2,2:2] = np.sort(arr[0:2,2:2] , axis = 0)
    ans = arr 
  
    return ans
   
function15()


# In[135]:


#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.hstack([x,y])
  
    return ans
function16()


# In[136]:


#task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    return np.where((arr%3 == 0)&(arr%5 == 0),"YES","NO")
function17()


# In[137]:


#task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = len(set(piaic)&set(students))
    return x
function18()


# In[140]:


#task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X =  np.arange(1,26).reshape(5,5,)
    W =  X.copy()
    W =  W.T
    b =  5
    output = (X*W)+b
    return output
    
function19()


# In[141]:


#task20
def fucntion20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def xyz(x):
        return x*2+3-2

    return xyz(x)
fucntion20()


# In[ ]:




