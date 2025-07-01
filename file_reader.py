# my_file = open("C:\\Users\\ranga\\Documents\\python\\python_works\\sample.txt.txt")
#
# print(my_file.read())
# my_file.seek(1)
# print(my_file.read())
# my_file.seek(2)
# print(my_file.read())
from translate import Translator
# with open('sample.txt.txt', mode ='a+') as my_file:
#     my_file.write('new line')
#     my_file.seek(0)
#     print(my_file.read())

from translate import Translator
trans=Translator(to_lang="ja")
with open('sample.txt.txt', mode ='r') as my_file:
    text=my_file.read()
    b= trans.translate(text)

with open('sample-jap.txt',mode='w',encoding="utf-8") as tr_file:
    tr_file.write(b)

