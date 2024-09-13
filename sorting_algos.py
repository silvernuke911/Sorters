import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from matplotlib.animation import PillowWriter

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            print(arr)
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr

def BubbleSort(arr):
    didswap=True
    length=len(arr)
    while didswap==True:
        i=0
        length-=1
        didswap=False
        while i<length:
            if arr[i]>arr[i+1]:
                didswap=True
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
            i+=1

def bubbleSortAnim(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def BubbleSortAnim(arr):
    didswap=True
    length=len(arr)
    ret_arr=[]
    while didswap==True:
        i=0
        length-=1
        didswap=False
        while i<length:
            x=[]
            if arr[i]>arr[i+1]:
                didswap=True
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                j=arr
                print(arr,j)
                ret_arr.append(tuple(j))
            i+=1
    return ret_arr

def FisherYatesShuffle(list_arr):
    length=len(list_arr)
    last_index=length-1

    while last_index>0:
        rand_index = round(rnd.random()*last_index)
        temp=list_arr[last_index]
        list_arr[last_index]=list_arr[rand_index]
        list_arr[rand_index]=temp
        last_index-=1

def is_sorted(array):
    length=len(array)
    if length==1:
        return True
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return False
    return True

x=[]
y=[]
n=30
for i in range(n):
    x.append(i)
    y.append(i)
plt.bar(x,y)
plt.show()
# for i in range(n):
#     plt.clf()
#     plt.bar(x,y)
#     plt.pause(0.01)
#     FisherYatesShuffle(y)
    
print(y)
FisherYatesShuffle(y)
print(y)
# for i in range(100):
#     plt.clf()
#     plt.bar(x,y)
#     plt.pause(0.1)
#     BubbleSortAnim(y)
#     print(y)
#     if  is_sorted(y)==True:
#         break


fig = plt.figure()

plt.xlim(0, n)
plt.ylim(0, n)

ret_arr=BubbleSortAnim(y)
print(ret_arr)
metadata = dict(title='Movie', artist='silver')
writer = PillowWriter(fps=15, metadata=metadata)

with writer.saving(fig, "bubble6.gif", 100):
    for i in range(len(ret_arr)):
        y=list(ret_arr[i])
        plt.bar(x,y)
        writer.grab_frame()
        print(x,list(ret_arr[i]))
        plt.pause(0.001)
        print(str(round(i/len(ret_arr),2)*100)+'%')
        plt.clf()
print('Done!')



def BubbleSort(arr):
    didswap=True
    length=len(arr)
    while didswap==True:
        i=0
        length-=1
        didswap=False
        while i<length:
            if arr[i]>arr[i+1]:
                didswap=True
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                #print(arr)
            i+=1

def InsertionSort(arr):
    length=len(arr)
    for i in range(length):
        current_val=arr[i]
        j=i-1
        while (j>=0 and arr[j]>current_val):
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=current_val
            #print(arr)

def QuickSort(arr,lowindex=0):
    highindex=len(arr)
    def Swap(arr,index1,index2):
        temp=arr[index1]
        arr[index1]=arr[index2]
        arr[index2]=temp
    def Partition(arr,low,high):
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<pivot:
                i+=1
                Swap(arr,i,j)
    if lowindex<highindex:
        pi=Partition(arr,lowindex,highindex)
        QuickSort(arr,lowindex,pi-1)
        QuickSort(arr,pi+1,highindex)
    
y=[]
for i in range(1,20+1):
    y.append(i)
FisherYatesShuffle(y)
print(y)
QuickSort(y)
print(y)

# def QuickSort(arr,lowindex=0,highindex=len(arr)):
#     def Swap(arr,index1,index2):
#         temp=arr[index1]
#         arr[index1]=arr[index2]
#         arr[index2]=temp
#     def Partition(arr,low,high):
#         pivot=arr[high]
#         i=low-1
#         for j in range(low,high):
#             if arr[j]<pivot:
#                 i+=1
#                 Swap(arr,i,j)
#     if lowindex<highindex:
#         pi=Partition(arr,lowindex,highindex)
#         QuickSort(arr,lowindex,pi-1)
#         QuickSort(arr,pi+1,highindex)

# function QuickSort{
#     local parameter InputArray.
#     local parameter lowindex is 0.
#     local parameter highindex is InputArray:length-1.
#     print ArrayDisplay(InputArray).
#     if lowindex<highindex{
#         local pi is Partition(InputArray,lowindex,highindex).
#         QuickSort(InputArray,lowindex,pi-1).
#         QuickSort(InputArray,pi+1,highindex).
#     }
#     local function Partition{
#         local parameter Array.
#         local parameter low.
#         local parameter high.
#         local pivot is Array[high].
#         local i is (low-1).
#         from {local j is low.} until not(j<=high) step {set j to j+1.} do {
#             if Array[j]<pivot {
#                 set i to i+1.
#                 swap(Array,i,j).
#             }
#         }
#         swap (Array, i+1, high).
#         return (i+1).
#     }
#     local function Swap{
#         local parameter Array1.
#         local parameter index1.
#         local parameter index2. 
#         local temp is array1[index1].
#         set Array1[Index1] to Array1[index2].
#         set Array1[index2] to temp.        
#     }
# }

# function BogoSort{
#     local parameter InputArray.
#     until IsSorted(InputArray) {
#         Shuffle(InputArray).
#         print ArrayDisplay(InputArray).
#     }
#     local function IsSorted{
#         local parameter Array.
#         local length is Array:length.
#         if length=1{
#             return true.
#         }
#         from {local i is 0.} until i=(length-1) step {set i to i+1.} do {
#             if Array[i]>Array[i+1]{
#                 return false.
#             }
#         }
#         return true.
#     }
#     local function Shuffle{
#         local parameter Array.
#         local length is Array:length.
#         local lastIndex is length-1.
#         until not(lastIndex>0){
#             local randIndex is round(random()*(lastIndex)).
#             local temp to Array[lastIndex].
#             set Array[lastIndex] to Array[randIndex].
#             set Array[randIndex] to temp.
#             set lastIndex to lastIndex-1.
#         }
#     }   
# }

# function MergeSort{
#     parameter InputArray.
#     print ArrayDisplay(InputArray).
#     local InputLength is InputArray:length.
#     if InputLength<2{
#         return.
#     }
#     local midindex is round(InputLength/2).
#     local lefthalf to list().
#     local righthalf to list().
#     from {local i is 0.} until i=midindex step {set i to i+1.} do {
#         lefthalf:add(0).
#     }
#     from {local i is 0.} until i=(inputlength-midindex) step {set i to i+1.} do {
#         righthalf:add(0).
#     }
#     from {local i is 0.} until (i<midindex)=false step{set i to i+1.} do {
#         set lefthalf[i] to InputArray[i].
#     }
#     from {local i is midindex.} until (i<InputLength)=false step{set i to i+1.} do {
#         set righthalf[i-midindex] to InputArray[i].
#     }
#     MergeSort(lefthalf).
#     MergeSort(righthalf).
#     Merge(InputArray,lefthalf,righthalf).
    
#     local function Merge{
#         local parameter Array.
#         local parameter LefthalfArr.
#         local parameter RightHalfArr.
#         print ArrayDisplay(Array).
#         local leftSize is LefthalfArr:length.
#         local rightSize is RightHalfArr:length.
#         local i is 0. local j is 0. local k is 0.
#         until not(i<leftsize and j<rightSize){
#             if leftHalfArr[i]<=rightHalfArr[j]{
#                 set Array[k] to lefthalfArr[i].
#                 set i to i+1.
#             }
#             else {
#                 set Array[k] to righthalfArr[j].
#                 set j to j+1.
#             }
#             set k to k+1.
#         }
#         until not(i<leftsize){
#             set Array[k] to lefthalfArr[i].
#             set i to i+1.
#             set k to k+1.
#         }
#         until not(j<rightsize){
#             set Array[k] to righthalfArr[j].
#             set j to j+1.
#             set k to k+1.
#         }
#     }
# }

# function ShellSort{
#     parameter InputArray.
#     local len is InputArray:length.
#     from {local gap is round(len/2).} until not(gap>0) step{set gap to round(gap/2).} do {
#         from {local i is gap.} until not(i<len) step{set i to i + 1.} do {
#             local k to InputArray[i].
#             local j to i.
#             until not(j>=gap and InputArray[j-gap]>k) {
#                 set InputArray[j] to InputArray[j-gap].
#                 set j to j-gap.
#             }
#             set InputArray[j] to k.
#             print ArrayDisplay(InputArray).
#         }  
#     }
# }

# function HeapSort{
#     parameter InputArray.
#     local N is InputArray:length.
#     from {local i is round(N/2)-1.} until not(i>=0) step {set i to i-1.} do {
#         heapify(InputArray,N,i).
#         print ArrayDisplay(InputArray).
#     }
#     from {local i is N-1.} until not(i>0) step {set i to i-1.} do {
#         local temp to InputArray[0].
#         set InputArray[0] to InputArray[i].
#         set InputArray[i] to temp.
#         heapify(InputArray,i,0).
#         print ArrayDisplay(InputArray).
#     }
#     local function heapify{
#         local parameter Arr.
#         local parameter ln.
#         local parameter i.
#         local largest is i.
#         local l is 2*i+1.
#         local r is 2*i+2.
#         if (l<ln and arr[l]>arr[largest]){
#             set largest to l.
#         }
#         if (r<ln and arr[r]>arr[largest]){
#             set largest to r.
#         }
#         if not(largest=i) {
#             local swap is arr[i].
#             set arr[i] to arr[largest].
#             set arr[largest] to swap.
#             heapify(arr,ln,largest).
#         }
#     }
# }

# function SelectionSort{
#     local parameter InputArray.
#     local length is InputArray:length.
#     from {local i is 0.} until i=(length-1) step {set i to i+1.} do {
#         local min to InputArray[i].
#         local MinIndex to i.
#         from {local j is i+1.} until j=length step {set j to j+1.} do{
#             if InputArray[j]<min{
#                 set min to InputArray[j].
#                 set MinIndex to j.
#             }
#         }
#         swap(InputArray,i,MinIndex).
#         print ArrayDisplay(InputArray).
#     }
#     local function Swap{
#         local parameter Array1.
#         local parameter index1.
#         local parameter index2. 
#         local temp is array1[index1].
#         set Array1[Index1] to Array1[index2].
#         set Array1[index2] to temp.
#     }
# }

# function GnomeSort{
#     parameter InputArray.
#     local N is InputArray:length.
#     local index is 0.
#     until not(index<N) {
#         if index=0 {
#             set index to index+1.
#         }
#         if (InputArray[index]>=InputArray[index-1]){
#             set index to index+1.
#         }
#         else {
#             local temp is InputArray[index].
#             set InputArray[index] to InputArray[index-1].
#             set InputArray[index-1] to temp.
#             set index to index-1.
#         }
#         print ArrayDisplay(InputArray).
#     }
# }

# function InsertionSort{
#     parameter InputArray.
#     local len is InputArray:length-1.
#     from {local i is 1.} until i>len step{set i to i + 1.} do {
#         local currentvalue is InputArray[i].
#         local j is i - 1.
#         until not(j>=0 and InputArray[j]>currentvalue) {
#             set InputArray[j+1] to InputArray[j].
#             set j to j - 1.
#             set InputArray[j+1] to currentvalue.
#             print ArrayDisplay(InputArray).
#         }
#     }
# }

# function BubbleSort{
#     parameter InputArray.
#     set DidSwap to true.
#     set len to InputArray:length.
#     until DidSwap=false{
#         local i is 0.
#         set len to len-1.
#         set DidSwap to false.
#         until not(i < len) {
#             if InputArray[i]>InputArray[i+1]{
#                 set DidSwap to true.
#                 local temp is InputArray[i].
#                 set InputArray[i] to InputArray[i+1].
#                 set InputArray[i+1] to temp.
#                 print ArrayDisplay(InputArray).
#             }
#             set i to i + 1.
#         }
#     }
# }