def compare(obj1, obj2):
    if obj1 is None or obj2 is None:
        return False

    if obj1.__class__ != obj2.__class__:
        return False

    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False

        if len(set(obj1.keys()).symmetric_difference(set(obj2.keys()))) > 0:
            return False

        for key1 in obj1.keys():
            if not compare(obj1.get(key1), obj2.get(key1)):
                return False

        return True

    elif isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False

        for item1 in obj1:
            match = False

            for item2 in obj2:
                if item1.__class__ == item2.__class__:
                    match = compare(item1, item2)
                    if match:
                        break

            if not match:
                return False

        return True

    else:
        return obj1 == obj2
