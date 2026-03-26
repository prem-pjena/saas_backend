import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .validators import validate_user
from .services import create_user_service


@csrf_exempt
def create_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    result = validate_user(data)

    if not result["success"]:
        return JsonResponse(result, status=400)

    response = create_user_service(result["data"])

    return JsonResponse(response, status=201)