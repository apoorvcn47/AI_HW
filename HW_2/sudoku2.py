import xlrd
import string
import random
import math
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
total_blanks = 0
for i in range(0,sudoku_size):
    for j in range(0,sudoku_size):
        if(sheet.cell_value(i,j) == '_'):
            
            sudoku_int_array[i][j] = ' '
            total_blanks = total_blanks+1
        else:
            sudoku_int_array[i][j] = int(sheet.cell_value(i,j))#string.atoi(sudoku_array[i,j])
            #Saving location of permanent nos
            perm_no_memory.append([i,j])

blank_space_flag = bool(1)            

#while(blank_space_flag == bool(1) ):
    #parsing through all cells
max_constrains = 0
changed_no_add_list = []

#loop that assigns random available value to a cell
while(len(changed_no_add_list)<total_blanks):
    #loop that selects most constrained cell
    for i in range(0,sudoku_size):
        for j in range(0,sudoku_size):
            total_constrains = 0
            #checking the cells which can be edited
            if(perm_no_memory.count([i,j])==0):
                #checking vertical constrains
                for p in range(0,sudoku_size):
                    if(sudoku_int_array[p][j]!=' '):
                        total_constrains = total_constrains +1
                #checking horizontal constrains
                for q in range(0,sudoku_size):
                    if(sudoku_int_array[i][q]!=' '):
                        total_constrains = total_constrains +1
                quad_i = int(math.ceil((i+1)/math.sqrt(sudoku_size)))
                quad_j = int(math.ceil((j+1)/math.sqrt(sudoku_size)))
                #checking block constrains
                for r in range(0,int(math.sqrt(sudoku_size))):
                    for s in range(0,int(math.sqrt(sudoku_size))):
                        if(sudoku_int_array[r+int((quad_i-1)*(math.sqrt(sudoku_size)))][s+int((quad_j-1)*(math.sqrt(sudoku_size)))]!=' '):
                            total_constrains = total_constrains +1
                #looking for a cell with max constrains
                if((max_constrains < total_constrains) and changed_no_add_list.count([i,j]) == 0):
                    max_constrains = total_constrains
                    max_constrains_address = [i,j]
    
    existing_constrains_list = [0]
    possible_options_list = []
    max_constrains = 0
    
    #finding existing numbers in corresponding column
    for p in range(0,sudoku_size):
        existing_constrains_list.append(sudoku_int_array[p][max_constrains_address[1]])
    
    #finding existing numbers in corresponding row
    for q in range(0,sudoku_size):
        existing_constrains_list.append(sudoku_int_array[max_constrains_address[0]][q])
    
    quad_i = int(math.ceil((max_constrains_address[0]+1)/math.sqrt(sudoku_size)))
    quad_j = int(math.ceil((max_constrains_address[1]+1)/math.sqrt(sudoku_size)))
    
    #finding existing numbers in corresponding block
    for r in range(0,int(math.sqrt(sudoku_size))):
        for s in range(0,int(math.sqrt(sudoku_size))):
            existing_constrains_list.append(sudoku_int_array[r+int((quad_i-1)*(math.sqrt(sudoku_size)))][s+int((quad_j-1)*(math.sqrt(sudoku_size)))])
    
    #finding possible options
    for i in range(1,(sudoku_size+1)):
        if(existing_constrains_list.count(i)==0):
            possible_options_list.append(i)
        
    if (len(possible_options_list)!=0):    
        sudoku_int_array[max_constrains_address[0]][max_constrains_address[1]] = random.choice(possible_options_list)
    changed_no_add_list.append([max_constrains_address[0],max_constrains_address[1]])
   
#check if there are still unassigned places (ie local minima),
#reset row, column and block constrains to ' '
for i in range(0,sudoku_size):
    for j in range(0,sudoku_size):
        if(sudoku_int_array[i][j] == ' '):
            blank_space_flag = bool(1)
            
            for p in range(0,sudoku_size):
                if(perm_no_memory.count([p,j])==0):
                    sudoku_int_array[p][j] = ' '
    
            for q in range(0,sudoku_size):
                if(perm_no_memory.count([i,q])==0):
                    sudoku_int_array[i][q] = ' '
    
            quad_i = int(math.ceil((max_constrains_address[0]+1)/math.sqrt(sudoku_size)))
            quad_j = int(math.ceil((max_constrains_address[1]+1)/math.sqrt(sudoku_size)))

            for r in range(0,int(math.sqrt(sudoku_size))):
                for s in range(0,int(math.sqrt(sudoku_size))):
                    if(perm_no_memory.count([r+int((quad_i-1)*(math.sqrt(sudoku_size))),s+int((quad_j-1)*(math.sqrt(sudoku_size)))])==0):
                        sudoku_int_array[r+int((quad_i-1)*(math.sqrt(sudoku_size)))][s+int((quad_j-1)*(math.sqrt(sudoku_size)))] = ' '
            break
            
        else:
            blank_space_flag = bool(0)
    
    if(sudoku_int_array[i][j] == ' '):
        break
                
    