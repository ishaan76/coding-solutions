def joinMiddle(bound_by, tag_name):
    """ code here """
    n = len(bound_by)//2
    return bound_by[0 : n] + tag_name + bound_by[n:]