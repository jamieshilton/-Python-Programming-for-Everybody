hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Hourly rate:")
r = float(rate)

if h > 40:
    basic = 40 * r
    overtime = (h - 40) * r * 1.5
    pay = basic + overtime
    
else:
    pay = h * r
    
print pay