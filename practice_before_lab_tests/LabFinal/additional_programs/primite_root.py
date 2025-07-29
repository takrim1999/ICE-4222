def is_primitive(a,b):
    root_set = set()
    for i in range(1,b):
        root_set.add((a**i) % b)
    if len(root_set) == b-1:
        return True
    return False

print(is_primitive(11,10))