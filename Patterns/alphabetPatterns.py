#################### Pattern 14 ########################
#A
#B B
#C C C
#D D D D
#E E E E E
#############################################

n = 5
for i in range(1, n + 1):
    ch = chr(64 + i)
    for j in range(i):
        print(ch, end=" ")
    print()


################ Pattern 15 #######################
#A
#AB
#ABC
#ABCD
#ABCDE
#################################################

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()


################ Pattern 16 #######################
#A
#B C
#D E F
#G H I J
#K L M N O
################################################

n=5
char=1
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+char),end=" ")
        char+=1
    print()


############### Pattern 17 #####################
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
###############################################

n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(2*i-1):
        print("*",end="")
    print()


############### Pattern 18 #####################
#*       *
# *     *
#  *   *
#   * *
#    *
#   * *
#  *   *
# *     *
#*       *
################################################

n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")

for i in range(2,n+1):
    print(" "*(n-i),end="")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")


################### Pattern 19 ################
#* * * * *
#*       *
#*       *
#*       *
#* * * * *
############################################

n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


################ Pattern 20 ##############################
#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15
#4 8 12 16 20
#5 10 15 20 25
###########################################

n=5
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    print()

############################################
