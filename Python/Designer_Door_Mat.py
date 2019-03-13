#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#Mat size must be X. ( is an odd natural number, and  is  times .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.
#Sample Designs

#    Size: 7 x 21 
#    ---------.|.---------
#    ------.|..|..|.------
#    ---.|..|..|..|..|.---
#    -------WELCOME-------
#    ---.|..|..|..|..|.---
#    ------.|..|..|.------
#    ---------.|.---------
    
#    Size: 11 x 33
#    ---------------.|.---------------
#    ------------.|..|..|.------------
#    ---------.|..|..|..|..|.---------
#    ------.|..|..|..|..|..|..|.------
#    ---.|..|..|..|..|..|..|..|..|.---
#    -------------WELCOME-------------
#    ---.|..|..|..|..|..|..|..|..|.---
#    ------.|..|..|..|..|..|..|.------
#    ---------.|..|..|..|..|.---------
#    ------------.|..|..|.------------
#    ---------------.|.---------------

#Input Format

#A single line containing the space separated values of  and .


#Output Format

#Output the design pattern.

#Sample Input

#9 27
#Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------




# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = input().split()
x, y = int(x), int(y)
b = 1
string = ".|."
if(x % 2 != 0 and y == 3 *x):
    for i in range(x//2):
        print((b*string).center(y, '-'))
        b = b + 2
        c = b-2
    print("WELCOME".center(y, '-'))
    for i in range(x//2):
        print((c * string).center(y, '-'))
        c = c - 2

# Another solution
# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
    

