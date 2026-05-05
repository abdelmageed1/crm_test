from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ['timestamp']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'manager_comments': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'lead_owner': 'المسؤول',
            'phone_number': 'رقم الهاتف',
            'client_code': 'كود العميل',
            'client_name': 'اسم العميل',
            'project_name': 'اسم المشروع',
            'date': 'التاريخ',
            'notes': 'الملاحظات',
            'status': 'الحالة',
            'email_address': 'البريد الإلكتروني',
            'type': 'النوع',
            'location': 'الموقع',
            'manager_comments': 'تعليقات المدير',
        }
