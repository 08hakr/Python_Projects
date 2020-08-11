class Equation_Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Solve(self,s):
        if s=='+' : print(self.a+self.b)
        elif s=='-' : print(self.a-self.b)
        elif s=='*' : print(self.a*self.b)
        elif s=='/' : print(self.a/self.b)
        elif s=='%' : print(self.a%self.b)
print("\n\n\t\t\t\t\"EQUATION CALCULATOR\"")
print("\t\"How to use Equation Calculator\" \nNote :\n\t* You have to enter equation.\n\t* You can do \'+\',\'-\',\'/\',\'*\',\'%\' this operation.\n\t* If you want to exit from program just type \'exit\' at equation.\n\t* In this you can use only two no.\n\tEx. 1+2,22-12\n\n")
equ='0'
no1=0
no2=0
while equ!='exit' :
    equ = input("Enter Equation: ")
    if equ=='exit' :
        print("Exite from program.......................\nLanguage use Python.\nSimple mini Project using function.\nDevelop By 08hakr.")
    else :
        change = 0
        no=0
        for i in equ :
            if(i=='+' or i=='-' or i=='*' or i=='/' or i=='%') :
                sign=i
                change = 1
                no=0
            else :
                i=int(i)
                no=no*10+i
                if change == 0:
                    no1 =no
                else:
                    no2 = no
        s = Equation_Calculator(no1, no2)
        s.Solve(sign)
