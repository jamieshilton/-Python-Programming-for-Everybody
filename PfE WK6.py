def computepay(h,r):
    if h > 40:
        pay = (40 * r) + ((h - 40) * 1.5 * r)
    elif h <= 40:
        pay = h * r   
    
    return pay

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate of pay:")

a = float(hrs)
b = float(rate)

print computepay(a,b)