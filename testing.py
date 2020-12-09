from pymongo import MongoClient

import pprint

nukefile = '''set cut_paste_input [stack 0]
version 12.2 v2
push $cut_paste_input
Transform {
 center {1024 778}
 name Transform1
 selected true
 xpos -302
 ypos 347
}

'''

server = MongoClient('localhost',27017)

DB = server['NukeShare']

collection = DB['Nukescript']

find = collection.find_one({})
script = find['script']
print(script)




















# # importing the library
# import pyperclip as pc
#
# text1 = "GeeksforGeeks"
#
# # copying text to clipboard
# pc.copy(text1)
#
# # pasting the text from clipboard
# text2 = pc.paste()
#
# print(text2)
