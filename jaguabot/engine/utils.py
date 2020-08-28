def pixels2percent(start, end, current):
    '''converts pixels to a percentage.'''
    total = end - start
    to_pc = total / 100
    current_pc = (current - start) / to_pc
    return current_pc