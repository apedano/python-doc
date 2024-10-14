# https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna
import lasagna

print(lasagna.BAKING_TIME)

still_to_bake = lasagna.calculate_remaining_baking_time(15)

print(still_to_bake)

time_to_prepare_4_layers = lasagna.preparation_time_in_minutes(4)

print (time_to_prepare_4_layers)

from lasagna import elapsed_time_in_minutes

print(elapsed_time_in_minutes.__doc__)

print(elapsed_time_in_minutes(3, 10))


def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
#spam