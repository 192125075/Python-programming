def SimpleInterest(P,N,R):
    SI=(P*N*R)/100
    return SI
P=int(input("Enter the principal amount: "))
N=int(input("Enter the number of years: "))
if(N>0)and(P>0):
    
    S=input("Is customer senior citizen (y/n): ")
    if (S=='y'):
        R=12
    else:
        R=10
        
    SI=SimpleInterest(P,N,R)
    print("Simple Interest : ",SI)
else:
    print("Enter positive values")
