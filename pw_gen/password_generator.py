import random
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from tabulate import tabulate


class PasswordGenerator:
    def __init__(
        self,
        length: int = 20,
        use_capital: bool = True,
        use_digits: bool = True,
        use_symbols: bool = True,
    ):
        self.length = length
        self.use_capital = use_capital
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def __str__(self):
        headers = ["#", "Setting Name", "Value"]
        table = [
            [1, "Password Length", self.length],
            [2, "Use Capital Letters", self.use_capital],
            [3, "Use Numbers", self.use_digits],
            [4, "Use Symbols", self.use_symbols],
        ]
        return tabulate(table, headers, tablefmt="github")

    def gen_pw(self) -> str:
        password = ""
        choices = [ascii_lowercase]

        if self.use_capital:
            choices.append(ascii_uppercase)
        if self.use_digits:
            choices.append(digits)
        if self.use_symbols:
            choices.append(punctuation)

        for _ in range(self.length):
            password += random.choice(random.choice(choices))
        return password
