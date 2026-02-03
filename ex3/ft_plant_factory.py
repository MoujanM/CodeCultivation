# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 16:01:36 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/02 16:50:20 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def aged(self):
        self.age += 1

    def get_info(self) -> tuple:
        return (self.name, self.height, self.age)

    " classmethod function "
    " creates plant objest from given list of params "
    @classmethod
    def init_factory(cls, info_lst: list) -> "Plant":
        return cls(*info_lst)


if __name__ == "__main__":
    plant_data = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    my_garden = [Plant.init_factory(data) for data in plant_data]
    for plant in my_garden:
        print(f'Created: {plant.name} ({plant.height}cm, {plant.age}days)')
