import random

import random

threeDigitCode = ""
for x in range(3):
    threeDigitCode += str(random.randint(1, 9))

fourDigitCode = ""
for x in range(4):
    fourDigitCode += str(random.randint(1, 6))

print(fourDigitCode)
print(threeDigitCode)