class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def print_data(my_garden):
    print("=== Garden Plant Registry ===")
    for plant in my_garden:
        print(f'{plant.name}: {plant.height}cm, {plant.age} days old')
    print("=== End of Program ===")
    
    
if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    my_garden = [plant1, plant2, plant3]
    print_data(my_garden)