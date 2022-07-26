from django.shortcuts import render
from myapp.models import Newuser
from django.contrib import messages
# Create your views here.


# def Indexpage(request):
#    return render(request, "index.html")


def Signup(request):
    if request.method == 'POST':
        UserType = request.POST['Usertype']
        First_Name = request.POST['FirstName']
        Last_Name = request.POST['LastName']
        Username = request.POST['UserName']
        Email_Id = request.POST['Email']
        Password = request.POST['Password1']
        Confirm_Password = request.POST['Password2']
        Adress1 = request.POST['Line1']
        Adress2 = request.POST['City']
        Adress3 = request.POST['State']
        Adress4 = request.POST['Pincode']
        print(Adress1)
        Adress = " , ".join([Adress1, Adress2, Adress3, Adress4])
        if (Password != Confirm_Password):
            messages.error(request, " Passwords do not match")
            return render(request, 'signup.html')
        Newuser(UserType=UserType, First_Name=First_Name, Last_Name=Last_Name, Username=Username,
                Email_Id=Email_Id, Password=Password, Confirm_Password=Confirm_Password, Adress=Adress).save()
        messages.success(request, 'The New User ' +
                         str(First_Name) + " Is created successfully")
        return render(request, "signup.html")
    else:
        return render(request, "signup.html")


def loginpage(request):
    if request.method == "POST":
        try:
            Userdetails = Newuser.objects.get(
                Username=request.POST["Username"], Password=request.POST['Password'])
            print("Username=", Userdetails)
            request.session['Username'] = Userdetails.Username
            return render(request, 'logout.html')
        except Newuser.DoesNotExist as e:
            messages.success(request, 'Username / Password Invalid..!')
    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['Username']
    except:
        return render(request, 'signup.html')
    return render(request, 'signup.html')
