print("Список - упорядоченная коллекция данных, можно обращаться к элементам по индексам (начиная с 0) как со строкаими.\n"
      "Список изменяемый, то есть можно использовать 'list1[n] =' чтобы присвоить элменту n новое значение:")
list1=["a","b","c","d"]
print(f"list1 = '{list1}'.")
list1[2] = 123
print(f"list1[2] = {list1[2]}, тогда list1 = {list1}.\n"
      f"Видно, что списки могут содержать любой тип данных, в том числе сами списки (вложенные списки).")

print("\n======================================================================")
print("Список можно задать так: a = [n,...], можно так a = list([n,...])\n"
      f"Кстати, фунция list() может создавать список из любых перибираемых объектов, например:\n"
      f"a = list('список') = {list('список')}")

print("\n======================================================================")
print("\tlen() - длина списка, возвращает длину списка в int"
      "\tmax() - максимальное значение в списке, для цифр все понятно, для символов - Ascii.\n"
      "\tmin() - минимальное значение в списке, для цифр все понятно, для символов - Ascii.\n"
      "\tsum() - вычисление суммы, только для чисел.\n"
      "\tsorted() - сортировка коллекции, возвращает отсортированный список по возрастанию, для цифр все понятно, для символов - Ascii.\n"
      "\tМожно определить второй параметр True, чтобы сортировка была по убыванию.\n")

print("\n======================================================================")
print(f"+, *, in, del"
      f"ИЗ ЗА МОЕЙ РАБОТЫ СЕЙЧАС НЕТ ВРЕМЕНИ ПИСАТЬТ КОНСПЕКТ В ТАКОМ ФОРМАТЕ, ПОКА ЧТО УЧУСЬ ПРОСТО ТАК")