# Find the correct order of traveled cities.
# input = [("Del", "Jam"), ("Jam","Kok"),("Hyd", "Mum"), ("Mum", "Ahm"), ("Ahm", "Del")]
# output = [("Hyd", "Mum"),("Mum", "Ahm"),("Ahm", "Del"),("Del", "Jam"),("Jam","Kok")]
# Cities are not repeated

# Idea is to find the start city and then lookup the next city on the basis of last destination

def get_route_order(cities: list) -> list:
    routes = dict(cities)
    result = []
    # Find the start city using getting difference of key value
    start = next(i for i in routes if i not in routes.values()) # Or start = next(iter(routes.keys() - routes.values()))
    # Iterate over and collect cities and keep changing start city on the basis of previous destination
    for _ in range(len(routes)):
        result.append((start, routes[start]))
        start=routes[start]

    return result

cities_visited = [("Del", "Jam"), ("Jam","Kok"),("Hyd", "Mum"), ("Mum", "Ahm"), ("Ahm", "Del")]
print(get_route_order(cities_visited)) # [("Hyd", "Mum"),("Mum", "Ahm"),("Ahm", "Del"),("Del", "Jam"),("Jam","Kok")]

