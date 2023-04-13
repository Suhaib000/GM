from rest_framework import generics ,viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PostJob ,AppliedJob
from .serializers import UserSerializer ,PostJobSerializer ,AppliedJobSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def filter_user(self, request):
        username = request.GET.get('username', None)

        queryset = User.objects.all()
        if username is not None:
            queryset = queryset.filter(username=username)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

# class LoginView(ObtainAuthToken):
    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data,
    #         context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     token, created = Token.objects.get_or_create(user=user)
    #     return Response({'token': token.key})
# class LoginView(APIView):

#     def post(self, request, format=None):
#         # get username and password from request data
#         username = request.data.get('username')
#         password = request.data.get('password')
#         usertype = request.data.get('usertype')
#         # authenticate user
#         user = authenticate(username=username, password=password )
#         if user is None:
#             return Response({'error': 'Invalid credentials'})
        
#         # generate token
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key,})

class PostJobViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer
    
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def user_filter(self, request, user_id=None):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ApplyJobViewSet(viewsets.ModelViewSet):

    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobSerializer

    @action(detail=False, methods=['get'], url_path='job/(?P<job_id>[^/.]+)')
    def job_filter(self, request, job_id=None):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(job_id=job_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



# class UserLoginAPIView(APIView):
#     def post(self, request, format=None):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         usertype = request.data.get('usertype')
#         user = UserTable.objects.filter(username=username, password=password, usertype=usertype).first()
#         if user:
#             # user = authenticate(username=username, password=password)
#             # login(request, user)
#             return Response({'message': 'Login successful' , "usertype":usertype})
#         else:
#             return Response({'message': 'Invalid credentials'})


# class UserRegistration(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'username': user.username, 'email': user.email}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from .serializers import SignupSerializer, LoginSerializer

# @api_view(['POST'])
# def signup(request):
#     serializer = SignupSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login_view(request):
#     serializer = LoginSerializer(data=request.data)
#     if serializer.is_valid():
#         user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'login success'}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserList(generics.ListCreateAPIView):
#     # permission_classes = (IsAuthenticatedOrWriteOnly,)
#     serializer_class = UserSerializer

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
