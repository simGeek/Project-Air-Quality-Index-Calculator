🔹PROJECT-MEDICAL-DATA-EXTRACTION🔹

1️⃣ PURPOSE

To predict AQI given the values of 6 pollutants:

1) PM2.5

2) PM10

3) NO2

4) NOx

5) NH3

6) CO

2️⃣ PROBLEMS SOLVED

🔹No single-input AQI calculators

🔹Lack of visualization

🔹Faster decision-making

🔹Usable for public & researchers

3️⃣ TECH STACK

🔹Frontend: HTML, JS, CSS

🔹Backend: Python, Machine Learning, Django

🔹Infrastructure: AWS

4️⃣ LIBRARIES USED [See 'requirements.txt' for specific versions]

5️⃣ WORKFLOW

🔹INPUT: The user enters the values of six pollutants in micrograms.

🔹SUBMIT: The user submits the values by clicking on the submit button.

🔹RESULT: The AQI value and the AQI descriptor along with a visualization is displayed.

6️⃣ INSTALLATION (with VS Code)

Drive link to download the model:
https://drive.google.com/file/d/1obXfMWY6871IMdyx9yrlMQJ1alpnEzhD/view?usp=drive_link

🔹Install:

VS Code (https://code.visualstudio.com/download)

Python (https://www.python.org/downloads/)

🔹Open VS Code

🔹Click on 'Clone Git Repository' and paste 'https://github.com/simGeek/Project-Air-Quality-Index-Calculator.git' in the space prompted for the git url

🔹Hit 'Enter' and select a folder locally where to include the project files; open the folder in VS Code

🔹Open Terminal > New Terminal

🔹Run following commands:

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

🔹Run following commands:

django-admin startproject my_project

python manage.py startapp home

🔹Delete 'views.py' from 'home'; cut and paste 'urls.py' and 'views.py' from the cloned files to 'home'

🔹Create new folders inside the 'project-air-quality-index-calculator' named 'templates' and 'static'

🔹Create new folders named 'js' and 'css' inside 'static'

🔹Cut and paste the following to the respective folders:

.html files --> templates

.css files --> css inside static

.js files --> js inside static

.py files --> home (except manage.py)

🔹Add the following in settings.py inside my_project:

import os

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

🔹Inside settings.py --> 'INSTALLED_APPS', include 'home'

🔹Inside settings.py --> 'TEMPLATES', paste 'os.path.join(BASE_DIR, 'templates')' in DIRS = [PASTE HERE]

🔹Add in 'my_project' --> 'urls.py',

from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

path('admin/', admin.site.urls),

path('', include('home.urls')),

]

🔹Run 'python manage.py migrate' in the VS Code terminal

🔹Run 'python manage.py runserver' in the VS Code terminal

7️⃣ CHALLENGES

🔹Choosing the ideal number of input pollutants

🔹Selecting the right pollutants

🔹Determining the most accurate regression model

🔹Picking a proper visualization chart

8️⃣ KEY LEARNINGS

🔹Exploratory Data Analysis

🔹Handling missing values and outliers

🔹Model building

🔹Regression techniques

9️⃣ DEPLOYED PROJECT IMAGES

![p2-1](https://github.com/user-attachments/assets/d34a212d-2cc2-4771-9c2c-587caa470138)

![p2-2](https://github.com/user-attachments/assets/757fffc7-7f18-4383-8491-ccbf3ee43a4f)





