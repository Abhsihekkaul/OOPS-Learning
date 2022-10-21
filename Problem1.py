#find out the sum of three number and if all three numbers are same then return the thrice of one value 
class PromptedNums:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        if not (num1 and num2 and num3):
            raise ValueError("Hey! please type a Invalid value ")
        if num1 == num2 and num2 == num3:
            print("All numbers having the same values so the addiion is 3 x anynumber : ", 3*num1)

def main():
    numbers = inputs()
    addition = numbers.num1 + numbers.num2 + numbers.num3
    print("The addition is : " , addition)

def  inputs():
    num1 = int(input("Enter the First Value : "))
    num2 = int(input("Enter the First Value : "))
    num3 = int(input("Enter the First Value : "))
    return PromptedNums(num1,num2,num3)


main()



        
