# Can you translate this driver code to unit tests?

from char_count import char_count

print(char_count("aaabbc") == [
  ["a", 3],
  ["b", 2],
  ["c", 1]
])

print(char_count("an apple a day will keep the doctor away") == [
  ["a", 6],
  ["e", 4],
  ["l", 3],
  ["p", 3],
  ["d", 2],
  ["o", 2],
  ["t", 2],
  ["w", 2],
  ["y", 2],
  ["c", 1],
  ["h", 1],
  ["i", 1],
  ["k", 1],
  ["n", 1],
  ["r", 1]
])
