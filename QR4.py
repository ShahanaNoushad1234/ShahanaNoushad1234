import qrcode
list=[]
for i in range(3):
 a=input('enter name')
 b=input('enter age')
 c=input('enter place')
 data=[a,b,c]
 list.append(data) 
 k=0
for i in list:
    k+=1
    s=str(k)
    img = qrcode.make(i)
    type(img)
    img.save(s+"e_file.png")