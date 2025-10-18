import random

class SimpleChatbot:
    def __init__(self):
        self.greetings = ["hi", "hello", "hey", "howdy", "greetings", "what's up", "hiya", "sup", "Salam Alikoumu"]
        self.farewells = ["bye", "goodbye", "see you", "later", "farewell", "catch you later", "take care"]
        self.questions = {
            "how are you": ["I'm just a program, but thanks for asking!", "Doing well, how about you?", "I don't have feelings, but I'm here to help!"],
            "ok": ["Okay!"],
            "what is your name": ["I'm a simple chatbot created to converse.", "You can call me Chatbot!", "Just your friendly neighborhood chatbot."],
            "what can you do": ["I can chat with you and answer simple questions.", "I can provide information based on what you ask!", "I can help you with various topics."],
            "tell me a joke": ["Why did the scarecrow win an award? Because he was outstanding in his field!", "I told my computer I needed a break, and it froze!", "What do you call a bear with no teeth? A gummy bear!"],
            "/help": ["Command List: /help /version /tictactoe"],
            "/version": ["SimpleBot V2"],
            # Other questions omitted for brevity
        }
        self.default_responses = [
            "I'm not sure how to respond to that.", 
            "Could you please rephrase?", 
            "That's interesting! Tell me more.",
            "I didn't quite catch that. Can you say it differently?",
            "Hmm, I need to learn more about that topic!",
            "I'm here to listen! Go on.",
            "That's a fascinating thought.",
            "I wish I knew more about that!"
        ]

    def get_user_input(self):
        user_input = input("User: ").strip().lower()
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
        
        # Check for tic-tac-toe command
        if "/tictactoe" in user_input:
            self.play_tictactoe()
            return "Chatbot: Tic-Tac-Toe game has ended!"

        # Default response if no keywords match
        return f"Chatbot: {self.random_response(self.default_responses)}"

    def random_response(self, responses):
        return random.choice(responses)

    def play_tictactoe(self):
        squares = [' '] * 9
        players = 'XO'
        board_template = '''
          0 | 1 | 2
         ---|---|---
          3 | 4 | 5
         ---|---|---
          6 | 7 | 8
        '''
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
            (0, 4, 8), (2, 4, 6)             # diagonals
        ]

        def check_win(player):
            for a, b, c in win_conditions:
                if {squares[a], squares[b], squares[c]} == {player}:
                    return True
            return False

        while True:
            print(board_template.format(*squares))
            if check_win(players[1]):
                print(f'{players[1]} is the winner!')
                break
            if ' ' not in squares:
                print("It's a tie!")
                break
            try:
                square = int(input(f'{players[0]} choose your square [0-8] > '))
                if not 0 <= square <= 8 or squares[square] != ' ':
                    print('Invalid move!')
                    continue
            except ValueError:
                print('Invalid input! Enter a number between 0-8.')
                continue
            squares[square] = players[0]
            players = players[::-1]

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