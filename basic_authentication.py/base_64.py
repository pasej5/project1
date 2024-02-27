#!/usr/bin/env python3

import base64

# my_text = "Hello World"
# my_text = my_text.encode("ascii")
# my_text_b64 = base64.b64encode(my_text)

# print(my_text_b64)

with open("lethabo.jpg", 'rb') as file:
   data = file.read()
   
with open("image.jpg", "wb") as file:
    file.write(data)
    
    
    
    class Solution:
       def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
          
          for i in range(len(intervals)):
             if newInterval[1] < intervals[i][0]
    
    