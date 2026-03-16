"""
Part III: The Great Pathway Debate
Demonstration script (at repository root)
"""

import alchemy.transmutation
from alchemy.transmutation import (lead_to_gold,
                                   stone_to_gem,
                                   philosophers_stone,
                                   elixir_of_life)


def bold(text: str) -> str:
    """A function making strings of text bold."""
    w, r = "\033[1;97m", "\033[0m"
    return f"{w}{text}{r}"


def div() -> None:
    """Prints a line divider."""
    print(" " + "-" * 60)


def demo() -> None:
    """Part III: The Great Pathway Debate - Demo"""

    print()
    print(bold(' 🗺️ Pathway Debate Mastery'))
    div()

    try:
        print()
        print(bold(' Testing Absolute Imports (from basic.py):'))
        print(f' lead_to_gold(): {lead_to_gold()}')
        print(f' stone_to_gem(): {stone_to_gem()}')

        print()
        print(bold(' Testing Relative Imports (from advanced.py):'))
        print(f' philosophers_stone(): {philosophers_stone()}')
        print(f' elixir_of_life(): {elixir_of_life()}')

        print()
        print(bold(' Testing Package Access:'))
        print(' alchemy.transmutation.lead_to_gold():'
              f' {alchemy.transmutation.lead_to_gold()}')
        print(' alchemy.transmutation.philosophers_stone():'
              f' {alchemy.transmutation.philosophers_stone()}')

        print()
        print(' Both pathways work! Absolute: clear, Relative: concise')

    except Exception as e:
        print()
        print(f' Error: {e}.')

    print()


if __name__ == "__main__":
    demo()
