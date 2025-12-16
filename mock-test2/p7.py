def f(array):
    count = 0
    for username in array:
        if 4 <= len(username) <= 12:
            valid = True
            for char in username:
                if not (char.isdigit() or char.islower() or char == "_"):
                    valid = False
                    break
            if valid == True:
                count += 1
    return count

def f(array2):
    count = 0
    for username in array2:
        if 4 <= len(username) <= 12 and all(c.isdigit() or c.islower() or c == "_" for c in username):
            count += 1
    return count
