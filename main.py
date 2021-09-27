#from gs_flight import FlightController, CallbackEvent
#from gs_navigation import LocalNavigation
import cv2
from apriltag import Detector,Detection


class Pioneer:
    def __init__(self, x, y, z):
        self.coordinates_copter = [(x, y), z]

class algorithms_control():
    def __init__(self):
        pass

    # min_distance = минимлаьное расстояние в матрах
    # clients = лист клиентов. У клиента есть поле coordinates_copter = [(x, y), z]
    def check_min_distance(self, min_distance, clients):
        calculating_distance = lambda p1, p2: ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

        ind_copters = []
        for i in range(len(clients)):
            for j in range(i + 1, len(clients)):
                dist = calculating_distance(clients[i].coordinates_copter[0], clients[j].coordinates_copter[0])
                if dist <= min_distance:
                    ind_copters.append(((i, j), dist))
        return ind_copters


    # Возвращает спиком траекторию для поиска маркеров
    # point1 = левый нижний угол зоны поиска
    # point2 = правый верхний угол зоны поиска
    # z = высота полета
    # dx, dy = шаг в метрах между проелатми
    def trajectory_generation(self, point1, point2, z, dx = 1, dy = 1):
        coordinates = [] # лист выходных координат

        # начальная точка создания траектории
        x = point1[0]
        y = point1[1]

        # "переключатели"
        x_step = True
        y_step = True

        # сохраняем нулевую точку
        coordinates.append((x, y, z))
        # множитель направления
        turn = 1
        while x_step:
            while y_step:
                y = y + dy * turn
                if y >= point2[1]:
                    turn = -1
                    y_step = False
                elif y <= point1[1]:
                    turn = 1
                    y_step = False
                coordinates.append((x, y, z))

            x = x + dx
            y_step = True
            if x > point2[0]:
                x_step = False
                break
            coordinates.append((x, y, z))
        return coordinates

    def find_apriltags(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = detector.detect(img)


if __name__ == '__main__':

    pass
