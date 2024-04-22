# utils/code.py
import requests

class Code:
    def __init__(self, level) -> None:
        self.level = level
        self.num = 4
        self.min = 0
        self.max = 6 + level
        self.vars = self.max - self.min + 1
        self.code = []
        self.generate_code()
        
    def generate_code(self):
        u1 = "https://www.random.org/integers/?num="
        u2 = "&min="
        u3 = "&max="
        u4 = "&col=1&base=10&format=plain&rnd=new"
        
        # add try here
        response = requests.get(f"{u1}{self.num}{u2}{self.min}{u3}{self.max}{u4}")

        if response.status_code == 200:
            code_string = response.text.replace('\n', '')
            random_ints = [int(char) for char in code_string]

            # print(f"{random_ints}")
            self.code = random_ints
        else:
            print("Failed to generate code:", response.status_code)

        