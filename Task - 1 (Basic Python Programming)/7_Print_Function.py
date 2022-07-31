#Task1_Q7
# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, try to print the following: 123....n
# Note that "...." represents the consecutive values in between.


n = int(input("Enter a number:"))
strr = ''
for i in range(1,n+1):
    strr = strr + str(i)
print(strr)