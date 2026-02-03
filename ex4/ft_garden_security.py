# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 16:52:09 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/02 18:07:26 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.__height = 0
        self.__age = 0
        # guarding against initialization with negs
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height >= 0:
            self.__height = height
            print(f'Height updated: {height}cm [OK]')
        else:
            print(f'Invalid operation attempted: height {height}cm [REJECTED]')
            print("Security: Negative height rejected")

    def set_age(self, age):
        # cannot be negative
        # print error msg
        if age >= 0:
            self.__age = age
            print(f'Age updated: {age} days [OK]')
        else:
            print(f'Invalid operation attempted: age {age}days [REJECTED]')
            print("Security: Negative age rejected")

    def get_height(self):
        # encapsulated - private property
        return self.__height

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    plant = SecurePlant("Rose", 10, 5)
    print("=== Garden Security System ===")
    print(f'Plant created: {plant.name}')
    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    info = f'({plant.get_height()}cm, {plant.get_age()} days)'

    print(f'Current plant: {plant.name} {info}')
