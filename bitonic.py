def longest_bitonic(distances):
    inflection = (len(distances) - 1) / 2
    tendency = 0
    t_list = []
    choices = []
    indices = []
    escape = 0
    for x in range(0, len(distances) - 1):
        if distances[x + 1] >= distances[x]:
            tendency = 1
            t_list.append(tendency)
        else:
            tendency = -1
            t_list.append(tendency)

    start_indices = [i for i, x in enumerate(t_list) if x == 1]

    for index in start_indices:
        run_length = 0
        for x in range(len(t_list)):
            if index < len(t_list) - 1:
                if (t_list[index] == t_list[index + 1]):
                    run_length += 1
                    index += 1
                elif (t_list[index] > t_list[index + 1]):
                    inflection = index
                    index += 1
                    run_length += 1

        choices.append(run_length)
        indices.append(inflection)
    for i, x in enumerate(choices):
        if x == max(choices):
            escape = indices[i]
    return escape
