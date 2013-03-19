# -*- coding: utf-8 -*-

'''
@access public
@param  int, for example '4111111111111111'
@return int
'''
def valid_card_number(card_number):
    checksum = 0
    roll = lambda numeric: [int(number) for number in str(numeric)]
    
    for i, number in enumerate(roll(card_number)):
        if i % 2 == 0:
            checksum += sum(roll(number * 2))
        else:
            checksum += number

    if checksum % 10 == 0:
        return 'Valid'
    else:
        return 'Not valid'