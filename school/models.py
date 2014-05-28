from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm

CLASS_CHOICES = (
    ('0', 'Pre-School'),            
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
    ('Private aided by government', 'Private aided by government'),
    ('Private Unaided', 'Private Unaided'),
    ('Government', 'Government'),
    ('Religious', 'Religious'),
    ('Special School', 'Special Needs School'),
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
    name = models.CharField("School Name*", max_length=100)
    lowest_class = models.CharField("Lowest Class*", max_length=10, choices=CLASS_CHOICES)
    highest_class = models.CharField("Highest Class*", max_length=10, choices=CLASS_CHOICES)
    recognized = models.CharField("Recognized ?*", max_length=10, choices=RECOGNIZED_CHOICES)
    management_type = models.CharField("Management Type*", max_length=100, choices=TYPE_CHOICES, help_text="Select Management Type")
    teacher_strength = models.IntegerField("Teacher Strength", max_length=10, blank=True, null=True)
    student_strength = models.IntegerField("Student Strength", max_length=10, blank=True, null=True)
    medium_of_instruction = models.CharField("Medium of Instruction*", max_length=100, choices=LANGUAGE_CHOICES)
    other_language = models.CharField("Other Language", max_length=20, null=True, blank=True)
    min_fee = models.IntegerField("Minimum Monthly Fee", max_length=6, null=True, blank=True, help_text="Enter only numbers without comma or rupee symbol")
    max_fee = models.IntegerField("Maximum Monthly Fee", max_length=6, null=True, blank=True, help_text="Enter only numbers without comma or rupee symbol")
    establishment = models.IntegerField("Year of Establishment* (YYYY)", max_length=4)
    recognition = models.IntegerField("Year of Recognition* (YYYY)", max_length=4)
    image = models.ImageField("School Photo", upload_to='school', null=True, blank=True)
    street_address_1 = models.CharField("Street Address 1", max_length=100, blank=True, null=True)
    street_address_2 = models.CharField("Street Address 2", max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True, choices=STATE_CHOICES, help_text='Select State')
    pincode = models.IntegerField(max_length=6, null=True, blank=True)
    email = models.EmailField("E-Mail", null=True, blank=True)
    phone_number = models.IntegerField("Phone Number", max_length=12, null=True, blank=True, help_text='STD code- phone number/ Mobile number')
    latitude = models.DecimalField(max_digits=31, decimal_places=28, null=True, blank=True,
                                   validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.DecimalField(max_digits=32, decimal_places=28, null=True, blank=True,
                                    validators=[MaxValueValidator(180), MinValueValidator(-180)])
    

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    class Meta:
        unique_together = ('name', 'street_address_1', 'street_address_2', 'pincode')

class SchoolForm(ModelForm):
    class Meta:
        model = School
