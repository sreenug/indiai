from django.contrib import admin
from college.models import Leadership, Recognition, Accreditation, Award, College


admin.site.register(College)
admin.site.register(Leadership)
admin.site.register(Recognition)
admin.site.register(Accreditation)
admin.site.register(Award)