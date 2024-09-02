import os
import cv2

list_of_names = []


def cleanup_data():
   with open('name-data.txt',r) as f:
      for line in f:
          list_of_names.append(line.strip())
print(list_of_names)         



cleanup_data()
