airports = {"DCA": "Washington D.C.", "IAD": "Dulles",
            "LHR": "London-Heathrow", "SVO": "Moscow",
            "CDA": "Chicago Midway", "SBA": "Santa Barbara",
            "LAX": "Los Angeles", "JFK": "New York City",
            "MIA": "Miami", "AUM": "Austin, Minnesota"}

flights = [("Southwest", 145, "DCA", 1, 6.00), ("United", 31, "IAD", 1, 7.1), ("United", 302, "LHR", 5, 6.5),
           ("Aeroflot", 34, "SVO", 5, 9.00), ("Southwest", 146, "CDA", 1, 9.60),
           ("United", 46, "LAX", 5, 6.5), ("Southwest", 23, "SBA", 6, 12.5),
           ("United", 2, "LAX", 10, 12.5), ("Southwest", 59, "LAX", 11, 14.5),
           ("American", 1, "JFK", 12, 11.3), ("USAirways", 8, "MIA", 20, 13.1),
           ("United", 2032, "MIA", 21, 15.1), ("SpamAir", 1, "AUM", 42, 14.4)]

if __name__ == '__main__':
    flights.sort(key=lambda flight: flight[0])
    f = 'Flight'
    d = 'Destination'
    g = 'Gate'
    t = 'Time'
    print(f'{f:13}\t\t{d:17}\t{g:4}\t{t:4}')
    print("----------------------------------------------------")
    for n, i in enumerate(flights):
        j = 0
        toPrint = []
        for item in i:
            toPrint.append(item)
        flightName = str(toPrint[0]) + " " + str(toPrint[1])

        dest = airports[str(toPrint[2])]

        print(f'{flightName:13}\t\t{dest:17}\t{toPrint[3]:2}\t\t{toPrint[4]:4}')

