import pyqrcode
import png



url = pyqrcode.create(input('what url would you like to turn into a qrcode?\nmust include www. and .com\n'))

print('this is your qr code')
print(url.terminal(quiet_zone=1))

image_view = input('\nwould you like to see this with an image viewer?\n\nIMAGE VIEWING IS TEMPORARY(OPTION TO DOWNLOAD AFTER THIS PROMPT!)\n\nTYPE yes or no')



if image_view == 'yes':
    url.show(wait=10)
else:
    pass

download = input('\nwould you like to download your qr code?yes or no?')

if download == 'yes':
    url.svg("yourqr.svg", scale = 8)
    url.png('yourqr.png', scale = 6)
    print('\nIMAGE DOWNLOADED TO CURRENT PATH AS PNG AND SVG')
else:
    print('\nIMAGE NOT DOWNLOADED')
