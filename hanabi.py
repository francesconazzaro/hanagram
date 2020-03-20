from collections import namedtuple
from sys import getsizeof

        
colors = ['white', 'red', 'blue', 'green', 'yellow']

deck = [];        
for color in colors:
    for i in range(1, 6):
        count = 2
        if i == 1: count = 3
        if i == 5: count = 1
        for _ in range(count):
            deck.append(namedtuple('Card', 'color value')(color, i))

def main():
    for card in deck:
        print(str(card.value) + " " + card.color)

if __name__ == '__main__':
    main()