from django import forms
from .models import Friend,Distance,Patient,PatientNeed,Service,ServiceAttr,ServicePost

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['address','mail','job','name']

class DistanceForm(forms.ModelForm):
    class Meta:
        model = Distance
        fields = ['start_id','target_id','x','y']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['need']

class PatientNeedForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['need']
        widgets = {
            'need': forms.CheckboxSelectMultiple
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = PatientNeed
        fields = ['status']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['attr']
        
class ServiceAttrForm(forms.ModelForm):
    class Meta:
        model = ServiceAttr
        fields = ['attributes']
        widgets = {
            'attributes': forms.CheckboxSelectMultiple
        }
        
class ServicePostForm(forms.ModelForm):
    class Meta:
        model = ServicePost
        fields = ['title','date','text','name']
        
