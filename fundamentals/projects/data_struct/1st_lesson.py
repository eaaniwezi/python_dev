# https://www.youtube.com/watch?v=pkYVOmU3MgA&t=21s&ab_channel=freeCodeCamp.org
# https://jovian.com/learn/data-structures-and-algorithms-in-python

from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

cards = [13, 11, 10, 7, 13, 4, 3, 1, 0]


def locate_card_linear_search(cards, query):
    cards.sort(reverse=True)
    postion = 0
    if query in cards:
        for num in cards:
            if query == num:
                return postion
            else:
                postion += 1
                pass
    else:
        return -1


def test_location(cards, query, mid):
    mid_num = cards[mid]
    if mid_num == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_num < query:
        return 'left'
    else:
        return 'right'


def locate_card_binary_search(cards, query):
    low, high = 0, len(cards) - 1

    while low <= high:
        middle_index = (low+high) // 2
        middle_number_result = test_location(cards, query, middle_index)
        print('low:', low, 'high', high, 'middle_index',
              middle_index, 'middle_number_result', middle_number_result)

        if middle_number_result == 'found':
            return middle_index
        elif middle_number_result == 'left':
            high = middle_index - 1
        elif middle_number_result == 'right':
            low = middle_index - 1
    return -1


large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998

}

evaluate_test_case(locate_card_binary_search, large_test)
#! The time complexity of linear search is O(N) and its space complexity is O(1).
#! The time complexity of binary search is O(logN) and its space complexity is O(1).
