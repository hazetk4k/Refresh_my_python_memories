try:

    #     file = open("new_file.txt", encoding="utf-8")
    #     # try:
    #     #     s = file.readlines()
    #     #     print(s)
    #     # finally:
    #     #     file.close()
    with open("new_file.txt", encoding="utf-8") as file:
        s = file.readlines()
        print(s)
except FileNotFoundError:
    print("файл не найден")
except:
    print("Ошибка при работе с файлом")
finally:
    print(file.closed)
