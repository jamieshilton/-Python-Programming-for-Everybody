score_input = raw_input("Please enter your score: ")

try:
    score = float(score_input)
except:
    score = -1

if score >= 0.9 :
    grade = "A"
elif score >= 0.8:
   grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
elif score < 0.6:
    grade = "F"
else:
    print "Please enter a numberic score between 0.0 and 1.0"
    exit()
    
print grade