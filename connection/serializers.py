from django.contrib.auth import authenticate, user_logged_in
from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import ConnectionUserProfile, Connections
import django_filters
import calendar
from rest_auth.models import TokenModel



class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """
    success = serializers.SerializerMethodField()
    msg = serializers.SerializerMethodField()

    def get_msg(self,instance):
        return "Login successfully"

    def get_success(self,instance):
        Connections.objects.create(user_id=instance.user_id)
        return "true"

    class Meta:
        model = TokenModel
        fields = ('key', 'user_id','msg', 'success')   # there I add the `user` field ( this is my need data ).


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
    token= serializers.SerializerMethodField()
    mobile= serializers.SerializerMethodField()
    connections= serializers.SerializerMethodField()

    def get_connections(self,instance):
        try:
            conncount = Connections.objects.filter(user_id=instance.id).count()
            return conncount
        except Exception as e:
            print(e)


    def get_token(self,instance):
        token=TokenModel.objects.filter(user=instance).values_list('key', flat=True)
        for tk in token:
            return tk

    def get_fullname(self,instance):
        return str(instance.first_name)+" "+str(instance.last_name)

    def get_gender(self,instance):

    	gender=ConnectionUserProfile.objects.filter(user=instance.id).values_list('gender', flat=True)

    	for gn in gender:
    		return gn

    def get_mobile(self,instance):

    	phonenumber=ConnectionUserProfile.objects.filter(user=instance.id).values_list('phone_number', flat=True)

    	for pn in phonenumber:
    		return pn


    def get_graph(self,instance):
        try:
            conn = Connections.objects.filter(user_id=instance.id).values_list('created_at__month').annotate(total_user_id=Count('user_id')).order_by('created_at__month')
            connlist=[]
            maindict=[]
            for cn in conn:
                connlist.append(list(cn))
            count=1
            for cl in connlist:
                conndict={}
                conndict["month"]=calendar.month_name[cl[0]]
                conndict["value"]=cl[1]
                conndict["user_id"]=instance.id
                conndict["id"]=count
                count=count+1
                maindict.append(conndict)
            return maindict
        except Exception as e:
            print(e)

    class Meta:
        model = User
        fields = ('__all__')
