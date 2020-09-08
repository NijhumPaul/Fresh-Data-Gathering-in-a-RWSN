import numpy as np
import random
from operator import itemgetter
import tsp
import matplotlib.pyplot as plt
import pickle

def network_generate(i, area, minimum_remaining_energy, maximum_energy):
    x = random.randint(0,area)
    y = random.randint(0,area)
    energy = minimum_remaining_energy + random.random() * maximum_energy
    #print(e)
    sensor = {'Node' : i ,'coordinates': [x,y], 'energy': energy}
    return sensor


def neighbors_selection(sensor, list_of_sensors):
    new_list_of_sensors = []
    for i in range (len(list_of_sensors)):
        #print("iteration i", i)
        #print("neighbors of coordinate " + str(list_of_sensors[i]['coordinates']) + "are.... ")
        x1 = list_of_sensors[i]['coordinates'][0]
        y1 = list_of_sensors[i]['coordinates'][1]
        #neighbor = []
        #list_of_sensors = [k for k in list_of_sensors if not (k['coordinates'] == i['coordinates'])]
        #print(len(list_of_sensors))
        neighbor = []
        for j in range (len(list_of_sensors)):
            #print("iteration j: ",j)
            x2 = list_of_sensors[j]['coordinates'][0]
            y2 = list_of_sensors[j]['coordinates'][1]
            #print(list_of_sensors[j]['coordinates'])
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

            if dist <= tx_range and list_of_sensors[i]!=list_of_sensors[j]:
                #print(dist)
                neighbor.append(list_of_sensors[j]['coordinates'])

        #print("nbr",neighbor)
        list_of_sensors[i]['neighbors'] = neighbor
        new_list_of_sensors.append(list_of_sensors[i])
    return new_list_of_sensors

def priority_value_calculation(new_sensor_list):
    new_list_for_priority = []
    for i in range(len(new_sensor_list)):
        #print("i", new_sensor_list[i])
        energy_i = new_sensor_list[i]['energy']
        #print(energy_i)
        neighbors_i = new_sensor_list[i]['neighbors']
        #print(neighbors_i)
        energy_sum = []
        for neighbors in range(len(neighbors_i)):

            #print(neighbors_i[neighbors])
            for j in range(len(new_sensor_list)):
                if str(new_sensor_list[j]['coordinates']) == str(neighbors_i[neighbors]):
                    #print("j", new_sensor_list[j])
                    neighbor_energy = new_sensor_list[j]['energy']
                    #print("neighbor_energy", neighbor_energy)
                    energy_sum.append(neighbor_energy)
        #print(energy_sum)
        #print(sum(energy_sum))
        priority_value_of_i = energy_i/(sum(energy_sum)+0.00001)
        #print("priority_value_of_i ", priority_value_of_i)
        new_sensor_list[i]['priority_value'] = priority_value_of_i
        new_list_for_priority.append(new_sensor_list[i])
    return new_list_for_priority



def ap_selection(sorted_priority_list):
    #print(sorted_priority_list)
    new_list = sorted_priority_list
    anchor_point_list = []
    while len(sorted_priority_list) > 0:
        #print(len(sorted_priority_list))
        anchor_point_list.append(sorted_priority_list[0]['coordinates'])
        #print("AP : ",anchor_point_list)
        neighbors_of_a = sorted_priority_list[0]['neighbors']
        sorted_priority_list.pop(0)
        for sensors in (neighbors_of_a):
            if len(sorted_priority_list) > 0:
                for nodes in new_list:
                    if nodes['coordinates'] == sensors:
                        sorted_priority_list.remove(nodes)



    return anchor_point_list

def solve_tsp_tsp(tuples_AP):
    t = tsp.tsp(tuples_AP)
    print("-----tsp-----")

    #print("Travelling distance: ", t[0])
    print("sequence", t[1])
    return  t[0]


def check_tsp():
    points = [(6734, 1453), (2233, 10),(5530, 1424),(401,  841),(3082, 1644),(7608, 4458),(7573, 3716),(7265, 1268),
(6898, 1885),(1112, 2049),(5468, 2606),(5989, 2873),(4706, 2674),(4612, 2035),(6347, 2683),(6107, 669),(7611, 5184),
(7462, 3590),(7732, 4723),(5900, 3561),(4483, 3369),(6101, 1110),(5199, 2182),(1633, 2809),(4307, 2322),(675, 1006),
(7555, 4819),(7541, 3981),(3177,  756),(7352, 4506),(7545, 2801),(3245, 3305),(6426, 3173),(4608, 1198),(23, 2216),
(7248, 3779),(7762, 4595),(7392, 2244),(3484, 2829),(6271, 2135),(4985, 140),(1916, 1569),(7280, 4899),(7509, 3239),
(10, 2676),(6807, 2993),(5185, 3258),(3023, 1942)]
    t = tsp.tsp(points)
    print("----check -tsp-----")
    # print("Travelling distance: ", t[0])
    print("sequence", t[1])
    print("distance", t[0])

def plot_network(new_sensor_list,achor_points):
    x = []
    y = []
    for i in range (len(new_sensor_list)):
        x.append(new_sensor_list[i]['coordinates'][0])
        y.append(new_sensor_list[i]['coordinates'][1])
    plt.scatter(x,y)
    plt.show()

    point1 = [1, 2]
    point2 = [3, 4]
    for i in range (len(anchor_points)-1):
        pt1 = anchor_points[i]
        pt2 = anchor_points[i+1]
        x_values = [pt1[0], pt2[0]]
        y_values = [pt1[1], pt2[1]]
    plt.plot(x_values, y_values)
    plt.show()


if __name__ == "__main__":
    #check_tsp()
    number_of_sensors = 300
    print("Number of sensors: ", number_of_sensors )
    area = 100
    print("Area of the network (meter-square): ", area)
    tx_range = 25
    minimum_remaining_energy = 10
    maximum_energy = 200
    print("Transmission range of each sensor (meter): ", tx_range)
    number_of_simulations = 100
    simulation_result = []
    simulation_ap = []
    for simulation in range(number_of_simulations):
        list_of_sensors = []
        for i in range(number_of_sensors):
            sensors = network_generate(i, area, minimum_remaining_energy, maximum_energy)
            list_of_sensors.append(sensors)


        '''with open('list_of_sensors', 'wb') as f:
            pickle.dump(list_of_sensors, f)
        with open('list_of_sensors', 'rb') as f:
            list_of_sensors = pickle.load(f)'''
        #list_of_sensors = list_of_sensors['arr_0']
        #print(list_of_sensors)
        new_sensor_list = neighbors_selection(sensors,list_of_sensors)
        priority_value_calculation(new_sensor_list)
        new_sensor_list = priority_value_calculation(new_sensor_list)
        sorted_priority_list = sorted(new_sensor_list,key=itemgetter('priority_value'),reverse=False)
        #ap_selection(sorted_priority_list)
        anchor_points = ap_selection(sorted_priority_list)
        simulation_ap.append(len(anchor_points))
        #plot_network(new_sensor_list, anchor_points)
        #print(anchor_points)
        tuples_AP = [tuple(l) for l in anchor_points]
        #print(tuples_AP)
        solve_tsp_tsp(tuples_AP)
        distance = solve_tsp_tsp(tuples_AP)
        simulation_result.append(distance)
    print("Number of sensors: ", number_of_sensors)
    print("Area of the network (meter-square): ", area)
    print("Transmission range of each sensor (meter): ", tx_range)
    print("Number of anchor points: ", (sum(simulation_ap)/number_of_simulations))
    final_distance = sum(simulation_result)/number_of_simulations
    print(final_distance)