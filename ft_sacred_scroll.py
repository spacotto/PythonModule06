"""
Part I: The Sacred Scroll
Demonstration script (at repository root)
"""

import alchemy as alch
import alchemy.elements as elem


def bold(text: str) -> str:
    """A function making strings of text bold."""
    w, r = "\033[1;97m", "\033[0m"
    return f"{w}{text}{r}"


def div() -> None:
    """Prints a line divider."""
    print(" " + "-" * 60)


def demo() -> None:
    """Part I: The Sacred Scroll - Demo"""

    print()
    print(bold(' 📜 Sacred Scroll Mastery'))
    div()

    try:
        print(bold(' Testing direct module access:'))
        print(f" alchemy.elements.create_fire(): {elem.create_fire()}")
        print(f" alchemy.elements.create_water(): {elem.create_water()}")
        print(f" alchemy.elements.create_earth(): {elem.create_earth()}")
        print(f" alchemy.elements.create_air(): {elem.create_air()}")

        print()
        print(bold(' Testing package-level access'
                   ' (controlled by __init__.py):'))

    except AttributeError as e:
        print(f" Error: {e}")

    try:
        print(f" alchemy.create_fire(): {alch.create_fire()}")
    except AttributeError:
        print(" alchemy.create_fire(): AttributeError - not exposed")

    try:
        print(f" alchemy.create_water(): {alch.create_water()}")
    except AttributeError:
        print(" alchemy.create_water(): AttributeError - not exposed")

    try:
        print(f" alchemy.create_earth(): {alch.create_earth()}")
    except AttributeError:
        print(" alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f" alchemy.create_air(): {alch.create_air()}")
    except AttributeError:
        print(" alchemy.create_air(): AttributeError - not exposed")

    print()
    print(bold(' 📦 Package metadata'))
    div()
    print(f"{bold(' Version:')} {alch.__version__}")
    print(f" {bold('Author:')} {alch.__author__}")
    print()


if __name__ == "__main__":
    demo()
