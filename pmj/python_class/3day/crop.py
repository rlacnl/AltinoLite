#원본파일을 열어준다
originFile = open("C:\\tmp\\a.bmp","rb")
#새로 만들 파일을 열어준다
cropFile = open("C:\\tmp\\result.txt","wb")
#원본파일에서 합쳐진파일의 크기만큼 읽어 새로만들 파일에 써준다.
#원본파일의 크기는 6750054 이고 합쳐진파일 크기는 알수없다
# 코드를 완성해라

originFile.read(6750054)
cropFile = originFile.read()


#파일을 닫아준다
originFile.close()
cropFile.close()

