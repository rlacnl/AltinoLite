MyFile = open("C:\\tmp\\setup_sec.exe", "rb")
SecFile = open("C:\\tmp\\setup.exe", "wb")

data = MyFile.read(1)

while data :
    result = int.from_bytes(data, byteorder='big') ^ 10
    SecFile.write(int.to_bytes(result,length=1,byteorder='big'))
    data = MyFile.read(1)

MyFile.close()
SecFile.close()