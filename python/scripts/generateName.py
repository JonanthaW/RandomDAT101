import os, sys, random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.human.values import names

def generateName():
    print(names.names[random.randint(0, len(names.names) - 1)])
