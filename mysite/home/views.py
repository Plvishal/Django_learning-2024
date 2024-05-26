from django.shortcuts import render


# Create your views here.
def home(request):
    peoples=[
        {"name":"Vishal","age":23},
        {"name":"Ravi","age":25},
        {"name":"Shivendra","age":24},
        {"name":"Mangla","age":25},
        {"name":"Akash","age":22},
        {"name":"Krit","age":24},
        {"name":"Risabh","age":23},
        {"name":"Shailesh","age":25},
        {"name":"Sonu","age":22},
        {"name":"Harsha","age":14},
             
             ]
    return render(request,"index.html",context={'peoples':peoples})

