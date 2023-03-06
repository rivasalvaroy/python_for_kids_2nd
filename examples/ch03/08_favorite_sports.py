favorite_sports = {'Ralph Williams': 'Football',
                   'Michael Tippett': 'Basketball',
                   'Edward Elgar': 'Baseball',
                   'Rebecca Clarke': 'Netball',
                   'Ethel Smyth': 'Badminton',
                   'Frank Bridge': 'Rugby'}

print(favorite_sports['Rebecca Clarke'])
del favorite_sports['Ethel Smyth']
print(favorite_sports)
favorite_sports['Ralph Williams'] = 'Ice Hockey'
print(favorite_sports)

favorite_sports = {'Rebecca Clarke': 'Netball',
                   'Michael Tippett': 'Basketball',
                   'Ralph Williams': 'Ice Hockey',
                   'Edward Elgar': 'Baseball',
                   'Frank Bridge': 'Rugby'}

favorite_colors = {'Malcolm Warner': 'Pink polka dots',
                   'James Baxter': 'Orange stripes',
                   'Sue Lee': 'Purple paisley'}

# favorite_sports + favorite_colors
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
