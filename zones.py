def get_node(x, y):
    if x < 150:
        return "C"   # entry
    elif x < 300:
        return "F"   # shoe rack
    elif x < 450:
        return "G"   # queue
    elif x < 600:
        return "I"   # security
    elif x < 750:
        return "K"   # sanctum
    else:
        return "N"   # exit