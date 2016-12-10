import sys

with open('./enable1.txt', 'r') as content_file:
    english = [line.replace('\r\n', '') for line in content_file]

def longest(tiles):
  longest_word = ""
  for word in english:
    if scrabble(tiles, word):
      if len(word) > len(longest_word):
        longest_word = word
  return longest_word

def scrabble(tiles, word):
  tiles_len = len(tiles)
  for letter in list(word):
    old_length = len(tiles)
    tiles = tiles.replace(letter, '', 1)
    if len(tiles) == old_length:
      tiles = tiles.replace('?', '', 1)
  return len(tiles) + len(word) == tiles_len

print scrabble("ladilmy", "daily")
print scrabble("eerriin", "eerie")
print scrabble("orrpgma", "program")
print scrabble("orppgma", "program")
print
print scrabble("pizza??", "pizzazz")
print scrabble("piizza?", "pizzazz")
print scrabble("a??????", "program")
print scrabble("b??????", "program")
print
print longest("dcthoyueorza") == "coauthored"
print longest("uruqrnytrois") == "turquois"
print longest("rryqeiaegicgeo??") == "greengrocery"
print longest("udosjanyuiuebr??") == "subordinately"
print longest("vaakojeaietg????????") == "ovolactovegetarian"