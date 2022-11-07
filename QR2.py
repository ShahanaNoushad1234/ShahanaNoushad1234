import qrcode   
data=input('Enter any data')  
list=[]     
list.append(data)                          
img = qrcode.make(data)
type(img)
img.save("DATA.png")