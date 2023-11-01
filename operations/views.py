from django.shortcuts import render

# Create your views here.

from django.views.generic import View


class HelloWorldView(View):

    def get(self,request,*args,**kwargs):
        print("helloworld view")
        return render(request,"helloworld.html")
    

# goodmorning view

class GoodMorning(View):

    def get(self,request,*args,**kwargs):
        print("goodmorning view")
        return render(request,"morning.html")

    
# add view

class AddView(View):
    def get(self,request,*args,**kwargs):
        print("adding view")
        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)

        return render(request,"add.html",{"out":result})
    

# multiplication view

class MulView(View):
    def get(self,request,*args,**kwargs):
        print("multiplication view")
        return render(request,"mul.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print(result)
        return render(request,"mul.html",{"out":result})
    

# division view

class DivisionView(View):
    def get(self,request,*args,**kwargs):
        print("Division View")
        return render(request,"div.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        print(result)
        return render(request,"div.html",{"out":result})
    

# sub view

class SubView(View):
    def get(self,request,*args,**kwargs):
        print("subview")
        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print(result)
        return render(request,"sub.html",{"out":result})
    

    
# cube view

class CubeView(View):
    def get(self,request,*args,**kwargs):
        print("cubeview")
        return render(request,"cube.html")
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        result=int(n)**3
        print(result)
        return render(request,"cube.html",{"out":result})
    


# factorial view

class FactorialView(View):
    def get(self,request,*args,**kwargs):
        print("factorial view")
        return render(request,"factorial.html")
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        fact=1

        for i in range(1,int(n)+1):
            fact=fact*i
        print(fact)
        return render(request,"factorial.html",{"out":fact})

    
# leap year view 

class LeapYearView(View):
    def get(self,request,*args,**kwargs):
        print("leapyear")
        return render(request,"leapyear.html")
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        n=int(n)

        if n%100==0 and n%400==0:
            print(f"{n} is a leap year")
            result=(f"{n} is a leap year")
        elif n%100!=0 and n%4==0:
            print(f"{n} is a leap year")
            result=(f"{n} is a leap year")        
        else:
            print(f"{n} is not a leap year")
            result=(f"{n} is a leap year")
 
        return render(request,"leapyear.html",{"out":result})

# odd even view

class OddEvenView(View):
    def get(self,request,*args,**kwargs):
        print("OddEVenView")
        return render(request,"oddeven.html")
    
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        if n%2==0:
            result=f"{n} is a even number"
        else:
            result=f"{n} is a odd number"
        
        return render(request,"oddeven.html",{"out":result})
    
# prime number view

class PrimeView(View):
    def get(self,request,*args,**kwargs):
        print("primeview")
        return render(request,"prime.html")
    
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        prime=[i for i in range(2,n) if n%i==0]
        result="not a prime number" if any(prime)==True else "is a prime number"

        return render(request,"prime.html",{"out":result}) 
        




# index view

class IndexView(View):
    def get(self,request,*args,**kwargs):
        print("index view")

        return render(request,"index.html")
    
# bmi view

class BmiView(View):
    def get(self,request,*args,**kwargs):
        print("bmiview")
        return render(request,"bmi.html")

    def post(self,request,*args,**kwargs):
        weight_in_kg=int(request.POST.get("weight_in_kg"))
        height_in_cm=int(request.POST.get("height_in_cm"))
        height_in_meter=height_in_cm/100
        bmi=weight_in_kg/(height_in_meter)**2
        print(bmi)

        return render(request,"bmi.html",{"out":bmi})
    

# EMI view

class EmiView(View):
    def get(self,request,*args,**kwargs):
        print("emiview")
        return render(request,"emi.html")
    
    def post(self,request,*args,**kwargs):
        R=int(request.POST.get("interest_rate"))
        r=R/12
        P=int(request.POST.get("principal_amount"))
        year=int(request.POST.get("number_of_year"))
        n=year*12
        emi=(P*r*(1+r)**n)/(((1+r)**n)-1)
        
        return render(request,"emi.html",{"out":emi})


