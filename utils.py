import turtle


def find_max(numbers):
    maximum = numbers[0]
    for item in numbers:
        if item > maximum:
            maximum = item
    return maximum


def createhid(word, accessor):
    stick = "_" * len(word)
    return stick


def makeman(man):
    man.color("green")
    man.pencolor("black")
    size_of_bottom = 50
    man.goto(0, size_of_bottom)
    man.goto(100, size_of_bottom)
    man.goto(100, 0)
    man.goto(100, size_of_bottom)
    man.goto(50, size_of_bottom)
    man.goto(50, 200)
    man.goto(150, 200)
    man.goto(150, 150)


def hurt(counter, man):
    if counter == 1:
        man.penup()
        man.goto(150, 130)
        man.pendown()
        man.circle(10)
    if counter == 2:
        man.goto(150, 120)
        man.goto(140, 110)
    if counter == 3:
        man.goto(150, 120)
        man.goto(160, 110)
    if counter == 4:
        man.goto(150, 120)
        man.goto(150, 90)
    if counter == 5:
        man.goto(140, 80)
    if counter == 6:
        man.goto(150, 90)
        man.goto(160, 80)


def hangman():
    wn = turtle.Screen()
    wn.bgcolor("green")
    man = turtle.Turtle()
    makeman(man)
    letters = []
    word = input("Word: ")
    for item in range(20):
        print()
    stick = createhid(word, "_")
    counter = 0
    chack = 0
    print(stick + " Word Length: " + str(len(word)))
    while word != stick and counter < 6:
        print(f"Used Letters: {letters}")
        guess = input("letter: ")
        if not(guess in letters):
            letters.append(guess)
        while (len(guess) != 1) and guess != word :
            guess = input("You can only write a new letter or the word. Choose again: ")
        if not (guess in word):
            counter += 1
        else:
            if guess == word:
                stick = word
                break

            for item in range(len(word)):
                if guess == word[item]:
                    stick = stick[:item] + word[item] + stick[item + 1:]
        print()
        print(stick + " Word Length: " + str(len(word)))
        print(f"Counter: {counter}")
        if counter != chack:
            hurt(counter, man)
            chack = counter

    if word == stick:
        print("You won")
    else:
        print("You lost")

    wn.exitonclick()
