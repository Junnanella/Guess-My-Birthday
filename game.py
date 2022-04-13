from random import randint

# Asks your name with the prompt "Hi! What is your name?"
name = input("Hi! What is your name?")

print(name)


# Python asks you up to five times
# Tries to guess your birth month and year with a prompt formatted like
# Guess «guess number» : «name» were you born in «m» / «yyyy» ?
# then prompts with "yes or no?"

for guess in range(1, 6):
    print("Guess ", guess, ":", name,
          "were you born in ", randint(1, 12), "/", randint(1924, 2004), "?")
    answer = input("yes or no?")

    if answer == "yes":
        print("I knew it!")
        exit()
    else:
        print("Drat! Lemme try again!")

print("I have other things to do. Goodbye")


# If the computer guesses it correctly because you respond yes,
# it prints the message I knew it! and stops guessing

# If the computer guesses incorrectly because you respond no,
# it prints the message Drat! Lemme try again! if it's only guessed 1, 2, 3, or 4 times.
# Otherwise, it prints the message I have other things to do. Good bye.

# It should only guess years between 1924 and 2004 including those years.
