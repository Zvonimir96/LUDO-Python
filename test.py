from utilities import fade_max_limit, fade_min_limit

num_figures = 5
fade_alfa = 100

# Postaviti vrijednost početne pozicije
value = fade_alfa
print(value)

fade_range = fade_max_limit - fade_min_limit
step = fade_range/num_figures

for i in range(num_figures):
    value -= step

    if value < fade_min_limit:
        value = fade_min_limit + fade_min_limit - value
        step = -step

    print(value)
