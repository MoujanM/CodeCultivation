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