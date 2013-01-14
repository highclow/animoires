def movBackAndForth(i, c, t):
    step = 2
    tm100 = t % 100
    tm50 = t % 50
    if (tm100 > 75):
        return i - ((100 - tm100) * step)
    else:
        if (tm100 > 50):
            return i - ((tm100 - 50) * step)
        else:
            if (tm100 > 25):
                return i + ((50 - tm100) * step)
            else:
                return i + ((tm100) * step)