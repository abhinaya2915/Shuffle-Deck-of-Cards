import random, itertools

# Generate all deck of cards (52 cards) 
deck = list(itertools.product(range(1,14), ["heart", "spade", "club", "diamond"]))

# shuffle deck of cards 
random.shuffle(deck)

# print first 5 randomly shuffled cards

for i in range(5):
    print(f"{deck[i][0]} of {deck[i][1]}")
