import requests
from django.shortcuts import render

def chat_view(request):
    response_text = ''
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        ollama_url = 'http://localhost:11500/api/generate'
        model_name = 'mistral:7b'  # or 'mistral:7b' if tagged

        response = requests.post(ollama_url, json={
            "model": model_name,
            "prompt": user_input,
            "stream": False
        })

        if response.ok:
            response_text = response.json().get('response', 'No response text found.')
        else:
            response_text = f"Error: {response.status_code} {response.text}"

    return render(request, 'chat_interface.html', {
        'response_text': response_text
    })
