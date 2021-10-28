from math import sqrt

def polnaya_zzalupa (): #ax²+bx+c=0
    a1 = input("Введите число а: ")
    b1 = input("Введите число b: ")
    с1 = input("Введите число с: ")
    a = float (a1.replace (',', '.'))
    b = float (b1.replace (',', '.'))
    с = float (с1.replace (',', '.'))

    D = (b ** 2) - (4 * a * с)
    if D > 0:
        print("x₁ =", str((-b + sqrt(D)) / (2 * a)))
        print("x₂ =", str((-b - sqrt(D)) / (2 * a)))
    elif D == 0:
        print("x =", str(-b / (2 * a)))
    else:
        print("Действительных корней нет.")

def nepolnaya_zzalupa_1 (): #ax²+bx=0
    a1 = input("Введите число а: ")
    b1 = input("Введите число b: ")
    a = float (a1.replace (',', '.'))
    b = float (b1.replace (',', '.'))
    print("x₁ = 0")
    print("x₂ =", str(-b / a))

def nepolnaya_zzalupa_2 (): #ax²+с=0
    a1 = input("Введите число а: ")
    c1 = input("Введите число c: ")
    a = float (a1.replace (',', '.'))
    c = float (c1.replace (',', '.'))
    k = -c/a
    if k > 0:
        print("x₁ =", str(sqrt(k)))
        print("x₂ =", str(-sqrt(k)))
    else:
        print("Действительных корней нет.")

def nepolnaya_zzalupa_3 (): #ax²=0
    print ("x = 0")

while True:
    print ("Щеглы и щеглыхи, на выбор у вас есть несколько типов квадратного уравнения:")
    print ("")
    print ("1 - ax²+bx+c=0")
    print ("2 - ax²+bx=0")
    print ("3 - ax²+с=0")
    print ("4 - ax²=0")
    print ("")
    try:
        h = int(input ("Выберите тип квадратного уравнения: "))
        if h == 1:
            print ("")
            polnaya_zzalupa()
            print ("")
            print ("*Смачно сквиртанул и выключил программу*")
            break
        elif h == 2:
            print ("")
            nepolnaya_zzalupa_1()
            print ("")
            print ("*Смачно сквиртанул и выключил программу*")
            break
        elif h == 3:
            print ("")
            nepolnaya_zzalupa_2()
            print ("")
            print ("*Смачно сквиртанул и выключил программу*")
            break
        elif h == 4:
            print ("")
            nepolnaya_zzalupa_3()
            print ("")
            print ("*Смачно сквиртанул и выключил программу*")
            break
        elif h == 993:
            print ("")
            print ("*Смачно сквиртанул и выключил программу*")
            break
        else:
            print ("Выбор некорректен, повторите ещё раз или введите 993 для выхода.")
    except:
        print ("Выбор некорректен, повторите ещё раз или введите 993 для выхода.")