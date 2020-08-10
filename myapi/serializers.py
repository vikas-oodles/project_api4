from rest_framework import serializers
from rest_framework.validators import UniqueValidator



from django.core.exceptions import ValidationError
from django.db.models import Q
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils import timezone

UserModel = get_user_model()



class UserModelSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all())],
    )
    password = serializers.CharField(min_length=8, write_only=True)
    name = serializers.CharField(
        required=True,
    )
    phone_number = serializers.IntegerField(
        required=True,
        allow_null=True,
    )
    gender = serializers.CharField(
        default='Male',
        required=False,
    )
    date_of_birth = serializers.DateTimeField(
        default= timezone.now(),
        required=False,
    )

    def create_user(self,validated_data):
        user = UserModel.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
            phone_number = validated_data['phone_number'],
            gender = validated_data['gender'],
            date_of_birth = validated_data['date_of_birth'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta():
        model = UserModel
        fields = ('email','password','name','phone_number','gender','date_of_birth')
        

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self,data):
        email = data.get("email",None)
        password = data.get("password",None)
        if not email and not password:
            raise ValidationError("Details not entered")
        user = None

        if '@' in email:
            user = UserModel.objects.filter(
                Q(email=email) &
                Q(password=password)
            ).distinct()
            print(user)
            if not user.exists():
                raise ValidationError("User Credential are not correct1!")
            
            user = UserModel.objects.get(email=email)
        

        if user.ifLogged:
            raise ValidationError("user already logged in!")

        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta():
        model = UserModel
        fields = (
            'email',
            'password',
            'token',
        )