class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(word)
        self.guessedChars = set()

    def guess(self, character):
        self.guessedChars |= {character}
        if character not in self.secretWord:
            return False
        else:
            current_status = ''
            for c in self.secretWord:
                if c in self.guessedChars:
                    current_status += c
                else:
                    current_status += '_'

            self.currentStatus = current_status
            return True

    def finished(self):
        return self.currentStatus == self.secretWord

    def displayCurrent(self):
        guess_word = ''
        for c in self.currentStatus:
            guess_word += (c + ' ')
        return guess_word

    def displayGuessed(self):
        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed
