import os, sys, random
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from data.humano.values import nomes

class generateName:
    def generateName():
        print(nomes.nomes[random.randint(0, len(nomes.nomes) - 1)])

if __name__ == '__main__':
  generateName.generateName()
