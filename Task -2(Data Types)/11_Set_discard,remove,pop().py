#Task2_Q11
# You have a non-empty set s, and you have to execute n commands given in n lines.
# The commands will be pop, remove and discard.

# Input Format
# The first line contains integer n, the number of elements in the sets s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

n = int(input())
s = set(map(int,input().split()))
num = int(input())
for i in range(num):
    opt = input().split()
    if opt[0]=="remove":
        s.remove(int(opt[1]))
    elif opt[0]=="discard":
        s.discard(int(opt[1]))
    else :
        s.pop()
print(sum(list(s)))