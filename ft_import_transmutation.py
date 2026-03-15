"""
Part II: Import Transmutation
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
    """Part II: Import Transmutation - Demo"""
    pass


if __name__ == "__main__":
    demo()
