from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .src.segrigater import gemini
from django.views.decorators.csrf import csrf_exempt
import logging

# Create your views here.

@csrf_exempt
def Segrigation(request):
    if request.method == "POST":
        try:
            logging.info(f"Request POST data: {request.POST}")
            Comment = request.POST.get("Comment")
            Headings = request.POST.get("Headings")

            if not Comment:
                return JsonResponse({'error': 'Comment missing or invalid'}, status=400)
            
            if not Headings:
                Headings = ""
            
            response = gemini(Comment, Headings)
            return JsonResponse({"Segrigator": response})
        except Exception as e:
            logging.error(f"Exception: {e}")
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method."}, status=405)


def Index(request):
    return render(request, 'index.html')