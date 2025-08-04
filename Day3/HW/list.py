#You are given a list of colors and you need to print a sentence for each color.
#The sentence should be "I like red","I like blue","I like green".

new_list = ['red', 'blue', 'green']
output = ''
for color in new_list:
    if output != '':
        output = output + ', '
    output = output + 'I like ' + color
print(output)
