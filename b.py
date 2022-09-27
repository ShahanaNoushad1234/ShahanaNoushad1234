num=[1,3,5,1]
a=len(num)
maxval=num[0]
for i in range(0,len(num),1):
    if maxval<num[i]:
        maxval=num[i]
print(maxval)
m = max(num)
