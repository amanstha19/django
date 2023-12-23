# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
def hello_world(request):
    return HttpResponse('''
    
    <html>
    <head>
    <title> Learning Python </title>
    </head>
    
    <body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    </body>
    </html>
    
    ''')

def hello(request):
    return HttpResponse("<h1> HELLO </h1>")


def home(request):
    return render(request, template_name='myapp/home.html')
def portfolio(request):
    return render(request, template_name="myapp/index.html")
def temp_inherit_home(request):

    items = [
        {"name": "shirt", "store_location": "KTM", "price": 1000},
        {"name": "hoodies", "store_location": "BKT", "price": 3000},
        {"name": "trousers", "store_location": "LTP", "price": 2000},

    ]
    return render(request, template_name='myapp/temp_inherit_home.html', context={"name": "Aman Shrestha", "age": 21,
                                                                "address": "Bhaktapur", "items": items})
def temp_inherit_features(request):
    items = [
        {"name": "hock Resistant Portable Bluetooth Speaker",
         "description": "The design is amazing and feels"
                        " like premium product. The sound quality is good and supports multiple devices both via Bluetooth and AUX mode. It would have "
                        "been awesome if the device come of with type c charging as it is widely used by most of the devices these days. But, this does not hold us back to buy this amazing Nepali brand product. I would recommend this product to everyone who are looking for budget friendly, "
                        "quality Bluetooth speaker"},


        {
            "name": " Office Editing and Gaming Desktop With Intel Core i5 6th Gen 6500 3.6Ghz"
                    " Processor, 60Hz 19” PS Tech "
                    "LED HD Monitor, 8GB 3200Mhz"
                    " RAM",
            "description": "Processor: Intel core i5 6500 3.6Ghz Turbo Quad Core Skylake LGA 1151 6MB Cache 6th Gen Processor With 4 Logical Cores and 4 Threads "
                           "(3 Yrs. Warranty)"
"Board: Esonic H110 Dual RAM Channel Pcie Board (1 Year Warranty)"
"RAM: Crucial Best Brand 8GB 3200Mhz RAM(Lifetime Brand Warranty on Crucial)"
"SSD: Kingston SATA 256GB Branded SSD (1 Year Warranty)"
        }


    ]
    return render(request, template_name='myapp/temp_inherit_features.html', context={"name": "Aman Shrestha", "age": 21,
                                                                "address": "Bhaktapur", "items": items})

def temp_inherit_pricing(request):
    students = Student.objects.all()
    return render(request, template_name='myapp/temp_inherit_pricing.html',
                  context={"students": students})
