from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField


annual = 'annual'
bounce = 'bounce'
no_paid_vacation = 'no_paid'

LEAVE_CHOICES = (
    (annual, _('Annual Leave')),
    (bounce, _('Bounce Leave')),
    (no_paid_vacation, _('No Paid Vacation'))
)

in_review = 'in_review'
approved = 'approved'
declined = 'declined'

LEAVE_STATUSES = (
    (in_review, ('In Review')),
    (approved, ('Approved')),
    (declined, ('Declined')),
)


class Users(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")
    team = models.ManyToManyField('self', blank=True, null=True, related_name='selected_by_users')
    editable = models.BooleanField(default=False, null=True)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class DayOff(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    off_type = models.CharField(max_length=10, choices=LEAVE_CHOICES, null=True)
    dayoff_reason = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=10, choices=LEAVE_STATUSES, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.dayoff_reason
    