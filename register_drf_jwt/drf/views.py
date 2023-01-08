from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import generics,status
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import *

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class TestJWTView(generics.ListCreateAPIView):
    queryset = TestFieldsForJwt.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TestForJWTSerializer

    
class VerifyUser(generics.CreateAPIView):
    # queryset = UserProfile.objects.all()
    serializer_class = VerifyAccountSerializer
    def post(self,request):
        data = request.data
        serializer = VerifyAccountSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data['email']
            otp = serializer.data['otp']
            user = User.objects.filter(email = email)

            if not user.exists():
                return Response({
                    'status':400,
                    'message':'wrong',
                    'data':'invalid email'
                })
            if user[0].otp != otp:
                return Response({
                    'status':400,
                    'message':'wrong',
                    'data':'invalid OTP'
                })
            user = user.first()
            user.is_verified = True
            user.save()

            return Response({
                    'status':200,
                    'message':'good verifield',
                    'data':serializer.data
                }) 