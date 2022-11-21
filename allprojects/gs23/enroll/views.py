from django.shortcuts import render
from enroll.models import Student
from enroll.forms import Register

# Create your views here.



def stuinfo(request):
    stus = Student.objects.all()
    print("-----------")
    print(type(stus))
    stu = Student.objects.get(pk=2)
    print(type(stu))
    return render(request, "enroll/home.html", {"stus" : stus})


def showform(request):
    #setting label id and initial value    
    # default_reg_form = Register( label_suffix="+", initial={"name":"jiyaulla"}) # auto_id= "id_%s"
    # string_reg_form = Register(auto_id='some_%s', label_suffix="?", initial={"name":"mamata"})
    # true_reg_form = Register(auto_id=True, label_suffix="%", initial={"name":"noor"})
    # false_reg_form = Register(auto_id=False, label_suffix="$ooooooo", initial={"email":"vishwa@gmail.com"})


    #how to set the value
    # reg_form = Register()
    # reg_form.order_fields(field_order=["email","first_name", "name"])


    #field attributes related form fields
    # reg_form = Register()

    #how to loop the form fields
    reg_form = Register()

    return render(request, "enroll/registerpage.html", {'reg_form': reg_form})