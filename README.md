# Ex.04 Design a Website for Server Side Processing
## Date:09-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```

math.html 

<html>
    <head>
        <title>
            Mileage
        </title>
        <style>
            body
            {
               background-color: rgb(17, 244, 213); 
            }
            .box
            {
               width: 650px;
               height: 400px;
               background-color: rgb(251, 4, 103);
               border:dashed 3px rgba(3, 72, 247, 0.808);
               padding: 10px;
               margin-left: 250px;
               margin-top: 100px;
               position:fixed;
               top: 100px;
               left: 300px; 
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2 align="center">VEHICLE MILEAGE</h2>
            <h3 align="center">V SURUTHIKA(25000884) </h3>
            <h2 align="center">Calculation of Mileage</h2>
            <form method="post" align="center">
                {% csrf_token %}
                <label>Distance(in km)</label>
                <input type="text" name="distance" value="{{ distance }}">
                <br>
                <br>
                <label>Fuel Consumed(in l)</label>
                <input type="text" name="fuelconsumed" value="{{ fuelconsumed }}">
                <br>
                <br>
                <input type="submit" value="result">
                <br>
                <br>
                <label>Mileage(in km/l):</label>
                <input type="text" name="mileage" value="{{ mileage }}">
            </form>
        </div>
    </body>
</html>

views.py

from django.shortcuts import render
def vehicle(request):
    distance=int(request.POST.get('distance',0))
    fuelconsumed=int(request.POST.get('fuelconsumed',0))
    mileage=distance/fuelconsumed if request.method=='POST' else 0
    print("Distance travelled=",distance)
    print("Fuel consumed=",fuelconsumed)
    print("Vehicle mileage=",mileage)
    return render(request,'mathapp/math.html',{'distance':distance,'fuelconsumed':fuelconsumed,'mileage':mileage})

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('',views.vehicle,name='vehicle')
]
```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (28).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (29).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
