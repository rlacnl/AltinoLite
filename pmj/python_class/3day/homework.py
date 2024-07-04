secretFile = open("c:\\tmp\\extracted.txt", "wb")

imageFile = open("c:\\tmp\\enc.bmp", "rb")

imageFile.read(54)

imageData = imageFile.read()

secretFile.write(imageData)

imageFile.close()
secretFile.close()
