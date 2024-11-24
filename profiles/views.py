from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile


class Profilelist(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)