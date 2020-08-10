from enum import Enum


class TicketClass(int, Enum):
    upper = 1
    middle = 2
    lower = 3


class Sex(str, Enum):
    male = "male"
    female = "female"
