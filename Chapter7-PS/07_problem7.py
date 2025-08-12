'''
for n = 3
   *
  ***
 *****

 For n = 5
      *
     ***
    *****
   ********
************

'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-1), end="")
    print("*"* (2*1-1), end="")
    print("")