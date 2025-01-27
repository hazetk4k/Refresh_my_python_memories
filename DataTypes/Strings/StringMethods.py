str1 = "SKIBIDI"
print(f"Используй множество методов со строкой или переменной ссылающейся на строку используя конструкцию:\n"
      f"объект.метод(аргументы)\n"
      f"Например: str1 = {str1}, str1.lower() = {str1.lower()}\n")

print(f"upper() делает заглавные, а lower() делает строчные,\n"
      f"причем при применении создается новый объект, ссылка на который будет отлична от str1 (Строки не меняются).\n"
      f"Кстати,методы можно вызывать и без круглых  скобочек но тогда вернется не результат,\n"
      f"а сообщение что создан новый объект и на него есть ссылка: str1.lower = {str1.lower}")

print("\n======================================================================")
sub1 = "i"
str1 = "skibidi"
print(f"Метод count(sub, start, end) может посчитать количество повторений подстроки в строке.\n"
      f"Обязательный аргумент - подстрока.\n"
      f"Два необязательных - индексы начального и конечного индекса строки,\n"
      f"между которыми идет поиск. Работает аналогично срезам:\n"
      f"\tsub1 = {sub1}, str1 = {str1}\n"
      f"\tstr1.count(sub1) = {str1.count(sub1)}\n"
      f"\tstr1.count(sub1, 3) = {str1.count(sub1, 3)}\n"
      f"\tstr1.count(sub1, 3,6) = {str1.count(sub1, 3, 6)}\n")

print("\n======================================================================")
sub2 = "bi"
print(f"Метод find(sub, start, end) находит индекс первого вхождения суб в строку (только sub обязательный):\n"
      f"\tstr1.find(sub2) = {str1.find(sub2)}, аргументы start и end работают аналогично count...\n"
      f"Ну ладно, покажу еще пару примеров:\n"
      f"\tstr1.find('my patience') = {str1.find('my patience')} - возвращает -1 потому что не нашел суб.\n"
      f"\tstr1.find('i') = {str1.find('i')}, но если str1.find('i', 3) = {str1.find('i',3)}. Такие дела.")
print(f"Есть еще метод rfind который работает также но ищет с конца в начало, примеры приводить не буду, сам попробуй...\n"
      f"Боже, ладно, вот пример: str1.rfind('i') = {str1.rfind('i')}")

print("\n======================================================================")
print("Метод index(sub, start, end) - возвращает индекс суба но отличе в том что он выводит ошибку, если не находят суб,\n"
      " это можно использовать для обработки ошибок. Тут без примера, поверь просто наслово, окей?")

print("\n======================================================================")
print(f"replace(oldsub, newsub) - это прям полезный метод для строк, он заменят старую подстроку на новую,\n"
      f"причем если таких старых субов несколько, он заменит их всех:\n"
      f"\tstr1.replace('i', 1) = {str1.replace('i', '1')}\n"
      f"\tstr1.replace('i', '') = {str1.replace('i', '')}\n"
      f"УДОБНО, но если нужно заменить только несколько подстрок,"
      f"\nа не все, то можно указать количество заменяемых (поиск осуществляется с начала строки):"
      f"\tstr1.replace('i', 1, 2) = {str1.replace('i', '1', 2)}\n")

print("\n======================================================================")
print(f"isalpha вернет тру, если все символы строки - буквы, и фолз если нет:\n"
      f"\tstr1.isalpha() = {str1.isalpha()}\n"
      f"Только надо учитывать что знаки типа ' ' и '*' и тп не пройдут проверку.")

print("\n======================================================================")
print("isdigit - тру если строка содержит только числа:\n"
      "\tstr1.isalpha() = {str1.isalpha()}\n"
      "\t(если сделать число в стоке десятичным, проверка не будет пройдена из=зи '.')")

print("\n======================================================================")
new_str = "123"
print(f"rjust - нужен для создания новой строки из старой с добавлением дополнительных символов (слева), например:\n"
      f"\tnew_str = {new_str},\n"
      f"\tnew_str.rjust(4) = {new_str.rjust(4)},\n"
      f"\tnew_str.rjust(4, '0') = {new_str.rjust(4, '0')}\n"
      f"Символ заменитель пустой строки должен быть один, иначе будет ошибка. А если указать размер новой строки меньше старой,\n"
      f"то будет получена строка, равная старой. Такие дела")

print("\n======================================================================")
print(f"ljust работает так же но добавляет символ справа: new_str.ljust(5, 'x') = {new_str.ljust(5, 'x')}")

print("\n======================================================================")
long_str = "come lets watch the rain as its falling down"
print(f"split(sep) - возвращает колекцию строк из строки, разделенную через символ разделитель sep:\n" #вообще не коллекция а конкретно список но ладно
      f"\tlong_str = {long_str},\n"
      f"\tlong_str.split(' ') = {long_str.split(' ')}\n")

print("\n======================================================================")
str_nums = "12, 23 , 33, 111 , 3, 15"
my_str = str_nums.replace(' ', '')
mew_list = my_str.split(',')
print(f"Теперь можно быть классным и красивым и использовать все эти методы всете когда захочешь, например:\n"
      f"Есть строка str_nums = {str_nums}, из нее нужно получить список со всеми цифрами.\n"
      f"\t1) убери лишние пробелы: my_str = str_nums.replace(' ', '') = {my_str}\n"
      f"\t2) получи список: mew_list = my_str.split(',') = {mew_list}")

print("\n======================================================================")
print(f"C помошью join() можно из такого списка вернуть строку, для этого вызови этот метод от строки разделителя:\n"
      f"\t', '.join(mew_list) = {', '.join(mew_list)}\n")

print("\n======================================================================")
str_space = "           yes            "
print(f"strip() убирает пробелы с начла и конца:\n"
      f"\tstr_space = '{str_space}',\n"
      f"\tstr_space.strip() = {str_space.strip()}\n")
print("Попробуй догадаться что делают rstrip и lstrip. А еще догадайся буду ли я их показывать >:)")
