import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number, flag=False):
    '''
    function generates random 'jokes' from list's
    :param number: int
    :param flag: False(words can be repearted) or True(words will not be repeated)
    :return: string
    '''
    i = 0
    jokelist = []
    while i < number:
        joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        i += 1
        print(joke)
        if flag == True:
            jokelist = joke.split()
            for noun in nouns:
                for jok in jokelist:
                    if noun == jok:
                        nouns.remove(noun)

            for adverb in adverbs:
                for jok in jokelist:
                    if adverb == jok:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for jok in jokelist:
                    if adjective == jok:
                        adjectives.remove(adjective)



get_jokes(4, flag=False)