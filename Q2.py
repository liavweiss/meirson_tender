# this fun return the payment for each participant, by "Meirson tender".
def payments(values: list, choice_rule) -> list:
    payments_list = [0] * len(values)
    bool_list = choice_rule(values)
    for index in range(len(values)):
        if bool_list[index] is True:
            values_copy = values.copy()
            while True:  # calculate the threshold value for each participant.
                values_copy[index] -= 0.01
                bool_list_copy = choice_rule(values_copy)
                if bool_list_copy[index] is not True:
                    payments_list[index] = values_copy[index] + 0.01
                    break
    return payments_list


# Example 1: choice_rule = select_the_max_value
def select_the_max_value(values: list) -> int:
    bool_list = [False] * len(values)
    index = values.index(max(values))
    bool_list[index] = True
    return bool_list


# Example 2: choice_rule = select_the_two_max_value
def select_the_two_max_value(values: list) -> int:
    values_copy = values.copy()
    bool_list = [False] * len(values)
    index = values.index(max(values))
    bool_list[index] = True
    values_copy[index] = -1
    index = values_copy.index(max(values_copy))
    bool_list[index] = True
    return bool_list


# Example 3: choice_rule = select_the_three_max_value
def select_the_three_max_value(values: list) -> int:
    values_copy1 = values.copy()
    values_copy2 = values.copy()
    bool_list = [False] * len(values)
    index = values.index(max(values))
    bool_list[index] = True
    values_copy1[index] = -1
    values_copy2[index] = -1
    index = values_copy1.index(max(values_copy1))
    bool_list[index] = True
    values_copy1[index] = -1
    values_copy2[index] = -1
    index = values_copy2.index(max(values_copy2))
    bool_list[index] = True
    return bool_list


# Example 4: choice_rule = select_all_the_larger_ten_10
def select_all_the_larger_ten_10(values: list) -> int:
    bool_list = [False] * len(values)
    for index in range(len(values)):
        if values[index] > 10:
            bool_list[index] = True
    return bool_list


# Example 5: choice_rule = select_calculate_to_25_5
def select_calculate_to_25_5(values: list) -> int:
    bool_list = [False] * len(values)
    for index in range(len(values)):
        for index2 in range(len(values)):
            if values[index] + values[index2] == 25.5:
                bool_list[index] = True
                bool_list[index2] = True
    return bool_list


if __name__ == '__main__':
    example_list = [9.8, 9.9, 10.3, 10.5, 15.0]
    print("Example 1: choice_rule = select_the_max_value: ", payments(example_list, select_the_max_value))
    print("Example 2: choice_rule = select_the_two_max_value: ", payments(example_list, select_the_two_max_value))
    print("Example 3: choice_rule = select_the_three_max_value: ", payments(example_list, select_the_three_max_value))
    print("Example 4: choice_rule = select_all_the_larger_ten_10: ", payments(example_list, select_all_the_larger_ten_10))
    print("Example 5: choice_rule = select_calculate_to_25_5: ", payments(example_list, select_calculate_to_25_5))


