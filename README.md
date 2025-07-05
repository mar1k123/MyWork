# 🚀 My Coding Journey
Hi! This is my repository where I save solutions to problems, pet projects, and code experiments. Here you can track my programming progress and find useful examples.


## Explanation of the First Code for AI

This code performs how works fully connected AI with step activation function (Perceptron)
                            (Полносвязная НС со ступенчатой активационной функцией).

![image](https://github.com/user-attachments/assets/5bb55581-8c8e-4631-95b5-1365c9f7f74c)
![image](https://github.com/user-attachments/assets/7546f87a-6895-40ea-a5c7-2cb38eeda285)



## Explanation of the Second Code for AI

This code performs how works fully connected AI with step activation function
                            (Полносвязная НС со ступенчатой активационной функцией).

![image](https://github.com/user-attachments/assets/eeeed56e-8329-4aca-b7e0-c9cfbf43d4c4)
![image](https://github.com/user-attachments/assets/5d745b40-4267-4463-b1e9-e2f969c5e428)

### Explanation for the second picture in the second code:
Assume that all these images are shifted upward along the X₂ axis, meaning the situation looks like this – . If our line passes through the origin, then no matter how it is rotated, there will always be classification errors everywhere. Therefore, we need to add a bias term. That’s why in neural networks, an additional input is introduced for shifting the decision boundary (bias)—a threshold value that offsets our separating line. This additional input will always have a fixed value of +1 and its own weight. In this case, our line can be expressed in the following form:

Оъяснение для второго случая:
Предположим что все эти образы смещены вверх по оси X2, т.е картина такая - . Если нашая прямая будет проходить через начало координат, то как-бы она не была повернута, везде будут получаться ошибки классификации, т.е необходимо добавить смещение. Поэтому в НС дополнительно определяют еще один вход для смещения разделяющей гиперплоскости (bias),
т.е пороговое значение, которое смещает нашу разделяющею прямую. Дополнительный вход всегда будет иметь значение +1 и вес. И в этом случае наша прямая может быть записана в данном виде

### Task XOR
![image](https://github.com/user-attachments/assets/fb89f7fc-b293-44dc-b198-af1ec583593a)
![image](https://github.com/user-attachments/assets/1d3a3575-7dfb-4bc7-9926-9faad380daca)
![image](https://github.com/user-attachments/assets/bda08aa8-723a-4a51-b647-0877df240571)

##Explanation:
Let the images be distributed given images, then the linear dividing plane will not be able to classify the images. Then we can draw 2 diagonals. But what kind of NS is capable of this? In fact, each dividing line can be represented by a separate neuron, and then the result of their classification is combined by the resulting output neuron. That is, we must take more complex NS structures. This structure presents 2 neurons of the hidden layer for two dividing lines and a resulting neuron, which must combine the dividing planes so that we can select images C1, and beyond it C2. Let the signals 0 / 1 be fed to the input, then the entire set of our images can be represented as a truth table for the bitwise XOR operation. Next, each neuron will have an activation function f (x). It remains to determine the connection weights. But first, let's assume that the first neuron will form a line inclined at 45 degrees, having an angular coefficient of -1 and an offset of 1.5. That is, how we need to choose the weight coefficients in order to get this line. Let's use the previously calculated formula x2. Next, the 2nd neuron will form the next division (picture ). Now we need to combine the work of 2 neurons in such a way that this strip is formed, when added together we get the following picture (picture ), but by passing it through the activation function we get 1 and 0, i.e. we cannot simply combine them. We should subtract the result of the work of the 1st neuron from the result of the 2nd neuron, and then we will get the correct plane. Next, for reliability, we will shift (picture ) by -0.5, since the activation function is triggered at 0, and to make it more reliable we will shift it. That is, the final weights of our NN can be chosen as follows (picture ). Thus, thanks to the additional neurons of the hidden layer, we were able to form a more complex area for determining our images

Пусть образы, распределены данный образов, тогда линейно разделяющая плоскость не сможет классифицировать образы. Тогда можно провести 2 диагонали. Но что за НС, которая способна на это? В действительности каждая разделительная линия может быть представлена отдельным нейроном, а затем результат их классификации объединяется результирующим
выходным нейроном. То есть мы должны взять более сложные структуры НС. В данной структуре представлены 2 нейрона скрытого слоя для двух разделяющий линий и результирующий нейрон, который должен так объединять разделяющие плоскости, чтобы  мы могли выделять образы C1, а за её пределами С2. 
Пусть на вход подаются сигналы 0 / 1, тогда весь набор наших образов можно представить в виде таблицы истинности для битого операции XOR. Далее у каждого нейрона будет активационная функция f(x). Осталось определить веса связи. Но для начала предположим, что первый нейрон будет формировать линия, наклонённую по 45 гр, имеющую угловой коэф.-1 и смещение 1.5. Т.е как нам необходимо выбрать весовые коэф. для того, чтобы получилась данная прямая. Воспользуемся ранее вычисленной формулой x2. Далее 2 нейрон будет формировать следующее разделение (picture ). Теперь нам необходимо объединить работу 2 нейронов таким образом, чтобы сформировалась данная полоса, при сложении мы получим следующею картину (picture ), но пустив ее через активационную функцию мы получим 1 и 0, т.е просто сожить их не получиться. Следует вычесть из результата работы 2 нейрона результат работы 1 нейрона, и тогда получим верную плоскость. Далее для надежности (picture ) сместим на -0.5, т.к активационная функция срабатывает в 0, и чтобы это было надежнее мы это сместим. Т.е итоговые веса нашей НС можно выбрать такие (picture ). Таким образом, благодаря дополнительным нейронам скрытого слоя, мы смогли сформировать более
сложную область для определения наших образов


