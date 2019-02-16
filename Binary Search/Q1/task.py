def solve(question):
    max_n = 100000
    l_low = 1
    l_hi = max_n

    while l_hi - l_low > 1:
        mid = (l_hi + l_low) // 2
        ans = question.ask(1, mid)
        if ans:
            l_hi = mid
        else:
            l_low = mid

    if question.ask(1, l_low):
        l = l_low
    else:
        l = l_hi

    r_low = 1
    r_hi = max_n

    while r_hi - r_low > 1:
        mid = (r_hi + r_low) // 2
        ans = question.ask(mid, max_n)
        if ans:
            r_low = mid
        else:
            r_hi = mid

    if question.ask(r_hi, max_n):
        r = r_hi
    else:
        r = r_low

    return [l, r]
