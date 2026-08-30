########## Pattern 1 ############
*
* *
* * *
* * * *
* * * * *
#################################

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()


######### Pattern 2 #############
        *
      * *
    * * *
  * * * *
* * * * *
##################################

n = 5
for i in range(1, n + 1):
    for j in range(i, i + 1):
        print(" " * (n - i), end="")
        for k in range(1, i + 1):
            print("*", end="")
    print()


######### Pattern 3 #############
* * * * *
* * * *
* * *
* *
*
################################

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


######### Pattern 4 #############
* * * * *
  * * * *
    * * *
      * *
        *
#################################

n = 5
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()


########## Pattern 5 ##############
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
#################################

n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


########### Pattern 6 ############
        *
       * *
      *   *
     *     *
    *       *
     *     *
      *   *
       * *
        *
###################################

n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
