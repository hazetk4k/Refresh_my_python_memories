print("\n======================================================================")
a = 'THE WORLD'
print(f"Как я писал в String Basics, Строка - упорядоченный набор символов. Индексация символов начинается с нуля. Можно использовать [].\n"
      f"Строка: a = 'THE WORLD' \n"
      f"Можно вытащить отдельные симоволы вот так:\n"
      f"\ta[0] = '{ a[0] }',\n"
      f"\ta[3] = '{ [3] }' ,\n"
      f"Для разных циклов и всего такого можно использовать конструкцию len(a) - 1 для определения индекса последнего символа:\n"
      f"a[8] = { a[-1] }, len(a) - 1 = { len(a) - 1 }, a[len(a) - 1] = { a[len(a) - 1] }.\n"
      f"Но как будто проще использовать a[-1] = '{ a[-1] }' - можно использовать -1, -2, -3... для расчета с конца, но тогда начинать нужно с -1 а не с 0, очевидно.")

print("\n======================================================================")
str1 = 'skibidi'
x = 0
y = 5
z = 3
print(f"Важно понимать как работают 'СРЕЗЫ' строк.\n"
      f"Например из строки str1 можно получить ее срез если использовать следующую конструкцию:\n"
      f"str1 = { str1 }, str1[x:y] = { str1[x:y] }, где x = {x}, y = {y}.\n"
      f"то есть коснтрукция [] содержит начало и конец среза, причем начальный элемент с индексом x будет включен, а конечный с индексом y - не будет.")

print("\n======================================================================")
print(f"Кроме того можно использовать [x:] - начать с символа с индексом x и до конца строки, [:y] - начать с начала и до символа с индексом y.\n"
      f"z = { z }, srt1[z:] = { str1[z:] }, str1[:y] = { str1[:y] }.\n"
      f"Кстати, в теории если учитывать что конечный индекс str1 это 6,\n"
      f"то можно получиить срез вместе с последним символом еще и вот так: str1[0:7] = {str1[0:7]}. ОГО РЕАЛЬНО МОЖНО....")

print("\n======================================================================")
print("Не знаю зачем эта инфа, Но str1[:] - вернет полную строку str1. И если str2 = str1[:],\n"
      f"в таком случае и str2 и str1 ссылаются на один и тот же объект в памяти, хранящий строку... (o_0)")

print("\n======================================================================")
print(f"А вот и моя нелюбимая часть - в срезах можно использовать отрицательные индексы:\n"
      f"str1[0:-3] = { str1[0:-3] }. Можно даже делать так: str1[-4: -1] = { str1[-4: -1] }\n"
      f"\t(заметь что конечный символ с индексом -1 все еще не выводится, чтобы вывести всю оставшуюся строку после  -4 используй str1[-4:] = {str1[-4:]}.\n"
      f"Даже не пытайся использовать что-то типа str1[-2:2], результатом будет '{str1[-2:2]}', это равносильно str1[4:2]. Надеюсь подробнее объяснять не надо(((")

print("\n======================================================================")
print(f"И наконец 'ШАГ' среза int, который идет вот тут -> [::x].\n"
      f"Обычно он равен 1, то есть при срезе начиная с первого символа будет выводится каждый 1 символ: str1[0:6:1] = { str1[0:6:1] }."
      f"С шагом два будет выводится каждый второй символ: str1[::2] = { str1[::2] },\n"
      f"чтобы вывести буквы, через которые я сейчас перешагнул, можно сделать так:str1[::2] = { str1[1::2] }.\n"
      f"С помошью шага можно идти по срезу назад: str1[::-1] = { str1[::-1] }, или даже так str1[::-2] = { str1[::-2] }.\n")

print("\n======================================================================")
str2 = 'X'
print(f"У тебя не получится изменить строку так: str1[0] = 'X',\n"
      f"чтобы сделать новое слово из старого можно использовать срезы:\n"
      f"str2 = {str2}, str2 += str1[1:], str2 = {str2 + str1[1:]} и только так к сожалению...")

print("\n======================================================================")
print("Развлекайся со срезами, комбинируя все вышеупомянутое. Только не выходи за пределы индексов, а то будет ошибка!")

#print(str1[999]) #вот так не надо, не трогай