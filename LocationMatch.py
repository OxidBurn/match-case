from dataclasses import dataclass


@dataclass
class Location:
    country: str
    city: str

    def __init__(self, country, city):
        self.country = country
        self.city = city

def test_positional_args(location):
    match location:
        case Location("Germany", "Berlin"):
            print("Hallo Berlin!")
        case Location(_, "London"):
            print("There's London in multiple countries...")
        case Location("Canada", _):
            print("Hello Canada!")

test_positional_args(Location("Canada", "Toronto"))
