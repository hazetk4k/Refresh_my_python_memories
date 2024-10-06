import pickle  # библиотека для работы с бинарными данными

com1 = ["Spider-man", 200]
com2 = ["Iron-man", 300]
com3 = ["Avengers", 500]
com4 = ["Hellboy", 800]

try:
    with open("out.bin", "rb") as file:
        #pickle.dump(com1, file)
        #pickle.dump(com2, file)
        #pickle.dump(com3, file)
        #pickle.dump(com4, file)
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except:
    print("Smthng went wrong!(((")
print(b1, b2, b3, b4, sep="\n")
