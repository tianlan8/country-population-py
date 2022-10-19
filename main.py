# Tian Lan

from data import countries_and_capitals
import country
import random


def main():
    """
    This function creates a list of Country objects and handles all Value Error exception. If there's no exception,
    calls methods for each object and displays the data in certain format.
    :return: The data in certain format.
    """
    try:
        all_countries = []
        for i in countries_and_capitals:
            country_name = i[0]
            capital_name = i[1]
            population = random.randint(1000000, 1000000000)
            country_info = [country_name, capital_name, population]
            all_countries.append(country_info)  # a list of Country objects

        for country_info in all_countries:
            each_country = country.Country(country_info[0], country_info[1], country_info[2])
            each_country.print_details()
        print("-----------------------------------------------------------------------")

        for country_info in all_countries:
            each_country = country.Country(country_info[0], country_info[1], country_info[2])
            each_country.birth()
            each_country.print_details()
        print("-----------------------------------------------------------------------")

        for country_info in all_countries:
            each_country = country.Country(country_info[0], country_info[1], country_info[2])
            each_country.death()
            each_country.print_details()
        print("-----------------------------------------------------------------------")

        for country_info in all_countries:
            each_country = country.Country(country_info[0], country_info[1], country_info[2])
            each_country.disaster()
            each_country.print_details()
        print("-----------------------------------------------------------------------")
    except ValueError as v:
        print("oops")
        print(str(v))


if __name__ == '__main__':
    main()
