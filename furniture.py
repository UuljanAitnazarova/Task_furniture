class Furniture:
    def __init__(self, bed, wardrobe, table):
        self.bed = bed
        self.wardrobe = wardrobe
        self.table = table
        
class House(Furniture):
    def __init__(self, houshold_type, total_area, bed, wardrobe, table):
        self.houshold_type = houshold_type
        self.total_area = total_area
        super().__init__(bed, wardrobe, table)


    def remaining_area(self):
        remaining_area = (self.total_area - self.bed - self.wardrobe - self.table)
        return f'The ramaining area is {remaining_area}'

    def __str__(self):
        return f'This {self.houshold_type} has {self.total_area} sq.m, of which bed takes {self.bed} sq.m, wardrobe takes {self.wardrobe} sq.m and table takes {self.table} sq.m.'


house1 = House('apartment', 100, 4, 2, 1.5)
print(house1.remaining_area())
print(house1)
house2 = House('villa', 450, 4, 5, 4)
print(house2.remaining_area())
print(house2)