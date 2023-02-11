from argparse import ArgumentParser
from .password_generator import PasswordGenerator


def get_args():
    parser = ArgumentParser(
        prog="PasswordGenerator",
        description="Generates passwords with different options",
    )
    parser.add_argument(
        "--no-cli",
        help="Generate password without cli",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "--length",
        help="Password length",
        type=int,
        required=False,
        default=20,
    )
    parser.add_argument(
        "--no_capitals",
        help="Disable capital letters from being used in password",
        action="store_true",
        required=False,
        default=False,
    )
    parser.add_argument(
        "--no_digits",
        help="Disable numbers from being used in password",
        action="store_true",
        required=False,
        default=False,
    )
    parser.add_argument(
        "--no_symbols",
        help="Disable symbols from being used in password",
        action="store_true",
        required=False,
        default=False,
    )
    return parser.parse_args()


def change_pw_len():
    while True:
        pw_len = input("Change password length: ")
        try:
            pw_len = int(pw_len)
        except:
            print("Please use numeric digits.")
            continue
        if pw_len < 1:
            print("Please enter a positive number.")
            continue
        return pw_len


def get_user_input(password_generator: PasswordGenerator):
    cli_active = True
    cli_option = ""
    hint_msg = "G to generate password; H for help; S to show settings; Q to quit;"
    print(hint_msg)
    while cli_active:
        cli_option = input("> ").lower()

        match cli_option:
            case "1":
                password_generator.length = change_pw_len()
            case "2":
                password_generator.use_capital = not password_generator.use_capital
                print(
                    "Use Capital Letters set to: " + str(password_generator.use_capital)
                )
            case "3":
                password_generator.use_digits = not password_generator.use_digits
                print("Use Numbers set to: " + str(password_generator.use_digits))
            case "4":
                password_generator.use_symbols = not password_generator.use_symbols
                print("Use Symbols set to: " + str(password_generator.use_symbols))
            case "g":
                print(password_generator.gen_pw())
            case "h":
                print(hint_msg)
            case "q":
                print("Bye bye!")
                cli_active = False
            case "s":
                print(password_generator)


def main():
    args = get_args()
    password_generator = PasswordGenerator()
    if args.no_cli:
        password_generator.length = args.length
        password_generator.use_capital = not args.no_capitals
        password_generator.use_digits = not args.no_digits
        password_generator.use_symbols = not args.no_symbols
        print(password_generator.gen_pw())
    else:
        print(password_generator)
        get_user_input(password_generator)


if __name__ == "__main__":
    main()
