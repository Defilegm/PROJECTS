thesaurus_dict = {}


def thesaurus(*saurus):
    for name in saurus:
        for upper in name[1:]:
            if upper.istitle():
                if upper in thesaurus_dict:
                    if name[0] in thesaurus_dict[upper]:
                        thesaurus_dict[upper][name[0]].append(name)
                    else:
                        thesaurus_dict[upper][name[0]] = [name]
                else:
                    thesaurus_dict[upper] = dict.fromkeys([name[0]], [name])
                    


thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Анатолий Артемьев")
print(thesaurus_dict)