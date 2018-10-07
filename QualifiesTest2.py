# used to test part of the qualifies function, the marked line
# together with specific test cases that might happen
import requests
import math
import string
from bs4 import BeautifulSoup
red_flags = ["year", "lease", "male", "guy", "basement", "permanent","long-term"]

def qualifies(text):
  ##########################
  wordList=[word.strip(string.punctuation) for word in text.split()]
  ##########################
  print(wordList)
  for word in red_flags:
    if word in wordList:
      print(word)
      return False
  return True

w="femalessfsd" #true
s=" male "      #false
e=" male."      #false
t=" males."     #true
l="male"        #false
f=" male;"       #false
o="looking for a long-term roommate"      #true
print(qualifies(o))

#Minimum 4 month lease; qualified: because of ;

# solved:
# punctuation
# lease; return not qualified

# problem to solve:
# eg: males will reuturn qualifies
# fu shu (s)