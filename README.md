# Password Generator Console Program

## About 

Simple password generator that provides a CLI or a "No-CLI" mode

This program provides options such as:
- Changing the password length
- Toggling capital letters to be used
- Toggling numbers to be used
- Toggling symbols to be used

## Setup

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python -m pw_gen --help
```

## Example Usage
Start the program in cli:
`python -m pw_gen`

Generate password without cli:
`python -m pw_gen --no-cli`

Generating password with options without cli:
`python -m pw_gen --no-cli --length=10 --no_capitals --no_digits --no_symbols`
