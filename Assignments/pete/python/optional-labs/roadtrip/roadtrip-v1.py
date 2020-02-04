city_dict = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

city_dict2 = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

class Trip():

    def __init__(self, starting_city, hops=1, city_dict=city_dict, city_dict2=city_dict2):
        self.starting_city = starting_city
        self.hops = hops
        self.city_dict = city_dict
        self.city_dict2 = city_dict2
    
    def show_cities(self):
        one_hop_set = self.city_dict[self.starting_city]
        one_hop_list = [city for city in one_hop_set]
        two_hops = [self.city_dict[city] for city in one_hop_list]
        print(f"one hop: {one_hop_set}")
        print(f"two hops: {two_hops}")

start_city = input("Starting city: ")

this_trip = Trip(start_city)
this_trip.show_cities()