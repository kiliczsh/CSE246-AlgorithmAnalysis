import sys
import time
import numpy as np
import xlsxwriter
import insertion_sort from insertion_sort
import merge_sort from merge_sort

def writeColumnTitles(worksheet,row,column):
    worksheet.write(row,column+1,'Best Case')
    worksheet.write(row,column+2,'Random Array')
    worksheet.write(row,column+3,'Worst Case')

count=0
rowCount=0
workbook=xlsxwriter.Workbook('out/'+sys.argv[1])
worksheet=workbook.add_worksheet()

row=0
column=0
writeColumnTitles(worksheet,row,column)
for input_size in range(1000,10001,1000):
    rowCount+=1
    worksheet.write(row+rowCount,column,str(input_size))
    normal_array=np.random.random_integers(0,10000,size=(input_size))
    best_case=normal_array.copy()
    insertionSort(best_case,1)
    temp=best_case
    worst_case=list(reversed(temp)).copy()
    condition=int(sys.argv[2])
    for array in [best_case,normal_array,worst_case]:
        if condition==0:
            start_time=time.time()
            kthElement=insertionSort(array,9)
            end_time=time.time()
        else if(condition==1):
            start_time=time.time()
            kthElement=insertionSort(array,9)
            end_time=time.time()
        else if(condition==2):
            start_time=time.time()
            kthElement=insertionSort(array,9)
            end_time=time.time()

        if count==0:
            print("Best case: %f"%(end_time-start_time),end="   ")
            worksheet.write(row+rowCount,column+1,str(end_time-start_time))
        elif count==1:
            print("Normal array: %f"%(end_time-start_time),end="   ")
            worksheet.write(row+rowCount,column+2,str(end_time-start_time))
        else:
            print("Worst case: %f"%(end_time-start_time))
            worksheet.write(row+rowCount,column+3,str(end_time-start_time))
        count+=1
        count=count%3
workbook.close()
exit()