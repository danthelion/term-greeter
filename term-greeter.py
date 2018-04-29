import argparse
import random
from typing import List

from pyfiglet import figlet_format, FigletFont
from termcolor import cprint, COLORS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', type=str, help='Text to display.', required=True)
    parser.add_argument('-c', '--color', type=str, help='Color to use (-lc to list all available).')
    parser.add_argument('-f', '--font', type=str, help='Font to use (-lf to list all available).')
    parser.add_argument('-lc', '--list-colors', action='store_true', help='List available colors.')
    parser.add_argument('-lf', '--list-fonts', action='store_true', help='List available fonts.')
    return parser.parse_args()


def get_fonts() -> List[str]:
    return FigletFont.getFonts()


def get_random_font(fonts: List[str]) -> str:
    return random.choice(fonts)


def get_colors() -> List[str]:
    return [c for c in COLORS.keys()]


def get_random_color(colors: List[str]) -> str:
    return random.choice(colors)


def list_colors(colors: List[str]) -> None:
    print('Available colors')
    print('\n'.join(colors))
    exit(0)


def list_fonts(fonts: List[str]) -> None:
    print('Available fonts')
    print('\n'.join(fonts))
    exit(0)


def print_colored_text(text: str = 'PLACEHOLDER TEXT',
                       font: str = None,
                       color: str = None
                       ) -> None:
    if not font:
        font = get_random_font(fonts=get_fonts())

    if not color:
        color = get_random_color(colors=get_colors())

    cprint(
        figlet_format(
            text=text,
            font=font,
            width=180
        ),
        color=color
    )


def main():
    args = parse_args()

    if args.list_colors:
        list_colors(colors=get_colors())

    if args.list_fonts:
        list_fonts(fonts=get_fonts())

    text_to_render = args.text.strip()
    print_colored_text(text=text_to_render, font=args.font, color=args.color)


if __name__ == '__main__':
    main()
