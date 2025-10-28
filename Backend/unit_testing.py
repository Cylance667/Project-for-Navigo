import main

def coordinates_to_timezone_test():
    test_values = [(41.522459, -99.601647), (38.714447, -81.996503), (16.032615, 18.554861), (63.028812, 96.904030), ("hello", "world")]

    for test_value in test_values:
        print(f"Test Location: {test_value}, Function output: {main.lat_long_to_timezone(test_value[0], test_value[1])}")


def coordinates_to_news_test():
    main.initialize()
    test_coordinates = [(40.712776, -74.005974), (55.755825, 37.617298), (51.507351, -0.127758), (55.350232, -26.614342)]

    for test_coordinate in test_coordinates:
        main.get_news_for_location(test_coordinate[0], test_coordinate[1])
        print(f"Test Location: {test_coordinate}, Function output: {main.lat_long_to_timezone(test_coordinate)}\n")


def coordinates_to_weather_test():
    main.initialize()
    test_coordinates = [(40.712776, -74.005974), (55.755825, 37.617298), (51.507351, -0.127758), (55.350232, -26.614342)]
    test_units = ["Celsius", "Fahrenheit"]

    for test_coordinate, test_unit in zip(test_coordinates, test_units):
        main.get_weather_for_location(test_coordinate[0], test_coordinate[1], test_unit)
        print(f"Test Location: {test_coordinate}, Unit: {test_unit}, Function output: {main.get_weather_for_location(test_coordinate[0], test_coordinate[1], test_unit)}\n")


if __name__ == '__main__':
    result = coordinates_to_news_test()
    print(f"Function output: {result}")