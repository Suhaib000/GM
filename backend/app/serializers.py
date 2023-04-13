# serializers.py
from rest_framework import serializers
from .models import PostJob ,AppliedJob,Profile
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserTable
#         fields = ('username', 'password', 'usertype')
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id",'about_you', 'usertype')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer() # nested serializer for profile fields

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class PostJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJob
        fields = ("id",'jop_name', 'jop_discription','user','student_skills',"job_type","created_at",'job_pay_type')

class AppliedJobSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = AppliedJob
        fields = '__all__'
    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = User.objects.create(**user_data)
    #     applied_job = AppliedJob.objects.create(user=user, **validated_data)
    #     return applied_job




# class UserSerializer(serializers.ModelSerializer):
#     profile = PostJobSerializer(required=True)
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

#     def create(self, validated_data):

#         # create user 
#         user = User.objects.create(
#             username = validated_data['username'],
#             email = validated_data['email'],
#             password=validated_data['password'],
#         )

#         profile_data = validated_data.pop('profile')
#         # create profile
#         profile = Profile.objects.create(
#             user = user,
#             About_you = profile_data['About_you'],
#             usertype = profile_data['usertype'],
#         )

#         return user
    

# class SignupSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=254)
#     password = serializers.CharField(max_length=128)

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100)
#     password = serializers.CharField(max_length=128)

# class PostJobSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostJob
        
#         fields = ("id",'jop_name', 'jop_discription','user_id','student_skills')


