import sys
import Pyro4.util
from person import Person

sys.excepthook = Pyro4.util.excepthook

dictionary = Pyro4.Proxy("PYRONAME:example.warehouse")
name = input(" Enter name : ")
client_2 = Person(name)
client_2.visit(dictionary)
