"""
Demonstration script (at repository root)
"""

import alchemy
import alchemy.elements


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

    print(bold(' Testing direct module access:'))
    print(f" alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f" alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(f" alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f" alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print()
    print(bold(' Testing package-level access (controlled by __init__.py):'))

    try:
        print(f" alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError:
        print(" alchemy.create_fire(): AttributeError - not exposed")

    try:
        print(f" alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError:
        print(" alchemy.create_water(): AttributeError - not exposed")

    try:
        print(f" alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print(" alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f" alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print(" alchemy.create_air(): AttributeError - not exposed")

    print()
    print(bold(' 📦 Package metadata'))
    div()
    print(f"{bold(' Version:')} {alchemy.__version__}")
    print(f" {bold('Author:')} {alchemy.__author__}")
    print()

if __name__ == "__main__":
    demo()
