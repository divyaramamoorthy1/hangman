def enter_word():
    word = raw_input("Welcome to Hangman! Enter the word you want your friend to guess, and then hand your computer over to them: ")
    global word_list
    word_list = list(word)
    print(word_list)

def make_hidden():
    global hidden_list
    hidden_list = []
    for x in range(len(word_list)):
        hidden_list.append('_')
    print(hidden_list)

if __name__ == "__main__":
    enter_word()
    make_hidden()
