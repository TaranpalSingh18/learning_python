import qrcode as qr

image = qr.make("http://junglesafari.ap-south-1.elasticbeanstalk.com/")
image.save("Jungle Safari QR.png")

