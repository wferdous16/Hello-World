#Wakif Ferdous
#1770041

Roster=dict()
counter=0
for i in range(1,6):
    counter+=1
    print("Enter player {}'s jersey number:".format(counter))
    jersey=input()
    print("Enter player {}'s rating:".format(counter))
    rating=input()
    print()
    Roster[int(jersey)] = int(rating)
print('ROSTER')
for key, value in sorted(Roster.items()):
	print('Jersey number: {}, Rating: {}'.format(key, value))
print()
while True:
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    option=input('Choose an option:\n')

    if option=='o':
        print('ROSTER')
        for key, value in sorted(Roster.items()):
            print('Jersey number: {}, Rating: {}'.format(key, value))
        print()

    elif option=='a':
        print("Enter a new player's jersey number:")
        jersey= input()
        print("Enter the player's rating:")
        print()
        rating= input()
        if jersey not in Roster:
            Roster[int(jersey)] = int(rating)
    elif option == 'd':
        print("Enter a jersey number:")
        print()
        jersey=input()
        del Roster[int(jersey)]
    elif option=='u':
        print("Enter a jersey number:")
        jersey=int(input())
        print("Enter a new rating for player:")
        if jersey in Roster:
            rating = int(input())
            print()
            Roster[jersey] = rating
    elif option=='r':
        print('Enter a rating:')
        rating=int(input())
        print()
        print('ABOVE',rating)
        for key,value in sorted(Roster.items()):
            if value>rating:
                print('Jersey number: {}, Rating: {}'.format(key, value))
        print()
    elif option == 'q':
        break




















