from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserProfileSerializer

class UserMeView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return self.request.user
