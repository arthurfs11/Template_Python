from functools import wraps
import os

os.environ["MODE"]           = "DEV"
os.environ["USE_SELENOID"]   = "Y"

from app import *

main()
