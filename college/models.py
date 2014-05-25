from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm



ACCREDITED_CHOICES = (
    ('1', 'Yes'),
    ('0', 'No'),
)

STATE_CHOICES = (
      ('AP' , 'Andhra Pradesh'), (
      'AR' , 'Arunachal Pradesh'), (
      'AS' , 'Assam'), (
      'BR' , 'Bihar'), (
      'CT' , 'Chhattisgarh'), (
      'GA' , 'Goa'), (
      'GJ' , 'Gujarat'), (
      'HR' , 'Haryana'), (
      'HP' , 'Himachal Pradesh'), (
      'JK' , 'Jammu & Kashmir'), (
      'JH' , 'Jharkhand'), (
      'KA' , 'Karnataka'), (
      'KL' , 'Kerala'), (
      'MP' , 'Madhya Pradesh'), (
      'MH' , 'Maharashtra'), (
      'MN' , 'Manipur'), (
      'ML' , 'Meghalaya'), (
      'MZ' , 'Mizoram'), (
      'NL' , 'Nagaland'), (
      'OR' , 'Odisha'), (
      'PB' , 'Punjab'), (
      'RJ' , 'Rajasthan'), (
      'SK' , 'Sikkim'), (
      'TN' , 'Tamil Nadu'), (
      'TG' , 'Telangana'), (
      'TR' , 'Tripura'), (
      'UK' , 'Uttarakhand'), (
      'UP' , 'Uttar Pradesh'), (
      'WB' , 'West Bengal'), (
      'AN' , 'Andaman & Nicobar'), (
      'CH' , 'Chandigarh'),
      ('DN' , 'Dadra and Nagar Haveli'),
      ('DD' , 'Daman & Diu'),
      ('DL' , 'Delhi'),
      ('LD' , 'Lakshadweep'),
      ('PY' , 'Puducherry'),
)

LOCATION_CHOICES = (
    ('City', 'A city'),
    ('Town', 'A town'),
    ('CO', 'Outskirts of a city'),
    ('TO', 'Outskirts of a town'),
    ('NUA', 'A non urban area'),
)


class Leadership (models.Model):
    name_company = models.CharField(max_length=100)
    name_founder = models.CharField(max_length=40)
    year_trust = models.IntegerField(max_length=4)
    month_college = models.CharField(max_length=10)
    year_college = models.IntegerField(max_length=4)


class Recognition(models.Model):
    course_name = models.CharField(max_length=100)
    type_approval = models.CharField(max_length=100)
    easyness = models.TextField()
    criteria = models.TextField()

class Accreditation(models.Model):
    year_rating = models.IntegerField(max_length=4)
    rating = models.CharField(max_length=10)
    rating_body = models.CharField(max_length=100)

class Award(models.Model):
    name_award = models.CharField(max_length=100)
    awarding_body = models.CharField(max_length=100)
    year_award = models.IntegerField(max_length=4)


class College(models.Model):
    name = models.CharField("College Name", max_length=100)
    street_address_1 = models.CharField(max_length=100, blank=True, null=True)
    street_address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True, choices=STATE_CHOICES)
    pincode = models.IntegerField(max_length=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=31, decimal_places=28, null=True, blank=True,
                                   validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.DecimalField(max_digits=32, decimal_places=28, null=True, blank=True,
                                    validators=[MaxValueValidator(180), MinValueValidator(-180)])
    email = models.EmailField()
    telephone = models.CharField(max_length=12)
    principal_name = models.CharField(max_length=40)
    principal_number = models.CharField(max_length=12)
    respondent_name = models.CharField(max_length=40)
    respondent_designation = models.CharField(max_length=40)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    leaderships = models.ManyToManyField(Leadership)
    recognition = models.ManyToManyField(Recognition)
    college_accreditated = models.CharField(max_length=10, choices=ACCREDITED_CHOICES)
    accreditations = models.ManyToManyField(Accreditation)
    awards = models.ManyToManyField(Award)
    campus_size = models.CharField(max_length=20)
    builtup_area = models.CharField(max_length=20)
    distance_railway = models.CharField(max_length=20)
    distance_bus = models.CharField(max_length=20)
    number_labs = models.IntegerField(max_length=3)
    boys_hostel = models.FloatField(max_length=5)
    girls_hostel = models.FloatField(max_length=5)
    playground = models.CharField(max_length=10, choices=ACCREDITED_CHOICES)
    number_sport_centers = models.IntegerField(max_length=3)
    transport_facility = models.CharField(max_length=10, choices=ACCREDITED_CHOICES)
    number_buses = models.IntegerField(max_length=3)
    number_mini_buses = models.IntegerField(max_length=3)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class CollegeForm(ModelForm):
    class Meta:
        model = College
