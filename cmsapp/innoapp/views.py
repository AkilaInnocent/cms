from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"index.html")


def details(request):
    return render(request,"event-detail.html")

def event_list(request):
    return render(request,"event-listing.html")