lst = [10, 11, 12, 13, 14, 15]

rev = []
print("Before reverse: ", lst)
# print(len(lst))

for i in range(len(lst) - 1, -1,-1):
    rev.append(lst[i])


new= sorted(lst, reverse=True)
print(new)
print("After reverse: ",rev)

#approach 2 if the numbers in sequence

lst = [10, 11, 12, 13, 14, 15]
newlist=sorted(lst,reverse=True)
print(newlist)

#approach 2 to reverse list

newlist1=[]
lst = [10, 11, 12, 13, 14, 15]
for i in lst:
    newlist1.append(str(i))
print(newlist1)

new=[]

for n in newlist1 :  #newlist1=['10', '11', '12', '13', '14', '15']
    new=[n]+new
print(new)

# anotherway after converting list to string using loop
newlist1=[]
lst = [10, 11, 12, 13, 14, 15]
for i in lst:
    newlist1.append(str(i))  #newlist1=['10', '11', '12', '13', '14', '15']
print(newlist1)

print(newlist1[::-1])






