#method-1
n = 1234
rev =0
while n>0:
    x = n%10
    rev = rev*10+x
    n =n//10
print(rev)

#method-2
m=4567
rev_int = int(str(m)[::-1])
print(rev_int)


#approach1 reversing the string and number
x="rakesh"
print(x[::-1])


n=1234
y=str(n)
z=y[::-1]
print(z)

#approach 2 to reverse string
x="rakesh"
y=""
for l in x:
    y=l+y
print(y)


#approach2 to reverse number
x=12345
y=str(x)
# print(type(y))
# print(y)
z=list(y)
print(z)


b=int(y[4])
li=[]
x=4
for i in z:
    if int(i)<=b:
        li.append(int(i)+x)
        x=x-2
print(li)


string=""
for item in li:
    string=string+f"{item}"
print(string)



