"""
Part IV: Breaking the Circular Curse
Validates spell ingredients
"""


def validate_ingredients(ingredients: str) -> str:
    """Check if ingridients are valid or not."""
    valid_elements = ["fire", "water", "earth", "air"]
    for element in valid_elements:
        if element in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
