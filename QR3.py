import qrcode
a=input('enter name')
b=input('enter age')
c=input('enter place')
data=[a,b,c]
img = qrcode.make(data)
type(img)
img.save("DATA2.png")