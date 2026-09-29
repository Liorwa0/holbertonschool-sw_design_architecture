#!/usr/bin/env python3
"""
Decorator Pattern - Coffee shop beverage customization
"""
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract base class for beverages."""

    @abstractmethod
    def cost(self) -> int:
        """Return the total cost of the beverage."""
        pass

    @abstractmethod
    def description(self) -> str:
        """Return the description of the beverage."""
        pass


class Coffee(Beverage):
    """Base coffee beverage implementation."""

    def cost(self) -> int:
        """Return base coffee cost."""
        return 50

    def description(self) -> str:
        """Return base coffee description."""
        return "Coffee"


class MilkDecorator(Beverage):
    """Decorator to add milk to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize with inner beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Add milk cost to inner beverage."""
        return self._inner.cost() + 10

    def description(self) -> str:
        """Add milk description to inner beverage."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Decorator to add sugar to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize with inner beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Add sugar cost to inner beverage."""
        return self._inner.cost() + 5

    def description(self) -> str:
        """Add sugar description to inner beverage."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Decorator to add caramel to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize with inner beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Add caramel cost to inner beverage."""
        return self._inner.cost() + 15

    def description(self) -> str:
        """Add caramel description to inner beverage."""
        return self._inner.description() + " + caramel"


def main() -> None:
    """Main execution point."""
    b1 = MilkDecorator(Coffee())
    print(f"{b1.description()} {b1.cost()}")

    b2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{b2.description()} {b2.cost()}")

    b3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{b3.description()} {b3.cost()}")


if __name__ == "__main__":
    main()
