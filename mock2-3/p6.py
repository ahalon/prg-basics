def f(min_len):
    count = 0
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            if any(len(word) >= min_len for word in words):
                count += 1
    return count

to do 4,7,8