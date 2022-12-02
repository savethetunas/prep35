def get_common_movies(list_of_sets):
    ret = {}
    for thing in list_of_sets:
        for movie in thing:
            ret[movie] = 0

    ret1 = []
    for mov in list_of_sets:
        for j in mov:
            ret1.append(j)

    dict_keys = ret.keys()
    for ele in ret1:
        if ele in dict_keys:
            ret[ele] += 1

 #   small_tot = tuple_of_data[0]  # saves the total small dictionary
    max_small = max(ret.values())  # saves the max value of the small dict
    small_word = [key for key, value in ret.items() if value == max_small]

    return (set(small_word))




