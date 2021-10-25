number_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}



def num_translate(str_number):
    if str_number.lower() in number_dict:
        if str_number.istitle():
            return number_dict[str_number.lower()].capitalize()
        else:
            return number_dict[str_number]
    else:
        return None


print(num_translate('Five'))