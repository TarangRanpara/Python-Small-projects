import json
from difflib import get_close_matches

def translate(word):

    #opening a json file
    with open('data.json','r') as file:
        data = json.load(file)

    #making word, case-insensitive
    word = word.lower()

    #if directly found!
    if word in data:
        answer = '\n'.join(str(d) for d in data[word])
        return 'Meanings found:\n\n'+answer

    #Some special words for ex. Texas
    elif word.title() in data:
        answer = '\n'.join(str(d) for d in data[word.title()])
        return 'Meaning found:\n\n'+answer

    else:

        #getting most probable results by cutoff being 70% match at least
        possibilities = get_close_matches(word,data.keys(),cutoff=0.7)

        if len(possibilities) == 0:
            return 'Not Found!'
        
        else:
            ask = 'did you mean ' + possibilities[0] + '??'
            
            resp = input(ask + "\nenter Y or N:")

            if resp == 'Y':
                answer = '\n'.join(str(d) for d in data[possibilities[0]])
                return 'Meanings found:\n\n'+answer
            else:
                return 'try to remember some other word!'

#kind of a main function, to ensure the flow
def main():
    word = input("enter word to be searched:")
    print(translate(word))

if __name__ == '__main__':
    main()


