# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:25:48 2021

@author: saran
"""

###show fabbonacci series
def fab_sereries_generator():
    fab_series=[0,1]
    ### fabbonachi series
    for c in range(2, 24):
        next_ele=fab_series[c-2]+fab_series[c-1]
        fab_series.append(next_ele)
    print(fab_series)
    
####find second maximum number    
def second_max_number(arr):
    if len(arr)<2:
        print('cant find second max number')
        return 
    else:
        curr_max=-100000
        prev_max=-120000
        for i in range(0,len(arr)):
            if arr[i]>curr_max:
                prev_max=curr_max
                curr_max=arr[i]
            elif arr[i]>prev_max:
                prev_max=arr[i]
    return prev_max
print('second maximum number is',second_max_number([-5,-1,-13,-15,0,-11, -3]))

#####find an armstrong number
def is_armstrong_num(num):
    num=str(num)
    num=list(num)
    print(num)
    sum_num=0
    for i in range(0,len(num)):
        cube_of_num=int(num[i])*int(num[i])*int(num[i])
        sum_num=sum_num+cube_of_num
    print(cube_of_num)
    print(sum_num)
    if sum_num==num:
        print("num is armstrong number")
    else:
        print("num is not armstrong num")
is_armstrong_num(371)

#####que using arrays implement queue
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.queue=list()
    def push_que(self,num):
        if len(self.queue)==0:
            self.queue.append(num)
            self.front=0
            self.rear=0
        else:
            self.queue.append(num)
            self.rear=self.rear+1
    def pull_que(self):
        if len(self.queue)==0:
            print('empty_queue')
            
        else:
            self.queue.pop(0) 
            self.rear=self.rear-1
    def display_que(self):
        print(self.queue)
        print(self.front)
        print(self.rear)
        
first_que=Queue()
first_que.display_que()
first_que.push_que(5)
first_que.push_que(6)
first_que.push_que(7)
first_que.push_que(8)
first_que.display_que()
first_que.pull_que()
first_que.display_que()                
                
            


