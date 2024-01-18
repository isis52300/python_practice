import sys

def print_matrix(m):
    for i in m:
        print(i)
    print('~~~~~~~~~')

#find all of the subarrays in the matrix
mat = [[1, 0, 1], [1, 1, 0], [1, 1, 1]]

#fill marks matrix
marks = []
for i in range(len(mat)):
    temp = []
    for j in range(len(mat[i])):
        temp.append(0)
    marks.append(temp)

print('Matrix:')
print_matrix(mat)

sum = 0

#make the marks 
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 1:
            #sum += 1
            marks[i][j] = 1
            k = j+1
            while k in range(len(mat[i])):
                if mat[i][k] == 1:
                    marks[i][j] += 1
                    k += 1
                else:
                    k = len(mat[i])

#use the marks to find solution 
for j in range(len(marks[0])):
    min_val = sys.maxsize
    for i in range(len(marks)):
        if marks[i][j] != 0:
            min_val = marks[i][j]
            sum += min_val
            k = i+1
            while k < len(marks):
                if marks[k][j] == 0:
                    break
                if marks[k][j] < min_val:
                    min_val = marks[k][j]
                sum += min_val
                k += 1

print('Marks:')
print_matrix(marks)

print('Number of 1x1: 7')
print('Number of 1x2: 3')
print('Number of 1x3: 1')
print('Number of 2x1: 3')
print('Number of 2x2: 1')
print('Number of 2x3: 0')
print('Number of 3x1: 1')
print('Number of 3x2: 0')
print('Number of 3x3: 0')

print('Predicted solution: 7 + 3 + 1 + 3 + 1 + 1 =', 7+3+1+3+1+1)
print('Actual solution:', sum)