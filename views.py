import os
import joblib
import logging
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

logger = logging.getLogger(__name__)

def aqi_pollutants(request):
    return render(request, "aqi_pollutants.html")

def aqi_regression(request):
    if request.method == 'POST':
        try:
            # Retrieve and convert form data from POST request
            field1 = request.POST.get('pm2dot5')
            field2 = request.POST.get('pm10')
            field3 = request.POST.get('no2')
            field4 = request.POST.get('nox')
            field5 = request.POST.get('nh3')
            field6 = request.POST.get('co')

            # Validate inputs (Check for missing or non-numeric values)
            if None in (field1, field2, field3, field4, field5, field6):
                raise ValueError("Missing input values")

            try:
                field1, field2, field3, field4, field5, field6 = map(float, (field1, field2, field3, field4, field5, field6))
            except ValueError:
                raise ValueError("Invalid input: All values must be numeric")

            # Load the pre-trained regression model
            model_path = os.path.join(settings.BASE_DIR, 'ds_models', 'aqi_model.joblib')

            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found: {model_path}")

            model = joblib.load(model_path)

            # Prepare input data for prediction (Normalize based on predefined max values)
            input_data = [[
                field1 / 999.99, field2 / 1000.00, field3 / 432.30,
                field4 / 499.20, field5 / 485.52, field6 / 48.52
            ]]

            # Predict the AQI value
            prediction = model.predict(input_data)

            # Denormalize the prediction
            prediction = prediction * 818

            # Round the prediction to two decimal places
            prediction = round(prediction[0], 2)

            # Determine AQI category
            if 0 <= prediction <= 50:
                bucket = "Good"
            elif 51 <= prediction <= 100:
                bucket = "Satisfactory"
            elif 101 <= prediction <= 200:
                bucket = "Moderate"
            elif 201 <= prediction <= 300:
                bucket = "Poor"
            elif 301 <= prediction <= 400:
                bucket = "Very Poor"
            else:
                bucket = "Severe"

            # Prepare response data
            response_data = {
                'predictions': prediction,
                'bucket': bucket,
                'input_data': {
                    'pm2.5': field1, 'pm10': field2, 'no2': field3,
                    'nox': field4, 'nh3': field5, 'co': field6
                }
            }

            # Render p2aqi.html with prediction results
            return render(request, 'p2aqi.html', response_data)

        except Exception as e:
            error_message = f"Error: {str(e)}"
            logger.error(error_message)  # Log the error
            return JsonResponse({'error': error_message}, status=400)

    # If not a POST request, return an error message
    return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=405)

