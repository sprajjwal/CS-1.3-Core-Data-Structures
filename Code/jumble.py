from collections import OrderedDict
from search import binary_search

with open('/usr/share/dict/words') as f:
    words = f.read().splitlines()
    words = sorted([word.upper() for word in words])

def permutations(string, a, step = 0):
  """ inspired from an answer on stack overflow: https://stackoverflow.com/a/20955291"""
  # if we've gotten to the end, add to set
  if step == len(string):
    a.add("".join(string))

  # everything to the right of step has not been swapped yet
  for i in range(step, len(string)):
    # copy the string (store as array)
    string_copy = [character for character in string]

    # swap the current index with the step
    string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

    # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
    permutations(string_copy, a, step + 1)

def unscramble(word, numWords=[1]):
  """ takes the word list and an scrambled word and gets all possible unscrambled words"""
  a = set()
  permutations(word,a, 0)
  a = set(item.upper() for item in a )
  unscrambled = list()
  if numWords == [1]:
    for item in a:
      if binary_search(words, item) is not None:
        unscrambled.append(item)
  else:
    all_perms = set()
    permutations(word, all_perms)

  return unscrambled

def jumble(scrams, pick, word_counts):
  
  unscrambled = []
  for scram in scrams:
    unscram = unscramble( scram)
    unscrambled.append(unscram)
  
  print(unscrambled)
  final = []

  for i in range(len(pick)):
    new = []
    for items in unscrambled[i]:
      tba = ""
      for index in pick[i]:
        tba += items[index]
      if len(final) == 0:
        new.append(tba)
      else:
        for final_items in final:
          new.append(final_items + tba)
    final = new
      
      
  print(final)
  # print(unscramble(words, final, word_counts))

if __name__ == "__main__":
  scrams = ['LAISA', 'LAURR', 'BUREEK', 'PROUOT']
  pick = [[1, 2, 3], [0, 2], [0, 1], [2, 4, 5]]
  final = [5, 5]
  jumble(scrams, pick, final)

  