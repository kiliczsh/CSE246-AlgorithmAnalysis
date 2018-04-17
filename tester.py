import sys
import time
import numpy as np
import xlsxwriter
from insertion_sort import insertionSort
from merge_sort import mergeSort

sortTypes = {
    'merge-sort':['merge-sort',1],
    'insertion-sort':['insertion-sort',3]
}

printCases=['Random Array','Worst Case','Best Case']

filename=sys.argv[1]
condition=sys.argv[2]
kthElement=9
row=0
column=0

def writeColumnTitles(worksheet,row,column,condition):
    for i in range(1,sortTypes[condition][1]+1):
        worksheet.write(row,column+i,printCases[i-1])

def prepareArraysForCases(condition):
    normal_array=np.random.random_integers(0,10000,size=(input_size))
    if(condition==sortTypes['insertion-sort'][0]):
        best_case=normal_array.copy()
        insertionSort(best_case,1)
        temp=best_case
        worst_case=list(reversed(temp)).copy()
        return [normal_array,worst_case,best_case]
    elif(condition==sortTypes['merge-sort'][0]):
        return [normal_array]
def runFunction(condition,alist,k):
    if condition == sortTypes['insertion-sort'][0]:
        start_time=time.time()
        kthElement=insertionSort(alist,k)
        end_time=time.time()
    elif condition == sortTypes['merge-sort'][0]:
        start_time=time.time()
        kthElement=mergeSort(alist)
        end_time=time.time()
    return end_time-start_time

rowCount=0
workbook=xlsxwriter.Workbook('out/'+filename)
worksheet=workbook.add_worksheet()


writeColumnTitles(worksheet,row,column,'merge-sort')

count=0
cases=[]
for input_size in range(1000,10001,1000):
    rowCount+=1
    worksheet.write(row+rowCount,column,str(input_size))
    endStr=''
    cases=prepareArraysForCases(condition)
    numOfCases=len(cases)
    print('Array Length: '+str(input_size),'-----',end=' ')
    for i in cases:
        totaltime=runFunction(condition,i,kthElement)
        if(count==numOfCases-1):
            endStr='\n'
        else:
            endStr='                '
        print(printCases[count]+": %f"%totaltime,end=endStr)
        worksheet.write(row+rowCount,column+count+1,totaltime)
    
        count+=1
        count=count%numOfCases

workbook.close()
exit()