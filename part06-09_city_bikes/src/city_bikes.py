# tee ratkaisu tänne
# Write your solution here

def get_station_data(filename: str) -> dict:
    
    name_location = {}
    with open(filename) as file:
        for line in file:
            if line[0].isalpha():
                continue
            line = line.strip()
            line_list = line.split(";")
            name_location[line_list[3]] =(float(line_list[0]), float(line_list[1]))  # setting location as key and coordinates as tuples and value
    return name_location

def distance(stations : dict, station1: str, station2: str) -> float:
    import math
    
    if station1 in stations and station2 in stations:
        longitude1 = stations[station1][0]
        latitude1 = stations[station1][1]

        longitude2 = stations[station2][0]
        latitude2 = stations[station2][1]
        

        x_km = (longitude1 - longitude2) * 55.26
        y_km = (latitude1 - latitude2) * 111.2
        distance_km = math.sqrt(x_km**2 + y_km**2)

        return distance_km

def greatest_distance(stations: dict):
    import math

    outcome_tuple = ()
    cities = []
   
    distance = 0

    for key,value in stations.items():
        cities.append(key)
    
    for key,value in stations.items():
        for city in cities:
            longitude1, latitude1 = stations[key]
            longitude2, latitude2 = stations[city]
            #print(longitude1, latitude1)
            #print(longitude2, latitude2)

            x_km = (longitude1 - longitude2) * 55.26
            y_km = (latitude1 - latitude2) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)

            if distance_km > distance:
                distance = distance_km
                outcome_tuple = (key,city,distance)
    return outcome_tuple

