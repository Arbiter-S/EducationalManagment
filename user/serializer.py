from rest_framework import serializers

import django_filters

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")

    class Meta:
        model = Student
        fields = "__all__"


class StudentFilterSet(django_filters.FilterSet):
    user_first_name = django_filters.CharFilter(field_name="user__first_name", lookup_expr="icontains")
    user_last_name = django_filters.CharFilter(field_name="user__last_name", lookup_expr="icontains")
    user_user_code = django_filters.CharFilter(field_name="user__user_code", lookup_expr="icontains")
    user_national_code = django_filters.CharFilter(field_name="user__national_code", lookup_expr="icontains")

    class Meta:
        model = Student
        fields = ["major", "department", "is_soldier"]


class ProfessorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")

    class Meta:
        model = Professor
        fields = "__all__"


class EducationalAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalAssistant
        fields = "__all__"


class ProfessorFilterSet(django_filters.FilterSet):
    user_first_name = django_filters.CharFilter(field_name="user__first_name", lookup_expr="icontains")
    user_last_name = django_filters.CharFilter(field_name="user__last_name", lookup_expr="icontains")
    user_user_code = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    user_national_code = django_filters.CharFilter(field_name="user__national_code", lookup_expr="icontains")

    class Meta:
        model = Professor
        fields = ["major", "department"]


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['user']


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "national_code", "phone_number", "gender", "birth_date",
                  "role"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "national_code", "phone_number", "gender", "birth_date"]


class EducationalAssistantFilterSet(django_filters.FilterSet):
    user_first_name = django_filters.CharFilter(field_name="user__first_name", lookup_expr="icontains")
    user_last_name = django_filters.CharFilter(field_name="user__last_name", lookup_expr="icontains")
    user_user_code = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    user_national_code = django_filters.CharFilter(field_name="user__national_code", lookup_expr="icontains")

    class Meta:
        model = EducationalAssistant
        fields = ["major", "department"]
