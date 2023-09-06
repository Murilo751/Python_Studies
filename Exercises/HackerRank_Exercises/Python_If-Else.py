import math
import os
import random
import re
import sys

n = int(input().strip())

if n % 2 == 1 or 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 or 5 <= n <= 5 or n > 20:
    print("Not Weird")
