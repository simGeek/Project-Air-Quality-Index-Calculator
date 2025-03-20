🔹PROJECT-AIR-QUALITY-INDEX-CALCULATOR🔹

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

4️⃣ LIBRARIES USED:

🔹scikit-learn: A machine learning library for building, training, and evaluating models.

🔹joblib: A library for saving/loading ML models efficiently and enabling parallel processing.

5️⃣ WORKFLOW

🔹INPUT: The user enters the values of six pollutants in micrograms.

🔹SUBMIT: The user submits the values by clicking on the submit button.

🔹RESULT: The AQI value and the AQI descriptor along with a visualization is displayed.

6️⃣ INSTALLATION (with VS Code)

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

cd my_project

python manage.py startapp home

🔹Delete 'views.py' from 'home'; cut and paste 'urls.py' and 'views.py' from the cloned files to 'home'

🔹Create new folders inside the outer 'my_project' named 'templates' and 'static'

🔹Create new folders named 'js' and 'css' inside 'static'

🔹Create new folder 'ds_models' inside outer 'my_project'

🔹Cut and paste the following to the respective folders:

.html files --> templates

.css files --> css inside static

.js files --> js inside static

🔹Add the following in settings.py inside inner 'my_project':

import os

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

🔹Inside settings.py --> 'INSTALLED_APPS', include 'home'

🔹Inside settings.py --> 'TEMPLATES', paste 'os.path.join(BASE_DIR, 'templates')' in DIRS = [PASTE HERE]

🔹Add in inner 'my_project' --> 'urls.py',

from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

path('admin/', admin.site.urls),

path('', include('home.urls')),

]

🔹Drive link to download the model:
https://drive.google.com/file/d/1obXfMWY6871IMdyx9yrlMQJ1alpnEzhD/view?usp=drive_link

🔹After downloading the model, save it inside 'ds_models'

🔹Make sure to save all the changes.

🔹Run 'python manage.py migrate' in the VS Code terminal

🔹Run 'python manage.py runserver' in the VS Code terminal

🔹Copy and paste the given link from the output terminal (http://127.0.0.1:8000/) in the browser

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





