class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def display_data(self):
        print(f"text={self.text},answer={self.answer}")