import test_pack

# файл __init__ говорит о том что это пакет, он выполняется автоматически при импорте пакета

print(dir(test_pack))
x = test_pack.get_python()
print(x)
print(test_pack.htmldoc.doc)
