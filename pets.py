def describe_pet(animal_type, pet_name):
    """Display information about pet. """
    print(f"\nI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}. ")

describe_pet('hamster', 'harry')
#practising multiple functions
describe_pet('dog', 'willie')

#default values
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}. ")

describe_pet("willie")

#the code can also be wriiten as the following and would still work 
describe_pet('harry', 'hamster')
describe_pet(pet_name="harry", animal_type='hamster')
describe_pet(animal_type='hamster', pet_name="harry")