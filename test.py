from main import Pioneer, algorithms_control
import random
import matplotlib.pyplot as plt

if __name__ == '__main__':

    name_test = "search"

    algorithms_control = algorithms_control()

    if name_test == "dist":
        client = []
        for i in range(10):
            client.append(Pioneer(random.uniform(0, 5), random.uniform(0, 5), 1))
            print(client[i].coordinates_copter)


        ind_copter = algorithms_control.check_min_distance(1, client)

        print(ind_copter)
    elif name_test == "search":
        list = algorithms_control.trajectory_generation(point1=(1, 1), point2=(6, 6), dx=1, dy=2, z=1)
        print(list)
        print(len(list))

        for i in range(len(list)):
            plt.scatter(list[i][0], list[i][1])
        plt.show()
