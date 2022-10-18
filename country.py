# Tian Lan


class Country:
    """Represents a country."""
    def __init__(self, country_name, capital_name, population):
        """
        This function assign the parameter values to the instance variables when the population is more than 2 million.
        Otherwise, a Value Error will be raised with a message.
        :param country_name: The name of the country.
        :param capital_name: The name of the capital.
        :param population: The population of the country.
        """
        if int(population) < 2000000:
            raise ValueError(f"Population {population} is too low.")
        else:
            pass
        self.country_name = country_name
        self.capital_name = capital_name
        self.population = population

    def print_details(self):
        """
        This function displays data in certain format.
        :return:
        """
        print(f"The capital of {self.country_name} (pop.{self.population}) is {self.capital_name.upper()}")

    def birth(self):
        """
        This function adds 1 to the object's own self's population.
        :return: The updated population.
        """
        self.population += 1

    def death(self):
        """
        This function subtracts 1 from the object's own self's population.
        :return: The updated population.
        """
        self.population -= 1

    def disaster(self):
        """
        This function subtracts 100 million from the population if the population of the country is 100 million or higher.
        For smaller countries, this function sets the population to 0.
        :return: The updated population
        """
        if self.population >= 100000000:
            self.population -= 100000000
        else:
            self.population = 0


def main():
    print("I should not be called.")


if __name__ == '__main__':
    main()
