BAKING_TIME=40

def calculate_remaining_baking_time(time_in_oven):
    return BAKING_TIME - time_in_oven

def preparation_time_in_minutes(number_of_layers):
    return 2 * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + calculate_remaining_baking_time(elapsed_bake_time)



