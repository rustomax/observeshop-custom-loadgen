import random

# Check that generated number passes LUHN algorithm
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

# Generate a valid VISA card number
def generate_visa_card():
    number = '4' + ''.join([str(random.randint(0, 9)) for _ in range(14)])
    check_digit = [str(d) for d in range(10) if luhn_checksum(number + str(d)) == 0][0]
    return number + check_digit

# Split VISA number into blocks of 4 digits separated by a '-'
def format_digits(s):
    if len(s) != 16 or not s.isdigit():
        return "Invalid input. Please provide a string with exactly 16 digits."
    return '-'.join(s[i:i+4] for i in range(0, len(s), 4))

# Generate 10 sample VISA credit card numbers
sample_card_numbers = [generate_visa_card() for _ in range(10)]

# Print out VISA numbers formatted with separators
for i in range(10):
    print(format_digits(sample_card_numbers[i]))


