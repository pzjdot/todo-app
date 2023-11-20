def parse(user_input):

    user_input = user_input.split(",")
    lower_bound = int(user_input[0])
    upper_bound = int(user_input[1])

    return {"lower_bound": lower_bound, "upper_bound": upper_bound}

