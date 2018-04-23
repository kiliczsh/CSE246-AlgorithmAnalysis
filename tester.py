import sys
import time
import numpy as np
import xlsxwriter
from insertion_sort import insertionSort
from merge_sort import merge_sort
from quick_select_pivot_first import quick_select_pivot_first
from quick_select_three_median import quick_select_three_median
sortTypes = {
    'merge-sort':['merge-sort',3],
    'insertion-sort':['insertion-sort',3],
    'quick-first':['quick-first',3],
    'quick-median':['quick-median',3]
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
def saveArray(arrayType,i_size,condition,array):
    saveString='arrays/'
    cases=['random-array_','best-case_','worst-case_']
    if(condition==sortTypes['insertion-sort'][0]):
        saveString=saveString+'insertion-sort/'
    elif(condition==sortTypes['merge-sort'][0]):
        saveString=saveString+'merge-sort/'
    elif(condition==sortTypes['quick-first'][0]):
        saveString=saveString+'quick-first/'
    elif(condition==sortTypes['quick-median'][0]):
        saveString=saveString+'quick-median/'
    for i in range(len(array)):
        saveStringNew=saveString+arrayType+'/'+cases[i]+arrayType+'-size-'+str(i_size)+'.txt'
        F=open(saveStringNew,'w')
        step=75
        lineEnd=step
        for j in range(len(array[i])):
            if j>=lineEnd:
                F.write('\n')
                lineEnd+=step
            F.write(str(array[i][j]))
            F.write('  ')
        F.close()

def prepareArraysForCases(i_size,condition):
    normal_array=np.random.random_integers(0,100000,size=(i_size))
    if(condition==sortTypes['insertion-sort'][0]):
        best_case=normal_array.copy()
        best_case=sorted(best_case)
        temp=best_case.copy()
        worst_case=list(reversed(temp)).copy()
        saveArray('input',i_size,condition,[normal_array,best_case,worst_case])
        return [[normal_array,9],[worst_case,9],[best_case,9]]
    elif(condition==sortTypes['merge-sort'][0]):
        worst_case=normal_array.copy()
        best_case=normal_array.copy()
        saveArray('input',i_size,condition,[normal_array,best_case,worst_case])
        return [[normal_array,9],[worst_case,9],[best_case,9]]
    elif(condition==sortTypes['quick-first'][0]):
        best_case=normal_array.copy()
        mergeSort(best_case)
        temp=best_case
        worst_case=list(reversed(temp)).copy()
        saveArray('input',i_size,condition,[normal_array,best_case,worst_case])
        return [[normal_array,9],[worst_case,len(worst_case)-1],[best_case,1]]
    elif(condition==sortTypes['quick-median'][0]):
        best_case=normal_array.copy()
        mergeSort(best_case)
        temp=best_case
        worst_case=list(reversed(temp)).copy()
        lnt=len(normal_array)
        halflnt=lnt//2
        best_case[0],best_case[halflnt]=best_case[halflnt],best_case[0]
        worst_case[halflnt],worst_case[lnt-1]=worst_case[lnt-1],worst_case[halflnt]
        saveArray('input',i_size,condition,[normal_array,best_case,worst_case])
        return [[normal_array,9],[worst_case,lnt-1],[best_case,1]]
def runFunction(condition,alist,k):
    if condition == sortTypes['insertion-sort'][0]:
        start_time=time.time()
        kthElement=insertionSort(alist,k)
        end_time=time.time()
    elif condition == sortTypes['merge-sort'][0]:
        start_time=time.time()
        kthElement=merge_sort(alist,k)
        end_time=time.time()
    elif condition == sortTypes['quick-first'][0]:
        start_time=time.time()
        kthElement=quick_select_pivot_first(alist,k)
        end_time=time.time()
    elif condition == sortTypes['quick-median'][0]:
        start_time=time.time()
        kthElement=quick_select_three_median(alist,k)
        end_time=time.time()
    return end_time-start_time

rowCount=0
workbook=xlsxwriter.Workbook('out/'+filename)
worksheet=workbook.add_worksheet()


writeColumnTitles(worksheet,row,column,condition)
count=0
cases=[]
step=10000
for input_size in range(1000,111000,step):
    rowCount+=1
    worksheet.write(row+rowCount,column,str(input_size))
    endStr=''
    cases=prepareArraysForCases(input_size,condition)
    print("Test cases generated")
    numOfCases=len(cases)
    print('Array size = '+str(input_size),end=' ---> ')
    for i in cases:
        totaltime=runFunction(condition,i[0],i[1])
        if(count==numOfCases-1):
            endStr='\n'
        else:
            endStr='                '
        print(printCases[count]+": %f"%totaltime,end=endStr)
        worksheet.write(row+rowCount,column+count+1,totaltime)

        count+=1
        count=count%numOfCases
    saveArray('output',input_size,condition,[cases[0][0],cases[1][0],cases[2][0]])
workbook.close()
exit()