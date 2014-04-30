from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm

CLASS_CHOICES = (
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third'),
    ('4', 'Fourth'),
    ('5', 'Fifth'),
    ('6', 'Sixth'),
    ('7', 'Seventh'),
    ('8', 'Eighth'),
    ('9', 'Nineth'),
    ('10', 'Tenth'),
    ('11', 'Eleventh'),
    ('12', 'Twelth'),
)

RECOGNIZED_CHOICES = (
    ('1', 'Yes'),
    ('0', 'No'),
)
TYPE_CHOICES = (
    ('Government Aided', 'Government Aided'),
    ('Private', 'Private'),
    ('Government', 'Government'),
    ('Religious', 'Religious'),
    ('Special School', 'Special School'),
)
LANGUAGE_CHOICES = (
    ('English','English'),
    ('Hindi','Hindi'),
    ('Mix English and Hindi','Mix English and Hindi'),
    ('Urdu','Urdu'),
    ('Gujarati','Gujarati'),
    ('Tamil','Tamil'),
    ('Telugu','Telugu'),
    ('Kannad','Kannad'),
    ('Punjabi','Punjabi'),
    ('Malayalam','Malayalam'),
    ('Marathi','Marathi'),
    ('Bengali','Bengali'),
    ('Oriya','Oriya'),
    ('Assamese','Assamese'),
    ('Other','Other'),
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

class School(models.Model):
    name = models.CharField(max_length=100)
    lowest_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    highest_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    recognized = models.CharField(max_length=10, choices=RECOGNIZED_CHOICES)
    management_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    medium_of_instruction = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    image = models.ImageField(upload_to='school', null=True, blank=True)
    street_address_1 = models.CharField(max_length=500, blank=True, null=True)
    street_address_2 = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True, choices=STATE_CHOICES)
    pincode = models.IntegerField(max_length=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=31, decimal_places=28, null=True, blank=True,
                                   validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.DecimalField(max_digits=32, decimal_places=28, null=True, blank=True,
                                    validators=[MaxValueValidator(180), MinValueValidator(-180)])
    

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class SchoolForm(ModelForm):
    class Meta:
        model = School
