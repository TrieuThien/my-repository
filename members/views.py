from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    """
    # Basic page show string "Hello, World!"
    return HttpResponse("Hello, World!")                        # Response to page the string "Hello, World!" 
    template = loader.get_template('myfirst.html')              # Load the all_members template
    """

    # Get all members from database
    mymembers = Member.objects.all().values()                   # Creates a mymembers object with all values of the Member
    template = loader.get_template("all_members.html")          # Load the all_members template

    # Creates a object containing the mymembers object
    contex = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(contex, request))       # render() -> send contex (object) to the template and rendered by the template 

def details(request, id):
    mymember = Member.objects.get(id = id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    before_sort_mymemeber = Member.objects.all()
    mymembers = Member.objects.all().order_by("lastname", "-id")

    template = loader.get_template("template.html")
    context = {
        # "fruits": ["Apple", "Banana", "Cherry"],
        # "name": "Lam Trieu Thien"
        "before_sort": before_sort_mymemeber,
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))

def for_loop(request):
    template = loader.get_template("for_loop.html")
    members = Member.objects.all()
    context = {
        "fruits": ["Apple", "Cherry", "Tomato", "Potato"],
        "members": members,
    }
    return HttpResponse(template.render(context, request))