import sys
import Pyro4.util
from person import Person

sys.excepthook = Pyro4.util.excepthook

dictionary = Pyro4.Proxy("PYRONAME:example.warehouse")  # get a Pyro proxy to the greeting object
name = input(" Enter name : ")
client_1 = Person(name)
client_1.visit(dictionary)
