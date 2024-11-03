from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class RoleCheckView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        allowed_roles = ['admin', 'moderator']

        if request.user.is_authenticated:
            if request.user.role in allowed_roles:
                return Response({'detail': 'Access granted to your role.'}, status=200)
            else:
                return Response({'detail': 'Access denied.'}, status=403)
        else:
            return Response({'detail': 'Unauthorized. Please provide a valid token.'}, status=401)
