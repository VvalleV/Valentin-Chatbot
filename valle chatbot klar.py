import random
import datetime
import os

# --- Funktioner ---
def get_time():
    now = datetime.datetime.now()
    print("Chatbot:", "The time is", now.strftime("%H:%M"))

def get_date():
    today = datetime.date.today()
    print("Chatbot:", "Today's date is", today)

def get_time_and_date():
    now = datetime.datetime.now()
    print("Chatbot:", "Now it is", now.strftime("%Y-%m-%d %H:%M"))

def get_day():
    today = datetime.datetime.now().strftime("%A")
    print("Chatbot:", "Today is", today)

def open_spotify():
    os.system("start spotify") 
    print("Chatbot:", "Opening Spotify...")

# --- Intents ---
intents = {
    "time": {
        "keywords": ["time", "what time", "current time", "clock"],
        "responses": ["Let me check the time."]
    },
    "date": {
        "keywords": ["date", "today's date", "what date"],
        "responses": ["Let me get the date."]
    },
    "time_date": {
        "keywords": ["time and date", "both time and date"],
        "responses": ["Let me check both time and date."]
    },
    "day": {
        "keywords": ["day", "what day", "day today", "weekday"],
        "responses": ["Let me check what day it is."]
    },
    "spotify": {
        "keywords": ["spotify", "open spotify", "music"],
        "responses": ["Opening Spotify for you."]
    }
}

# --- Rules ---
rules = [
    (["hello", "hi", "hey", "wsp", "wsg", "hello there", "yo"], [
        "Hey! Nice to meet you.",
        "Hello! How's your day going?",
        "Hi there!"
    ]),
    (["good", "very good", "great", "fine", "awesome"], [
        "That's great to hear!",
        "Nice! What are you planning to do today?",
        "I'm glad you're doing well."
    ]),
    (["bad", "not good", "tired", "sad", "angry", "upset"], [
        "Ah that sucks. Want to talk about it?",
        "Hope things get better soon.",
        "I'm here if you want to talk about it."
    ]),
    (["school", "exam", "teacher", "class", "homework"], [
        "School can be stressful sometimes.",
        "Do you like your classes?",
        "Are you preparing for any exams?"
    ]),
    (["gaming", "play", "video game"], [
        "Nice! What games do you play?",
        "That sounds fun! How often do you play?",
        "Do you usually play alone or with friends?"
    ]),
    (["weather", "rain", "sun", "cold", "hot", "temperature"], [
        "The weather can really affect your mood. How is it where you are?",
        "Do you like this kind of weather?",
        "I prefer sunny days, what about you?"
    ]),
    (["music", "song", "artist", "listen", "playlist"], [
        "What kind of music do you like?",
        "Music can say a lot about a person.",
        "Do you have a favorite artist?"
    ]),
    (["food", "eat", "hungry", "meal", "dinner", "lunch"], [
        "What's your favorite food?",
        "Are you hungry right now?",
        "Food is always a great topic, what do you like to eat?"
    ]),
    (["how are you", "how's it going", "how do you do"], [
        "I'm just a robot, but I'm doing great! How about you?",
        "All good here! How are you feeling today?",
        "I'm functioning perfectly! How about yourself?"
    ]),
    (["hobby", "hobbies", "activity", "what do you do", "fun"], [
        "Do you have any hobbies?",
        "What do you like to do in your free time?",
        "I love hearing about new hobbies, what's yours?"
    ]),
    (["sports", "football", "basketball", "tennis"], [
        "Do you play any sports?",
        "Which sport do you like the most?",
        "Sports can be exciting! Do you watch or play them?"
    ]),
    (["movie", "film", "tv show", "series", "netflix"], [
        "Have you watched any good movies lately?",
        "What's your favorite movie or show?",
        "I'd love to know what kind of movies you like."
    ]),
    (["travel", "trip", "vacation", "holiday", "tour"], [
        "Do you like traveling?",
        "Where was the last place you visited?",
        "I'd love to hear about your favorite destinations."
    ]),
    (["tech", "technology", "computer", "phone", "gadgets"], [
        "Are you into technology?",
        "What kind of gadgets do you use the most?",
        "Tech is amazing these days! Do you follow the latest trends?"
    ]),
    (["book", "reading", "novel", "story", "author"], [
        "Do you enjoy reading?",
        "What's your favorite book or author?",
        "Books can be such an adventure! Do you have a favorite genre?"
    ]),
    (["sad", "angry", "tired", "bored", "lazy"], [
        "How long have you been feeling like this?",
        "Want to talk more about it?",
        "I'm here to listen if you want to share more."
    ]),
    (["morning", "afternoon", "evening", "night", "routine", "bed"], [
        "Do you have a daily routine?",
        "What do you usually do in the mornings?",
        "Evenings are perfect to relax. How do you spend yours?"
    ])
]

fallback_responses = [
    "I'm not sure I understand. Can you explain that differently?",
    "That's interesting. Tell me more about it.",
    "Could you rephrase that?",
    "I didn't quite get that, but I'd like to understand."
]

# --- Variabler för namn och ålder ---
name = None
age = None

print("Chatbot: Hey there! Type 'bye' to exit.")

# --- Huvudloop ---
while True:
    user_input = input("You: ").lower()

    if "bye" in user_input:
        print("Chatbot: It was nice talking to you!")
        break

    matched = False

    # --- Kontrollera intents först ---
    for intent, data in intents.items():
        if any(keyword in user_input for keyword in data["keywords"]):
            print("Chatbot:", random.choice(data["responses"]))

            if intent == "time":
                get_time()
            elif intent == "date":
                get_date()
            elif intent == "time_date":
                get_time_and_date()
            elif intent == "day":
                get_day()
            elif intent == "spotify":
                open_spotify()

            matched = True
            break

    # --- Kontrollera rules om inget intent matchar ---
    if not matched:
        for keywords, responses in rules:
            if any(word in user_input for word in keywords):
                print("Chatbot:", random.choice(responses))
                matched = True
                break

    # --- Fråga namn och ålder om inget matchar och de inte är satta ---
    if not matched:
        if name is None:
            name = input("Chatbot: That sounds intresting, Ohh btw what's your name? ")
            print(f"Chatbot: Nice to meet you, {name}!")
        elif age is None:
            age = input(f"Chatbot: I forgot how old you are, {name}? ")
            print(f"Chatbot: Cool! {age} is a great and mature age.")
        else:
            # Fallback om inget matchar och namn/ålder redan satta
            print("Chatbot:", random.choice(fallback_responses))
