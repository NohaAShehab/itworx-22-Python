

def validateInt(variable):
    if isinstance(variable, int):
        return True


def validateIntOrFloat(variable):
    if isinstance(variable, int) or isinstance(variable, float):
        return True