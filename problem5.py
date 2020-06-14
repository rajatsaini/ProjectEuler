"""
From the user daushako, one of the neatest and efficient solution
"""

number=1
for i in range(2,21):
    if number%i !=0:
        for j in range(2, 21):
            if i % j == 0:
                number *= j
                break
print(number)