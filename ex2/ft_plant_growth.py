class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow_tall(self):
        self.height += 1

    def grow_old(self):
        self.age += 1

    def get_info(self) -> tuple:
        return (self.name, self.height, self.age)


def print_data(info: tuple):
    print(f'{info[0]}: {info[1]}cm, {info[2]} days old')


if __name__ == "__main__":
    # growth of Rose over a week #
    my_plant = Plant("Rose", 25, 30)
    plant_info = my_plant.get_info()
    print("=== Day 1 ===")
    print_data(plant_info)
    h1 = plant_info[1]
    i = 1
    for i in range(1, 7):
        my_plant.grow_tall()
        my_plant.grow_old()
        i += 1
    new_info = my_plant.get_info()
    h2 = new_info[1]
    print('=== Day 7 ===')
    print_data(new_info)
    print(f'Growth this week: +{h2 - h1}cm')