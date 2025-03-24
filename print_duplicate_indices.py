# lst = ['sri', 1, 4, 6, 1, 4, 5, 8, 'sri']
# indices ={}
# for i, item in enumerate(lst):
#     if item in indices:
#         indices[item].append(i)
#     else:
#         indices[item] =[i]
# for item, index in indices.items():
#     if len(index) >1:
#         print(f'duplicate of {item} occurs at {index}')
#this to find duplicates
# lst = ['sri', 1, 4, 6, 1, 4, 5, 8, 'sri']
# x=[]
# cou=1
# for item in  lst:
#     if item not in x:
#
#      x.append(item)
#     else:
#         cou=cou+1
#         print(f"duplicate in list:{item},{cou}")
# print(x)


#printing duplicates and number of times repeated
cou={}
lst = ['sri', 1, 4, 6, 1, 4, 5, 8, 'sri']
for item in  lst:
    if item in cou:
        cou[item]+=1
    else:
        cou[item]=1

for item,count in cou.items():
    if count>1:
        print(f"'{item}' occurred {count} times")







