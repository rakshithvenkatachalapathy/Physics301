airports = {"DCA": "Washington D.C.", "IAD": "Dulles",
            "LHR": "London-Heathrow", "SVO": "Moscow",
            "CDA": "Chicago Midway", "SBA": "Santa Barbara",
            "LAX": "Los Angeles", "JFK": "New York City",
            "MIA": "Miami", "AUM": "Austin, Minnesota"}


# class FlightsDeatails:
#     name = ""
#     number = 0
#     heading_to = ""
#     gate = 0
#     time = 0.
# 
#     def __init__(self, name, number, heading_to, gate, time):
#         self.name = name
#         self.number = number
#         self.heading_to = heading_to
#         self.gate = gate
#         self.time = time
# 
#     def __repr__(self):
#         return repr((self.name, self.number, self.heading_to, self.gate, self.time))


flights = [("Southwest", 145, "DCA", 1, 6.00), ("United", 31, "IAD", 1, 7.1), ("United", 302, "LHR", 5, 6.5),
           ("Aeroflot", 34, "SVO", 5, 9.00), ("Southwest", 146, "CDA", 1, 9.60),
           ("United", 46, "LAX", 5, 6.5), ("Southwest", 23, "SBA", 6, 12.5),
           ("United", 2, "LAX", 10, 12.5), ("Southwest", 59, "LAX", 11, 14.5),
           ("American", 1, "JFK", 12, 11.3), ("USAirways", 8, "MIA", 20, 13.1),
           ("United", 2032, "MIA", 21, 15.1), ("SpamAir", 1, "AUM", 42, 14.4)]
flights.sort(key=lambda flight: flight[0])

# for n, i in enumerate(flights):
#     temp = i[2]
#     #i[1] = airports[temp]
#     j=0
#     for item in i:
#         if j==0:
print("Flight\t\tDestination\t\tGate\t\tTime")
print("--------------------------------------------")
for n, i in enumerate(flights):
    j = 0
    for item in i:
        if j == 0:
            print(item + " ", end='')
        elif j == 2:
            print(airports[item] + "\t\t", end='')
        else:
            item = str(item)
            print(item + "\t\t", end='')
        j += 1
    print()

