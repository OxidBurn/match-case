from types import SimpleNamespace

class InSet(set):
    def __eq__(self, elem):
        return elem in self

Produce = SimpleNamespace(
    fruit=InSet({"apple", "banana", "peach"}),
    vegetable=InSet({"cucumber", "lettuce", "onion"})
)

food = "cucumber"

match food:
    case Produce.fruit:
        print(f"{food} is a fruit.")
    case Produce.vegetable:
        print(f"{food} is a vegetable.")