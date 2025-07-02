""" ПРИМЕР ПРОСТЕЙШЕЙ МОДЕЛИ НС ФРЕНКА РОЗЕНБЛАТТА """
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
    print("НУ ты норм бэйба")
else:
    print("Бачу, нищуган")