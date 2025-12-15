def f(subjects):
     best_subject = None
     best_avg = -1

     for subject, grades in subjects.items():
         avg = sum(grades)/len(grades)
     if avg > best_avg:
             best_avg = avg
             best_subject = subject
     return best_subject
    


