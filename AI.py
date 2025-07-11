# # """ ПРИМЕР ПРОСТЕЙШЕЙ МОДЕЛИ НС ФРЕНКА РОЗЕНБЛАТТА """
import numpy as np # вектора

def act(x):  # функция активации
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])  #вектор входного сигнала
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]  #веса для нейронов скрытого слоя

    weight1 = np.array([w11, w12]) #матрица 2х3 (2 нейрона скрытого слоя на 3 вход данных)
    weight2 = np.array([-1, 1])    #вектор связи для выходного нейрона 1х2

    sum_hidden = np.dot(weight1, x)  #вычисляем сумму на входах нейронов скрытого слоя
    print("Значение сумм на нейронах скрытого слоя: " +str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])  #вектор выходных значений с каждого нейрона скрытого слоя (
                                                                                        # сумму пропускаем через Func активации)
    print("Значение на выходах нейронов скрытого слоя:" +str(out_hidden))

    sum_end = np.dot(weight2, out_hidden) #вычисляем сумму на выходном нейроне последнего слоя
    y = act(sum_end) #пропускаем ее через функцию активации
    print("Выходные значения НС:" +str(y))

    return y

house = int(input("Есть дом?\n"))
rock = int(input("Любишь рок\n"))
attr = int(input("Ты красивый?\n"))

res = go(house,rock, attr)
if res == 1:
    print("Да, ты мне подходишь")
else:
    print("нет, не сойдемся")

'''------------------------------------------------------------------------------------------------------------------'''

#'''КЛАССЫ ЛИНЕЙНО РАЗДЕЛИМЫЙ ОБРАЗОВ '''
#'''Персептрона корректно классифицирует образы'''
#'''Первый случай без смещения '''
import matplotlib.pyplot as plt

N = 5  #кол-во образов для классов


x1 = np.random.random(N) #моделируем случайные величины по одной оси
x2 = x1 + [np.random.randint(10)/10 for i in range(N)]  # х2 будет моделироваться как х1 + случайное отклонение
C1 = [x1, x2] #точки лежат выше прямой

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for j in range(N)] - 0.1 #делаем "-", чтобы х2 была ниже прямой
C2 = [x1, x2]

f = [0, 1] # прямая под 45 гр

w = np.array([-0.3, 0.3]) # Задаем веса (k = 1) для нашей НС
for i in range(N): # Перебираем все образы для классав
    x = np.array([C1[0][i], C1[1][i]])   # Можно менять C1 с С2
    y = np.dot(w, x) # Вычисляем выходное значение y
    if y >= 0:
        print("Класс С1")
    else:
        print("Класс С2")

plt.scatter(C1[0][:], C1[1][:], s = 10, c = "red") # Отображаем точки для первого класса
plt.scatter(C2[0][:], C2[1][:], s = 10, c = "blue") # Отображаем точки для второго класса
plt.plot(f) # Отображаем разделяющею прямую
plt.grid(True)
plt.show()




#'''Второй случай смещения образов '''
N = 5  #кол-во образов для классов
b = 3 # Это само смещение


x1 = np.random.random(N) #моделируем случайные величины по одной оси
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] + b
C1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for j in range(N)] - 0.1 + b
C2 = [x1, x2]

f = [0+b, 1+b] # прямая под 45 гр


w2 = 0.5
w3 = -b * w2 # автоматически вычисляем омегу 3, зная омегу 2
w = np.array([-w2, w2, w3])
for i in range(N): # Перебираем все образы для классов
    x = np.array([C1[0][i], C1[1][i], 1])   # Можно менять C1 с С2
    y = np.dot(w, x) # Вычисляем выходное значение y
    if y >= 0:
        print("Класс С1")
    else:
        print("Класс С2")

plt.scatter(C1[0][:], C1[1][:], s = 10, c = "red") # Отображаем точки для первого класса
plt.scatter(C2[0][:], C2[1][:], s = 10, c = "blue") # Отображаем точки для второго класса
plt.plot(f) # Отображаем разделяющею прямую
plt.grid(True)
plt.show()



#'''Task XOR '''

def act(x):
    return 0 if x <= 0 else 1

def go(C):
    x = np.array([C[0], C[1], 1])
    w1 = [1, 1, -1.5]
    w2 = [1, 1, -0.5]
    w_hidden = np.array([w1, w2])
    w_out = np.array([-1, 1, -0.5])

    summa = np.dot(w_hidden, x)
    out = [act(x) for x in summa]
    out.append(1)
    out = np.array(out)

    summa = np.dot(w_out, out)
    y = act(summa)
    return y

C1 = [(1, 0), (0, 1)]
C2 = [(0, 0), (1, 1)]


print( go(C1[0]), go(C1[1]))
print( go(C2[0]), go(C2[1]))


