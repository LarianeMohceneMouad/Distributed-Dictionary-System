import Pyro4


# Run : python -m Pyro4.naming To start a name server
# Run : python -m Pyro4.nsc list To see what all known registered objects in the naming server are

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")  # mark the following items to be available for remote access
class Dictionary(object):
    def __init__(self):
        self.contents = {
            'quadrilateral': "a polygonal shape with four sides",
            'rectangle': 'a right-angled quadrilateral',
            'shape': "a geometric object in a plane",
            'square': "a rectangle having equal sides"
        }

    def words_list(self):
        return self.contents

    def get_meaning(self, word):
        if word in self.contents.keys():
            return self.contents[str(word)]

    def add_word(self, word, meaning):
        if word in self.contents.keys():
            return 'Error'
        else:
            self.contents[str(word)] = meaning

    def del_word(self, word):
        if word in self.contents.keys():
            self.contents.pop(str(word))
        else:
            return 'Error'

    def words_size(self):
        return len(self.contents.keys())


def main():
    Pyro4.Daemon.serveSimple(  # to publish a dict of objects/classes and start Pyro’s request loop
        {
            Dictionary: "example.warehouse"  # register the dictionary class (and its methods) as a Pyro object
        },
        ns=True)  # ns : naming server for the pyro's objects


if __name__ == "__main__":
    main()
