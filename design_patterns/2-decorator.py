from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


class Coffee(Beverage):
    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    b1 = MilkDecorator(Coffee())
    print(f"{b1.description()} {b1.cost()}")

    b2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{b2.description()} {b2.cost()}")

    b3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{b3.description()} {b3.cost()}")


if __name__ == "__main__":
    main()
