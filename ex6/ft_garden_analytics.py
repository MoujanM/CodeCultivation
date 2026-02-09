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
    """The Boss: handles and holds all gardens' data."""

    total_gardens = 0

    def __init__(self, owner: str) -> None:
        """
        Constructs garden with necessary attributes: Owner's name. 
        Each construction increments total_gardens.
        Class holds a list of plants in garden.
        """
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, new_plant: "Plant") -> None:
        """Function to add new plant to list of plants owned by a garden."""
        self.plants.append(new_plant)
        print (f"Added {new_plant.name} to {self.owner}'s garden.")
    
    def help_grow(self, plants: list) -> None:
        """"
        Function to grow all plants in garden simultaenously.
        Output used in report construction. 
        """
        print(f'{self.owner} is helping all plants grow ...')
        for plant in plants:
            plant.grow()
            print (f'{plant.name} grew 1cm')

    @classmethod
    def create_garden_network(cls, owners: list):
        """Classmethod to create network of all gardens managed."""
        network = []
        count = GardenManager.GardenStats.counter_help(owners)
        for i in range(count):
            network.append(cls(owners[i]))
        return network

    def get_garden_report(self) -> None:
        """Gets calculations from GardenStats and displays in organized way."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        plant_count = GardenManager.GardenStats.counter_help(self.plants)
        for i in range(plant_count):
            plant = self.plants[i]
            print(plant.report_status())
        print()
        print(f"Plants added: {plant_count}, Total growth: {plant_count}cm")
        types = GardenManager.GardenStats.count_types(self.plants)
        print(f"Plant types: {types["reg"]} regular, ", end="")
        print(f"{types["flow"]} flowering, ", end="")
        print(f"{types["prize"]} prize flowers")
        print()
        validation = GardenManager.GardenStats.height_validation(self.plants)
        print(f"Height validation test: {validation}")
        
    
    class GardenStats:
        """Child class to handle statistical calculations."""

        @staticmethod
        def counter_help(plants: list) -> int:
            """Because len() is not authorized."""
            count = 0
            for _ in plants:
                count += 1
            return count

        @staticmethod
        def count_types(plants: list) -> dict[str, int]:
            """
            Nested helper function to get plant-type stats.

            Attributes
            ----------
                plants : list
                    list of all plants in a garden
            
            Returns
            -------
                dictionary with plant : count format
            """
            types = {"reg" : 0, "flow" : 0, "prize" : 0}
            for p in plants:
                if p.__class__.__name__ == "PrizeFlower":
                    types["prize"] += 1
                elif p.__class__.__name__ == "FloweringPlant":
                    types["flow"] += 1
                else:
                    types["reg"] += 1
            return types

        @staticmethod
        def height_validation(plants: list) -> bool:
            """Utility function to validate all heights > 0."""
            count = GardenManager.GardenStats.counter_help(plants)
            for i in range(count):
                if plants[i].get_height() <= 0:
                    return False
            return True

        @staticmethod
        def get_score(plants: list) -> int:
            """Utility function to calculate a garden's score."""
            count = GardenManager.GardenStats.counter_help(plants)
            score = 0
            for i in range(count):
                score += 10
                score += plants[i].get_height()
                if plants[i].__class__.__name__ == "PrizeFlower":
                    score += plants[i].points
            return score

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
        """Constructs all necessary attributes for Plant object."""
        self.name = name
        if height > 0:
            self.__height = height
        if age > 0 and age < 5000:
            self.__age = age
    
    def report_status(self) -> str:
        """Function to streamline report creation."""
        return f"- {self.name}: {self.get_height()}cm"

    def grow(self) -> None:
        """Function to simulate plant growth"""
        self.__height += 1

    def get_height(self) -> int:
        """Function to access height safely."""
        return self.__height
    
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
        """
        super().__init__(name, height, age)
        self.color = color

    def report_status(self) -> str:
        """
        Function to streamline report creation.
        Calls super() to add specific info to base info.
        """
        base_info = super().report_status()
        return f"{base_info}, {self.color} flowers (blooming)"

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
        color : str
            specialized attribute
        points : int
            count of prize points
    """
    def __init__(self, name: str, height: int, age: int,
                 color: str, points: int) -> None:
        """
        Constructs all necessary attributes for Plant object.
        Calls super() to set up inherited basic features.
        """
        super().__init__(name, height, age, color)
        self.points = points

    def report_status(self) -> str:
        """
        Function to streamline report creation.
        Calls super() to add specific info to base info.
        """
        base_info = super().report_status()
        return f'{base_info}, Prize points: {self.points}'


if __name__ == "__main__":
    print(f'=== Garden Management System Demo ===')
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens[0]
    bob = gardens[1]
    
    p1 = Plant("Oak Tree", 100, 280)
    p2 = FloweringPlant("Rose", 25, 45, "red")
    p3 = PrizeFlower("Sunflower", 50, 60, "yellow", 10)
    p4 = PrizeFlower("Magic", 32, 50, "blue", 50)
    bob.plants = [p4]
    new_plants = [p1, p2, p3]
    for p in new_plants:
        alice.add_plant(p)
    print()
    alice.help_grow(alice.plants)
    print()
    # print alice's garden report
    alice.get_garden_report()
    # print additional info about garden network
    alice_score = GardenManager.GardenStats.get_score(alice.plants)
    bob_score = GardenManager.GardenStats.get_score(bob.plants)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")