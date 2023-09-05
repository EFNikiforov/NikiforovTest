import math

# Задаем координаты точек водителя A и B в формате [x1, y1, x2, y2]
driverKoord = [0, 0, 11, 8]

# Задаем массив заказов, где заказ содержит координаты точки А и Б в формате [x1, y1, x2, y2]
orderArray = [
    [1, 5, 3, 8],
    [7, 7, 8, 10],
    [4, 1, 4, 5],
    [12, 5, 13, 8],
    [7, 1, 9, 5],
    [7, 3, 9, 5],
    [0, -2, 5, -2],
    [5, 6, 8, 8],
    [2, 3, -2, -1],
    [14, 3, 10, 5],
    [0, 0, -2, 4],
    [5, 4, 6, 5],
    [8, 3, 10, 0],
    [3, -2, 7, -4],
    [3, 1, 5, 3],
    [3, 7, 4, 4],
]

# # Задаем координаты точек водителя A и B в формате [x1, y1, x2, y2]
# driverKoord = [-13, -2, 7, -6]

# # Задаем массив заказов, где заказ содержит координаты точки А и Б в формате [x1, y1, x2, y2]
# orderArray = [
#     [-9, 8, -5, 4],
#     [-14, 3, -10, 0],
#     [-9, -5, -9, 3],
#     [-17, -2, 1 - 12, -3],
#     [-1, -1, 3, -3],
#     [-6, -6, -4, -2],
#     [-6, -8, -2, -9],
#     [-9, -10, -13, -6],
#     [3, -9, -2, -12],
#     [10, -2, 7, -4],
# ]

# # Задаем координаты точек водителя A и B в формате [x1, y1, x2, y2]
# driverKoord = [6, -2, 6, 10]

# # Задаем массив заказов, где заказ содержит координаты точки А и Б в формате [x1, y1, x2, y2]
# orderArray = [
#     [1, 5, 3, 8],
#     [7, 7, 8, 10],
#     [4, 1, 4, 5],
#     [12, 5, 13, 8],
#     [7, 1, 9, 5],
#     [7, 3, 9, 5],
#     [0, -2, 5, -2],
#     [5, 6, 8, 8],
#     [2, 3, -2, -1],
#     [14, 3, 10, 5],
#     [0, 0, -2, 4],
#     [5, 4, 6, 5],
#     [8, 3, 10, 0],
#     [3, -2, 7, -4],
#     [3, 1, 5, 3],
#     [3, 7, 4, 4],
# ]

# # Задаем координаты точек водителя A и B в формате [x1, y1, x2, y2]
# driverKoord = [-6, -6, -2, 2]

# # Задаем массив заказов, где заказ содержит координаты точки А и Б в формате [x1, y1, x2, y2]
# orderArray = [
#     [-9, 8, -5, 4],
#     [-14, 3, -10, 0],
#     [-9, -5, -9, 3],
#     [-17, -2, 1 - 12, -3],
#     [-1, -1, 3, -3],
#     [-6, -6, -4, -2],
#     [-6, -8, -2, -9],
#     [-9, -10, -13, -6],
#     [3, -9, -2, -12],
#     [10, -2, 7, -4],
# ]


def main():
    # Далее проверяем подходят ли по направлению вектора заказов
    def napravleniePodxoditVektor(koord, driverKoord, koeffperpen):
        if (
            koeffPerpenDriver * (driverKoord[2] - driverKoord[0])
            + driverKoord[1]
            - driverKoord[3]
        ) > 0:
            if (
                koeffperpen * (koord[0] - driverKoord[0]) + driverKoord[1] - koord[1]
                > 0
            ):
                return True
            else:
                return False
        else:
            if (
                koeffperpen * (koord[0] - driverKoord[0]) + driverKoord[1] - koord[1]
                < 0
            ):
                return True
            else:
                return False

    # Находим координаты векторов заказов относительно точки A водителя.
    # Так мы поймем в какую сторону заказ (заказы с обратным направлением по пути водителя не берем)
    def koordVektora(arrayPoints, driverKoord):
        x = driverKoord[0] - arrayPoints[0] + arrayPoints[2]
        y = driverKoord[1] - arrayPoints[1] + arrayPoints[3]
        return x, y

    # Ищем координаты точки лежащую на прямой AB маршрута водителя, находящийся на расстоянии радиуса от точки A и не лежащий на отрезке AB.
    def koordnazad(koord, r):
        l = koord[2] - koord[0]
        h = koord[3] - koord[1]
        d = math.sqrt(l * l + h * h)
        k = -(d / r)
        x = (koord[2] - koord[0] + k * koord[0]) / k
        y = (koord[3] - koord[1] + k * koord[1]) / k
        return x, y

    # Ищем координаты точек лежащих на прямой перпендикулярной AB маршрута водителя, находящийся на расстоянии радиуса от точки A.
    def koordsleva(koord, koeffPerpenDriver, r):
        g = 1 + koeffPerpenDriver * koeffPerpenDriver
        # координаты точки лежащей справа от прямой перпендикулярной AB маршрута водителя
        x1 = math.sqrt(r * r / g) + koord[0]
        x2 = -math.sqrt(r * r / g) + koord[0]
        #     # координаты точки лежащей слева от прямой перпендикулярной AB маршрута водителя
        y1 = koeffPerpenDriver * x1 + (koord[1] - koeffPerpenDriver * koord[0])
        y2 = koeffPerpenDriver * x2 + (koord[1] - koeffPerpenDriver * koord[0])
        return (x1, y1, x2, y2)

    # Тут мы находим по какую сторону прямой находятся наши начальные точки. По этой стороне нам следует брать точки.
    def findDirection(koeff, koordinatDirection, koordinatStart):
        if (
            koeff * (koordinatDirection[0] - koordinatStart[0])
            + koordinatStart[1]
            - koordinatDirection[1]
        ) > 0:
            return "up"
        else:
            return "down"

    # Функция, которая определяет по координатам точек A и B, лежат ли они в подходящей стороне от прямой
    def napravleniePodxodit(points, mainPointX, mainPointY, koeff, napr):
        if napr == "down":
            if (koeff * (points[0] - mainPointX) + (-points[1]) + mainPointY < 0) and (
                koeff * (points[2] - mainPointX) + (-points[3]) + mainPointY < 0
            ):
                return True
            else:
                return False
        elif napr == "up":
            if (koeff * (points[0] - mainPointX) + (-points[1]) + mainPointY > 0) and (
                koeff * (points[2] - mainPointX) + (-points[3]) + mainPointY > 0
            ):
                return True
            else:
                return False

    # Функция, которая определяет по координатам точек нахождение в подходящей области.
    def orderPodxKoefNull(
        koord, FunctionBottom, FunctionLeft, FunctionRight, FunctionTop
    ):
        if (koord[1] > FunctionBottom) and (koord[1] < FunctionTop):
            if (koord[3] > FunctionBottom) and (koord[3] < FunctionTop):
                if (koord[0] > FunctionLeft) and (koord[0] < FunctionRight):
                    if (koord[2] > FunctionLeft) and (koord[2] < FunctionRight):
                        return True

    # Сложим координаты вектора в массив
    vektorKoordPass = []
    for arrayPointsPassenger in orderArray:
        vektorKoordPass.append(koordVektora(arrayPointsPassenger, driverKoord))

    # Создадим новый массив заказов с подходящими направлениями
    newOrderArray = []

    # Задаем радиус области для нахождения подходящих заказов. (Его можно будет менять в зависимости от времени)
    r = 5

    # Условие, когда маршрут водителя параллельна оси Oy. В зависимости от направления маршрута ищем границы области
    if driverKoord[0] == driverKoord[2]:
        if driverKoord[3] - driverKoord[1] > 0:
            perpendFunctionBottom = driverKoord[1] - r
            perpendFunctionLeft = driverKoord[0] - r
            perpendFunctionRight = driverKoord[0] + r
            perpendFunctionTop = driverKoord[3]

            # Создаем новый массив с подходящими направлениями заказов
            for index, koord in enumerate(vektorKoordPass):
                if driverKoord[1] < koord[1]:
                    newOrderArray.append(orderArray[index])

            # Проходим по новому массиву и узнаем находятся ли координаты точек заказа в подходящей области
            for points in newOrderArray:
                if (
                    orderPodxKoefNull(
                        points,
                        perpendFunctionBottom,
                        perpendFunctionLeft,
                        perpendFunctionRight,
                        perpendFunctionTop,
                    )
                ) == True:
                    print("Заказ с координатами", points, "подходит")
        else:
            perpendFunctionBottom = driverKoord[1] + r
            perpendFunctionLeft = driverKoord[0] - r
            perpendFunctionRight = driverKoord[0] + r
            perpendFunctionTop = driverKoord[3]

            # Создаем новый массив с подходящими направлениями заказов
            for index, koord in enumerate(vektorKoordPass):
                if driverKoord[1] > koord[1]:
                    newOrderArray.append(orderArray[index])

            # Проходим по новому массиву и узнаем находятся ли координаты точек заказа в подходящей области
            for points in newOrderArray:
                if (
                    orderPodxKoefNull(
                        points,
                        perpendFunctionTop,
                        perpendFunctionLeft,
                        perpendFunctionRight,
                        perpendFunctionBottom,
                    )
                ) == True:
                    print("Заказ с координатами", points, "подходит")

    # Условие, когда маршрут водителя параллельна оси Ox. В зависимости от направления маршрута ищем границы области
    elif driverKoord[1] == driverKoord[3]:
        if driverKoord[2] - driverKoord[0] > 0:
            perpendFunctionBottom = driverKoord[0] - r
            perpendFunctionLeft = driverKoord[1] - r
            perpendFunctionRight = driverKoord[1] + r
            perpendFunctionTop = driverKoord[2]

            # Создаем новый массив с подходящими направлениями заказов
            for index, koord in enumerate(vektorKoordPass):
                if driverKoord[0] < koord[0]:
                    newOrderArray.append(orderArray[index])

            # Проходим по новому массиву и узнаем находятся ли координаты точек заказа в подходящей области
            for points in newOrderArray:
                if (
                    orderPodxKoefNull(
                        points,
                        perpendFunctionLeft,
                        perpendFunctionBottom,
                        perpendFunctionTop,
                        perpendFunctionRight,
                    )
                ) == True:
                    print("Заказ с координатами", points, "подходит")
        else:
            perpendFunctionBottom = driverKoord[0] + r
            perpendFunctionLeft = driverKoord[1] - r
            perpendFunctionRight = driverKoord[1] + r
            perpendFunctionTop = driverKoord[2]

            # Создаем новый массив с подходящими направлениями заказов
            for index, koord in enumerate(vektorKoordPass):
                if driverKoord[0] > koord[0]:
                    newOrderArray.append(orderArray[index])

            # Проходим по новому массиву и узнаем находятся ли координаты точек заказа в подходящей области
            for points in newOrderArray:
                if (
                    orderPodxKoefNull(
                        points,
                        perpendFunctionLeft,
                        perpendFunctionTop,
                        perpendFunctionBottom,
                        perpendFunctionRight,
                    )
                ) == True:
                    print("Заказ с координатами", points, "подходит")

    else:
        # Уравнение прямой маршрута водителя y = kx + b
        # Если не подходит по предыдущим условиям, то вычисляем угловой коэффициент прямой по координатам двух точек (k)
        koefFuncDriver = (driverKoord[1] - driverKoord[3]) / (
            driverKoord[0] - driverKoord[2]
        )

        # Узнаем угловой коэффициент прямой проходящей перпендикулярно маршруту водителя
        koeffPerpenDriver = -1 / koefFuncDriver

        # Создаем новый массив с подходящими направлениями заказов
        for index, koord in enumerate(vektorKoordPass):
            if napravleniePodxoditVektor(koord, driverKoord, koeffPerpenDriver) == True:
                newOrderArray.append(orderArray[index])

        # Ищем координаты точки лежащую на прямой AB маршрута водителя, находящийся на расстоянии радиуса от точки A и не лежащий на отрезке AB
        koordnazadX, koordnazadY = koordnazad(driverKoord, r)

        # Ищем координаты точек лежащих на прямой перпендикулярной AB маршрута водителя, находящийся на расстоянии радиуса от точки A.
        x1, y1, x2, y2 = koordsleva(driverKoord, koeffPerpenDriver, r)

        # Проходим по новому массиву и узнаем находятся ли координаты точек заказа в подходящей области
        for points in newOrderArray:
            if (
                napravleniePodxodit(
                    points,
                    koordnazadX,
                    koordnazadY,
                    koeffPerpenDriver,
                    findDirection(
                        koeffPerpenDriver,
                        driverKoord[0:2],
                        [koordnazadX, koordnazadY],
                    ),
                )
            ) == True:
                if (
                    napravleniePodxodit(
                        points,
                        x1,
                        y1,
                        koefFuncDriver,
                        findDirection(koefFuncDriver, driverKoord[0:2], [x1, y1]),
                    )
                ) == True:
                    if (
                        napravleniePodxodit(
                            points,
                            x2,
                            y2,
                            koefFuncDriver,
                            findDirection(koefFuncDriver, driverKoord[0:2], [x2, y2]),
                        )
                    ) == True:
                        if (
                            napravleniePodxodit(
                                points,
                                driverKoord[2],
                                driverKoord[3],
                                koeffPerpenDriver,
                                findDirection(
                                    koeffPerpenDriver,
                                    driverKoord[0:2],
                                    driverKoord[2:4],
                                ),
                            )
                        ) == True:
                            print("Заказ с координатами", points, "подходит")
    return


if __name__ == "__main__":
    main()
