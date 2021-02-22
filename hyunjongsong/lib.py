def try_me(start, end):

    if end == start:
        return start

    mid = (start + end) // 2

    return try_me(start, mid) + try_me(mid + 1, end)
