import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def magic(magic_question, magic_responses):
    magic_number = random.randint(0, len(magic_responses) - 1)
    print(f"{magic_question}\n.............\n{magic_responses[magic_number]}")

def main():
    magic_responses = [
        'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely',
        'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
        'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later',
        'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
        'Don\'t count on it', 'My reply is no', 'My sources say no',
        'Outlook not so good', 'Very doubtful'
    ]

    while True:
        clear()
        magic_question = input("The magic 8-ball answers any yes/no question you throw at it.\n\nWhat will you ask the 8-ball?\n(Type 'exit' to quit)\n\n")
        
        if magic_question.lower() == 'exit':
            clear()
            print("Goodbye! May the odds be in your favor.")
            break

        if not magic_question.strip():
            clear()
            print("You didn't ask a question. Please try again.")
            continue

        clear()
        magic(magic_question, magic_responses)
        
        input("\nPress Enter to ask another question or type 'exit' to quit.")

if __name__ == "__main__":
    main()
