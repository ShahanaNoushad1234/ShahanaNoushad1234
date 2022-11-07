import qrcode                                         
img = qrcode.make('HELLO')
type(img) 
img.save("hello.png")