from django import forms
from .models import Form, Course


class FormsForm(forms.ModelForm):
    class Meta:
        model=Form
        fields = '__all__'
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'courses': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'purpose': forms.Select(attrs={'class': 'form-control'}),
            'material_provided': forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        GENDER_CHOICES = [
            ('male', 'Male'),
            ('female', 'Female'),
        ]

        gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)



    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['courses'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['courses'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['courses'].queryset = self.instance.department.course_set.order_by('name')