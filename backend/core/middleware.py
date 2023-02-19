from django.http import JsonResponse


class MiddlewareCatchException:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        data = {'error': repr(exception)}
        return JsonResponse(data=data, status=500)
