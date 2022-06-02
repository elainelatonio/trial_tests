def check_hamming_distance(string, list_of_strings):
    MAX_HAMMING_DISTANCE = 3

    def check_parameters():
        if not isinstance(string, str):
            raise TypeError("First parameter must be a string")
        if not isinstance(list_of_strings, list):
            raise TypeError("Second parameter must be a list of strings")
        if not is_list_of_same_len_strings():
            raise ValueError("List must contain strings of the same length as first parameter.")
        return True

    def is_list_of_same_len_strings():
        if all([isinstance(member, str) for member in list_of_strings]):
            return all([len(member) == len(string) for member in list_of_strings])
        return False

    def get_hamming_distances():
        hamming_distances = {}
        for member_string in list_of_strings:
            hamming_distances[member_string] = 0
            for position in range(len(string)):
                if member_string[position] != string[position]:
                    hamming_distances[member_string] = hamming_distances.get(member_string) + 1
        return hamming_distances

    if check_parameters():
        return [string for string, distance in get_hamming_distances().items() if distance <= MAX_HAMMING_DISTANCE]


print(check_hamming_distance("apple", ["apple", "apply", "tuple", "alter"]))
print(check_hamming_distance("monkey", ["donkey", "monday", "shaker"]))
