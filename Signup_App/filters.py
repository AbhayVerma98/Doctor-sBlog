from django.contrib.auth.models import User

from Signup_App.models import BlogModel
import django_filters
from django import forms


class BlogFilterForm_filter(django_filters.FilterSet):
    class Meta:
        model = BlogModel
        fields = ['category']


'''
class GeeksForm_filter(django_filters.FilterSet):
    class Meta:
        model = GeeksModel
        fields = [
            "title", "description",
        ]


class PlasmaDonerForm_filter(django_filters.FilterSet):
    class Meta:
        model = PlasmaDonor
        fields = '__all__'


class BloodDonerForm_filter(django_filters.FilterSet):
    class Meta:
        model = BloodDonor
        fields = '__all__'


class OxygenForm_filter(django_filters.FilterSet):
    class Meta:
        model = OxygenServiceProvider
        fields = '__all__'


class OtherServicesForm_filter(django_filters.FilterSet):
    class Meta:
        model = OtherServiceProvider
        fields = '__all__'


class MedicalForm_filter(django_filters.FilterSet):
    class Meta:
        model = MedicalServiceProvider
        fields = '__all__'
'''
