#famous school game
def flames(person1,person2):
    
    magic_string = 'flame'

    magic_dict = {
        'f':'friend',
        'l':'love',
        'a':'affection',
        'm':'marriage',
        'e':'enemies',
    }
    
    for x in person1:
        if (x in person1) and (x in person2):
            person1 = person1.replace(x,'')
            person2 = person2.replace(x,'')

    return magic_dict[magic_string[len(person1+person2)%5]]

print(flames(input('enter name of person-1:'),input('enter name of person-2:')))
