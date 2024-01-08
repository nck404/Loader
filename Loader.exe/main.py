from colorama import Fore, Style

def rgb(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"

colorspack = {
    "catpuccin": {
        "alpha": rgb(178, 186, 216),
        "digit": rgb(169, 137, 209),
        "bracket": rgb(88, 176, 194),
        "hyphen": rgb(40, 40, 40),
        "hash": rgb(241, 144, 130),
        "pipe": rgb(109, 151, 211),
        "other": Fore.WHITE,
    },
    "rose": {
        "alpha": rgb(178, 186, 216),
        "digit": rgb(169, 137, 209),
        "bracket": rgb(88, 176, 194),
        "hyphen": rgb(40, 40, 40),
        "hash": rgb(241, 144, 130),
        "pipe": rgb(109, 151, 211),
        "other": Fore.RED,
    }
}

def fprint(text, theme=None):
    default_colors = {
        "alpha": rgb(178, 186, 216),
        "digit": rgb(169, 137, 209),
        "bracket": rgb(88, 176, 194),
        "hyphen": rgb(40, 40, 40),
        "hash": rgb(241, 144, 130),
        "pipe": rgb(109, 151, 211),
        "other": Fore.WHITE,
    }

    colors = default_colors.copy()

    if theme and theme in colorspack:
        colors.update(colorspack[theme])

    for char in text:
        color_key = "other"
        if char.isalpha():
            color_key = "alpha"
        elif char.isdigit():
            color_key = "digit"
        elif char in ["[", "]"]:
            color_key = "bracket"
        elif char == "-":
            color_key = "hyphen"
        elif char == "#":
            color_key = "hash"
        elif char == "|":
            color_key = "pipe"

        print(colors[color_key] + char, end='')

    print(Style.RESET_ALL, end='')

# Example usage:
text = "Hello, world! This is [a sample] text with #numbers-and-symbols|."

# Get user input for theme
selected_theme = input("Choose a theme (catpuccin or rose): ")

# Print using the selected theme
if selected_theme in colorspack:
    fprint(text, selected_theme)
else:
    print("Invalid theme selected.")
