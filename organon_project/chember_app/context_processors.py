from .models import DoctorInfo


def doctor_info(request):
    doctor_info = DoctorInfo.objects.all()
    return {'doctor_info' : doctor_info}
