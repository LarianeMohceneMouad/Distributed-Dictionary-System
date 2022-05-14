# Distant-Dictionnary-System using Pyro4 library

Distant server that acts as a dictionnary server offering requested words meaning (which what a dictionnary do) to clients
using Pyro library  (Python remote object) 

## First 
Start the Pyro's naming server using this cmd command line : python -m Pyro4.naming

You can see active Pyro's objects using this cmd command line : python -m Pyro4.nsc list

## Second
After starting the naming server 

Run Dictionnary.py

Then 

Run both clients

### PS: We're using Pyro4, but still Pyro5 is available and has way more features I suggest to used this code to understand how it works but use Pyro5 in your code.
