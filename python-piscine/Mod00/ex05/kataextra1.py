##################################################
###  Python's Format Specification Mini-Language #
##################################################

# Integer formatting
print("{:d}".format(42))   # '42'
print("{:x}".format(42))   # '2a'
print("0x0{:07x}".format(42))   # '2a'
print("{:o}".format(42))   # '52'
print("{:b}".format(42))   # '101010'

# Floating-point formatting
print("{:f}".format(3.141592653589793))  # '3.141593'
print("{:.2f}".format(3.141592653589793)) # '3.14'
print("{:e}".format(3.141592653589793))  # '3.141593e+00'

# Padding and alignment
print("{:10}".format("test"))  # Right-aligned by default: '      test'
print("{:<10}".format("test"))  # Left-aligned: 'test      '
print("{:^10}".format("test"))  # Centered: '   test   '

# Sign handling
print("{:+f}".format(3.14))  # '+3.140000'
print("{:+f}".format(3.14))  # '-3.140000'
print("{: >15f}".format(3.14))  # '3.140000'

print("{:->42}".format("The right format"))

kata = (0, 4, 132.42222, 10000, 12345.67)
formatted_string = (
    "module_" + format(kata[0], "02d") +
    " ex_" + format(kata[1], "02d") +
    " : " + format(kata[2], ".2f") +
    ", " + format(kata[3], ".2E") +
    ", " + format(kata[4], ".2E")
)
print(formatted_string)