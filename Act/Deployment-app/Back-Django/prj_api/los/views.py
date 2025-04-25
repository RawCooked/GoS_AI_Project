from django.http import JsonResponse
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('random_forest_model.pkl')

def classify_lab_event(request):
    try:
        # Extract input parameters from the URL
        diag = int(request.GET.get('diag', 0))
        pres = int(request.GET.get('pres', 0))
        seq = int(request.GET.get('seq', 0))

        # Prepare input data for prediction
        input_data = pd.DataFrame([{
            'diagnosis_id': diag,
            'procedure_id': pres,
            'seq_num': seq
        }])

        # Make the prediction
        prediction = model.predict(input_data)[0]

        # Return the classification result (1 = abnormal, 0 = normal)
        return JsonResponse({'Los': float(prediction)})

    except Exception as e:
        # Handle errors gracefully
        return JsonResponse({'error': str(e)}, status=400)