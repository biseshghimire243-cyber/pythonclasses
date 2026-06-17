# write a program to fill a letter template given below with nae and date
letter = ''' Dear <|Name|>,
you are selected!
<|Date|>'''
print(letter.replace("<|Name|>", "Bishesh").replace("<|Date|","24 september 2050"))