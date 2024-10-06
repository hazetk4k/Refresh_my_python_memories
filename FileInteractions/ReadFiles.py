#open(file, mode, encoding) где mode - режим доступа, encoding - кодировка файла

# new_file.txt если в том же каталоге
# inner_cat/new_file.txt - если в папке в том же каталоге
# ../new_file.txt - если вне каталога
# ../inner_cat/new_file.txt - если вне каталога в какой-то папке

file = open("new_file.txt", encoding="utf-8")
# чтение посимвольно
# print(file.read(4))
# file.seek(0)
# print(file.read(4))
# pos = file.tell() #pos - значение в байтах
# print(pos)

# чтение построчно
#print(file.readline(), end="")
#print(file.readline(), end="")

# получить список строк
# list1 = file.readlines() - для больших файлов может быть ошибка нехватки памяти

for line in file:
    print(line, end="")

file.close()