# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 17:19:14 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 17:01:54 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """
    Class representing blueprint of all plants.

    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Constructs all necessary attributes for Plant object.

        Parameters
        ----------
            name : str
                plant name
            height : int
                height of plant in cm
            age : int
                age of plant in days
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """
        Function to access information about current plant status.
        Returns
        -------
            String containing plant type and attributes
        """
        class_type = self.__class__.__name__
        return f'{self.name} ({class_type}): {self.height}cm, {self.age} days'

    def special_info(self) -> str:
        """Placeholder for child-specific functions"""
        pass


class Flower(Plant):
    """
    Specialized child class of Plants representing blueprint of Flowers.

    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        color: str
            speciliazed attribute
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Constructs all necessary attributes for Plant object.
        Calls super() to set up inherited basic features.

        Parameters
        ----------
            name : str
                plant name
            height : int
                height of plant in cm
            age : int
                age of plant in days
            color: str
                speciliazed attribute
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f'{self.name} is blooming beautifully!'

    def get_info(self) -> str:
        generic_info = super().get_info()
        return f"{generic_info}, {self.color} color"

    def special_info(self) -> str:
        return self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = 3.14 * ((self.height / 100) ** 2)
        return f'{self.name} provides {shade} square meteres of shade'

    def get_info(self) -> str:
        generic_info = super().get_info()
        return f"{generic_info}, {self.trunk_diameter}cm diameter"

    def special_info(self) -> str:
        return self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition(self):
        return f'{self.name} is rich in {self.nutritional_value}'

    def get_info(self) -> str:
        generic_info = super().get_info()
        return f"{generic_info}, {self.harvest_season} harvest"

    def special_info(self) -> str:
        return self.get_nutrition()


if __name__ == "__main__":
    plant1 = Flower("Rose", 25, 30, "red")
    plant2 = Tree("Oak", 500, 1825, 50)
    plant3 = Vegetable("Tomato", 80, 90, "summer", "vitamic C")
    my_garden = [plant1, plant2, plant3]
    print("=== Garden Plant Types ===")
    for i in range(len(my_garden)):
        plant = my_garden[i]
        print(plant.get_info())
        print(plant.special_info())
        print()
