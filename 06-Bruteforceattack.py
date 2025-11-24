password = "12345"
tries = 5

while tries > 0:
    guess = input("Enter password: ")

    if guess == password:
        print("Correct. You may enter.")
        break
    else:
        tries = tries - 1
        print("Wrong password. Attempts left:", tries)

if tries == 0:
    print("Too many wrong tries. Authorities notified.")