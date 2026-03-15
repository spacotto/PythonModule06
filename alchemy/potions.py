"""
Part II: Import Transmutation
Advanced potion recipes
"""

from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    potion: str = "Healing potion brewed with"
    fire_result: str = create_fire()
    water_result: str = create_water()
    return f"{potion} {fire_result} and {water_result}"


def strength_potion() -> str:
    potion: str = "Strength potion brewed with"
    earth_result: str = create_earth()
    fire_result: str = create_fire()
    return f"{potion} {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    potion: str = "Invisibility potion brewed with"
    air_result: str = create_air()
    water_result: str = create_water()
    return f"{potion} {air_result} and {water_result}"


def wisdom_potion() -> str:
    potion: str = "Wisdom potion brewed with all elements:"
    fire_result: str = create_fire()
    water_result: str = create_water()
    earth_result: str = create_earth()
    air_result: str = create_air()
    all_four_results: str = (f"{fire_result}, "
                             f"{water_result}, "
                             f"{earth_result}, "
                             f"{air_result}")
    return f"{potion} {all_four_results}"
