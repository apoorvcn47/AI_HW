import xlrd
import string
import numpy as np


file = "/home/apoorv/AI_HW/HW_2/sudoku_problem.xlsx"
workbook = xlrd.open_workbook(file)
sheet = workbook.sheet_by_index(0)

sudoku_size = sheet.nrows
sudoku_array = np.chararray((sudoku_size,sudoku_size))

'''
for i in xrange(0,sudoku_size):
    for j in xrange(0,sudoku_size):
        sudoku_array[i,j] = sheet.cell_value(i,j)
'''        

sudoku_int_array = [ [0]*sudoku_size for _ in xrange(sudoku_size) ]
perm_no_memory = []

#creating array of ints and blanks
for i in range(0,sudoku_size):
    for j in range(0,sudoku_size):
        if(sheet.cell_value(i,j) == '_'):
            
            sudoku_int_array[i][j] = ' '
        else:
            sudoku_int_array[i][j] = int(sheet.cell_value(i,j))#string.atoi(sudoku_array[i,j])
            #Saving location of permanent nos
            perm_no_memory.append([i,j])
            

#parsing through all cells
for i in range(0,sudoku_size):
    for j in range(0,sudoku_size):
        if(perm_no_memory.count([i,j])==0):
            
