import utility

### Helper Functions for Printing Results ###
def print_reversed(input) -> None:
    print(input, "->", utility.utils.reversed(input))

def print_formatter(input):
    print(input, "->", utility.utils.formatter(input))

### Reversed Function Testing ###
print("REVERSE TESTING")

## String Test Cases
print("String Test Cases")
print_reversed("12345")
print_reversed("string")
print("\n")

## Float Test Cases
print("Float Test Cases")
print_reversed(12.345)
print_reversed(0.102)
print("\n")

## Integer Test Cases
# Include test cases with 0s to see if results get messed up
print("Integer Test Cases")
print_reversed(12345)
print_reversed(-10520)
print_reversed(20000)
print("\n")

### Formatter Testing ###
print("FORMATTER TESTING")

## String Test Cases
print("String Test Cases")
print_formatter("12345")
print_formatter("string")
print("\n")

## Float Test Cases
print("Float Test Cases")
print_formatter(12.345)
print_formatter(0.102)
print("\n")

## Integer Test Cases
# Include test cases with 0s to see if results get messed up
print("Integer Test Cases")
print_formatter(16)
print_formatter(-16)
print_formatter(1234)
print_formatter(-105)
print_formatter(200)
print_formatter(0)
print("\n")
