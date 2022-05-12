def enough(cap, on, wait):
    total = wait - (cap-on)
    if total > 0:
        return total
    elif total < 0:
        return 0
    else:
        return total