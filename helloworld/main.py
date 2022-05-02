# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

def say_hello() -> None:
    greeting = "Hello World"
    print(green(greeting))


if __name__ == "__main__":
    say_hello()
