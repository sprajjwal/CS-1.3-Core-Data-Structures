from collections import OrderedDict
from search import binary_search

with open('/usr/share/dict/words') as f:
    words = f.read().splitlines()
    words = sorted([word.upper() for word in words])

def permutations(string, mySet, step = 0):
  """ inspired from an answer on stack overflow: https://stackoverflow.com/a/20955291"""
  # if we've gotten to the end, add to set
  if step == len(string):
    mySet.add("".join(string))

  # everything to the right of step has not been swapped yet
  for i in range(step, len(string)):
    # copy the string (store as array)
    string_copy = [character for character in string]

    # swap the current index with the step
    string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

    # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
    permutations(string_copy, mySet, step + 1)

def unscramble(word, numWords=[1]):
  """ takes the word list and an scrambled word and gets all possible unscrambled words"""
  perms = set()
  unscrambled = set()
  if numWords == [1]:
    permutations(word, perms)
    perms = set(item.upper() for item in perms )
    for item in perms:
      if binary_search(words, item) is not None:
        unscrambled.add(item)
    
  else:
    for item in word:
      permutations(item, perms)
    for item in perms:
      i = 0
      for num in numWords:
        if binary_search(words, item[i:i+num]) is None:
          break
        i += num
      else:
        to_add = set()
        i=0
        for num in numWords:
          to_add.add(item[i:i+num])
          i += num
        for items in unscrambled:
          if to_add == items:
            break
        else:
          unscrambled.add(frozenset(to_add))
  return unscrambled

def jumble(scrams, pick, word_counts):
  
  unscrambled = []
  for scram in scrams:
    unscram = unscramble( scram)
    unscrambled.append(unscram)
  
  print("Unscrambling done: ")
  for i in range(len(scrams)):
    print(f"{scrams[i]}: {unscrambled[i]}")

  print("-------------------------------------------------------")
  final_scramble = []

  for i in range(len(pick)):
    new = []
    for items in unscrambled[i]:
      tba = ""
      for index in pick[i]:
        tba += items[index]
      if len(final_scramble) == 0:
        new.append(tba)
      else:
        for final_scramble_items in final_scramble:
          new.append(final_scramble_items + tba)
    final_scramble = new
      
  print("Possible Scramble words are: ", end="")
  print(final_scramble)
  print("-------------------------------------------------------")
  return unscramble(final_scramble, word_counts)

if __name__ == "__main__":
  scrams = ['AULFW', 'KIDNR', 'SEWBOT', 'XEOPES']
  pick = [[0, 1], [0, 4], [2, 3, 4], [4, 5]]
  word_counts = [3, 6]
  options = jumble(scrams, pick, word_counts)
  if len(options) == 0: 
    print("No solutions from ENGLISH Dictionary were found")
  else: 
    for item in options:
      print("solution found: ", end="")
      for word in item:
        print(word, end=" ")
      print()

  