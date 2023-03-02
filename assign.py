'''Python Program for simple interest
Simple interest formula is given by: 
Simple Interest = (P x T x R)/100 
Where, P is the principal amount 4
T is the time  
R is the rate'''
def simple_interest():
    p_amt = int(input("Enter Principal amount: "))
    time = int(input("Enter Time: "))
    roi = int(input("Enter Rate of Interest: "))
    return (p_amt * time * roi)/100

print(simple_interest())
