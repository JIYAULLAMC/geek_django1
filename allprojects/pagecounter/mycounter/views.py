from django.shortcuts import render

# Create your views here.

count_list = []
def home_counter(request):
    count = request.session.get("count", 0)
    new_count = count + 1
    request.session["count"] = new_count
    count_list.append(new_count)
    
    return render(request, "mycounter/home.html", {"count":count_list})