from .models import Course,Student
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"

        labels={
            "cid":"Course Id:",
            "cname":"Course Name:",
            "fees":"Course Fees:"
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

        labels={
            "course":"Course Name:",
            "sname":"Student Name:",
            "dob":"Date Of Birth:",
            "add":"Address:",
            "contact":"Contact"
        }
        widgets={
            "dob": forms.DateInput(attrs={"type":"date"}),
            "add": forms.Textarea(attrs={"placeholder":"Ex:- Pune, pin-000000","rows":3}),
        }