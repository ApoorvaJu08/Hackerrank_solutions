#Task 
#Read an integer . For all non-negative integers , print . See the sample for details.

#Input Format

#The first and only line contains the integer, .

#Constraints


#Output Format

#Print  lines, one corresponding to each .

#Sample Input 0

#5
#Sample Output 0

#0
#1
#4
#9
#16

n = int(input())
i = 0
if (n>=1 and n <=20):
    for i in range(0, n):
        x = i*i
        print(x)
else:
    print("Enter a number between 1 and 20")


