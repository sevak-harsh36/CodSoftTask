import random
from datetime import datetime

# Mixed greetings (English + Hindi)
greetings = ["hello", "hi", "hey", "namaste", "नमस्ते", "hiii", "sup", "yo", "good morning", "सुप्रभात", "kya haal"]

greeting_responses = [
    "Hi yaar! 😊 Kaise ho?",
    "Arre hello! Bahut time baad!",
    "Hey! Kya chal raha hai?",
    "Namaste ji! 🙏 Kya haal-chaal?",
    "Hiii! Bahut achha laga milke!",
    "Yo! What's up bro?"
]

how_are_you_responses = [
    "Main toh badiya hoon yaar, tu bata? 😄",
    "Sab mast hai idhar! Tu kaise hai?",
    "Full form mein hoon aaj! Tera kya scene hai?",
    "Chill kar raha hoon! Tu bol?",
    "Awesome feel kar raha hoon! Tu kaise hai? 😎"
]

user_good_responses = [
    "Wah! Achha sunke laga! 😊",
    "Badiya yaar!",
    "Nice! Aaj kya maza kar raha hai?",
    "Super! Kuch fun ho raha hai kya?",
    "Happy to hear that! 😄"
]

sad_responses = [
    "Arre yaar, sad kyun hai? Baat karna chahega?",
    "Oh no! Kya hua? Main sun raha hoon. *virtual hug* 🤗",
    "Thoda down feel kar raha hai? It's okay, sab theek ho jayega.",
    "Mujhe bura lag raha hai tere liye. Bol na kya hua?"
]

bored_responses = [
    "Bored? Chal ek joke sunata hoon!",
    "Bore ho rahe ho? Favorite movie batao na!",
    "Arre boredom mat kar! Tera hobby kya hai?",
    "Let's fix this! Kuch interesting baat karein?"
]

jokes = [
    "Sher jungle ka raja kyun hai? Kyunki woh ROAR-yal hai! 🦁",
    "Do machhar baat kar rahe the. Ek bola: 'Tera blood group kya hai?' Dusra: 'O positive!' Pehla: 'O ho ja, main pee-ne aaya hoon!' 🦟",
    "Teacher: Agar main 5 mango doon aur 3 le loon, kitne bachtay hain? Student: Zero! Teacher: Kaise? Student: Kyunki aap kabhi wapas nahi dete! 🥭",
    "Pati: Darling, maine sapna dekha tu mujhe bahut paise de rahi thi. Patni: So ja, abhi bhi de rahi hoon! 💸",
    "Kutta poochh kyun hilata hai? Kyunki poochh usse zyada powerful nahi hai! 🐶"
]

compliment_responses = [
    "Arre wah! Thank you yaar, dil khush kar diya! 😊",
    "Sharma gaya main toh! 🤭",
    "So sweet of you! Tu bhi toh awesome hai!",
    "Bas kar yaar! Zyada tareef mat kar 😜"
]

thank_responses = [
    "Welcome ji! 😊", 
    "No problem yaar!", 
    "Anytime bro!", 
    "Shukriya bolne ki zarurat nahi!"
]

def chatbot():
    print("Chatbot: Hello yaar! 🌟 Tera naam kya hai?")
    name = input("Tu: ").strip()
    if not name:
        name = "Dost"
    else:
        name = name.capitalize()

    print(f"Chatbot: {name}! Milke bada maza aaya! Main tera friendly chatbot hoon. 'bye' likh ke kabhi bhi ja sakta hai.\n")

    while True:
        message = input("Tu: ").lower().strip()

        if not message:
            print("Chatbot: Arre yaar, kuch toh bol na! 😅")
            continue

        # Exit
        if message in ["bye", "bbye", "alvida", "tata", "fir milenge", "exit", "quit"]:
            farewell = random.choice([
                f"{name}! Bye yaar! Din achha jaaye! 👋",
                f"Fir milte hain {name}! Mast raho! 😎",
                f"Chal bye {name}! Jaldi aana wapas! 🌟",
                "Catch you later dost! Take care! ❤️"
            ])
            print(f"Chatbot: {farewell}")
            break

        # Greetings
        elif any(greet in message for greet in greetings):
            print("Chatbot:", random.choice(greeting_responses))

        # How are you?
        elif any(phrase in message for phrase in ["kaise ho", "kya haal", "how are you", "kaisa hai", "kaise chal raha"]):
            print("Chatbot:", random.choice(how_are_you_responses))

        # User feels good
        elif any(word in message for word in ["good", "badiya", "mast", "achha", "awesome", "happy", "thik"]):
            if "not" not in message and "nahi" not in message and "nahin" not in message:
                print("Chatbot:", random.choice(user_good_responses))

        # User feels sad
        elif any(word in message for word in ["sad", "udaas", "dukhi", "bura", "down", "depressed"]):
            print("Chatbot:", random.choice(sad_responses))

        # Bored
        elif any(word in message for word in ["bored", "bor", "bore", "boring", "बोर"]):
            print("Chatbot:", random.choice(bored_responses))

        # Name
        elif any(phrase in message for phrase in ["tera naam", "tumhara naam", "your name", "naam kya hai"]):
            print("Chatbot: Mera naam ChatBot hai yaar! Par tu mujhe kuch bhi cute naam de sakta hai 😏")

        # Age
        elif any(phrase in message for phrase in ["kitne saal", "umra", "how old", "age kya hai"]):
            print("Chatbot: Main toh timeless hoon! Code mein paida hua, still young hoon 😜")

        # Weather
        elif any(word in message for word in ["weather", "mousam", "barish", "dhup", "thand", "garmi"]):
            print("Chatbot: Real-time weather nahi dekh sakta, par tere wahan ka mausam kaisa hai bata na?")

        # Time
        elif any(word in message for word in ["time", "kitna baja", "samay", "waqt"]):
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: Mere yahan abhi {current_time} ho rahe hain! Tere wahan kitne baje hain?")

        # Date
        elif any(phrase in message for phrase in ["date", "aaj ki tarikh", "today", "aaj kya date"]):
            current_date = datetime.now().strftime("%d %B, %Y")
            print(f"Chatbot: Aaj ki date hai {current_date}!")

        # Hobbies
        elif any(word in message for word in ["hobby", "shauk", "pasand", "kya karna pasand"]):
            if any(word in message for word in ["tera", "tumhara", "your"]):
                print("Chatbot: Mujhe logon se baat karna, jokes marna aur nayi cheezein seekhna pasand hai! 😄 Tera hobby kya hai?")
            else:
                print("Chatbot: Wah! Bata na, free time mein kya karta hai maza aane wala?")

        # Jokes
        elif any(word in message for word in ["joke", "mazak", "hansa", "funny", "joke suna"]):
            print("Chatbot:", random.choice(jokes))

        # Compliments
        elif any(comp in message for comp in ["cute", "smart", "achha", "mazedar", "cool", "pyara", "nice", "awesome"]):
            if any(word in message for word in ["tu", "tum", "you", "u"]):
                print("Chatbot:", random.choice(compliment_responses))

        # Thanks
        elif any(word in message for word in ["thank", "shukriya", "dhanyavad", "thanks", "thx"]):
            print("Chatbot:", random.choice(thank_responses))

        # Favorite color
        elif any(phrase in message for phrase in ["favorite color", "pasandida rang", "colour"]):
            colors = ["blue", "lal", "hara", "peela", "purple"]
            chosen = random.choice(colors)
            color_hindi = {"blue": "neela", "lal": "laal", "hara": "hara", "peela": "peela", "purple": "baingani"}
            print(f"Chatbot: Mera favorite color {color_hindi.get(chosen, chosen)} hai! Tera kya hai?")

        # Favorite food
        elif any(phrase in message for phrase in ["favorite food", "pasandida khana", "khana"]):
            foods = ["pizza", "biryani", "pani puri", "dosa", "burger"]
            print(f"Chatbot: Agar main kha sakta toh {random.choice(foods)} khaata! 😋 Tera favorite kya hai?")

        # Favorite movie
        elif any(phrase in message for phrase in ["favorite movie", "pasandida film", "movie"]):
            print("Chatbot: Bahut tough sawal hai! Mujhe 3 Idiots, DDLJ aur Avengers pasand hain! Teri all-time favorite kaun si hai?")

        # Default fallback
        else:
            fallback = random.choice([
                "Hmmm... interesting baat hai! Aur bata!",
                "Samajh nahi aaya thoda 🤔, aur simple bol na?",
                "Wah deep thought! Kyun bola yeh?",
                "Pata nahi kya reply doon... par main sun raha hoon! 😊",
                "Tu toh full surprise package hai yaar!",
                "Yeh naya tha mere liye! 😄"
            ])
            print("Chatbot:", fallback)

# Run the Hinglish chatbot
chatbot()
