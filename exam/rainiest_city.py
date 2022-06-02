def find_rainiest_city(filename):
    def get_rain_data():
        rain_data = []
        with open(filename, "r") as text:
            for line in text:
                rain_data.append(line.strip().split(";")[1:])
        return rain_data

    if not isinstance(filename, str):
        raise TypeError("Input filename as string, for example 'sample.txt'")

    rain_dict = {}
    for item in get_rain_data():
        city = item[0]
        rain_amount = int(item[1])
        rain_dict[city] = rain_dict.get(city, 0) + rain_amount
    return max(rain_dict, key=rain_dict.get)

# check output
print(find_rainiest_city("sample.txt"))
