
myfile = open("C:\\tmp\\test.txt","r")

myfile.read()

myfile.close()

a = str(input("복사할 파일 이름을 입력해 주세요"))

myfile = open("C:\\tmp\\"+a+".txt","w")

myfile.write()

myfile.close()

############################################
#2번째

source_path = str(input("원본경로를 입력해주세요 : "))
dest_path = str(input("복사할 경로를 입력해주세요 : "))

sourceFile = open(source_path,"r")
destFile = open(dest_path, "w")

destFile.write(sourceFile.read())

sourceFile.close()
destFile.close()