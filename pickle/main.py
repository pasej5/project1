#!/usr/env python3
"""pickle"""

import pickle
import json

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
        
    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')
        
if __name__ == "__main__":
    fruit: Fruit = Fruit('Banana', 100)
    fruit.describe_fruit()
    
    calories = 150
    
    with open('apples.json', 'w') as file:
        data = {'name': fruit.name, 'calories': fruit.calories}
        json.dump(data, file)