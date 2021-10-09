import string 
 
class Alphabet: 
    def __init__(self, lang, letters): 
        self.lang = lang 
        self.letters = letters 
 
    def show(self): 
        print(self.letters) 
 
    @property 
    def words_num(self): 
        return len(self.letters)
 
class EngAlphabet(Alphabet): 
    __letters_num = 26 
 
    def __init__(self): 
        super().__init__('En', list(string.ascii_uppercase)) 
 
    def is_en_word(self, let): 
         return let in self.letters
 
    @property 
    def letters_num(self): 
        return EngAlphabet.__letters_num
 
    @staticmethod 
    def sentence(): 
         return 'Bobi was a good boy!'
 
def main():
    word = EngAlphabet() 
    word.show() 
    word.words_num 
    word.is_en_word("G") 
    word.is_en_word("П") 
    print("English Example:") 
    EngAlphabet.sentence()

 
if __name__ == "__main__":
    main() 
