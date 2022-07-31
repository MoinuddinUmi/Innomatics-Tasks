# Task2_Q17
# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of k members per group where k ≠ 1.
# The Captain was given a separate room, and the rest were given one room per group.
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear k times per group except for the Captain's room.
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of k and the room number list.

# Input Format
# The first line consists of an integer, k, the size of each group.
# The second line contains the unordered elements of the room number list.

k = int(input())
rooms = list(map(int, input().split()))
a = set()
b = set()
for rm in rooms:
    if rm not in a:
        a.add(rm)
        b.add(rm)
    else:
        b.discard(rm)
print(list(b)[0])