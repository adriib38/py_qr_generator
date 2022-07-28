import pyqrcode

url = input("Enter a url: ")

url = pyqrcode.create(url)

url.svg("qr.svg", scale = 8)
print("QR created. qr.svg")


