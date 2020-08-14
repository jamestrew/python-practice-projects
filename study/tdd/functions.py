
def fibonnaci(n: int):
    """ Returns a fabonnaci sequence with length n """
    nums = [0, 1]
    if n < 0:
        raise ValueError
    elif n < 2 and n > -1:
        return nums[:n]

    for i in range(2, n):
        nums.append(nums[i - 2] + nums[i - 1])
    return nums


def chocolate_feast(spend, cost, w_exchange):
    eat_total = spend // cost
    wrapper = eat_total

    while wrapper // w_exchange:
        eat = wrapper // w_exchange
        wrapper = wrapper % w_exchange + eat
        eat_total += eat
    return eat_total
