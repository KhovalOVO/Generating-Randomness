import random


class Predictor:
    def __init__(self):
        self.start_balance = 1000
        self.string = ''
        self.test_string = ''
        self.min_length = 100
        self.freq = {bin(i)[2:].zfill(3): [0, 0] for i in range(8)}

    @staticmethod
    def remove_odd(s):
        return_string = ''
        for char in s:
            if char in ('0', '1'):
                return_string += char

        return return_string

    def get_string(self):
        my_str = input()

        return self.remove_odd(my_str)

    def get_len(self):
        length = len(self.string)

        return f'The current data length is {length}, {self.min_length - length} symbols left'

    def final_str(self):
        while len(self.string) < self.min_length:
            print('Print a random string containing 0 or 1:')
            self.string += self.get_string()
            if len(self.string) < self.min_length:
                print(self.get_len())
        else:
            print("Final data string:")
            print(self.string)
            self.counter()

    def counter(self):
        for i in range(len(self.string) - 3):
            self.freq[self.string[i:i+3]][int(self.string[i+3])] += 1

    def test_str(self):
        while True:
            print("Print a random string containing 0 or 1:")
            self.test_string = input()
            if self.test_string == "enough":
                return 'enough'
            self.test_string = self.remove_odd(self.test_string)
            if len(self.test_string) >= 4:
                self.predict()
                return self.compare()

    def predict(self):
        prediction = ''

        for i in range(len(self.test_string) - 3):
            if self.freq[self.test_string[i:i+3]][0] > self.freq[self.test_string[i:i+3]][1]:
                prediction += '0'
            elif self.freq[self.test_string[i:i+3]][0] < self.freq[self.test_string[i:i+3]][1]:
                prediction += '1'
            else:
                prediction += random.choice('01')

        return prediction

    def compare(self):
        right_guess = 0
        prediction = self.predict()
        print("predictions:")
        print(prediction)
        for i in range(3, len(self.test_string)):
            if self.test_string[i] == prediction[i - 3]:
                right_guess += 1

        accuracy = round(right_guess / (len(self.test_string) - 3) * 100, 2)
        print(f"Computer guessed {right_guess} out of {len(self.test_string) - 3} symbols right ({accuracy} %)")

        return right_guess

    def start_game(self):
        print("Please provide AI some data to learn...")
        print(self.get_len())

        self.final_str()

        print(f"You have ${self.start_balance}. Every time the system successfully predicts your next press, you lose $1. Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

        while True:
            rand_str = self.test_str()
            if rand_str == "enough":
                print('Game over!')
                break
            self.update_balance(rand_str, len(self.test_string) - 3)
            print(f"Your balance is now ${self.start_balance}")

    def update_balance(self, r_gs, length):
        self.start_balance -= r_gs - (length - r_gs)


if __name__ == "__main__":
    pred = Predictor()
    pred.start_game()
