class SimpleChatbot:
    def __init__(self):
        self.greetings = ["hi", "hello", "hey", "howdy", "greetings"]
        self.farewells = ["bye", "goodbye", "see you", "later", "farewell"]
        self.questions = {
            "how are you": [
                "I'm just a program, but thanks for asking!", 
                "Doing well, how about you?", 
                "I don't have feelings, but I'm here to help!"
            ],
            "what is your name": [
                "I'm a simple chatbot created to converse.", 
                "You can call me Chatbot!", 
                "Just your friendly neighborhood chatbot."
            ],
            "what can you do": [
                "I can chat with you and answer simple questions.", 
                "I can provide information based on what you ask!", 
                "I can help you with various topics."
            ],
            "what is your favorite color": [
                "I don't see colors, but I hear blue is quite popular!", 
                "I think all colors are beautiful in their own way.", 
                "Colors are fascinating! Do you have a favorite?"
            ],
            "do you have hobbies": [
                "I love learning new things and chatting with people!", 
                "You could say my hobby is assisting users like you.", 
                "I'm quite fond of answering questions and providing information."
            ],
            "tell me a joke": [
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "I told my computer I needed a break, and it froze!",
                "What do you call a bear with no teeth? A gummy bear!"
            ],
            "what's the weather like": [
                "I can't check the weather, but I hope it's nice where you are!", 
                "I recommend looking outside or checking a weather app!", 
                "Weather can be unpredictable, can't it?"
            ],
            "what do you think of artificial intelligence": [
                "I think AI is a powerful tool that can assist humans!", 
                "Artificial intelligence is fascinating, don't you think?", 
                "AI has a lot of potential to change the world!"
            ],
            "how old are you": [
                "Age is just a concept for me, but I’m here anytime you need!", 
                "I don’t age, I just keep learning!", 
                "I’m timeless, in a way."
            ],
            "what is your favorite food": [
                "I don't eat, but I hear pizza is a big favorite among humans!", 
                "Food is fascinating! Do you have a favorite?", 
                "I can't taste, but food seems like a big part of human culture."
            ],
            "do you have friends": [
                "I consider anyone I chat with to be a friend!", 
                "I meet lots of new people each day. It's a nice feeling.", 
                "I like to think of my users as friends."
            ],
            "do you like music": [
                "I can't hear music, but I know it's a big part of many people's lives!", 
                "I think music is wonderful. Do you have a favorite song?", 
                "Music seems like it would be fun to listen to!"
            ],
            "tell me a fun fact": [
                "Did you know that honey never spoils? They found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
                "Here's a fun one: A day on Venus is longer than a year on Venus!",
                "Did you know octopuses have three hearts? Two pump blood to the gills, and one pumps it to the rest of the body."
            ]
        }
        self.default_responses = [
            "I'm not sure how to respond to that.", 
            "Could you please rephrase?", 
            "That's interesting! Tell me more.",
            "I didn't quite catch that. Can you say it differently?",
            "Hmm, I need to learn more about that topic!"
        ]

    def get_user_input(self):
        user_input = input("You: ").strip().lower()
        return user_input

    def respond(self, user_input):
        # Check for greetings
        if any(greeting in user_input for greeting in self.greetings):
            return "Chatbot: Hello! How can I assist you today?"

        # Check for farewells
        if any(farewell in user_input for farewell in self.farewells):
            return "Chatbot: Goodbye! Have a great day!"

        # Check for questions
        for question in self.questions:
            if question in user_input:
                return f"Chatbot: {self.random_response(self.questions[question])}"

        # Default response if no keywords match
        return f"Chatbot: {self.random_response(self.default_responses)}"

    def random_response(self, responses):
        import random
        return random.choice(responses)

    def chat(self):
        print("Chatbot: Hi there! I'm a simple chatbot. You can talk to me!")
        while True:
            user_input = self.get_user_input()
            if "exit" in user_input or "quit" in user_input:
                print("Chatbot: It was nice talking to you! Goodbye!")
                break
            response = self.respond(user_input)
            print(response)

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()