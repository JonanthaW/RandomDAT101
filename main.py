import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from scripts import randomValue as main_from_module_one

if __name__ == '__main__':
    main_from_module_one()
