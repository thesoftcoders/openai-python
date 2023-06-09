from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
import openai
import json
from .serializers import AnswerSerializer
from .key import API_KEY

class OpenAIView(View):
    def post(self, request):
        data = json.loads(request.body)
        question = data.get('question')
        openai.api_key = API_KEY
        response = openai.Completion.create(
            engine='curie',
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response.choices[0].text.strip()
        print(answer)
        serializer = AnswerSerializer({'answer': answer})
        return JsonResponse(serializer.data)
    
    def get(self, request):
        return render(request, 'openai_response/index.html')