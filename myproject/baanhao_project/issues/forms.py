from django import forms
from .models import Complaint, Maintenance
from users.models import Resident, Technician 

class ComplaintForm(forms.ModelForm):
    # เพิ่ม Field ให้เลือก Resident ได้ (สำหรับ Admin)
    reporter = forms.ModelChoiceField(
        queryset=Resident.objects.all(),
        empty_label="Select Resident...",
        widget=forms.Select(attrs={'class': 'form-select rounded-3'})
    )

    class Meta:
        model = Complaint
        fields = ['title', 'description', 'location', 'evidence_image', 'reporter', 'priority', 'category']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control rounded-3', 'placeholder': 'e.g. ไฟถนนหลอดขาด'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-3', 'rows': 6, 'placeholder': 'รายละเอียดของปัญหา...'}),
            'location': forms.TextInput(attrs={'class': 'form-control rounded-3', 'placeholder': 'e.g. Zone A, 100/12, Gym'}),
            'evidence_image': forms.FileInput(attrs={'class': 'd-none', 'id': 'fileInput'}), # ซ่อน input ไว้แล้วใช้ JS หรือ Label ครอบ
            'priority': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'category': forms.Select(attrs={'class': 'form-select rounded-3'}),
        }

class MaintenanceForm(forms.ModelForm):
    reporter = forms.ModelChoiceField(
        queryset=Resident.objects.all(),
        empty_label="Select Resident...",
        widget=forms.Select(attrs={'class': 'form-select rounded-3'})
    )
    
    technician = forms.ModelChoiceField(
        queryset=Technician.objects.all(),
        required=False, # อาจจะยังไม่ assign ตอนสร้างก็ได้
        empty_label="-- Select Technician --",
        widget=forms.Select(attrs={'class': 'form-select rounded-3'})
    )

    class Meta:
        model = Maintenance
        fields = ['title', 'description', 'location', 'before_image', 'reporter', 'priority', 'technician', 'appointment_date']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-3', 'rows': 6}),
            'location': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'before_image': forms.FileInput(attrs={'class': 'd-none', 'id': 'fileInput'}),
            'priority': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control rounded-3', 'type': 'datetime-local'}),
        }