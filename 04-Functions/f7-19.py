def f(number):
    total = 0
    already_counted = []
    str_num = str(number)
    for i in str_num:
        if i not in already_counted:
            cnt = str_num.count(i)
            if cnt > 1:
                total += cnt * int(i)
        already_counted.append(i)
    return total
        
  

print(f(513553007))
