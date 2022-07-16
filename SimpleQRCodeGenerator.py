#First of all install qrcode and Image modules in your system
#Head to command prompt or simply terminal of pycharm
#Type the below commands:-
# "pip install qrcode" and "pip install Image"
#Now follow up the code below-

import qrcode
img=qrcode.make("https://www.youtube.com/channel/UCA6GG2XXVc_YvYOIV2hT3Xw")   #Link of the site you want to make QR of
img.save("HarryK1N6_Youtube.jpg")                                             #Name of the Image file which will be saved as QR Code


#For demo of the same VISIT:- https://youtu.be/4TYJYNQ1O8E
