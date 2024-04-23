# utils/helper.py

def binary_choice(question, a, b) -> bool:
        while True:
            answer = input(f"{question}").strip().lower()

            if answer == a:
                return True
            elif answer == b:
                return False
            else:
                print(f"Please enter either '{a}' or '{b}'.")