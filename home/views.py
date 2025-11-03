from django.http import JsonResponse
def sample_view(request):
    try:
        data = {"message": "Welcone to the restaurant!"}
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)