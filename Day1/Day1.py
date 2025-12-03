import argparse

parser = argparse.ArgumentParser("day1")
parser.add_argument("input_file", help="The name of the file to parse.", type=str)
args = parser.parse_args()

class Dial:
    def __init__(self):
        self.position = 50
        self.password = 0

    def rotate(self, rotation):
        direction = rotation[0]
        amount = int(rotation[1:])

        if amount > 100:
            amount %= 100

        if direction == "L":
            self.position -= amount
        elif direction == "R":
            self.position += amount

        if self.position >= 100:
            self.position -= 100
        elif self.position < 0:
            self.position = 100 + self.position

        print(f"Position: {self.position}")

        if self.position == 0:
            self.password += 1

dial = Dial()

with open(args.input_file, "r") as input_file:
    for line in input_file:
        dial.rotate(line)

print(dial.password)