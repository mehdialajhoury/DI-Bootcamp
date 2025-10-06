class Farm():

    # Init method : 2 attributes : farm name and dictionary of animals
    def __init__(self,farm_name):

        self.farm_name = farm_name
        self.animals = {}

    # If the animal exists in the dictionary, we increments the count with the count passed in arg
    # Else, we add the animal with its count
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    # Prints the name of each animal and its count
    def get_info(self):
        print(self.farm_name)
        for animal, count in self.animals.items():
            print(f"{animal} : {count}")
        print("“E-I-E-I-0!”")

    # Get list of all animal different types
    def get_animal_types(self):
        animal_list = []
        for animal, count in self.animals.items():
            animal_list.append(animal)
        return sorted(animal_list)
    
    # Returns a sentence that lists all types of animals
    # If several occurences of animals, we add a "s" in each animal type
    # Then, we return the complete sentence
    def get_short_info(self):

        string_output = "McDonald’s farm has "
        animal_types = self.get_animal_types()
        animal_list = []
        
        # Looping through the list of different animal types, and add a "s" if there are many of them of one type
        for animal in animal_types:
            count = self.animals[animal]
            if count > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)

        # String construction : looping through the animal list, and add each animal type
        # If the animal is not in the last or before the last position we add the type of animal sparated by a ","
        # Else if the animal is before the last on the list, we don't add a "," after,
        # Because otherwise, we add an "and" before the animal at the end of the list
        string_concat=""
        for animal in animal_list:
            if animal != animal_list[-1] and animal != animal_list[-2]:
                string_concat = string_concat + animal + ", "
            elif animal == animal_list[-2]:
                string_concat = string_concat + animal
            else:
                string_concat = string_concat + " and " + animal_list[-1]

        return string_output + string_concat
            
# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('pig', 1)
macdonald.get_info()
macdonald.get_animal_types()
print(macdonald.get_short_info())