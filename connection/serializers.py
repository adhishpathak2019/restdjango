from django.contrib.auth import authenticate, user_logged_in
from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import ConnectionUserProfile, Connections
import django_filters
import calendar

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class UserListSerializer(serializers.ModelSerializer):

    graph = serializers.SerializerMethodField()
    gender= serializers.SerializerMethodField()
    fullname= serializers.SerializerMethodField()

    def get_fullname(self,instance):
        return str(instance.first_name)+str(instance.last_name)

    def get_gender(self,instance):

    	gender=ConnectionUserProfile.objects.filter(user=instance.id).values_list('gender', flat=True)

    	for gn in gender:
    		return gn

    def get_phonenumber(self,instance):

    	phonenumber=ConnectionUserProfile.objects.filter(user=instance.id).values_list('phone_number', flat=True)

    	for pn in phonenumber:
    		return pn


    def get_graph(self,instance):
        try:
            conn = Connections.objects.filter(user_id=instance.id).values_list('created_at__month').annotate(total_user_id=Count('user_id'))
            conndict={}
            connlist=[]
            count=1
            for cn in conn:
                connlist=list(cn)
                conndict["month"]=calendar.month_name[connlist[0]]
                conndict["value"]=connlist[1]
                conndict["user_id"]=instance.id
                conndict["id"]=count
                count=count+1
            return conndict

        except Exception as e:
            print(e)

    class Meta:
        model = User
        fields = ('__all__')
