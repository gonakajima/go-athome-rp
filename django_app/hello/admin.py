from django.contrib import admin
from .models import Friend,Distance,Patient,PatientNeed,Service,ServiceAttr,ServicePost

# Register your models here.
admin.site.register(Friend)
admin.site.register(Distance)
admin.site.register(Patient)
admin.site.register(PatientNeed)
admin.site.register(Service)
admin.site.register(ServiceAttr)
admin.site.register(ServicePost)
