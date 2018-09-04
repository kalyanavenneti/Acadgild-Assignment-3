
# coding: utf-8

# # Date 3rd September 2018 - Session 3 - Assignment 3

# In[12]:


# Question 1.1: Write a Python Program to implement your own myreduce() function which works exactly like Python's 
# built-in function reduce()


def myreducefunc(func_input,list_input):
    l1=list_input[0]
    l2=list_input[1]
    output=func_input(l1,l2)
    l1=output
    count=0
    for val in list_input:
        count=count+1
        if count > 2:
            l2 = val
            output=func_input(l1,l2)
            l1=output
    return output
  
def funcAdd(a,b):
    return a+b

list_input=[1,2,3,4,5,6,7]
print("Add function", myreducefunc(funcAdd, list_input))


# In[16]:


# Question 1.2: Write a Python program to implement your own myfilter() function which works exactly like Python's 
# built-in function filter()

def myfilter(Func_input,List_input):    
    Output=[]
    for item in List_input:
        if Func_input(item)==True:
            Output.append(item)
    return Output

#Event Check Functions
def Func_Even(int_Input):
    if int_Input%2==0:
        return True

def Func_Odd(int_Input):
    if int_Input%2!=0:
        return True

List_input=list(range(1,50))
print('\nEven Numbers from list: \n\t', myfilter(Func_Even, List_input))
print('\nOdd Number from list: \n\t', myfilter(Func_Odd, List_input))


# In[17]:


# Question 2: Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

list1=[letter for letter in 'ACADGILD']
print(list1)

str1=('x','y','z')
list2=[val*num for val in str1 for num in range(1,5)]
print(list2)

str1=('x','y','z')
list3=[val*num for num in range(1,5) for val in str1]
print(list3)

int1=(2,3,4)
list4=[[val+num] for val in int1 for num in range(0,3)]
print(list4)

int1=(2,3,4,5)
list5=[[val+num for val in int1] for num in range(0,4)]
print(list5)

int2=(1,2,3) 
list6=[(num, val) for val in int2 for num in range(1,4)]
print(list6)


# In[22]:


# Question 3: Implement a function longestWord() that takes a list of words and returns the longest one

def longestword(word_input):
    long_word=''
    for word in word_input:        
        if len(long_word)<len(word):
            long_word=word
    return long_word


#Call the function with a list
str1='Implement List comprehensions to produce the following lists'
Words=list(str1.split(' '))
print('List of words: \n',Words, '\n')
print('Longest word: \n',longestword(Words))

