import string 
 
class Alphabet: 
    def __init__(self, lang, letters): 
        self.lang = lang 
        self.letters = letters 
 
    def print(self): 
        print(self.letters) 
 
    @property 
    def letters_num(self): 
        print(len(self.letters)) 
 
class EngAlphabet(Alphabet): 
    __letters_num = 26 
 
    def __init__(self): 
        super().__init__('En', list(string.ascii_uppercase)) 
 
    def is_en_letter(self, let): 
         print(let in self.letters) 
 
    @property 
    def letters_num(self): 
        print(EngAlphabet.__letters_num)
 
    @staticmethod 
    def example(): 
         print('Bobi was a good boy!')
 
def main(): 
    eng = EngAlphabet() 
    eng.print() 
    print(eng.letters_num) 
    eng.is_en_letter("F") 
    eng.is_en_letter("Щ") 
    print("English Example:") 
    EngAlphabet.example()

 
if __name__ == "__main__": 
    main()
