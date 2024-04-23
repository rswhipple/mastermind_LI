# utils/code.py
import requests

class Code:
    def __init__(self, level) -> None:
        self.num = 4
        self.min = 0
        self.max = 6 + level
        self.vars = self.max - self.min + 1
        self.base_url = "https://www.random.org/integers/"
        self.code = []
        self.generate_code()
        
    def generate_code(self):
        params = {
            'num': self.num,
            'min': self.min,
            'max': self.max,
            'col': 1,
            'base': 10,
            'format': 'plain',
            'rnd': 'new'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status() 
        except requests.RequestException as e:
            print(f"Failed to generate code: {e}")
            return None
        
        code_string = response.text.replace('\n', '')
        random_ints = [int(char) for char in code_string]
        self.code = random_ints

# In Progress
class RandomLetterCode(Code):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "https://www.random.org/strings/"

    # TODO: change to letters
    # def generate_code(self):
    #     params = {
    #         'num': self.num,
    #         'min': self.min,
    #         'max': self.max,
    #         'col': 1,
    #         'base': 10,
    #         'format': 'plain',
    #         'rnd': 'new'
    #     }

    #     try:
    #         response = requests.get(self.base_url, params=params)
    #         response.raise_for_status()  # Raises an HTTPError for bad responses
    #     except requests.RequestException as e:
    #         print(f"Failed to generate code: {e}")
    #         return None
        
    #     code_string = response.text.replace('\n', '')
    #     random_ints = [int(char) for char in code_string]
    #     self.code = random_ints

        