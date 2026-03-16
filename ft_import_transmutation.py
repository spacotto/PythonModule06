"""
Part II: Import Transmutation
Demonstration script (at repository root).
"""

# Method 1 - Full module import
import alchemy.elements

# Method 2 - Specific function import
from alchemy.elements import create_water

# Method 3 - Aliased import
from alchemy.potions import healing_potion as heal

# Method 4 - Multiple imports
from alchemy.elements import create_fire, create_earth
from alchemy.potions import strength_potion


def bold(text: str) -> str:
    """A function making strings of text bold."""
    w, r = "\033[1;97m", "\033[0m"
    return f"{w}{text}{r}"


def div() -> None:
    """Prints a line divider."""
    print(" " + "-" * 60)


def demo() -> None:
    """Part II: Import Transmutation - Demo"""

    print()
    print(bold(' 🪄 Import Transmutation Mastery'))
    div()
    print()

    try:
        print(bold(' Method 1 - Full module import:'))
        print(' alchemy.elements.create_fire():'
              f' {alchemy.elements.create_fire()}')
        print()

        print(bold(' Method 2 - Specific function import:'))
        print(f' create_water(): {create_water()}')
        print()

        print(bold(' Method 3 - Aliased import:'))
        print(f' heal(): {heal()}')
        print()

        print(bold(' Method 4 - Multiple imports:'))
        print(f' create_earth(): {create_earth()}')
        print(f' create_fire(): {create_fire()}')
        print(f' strength_potion(): {strength_potion()}')
        print()

        print(bold(' All import transmutation methods mastered!'))

    except Exception as e:
        print(f' Error: {e}.')

    print()


if __name__ == "__main__":
    demo()
