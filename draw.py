import xlrd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join,splitext
import os.path
import np

excel_files = [f for f in listdir("out/") if isfile(join("out/", f))]

for file_element in excel_files:
    current_file_name = os.path.splitext(file_element)[0]
    book = xlrd.open_workbook('out/'+file_element)
    sheet = book.sheet_by_name('Sheet1')
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    column1= [x[0] for x in data[1:11]]
    column2= [x[1] for x in data[1:11]]
    column3= [x[2] for x in data[1:11]]
    column4= [x[3] for x in data[1:11]]

    plt.plot(column1,column2,'-o')
    plt.plot(column1,column3,'-x')
    plt.plot(column1,column4,'-+')
    plt.legend([ 'Random Array', 'Worst Case','Best Case'], loc='upper left')
    plt.autoscale(enable=True, axis='y')
    plt.autoscale(enable=True, axis='x')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time')
    plt.title(current_file_name)
    plt.grid(True)
    plt.yscale('linear')
    plt.savefig('figures/'+current_file_name+'.png')
    plt.close()


        
