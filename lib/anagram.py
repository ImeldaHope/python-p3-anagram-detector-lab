# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word 

    @word.setter
    def word(self, word):
        self._word = word
    
    def match(self, match_list):
        matched_word = []

        for word in match_list:
            if sorted(self.word) == sorted(word):
                matched_word.append(word)          
                
        return matched_word
  
