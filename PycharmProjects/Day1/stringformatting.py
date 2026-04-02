planets = {'Mercury':57.91, 'Venus':108.2, 'Earth':149.597870,'Mars':227.94}

for planet_name in planets:
    print(planet_name)

for planet_name in planets.keys():
    print(planet_name)

for planet_distance in planets.values():
    print(planet_distance)

for index, planet_name in enumerate(planets.keys(), start=1):
    print(index, planet_name, planets[planet_name])

for index, planet_name in enumerate(planets.keys()):
    print(index, planet_name, planets[planet_name])

for index, planet_name in enumerate(planets.keys(), start=1):
    print("Planet Num: {:2d} Name: {:<10s} {:06.2f}".format(index, planet_name, planets[planet_name]))

for index, planet_name in enumerate(planets.keys(), start=1):
    print(f"{index:2d}")