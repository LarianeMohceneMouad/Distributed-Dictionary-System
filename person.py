class Person(object):
    def __init__(self, name):
        self.name = name

    def help(self):
        print("Commands : all | word | del-word | size | add-word | exit")

    def visit(self, dictionary, cmd='cmd'):
        print(f" This is client {self.name} ")
        print("Type 'help' to view Commands list | Type 'exit' to exit")
        command = cmd
        while bool(command):
            command = input("Type Command : ").strip()
            if command == "help":
                self.help()
            elif command == "all":
                self.all_words(dictionary)
            elif command == "word":
                self.word(dictionary)
            elif command == "del-word":
                self.delete(dictionary)
            elif command == "add-word":
                self.add(dictionary)
            elif command == "size":
                self.size(dictionary)
            elif command == "exit":
                break
        print("Thank you, come again!")

    def add(self, dictionary):
        word = input("Enter word to add to the Dictionary : ").strip()
        meaning = input("Type the word's meaning : ").strip()
        if word:
            error = dictionary.add_word(word, meaning)
            if error:
                print("word already exists in the Dictionary")

    def delete(self, dictionary):
        word = input("Enter word to delete from the Dictionary : ").strip()
        if word:
            error = dictionary.del_word(word)
            if error:
                print(" Can not delete word : word does not exist in the Dictionary")

    def word(self, dictionary):
        word = input("Enter word to get its meaning : ").strip()
        if word:
            meaning = dictionary.get_meaning(word)
            if meaning:
                print(f' {word} : {meaning}')
            else:
                print(" Can not get word's meaning  : word does not exist in the Dictionary")

    def all_words(self, dictionary):
        print("All words : ")
        words_list = dictionary.words_list()
        for k in words_list:
            print(f" {k} : {words_list[k]}")

    def size(self, dictionary):
        dict_size = dictionary.words_size()
        print(f'Dictionary size is {dict_size}')
