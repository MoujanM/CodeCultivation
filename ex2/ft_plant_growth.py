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
    
def print_data(info: tuple):
    print(f'{info[0]}: {info[1]}cm, {info[2]} days old')
    
    
if __name__ == "__main__":
    total_days = int(input("Enter number of days: "))
    my_plant = Plant("Rose", 25, 30)
    plant_info = my_plant.get_info()
    print("=== Day 1 ===")
    print_data(plant_info)
    h1 = plant_info[1]
    i = 1
    for i in range(1, total_days):
        my_plant.grow()
        my_plant.aged()
        i += 1
    new_info = my_plant.get_info()
    h2 = new_info[1]
    print(f'=== Day {total_days} ===')
    print_data(new_info)
    print(f'Growth these {total_days} days: +{h2 - h1}cm')