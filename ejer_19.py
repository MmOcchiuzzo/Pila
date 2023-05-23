#Ejercicio_19

peliculas = [
    {"título": "Película 1", "estudio": "DC", "año de estreno": 2014},
    {"título": "Película 2", "estudio": "Marvel", "año de estreno": 2014},
    {"título": "Película 3", "estudio": "DC", "año de estreno": 2018},
    {"título": "Película 4", "estudio": "Marvel", "año de estreno": 2016},
    {"título": "Película 5", "estudio": "DC", "año de estreno": 2016},
    {"título": "Película 6", "estudio": "Marvel", "año de estreno": 2016}
]

#a)
def peliculas_2014(peliculas):
    peliculas_2014 = [p["título"] for p in peliculas if p["año de estreno"] == 2014]
    return peliculas_2014
print(peliculas_2014(peliculas))

#b)
def peliculas_2018(peliculas):
    cantidad_peliculas_2018 = sum(1 for p in peliculas if p["año de estreno"] == 2018)
    return cantidad_peliculas_2018
print(peliculas_2018(peliculas))

#c)
def peliculas_marvel_2016(peliculas):
    peliculas_marvel_2016 = [p["título"] for p in peliculas if p["estudio"] == "Marvel" and p["año de estreno"] == 2016]
    return peliculas_marvel_2016
print(peliculas_marvel_2016(peliculas))
