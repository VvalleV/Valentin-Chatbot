import random

rules = [
    (["hello", "hi", "hey", "wsp", "wsg"], [
        "Hey! Nice to meet you.",
        "Hello! How's your day going?",
        "Hi there!"
    ]),

    (["good", "very good", "great", "fine"], [
        "That's great to hear!",
        "Nice! What are you planning to do today?",
        "It is very nice hearing that you are doing well"
    ]),

    (["bad", "not good", "tired"], [
        "Ah that sucks. Want to talk about it?",
        "Hope things get better soon.",
        "Thats not very good, If you want to talk about it im all ears"
    ]),
]

print("Hey there! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("It was nice talking to you!")
        break

    if name is None:
        name = input("By the way, what's your name? ")
        print(f"Nice to meet you {name}!")

    elif age is None:
        age = input(f"How old are you {name}? ")
        print(f"Cool! {age} is a very mature age.")

   