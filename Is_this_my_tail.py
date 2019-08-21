def correct_tail(body, tail):
    x = list(body)
    x.reverse()
    if x[0] == tail:
        return True
    else:
        return False