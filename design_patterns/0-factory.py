#!/usr/bin/env python3
"""
Factory pattern - Extending a registry without modifying creation logic.
"""


class Bus:
    """Bus vehicle type."""
    def mode(self) -> str:
        return "road"


class Train:
    """Train vehicle type."""
    def mode(self) -> str:
        return "rails"


class Bike:
    """Bike vehicle type."""
    def mode(self) -> str:
        return "lane"


class Scooter:
    """Scooter vehicle type."""
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    """Factory class managing vehicle creation via registry."""
    def __init__(self) -> None:
        self._registry = {}

    def register_kind(self, name: str, cls: type) -> None:
        """Register a new vehicle type mapping."""
        self._registry[name] = cls

    def create(self, kind: str):
        """Instantiate a vehicle based on the registered key."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main() -> None:
    """Main execution function."""
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
