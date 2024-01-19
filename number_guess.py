import random
print("HELLO :)")
random_number=random.randint(1,1000)

while True:
    user_input = int(input("Enter a number: "))

    if random_number==user_input:
        print("You guessed the number right!!")
        break

    if random_number>user_input:
        print("Number is too low")
        continue

    if random_number<user_input:
        print("Number is too high")
        continue
