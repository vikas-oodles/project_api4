from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth import get_user_model
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
    date_of_birth = serializers.DateField(
        default= timezone.now().date(),
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
        