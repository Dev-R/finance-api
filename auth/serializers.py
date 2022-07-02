from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    '''Over riding '''
    User = get_user_model()
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())] #the type of email attribute is an EmailField and that it is required and should be unique amongst all User objects in our database.
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name') # Fields that our registration form is contains.
        # Extra validations with extra_kwargs option
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        '''
        Password fields must be same. We can validate these fields with serializers validate(self, attrs) method:
        '''
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        '''
        https://www.django-rest-framework.org/api-guide/serializers/#saving-instances
        When send POST request to register endpoint, it calls RegisterSerializer’s create method which saves user object.
        '''
        User = get_user_model()
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user