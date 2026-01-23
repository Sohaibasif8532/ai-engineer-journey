class passwordChecker:
    Score=0
    def lengthCheck(password):
        return len(password)>=8
    def ContainUpper(password):
        return any(i.isupper()for i in password)
    def Containlower(password):
        return any(i.islower() for i in password)
    def hasdigit(password):
        return any(i.isdigit() for i in password)
    def hasspecial(password):
        return any(not i.isalnum() for i in password)
                
    
    def Scorechecker(password):

        score=0
        if passwordChecker.lengthCheck(password):
            score+=1
        else:
            print("Password must be at least 8 characters long")
        if passwordChecker.ContainUpper(password):
            score+=1
        else:
            print("Password must contain an uppercase letter")
        if passwordChecker.Containlower(password):
            score+=1
        else:
            print("Password must not contain a lowercase letter")
        if passwordChecker.hasdigit(password):
            score+=1
        else:
            print("Password must contain a digit")
        if passwordChecker.hasspecial(password):
            print("Password must not contain a special character")
        else:
            score+=1

        if score>=4:
            print("Password is Strong")
        elif score==3:
            print("Password is Medium")
        elif score==2:
            print("Password is Weak")
        elif score==1:
            print("Password is Very Weak")

        print("\n")
        print("Score:",score,"/5")
        


while True:
    print("Welcome To Password Checker!")
    print("--------------------------------------------------\n")
    password=input("Enter your password: ")
    passwordChecker.Scorechecker(password)
    print("\n")

        
            

