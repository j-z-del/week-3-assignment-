
count = 1
total = 0

# BUG: The while statement was missing a colon.
while count <= 5:
    # BUG: The original condition stopped at 4.
    # Using <= 5 includes the number 5.
    total = total + count
    count = count + 1

# BUG: An integer cannot be concatenated directly
# with a string, so an f-string is used instead.
print(f"Sum of 1 to 5 is: {total}")