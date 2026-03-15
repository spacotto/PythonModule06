"""
Part IV: Breaking the Circular Curse
Demonstration script (at repository root)
"""

def bold(text: str) -> str:
    """A function making strings of text bold."""
    w, r = "\033[1;97m", "\033[0m"
    return f"{w}{text}{r}"


def div() -> None:
    """Prints a line divider."""
    print(" " + "-" * 60)


def demo() -> None:
    """Part IV: Breaking the Circular Curse - Demo"""

    print()

    try:
        print(bold(' Circular Curse Breaking'))
        div()

        print()
        print(bold(' Testing ingredient validation:'))
        print(' validate_ingredients("fire air"): '
              f'{validate_ingredients("fire air")}')
        print(' validate_ingredients("dragon scales"): '
              f'{validate_ingredients("dragon scales")}')

        print()
        print(bold(' Testing spell recording with validation:'))
        print(' record_spell("Fireball", "fire air"): '
              f'{record_spell("Dark Magic", "shadow")}')
        print(' record_spell("Dark Magic", "shadow"): '
              f'{record_spell("Dark Magic", "shadow")}')

        print()
        print(bold(' Testing late import technique:'))
        print(' record_spell("Lightning", "air"): '
              f'{record_spell("Lightning", "air")}')

        print()
        print(' Circular dependency curse avoided using late imports!')
        print(' All spells processed safely!')

    except Exception as e:
        print(f' Error: {e}')

    print()


if __name__ == "__main__":
    demo()
