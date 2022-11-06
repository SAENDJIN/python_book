import qrcode

image = qrcode.make('https://tap.link/olena.shutka')
image.save('qr.png')