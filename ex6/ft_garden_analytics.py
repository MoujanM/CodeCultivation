# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/05 14:54:52 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 14:54:54 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenManager:
    """to handle multiple gardens"""
    
    # class-level variable to track all gardens
    total_gardens = 0

    def __init__(self, garden_owner: str) -> None:
        """
        Constructs garden with necessary attributes. 
        Each construction increments total_gardens.
        Class holds a list of plants in garden.
        """
        self.garden_owner = garden_owner
        self.plants = []
        GardenManager.total_gardens += 1
    
    @classmethod
    def create_garden_network(self):
        pass
    
    class GardenStats:
        """Child class to handle statistics calculations."""
        @staticmethod
        def count_types(plants: list) -> dict:
            
    
    

    @staticmethod
    def height_validation(height) -> bool:
        """Utility function to validate height > 0"""
        return height > 0

class Plant:
    """
    Parent class.
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
    
    def grow(self) -> None:
        """Function to simulate plant growth"""
        self.height += 1

class FloweringPlant(Plant):
    """
    Child class of Plant.

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
        """Specialised function returns bloom status."""
        return f'{self.name} is blooming beautifully!'

class PrizeFlower(FloweringPlant):
    """
    Grandchild of Plant.

    Attributes
    ----------
    name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        points : int
            count of prize points
    """
    def __init__(self, name: str, height: int, age: int,
                 points: int) -> None:
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
        self.points = points


