guests = []
name = ''
while name != 'DONE':
    name = input('Enter guest name(if no more guests, type done): ')
    guests.append(name)
guests.sort()
for guest in guests:
    print(guest)