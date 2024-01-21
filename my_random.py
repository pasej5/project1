#!/usr/bin/env python3

import random


deck = list(range(1, 53))
random.shuffle(deck)
hand = random.sample(deck, k=6)


print(hand)