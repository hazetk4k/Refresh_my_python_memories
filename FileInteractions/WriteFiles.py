try:
    with open("out.txt", "a+") as file: #w - обновляет файл, a - добовляет в конец файла новые записи, a+ - добавлять и читать
        file.seek(0)
        file.write("yes\n")
        print(file.read())
except:
    print("Ошибка при работе с файлом")