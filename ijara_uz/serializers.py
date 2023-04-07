from rest_framework import serializers
from .models import CustomUser, User, Apartment, Jobs
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    city = serializers.ChoiceField(choices=[
        'Andijan', 'Bukhara', 'Jizzakh', 'Kashkadarya', 'Navoi', 'Namangan', 'Samarkand', 'Samarkand', 'Sirdarya',
        'Surkhandarya', 'Tashkent',
        'Fergana', 'Khorezm'])

    class Meta:
        model = CustomUser
        fields = ('phone', 'password', 'password2', 'first_name', 'last_name', 'city')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        custom_user = CustomUser.objects.create(
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            city=validated_data['city'],
        )

        custom_user.set_password(validated_data['password'])
        custom_user.save()

        user = User.objects.create(
            phone=custom_user,
            full_name=validated_data['first_name'] + ' ' + validated_data['last_name'],
            city=validated_data['city']
        )
        user.save()

        return custom_user


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(read_only=True)
    city = serializers.ChoiceField(choices=[
        'Andijan', 'Bukhara', 'Jizzakh', 'Kashkadarya', 'Navoi', 'Namangan', 'Samarkand', 'Samarkand', 'Sirdarya',
        'Surkhandarya', 'Tashkent',
        'Fergana', 'Khorezm'])

    class Meta:
        model = User
        fields = ['id', 'full_name', 'phone', 'pic', 'city']

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'full_name': obj.full_name,
            'pic': 'http://127.0.0.1:8000' + obj.pic.url,
            'phone': obj.phone.phone,
            'city': obj.city,
        }


class ApartmentSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    list_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class JobsSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    list_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Jobs
        fields = '__all__'
