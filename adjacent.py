num=[1,2,3,1]
maxval=num[0]
for i in range(0,len(num),1):
    if maxval<num[i]:
        maxval=num[i]
print(maxval)
