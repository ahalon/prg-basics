def f(length):
    with open ("data.txt", "r", encoding = "utf-8") as file:
        text = file.read()
        words = text.split()
    count = 0
    for word in words:
        if len(word) == length:
            count += 1
    return count
    