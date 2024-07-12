from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


USER_TYPE =( 
    ('Freelancer','Freelancer'),
    ('Clients','Clients'),
)

class RegistrationSerialzers(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=USER_TYPE)
    confirm_password = serializers.CharField(required = True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'password', 'confirm_password']


    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        user_type = self.validated_data['user_type']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name, user_type = user_type)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account

