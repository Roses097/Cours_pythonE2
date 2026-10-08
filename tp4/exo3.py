# ♠,♣,♦,♥
from colorama import *

shades = ("♠", "♣", "♦", "♥")
shade_names = ("pique", "trefle", "diamond", "heart")

value_points = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
value_txts = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")

foreground_colors = (Fore.BLACK, Fore.BLACK, Fore.RED, Fore.RED)


class CardValue:
    def __init__(self, value_txt: str, value_pts: int):
        self.value_txt = value_txt
        self.value_pts = value_pts

    def __str__(self):
        return self.value_txt


class CardColor:
    def __init__(self, shade, shade_name, foreground_color, background_color):
        self.shade = shade
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color

    def __str__(self):
        return f"{self.shade} {self.shade_name} {self.foreground_color} {self.background_color}"


class Card:
    def __init__(self, value: CardValue, color: CardColor):
        self.value = value
        self.color = color

    def is_equal_value(self, card: "Card") -> bool:
        return self.value.value_pts == card.value.value_pts

    def __lt__(self, other):
        return self.value.value_pts < other.value.value_pts

    def __gt__(self, other):
        return self.value.value_pts > other.value.value_pts

    def __le__(self, other):
        return self.value.value_pts <= other.value.value_pts

    def __ge__(self, other):
        return self.value.value_pts >= other.value.value_pts

    def __str__(self):
        c = self.color
        return f"{c.background_color}{c.foreground_color} {self.value}{c.shade} {Style.RESET_ALL}"
