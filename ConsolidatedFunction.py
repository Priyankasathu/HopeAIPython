class Consolidated:
    def Subfields():
        print("Sub-fields in AI are:")
        domainList = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for subfield in domainList:
            print(subfield)

    def OddEven():
        getValue=int(input("Enter a number:"))
        if(getValue%2==0):
            checkResult=str(getValue) +" is Even number"
        else:
            checkResult=str(getValue) +" is odd number"
        return checkResult
        
    def Elegible():
        gender=input("Enter your gender (Male/Female): ")
        age=int(input("Enter your age: "))
        if(age>=18 and gender=='Female'):
            checkElegiblity="Elegible"
        elif(age>=21 and gender=='Male'):
            checkElegiblity="Elegible"
        else:
            checkElegiblity="Not Elegible"
        return checkElegiblity
        
    def percentage():
        Sub1=int(input("Enter Subject1 Marks: "))
        Sub2=int(input("Enter Subject2 Marks: "))
        Sub3=int(input("Enter Subject3 Marks: "))
        Sub4=int(input("Enter Subject4 Marks: "))
        Sub5=int(input("Enter Subject5 Marks: "))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        Percentage=Total/5
        print("Total Marks:", Total)
        print("Percentage:", Percentage)
        
    def Area(Height,Breadth):
        totalArea=(Height*Breadth)/2
        return totalArea
     
    def Perimeter(Height1,Height2,Height3):
        totalPerimeter=Height1+Height2+Height3
        return totalPerimeter

    


   
       