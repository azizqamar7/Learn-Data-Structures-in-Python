# QUESTION 1:
# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.


def test_locate(cards, query, mid):
    mid_number = cards[mid]
    print("mid", mid, "mid_number:", mid_number)
    if mid_number == query:
        if mid-1 <= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_cards(cards, query):
    lo, hi = 0, len(cards)-1

    while lo <= hi:
        mid = (lo+hi)//2

        print("lo:", lo, "hi:", hi)

        result = test_locate(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 4
    },
    'output': 4
}

result = locate_cards(**test['input'])
print(result)
