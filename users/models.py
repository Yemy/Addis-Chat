from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    Male = 'M'
    Female = 'F'
    Gender = [
        (Male, 'M'),
        (Female, 'F'),
    ]
    gender = models.CharField(max_length=1, choices=Gender, default="",)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
    date_registered = models.DateTimeField(default=timezone.now)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    class Meta:
        verbose_name_plural = "Profile"

    # for deleting prev profile pic
        # def save(self, *args, **kwargs):
        #     try:
        #         this = MyModelName.objects.get(id=self.id)
        #         if this.MyImageFieldName != self.MyImageFieldName:
        #             this.MyImageFieldName.delete(save=False)
        #     except: pass
        #     super(MyModelName, self).save(*args, **kwargs)

class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedBack = models.TextField()

    class Meta:
        verbose_name_plural = "FeedBack"


    def __str__(self):
        return self.feedBack

    # def get_absolute_url(self):
    #     return reverse('main-home')


class Issues(models.Model):
    reg = 'Registration'
    log = 'Login'
    profile = 'Profile'
    chgpass = "Changing Password"
    rstpass = "Resting Password"
    course = "Message"
    chapter = "Notification"
    topic = "Posts"
    other = "Other"

    types = [
        (reg, 'Registration'),
        (log, 'Login'),
        (profile, 'Profile'),
        (chgpass, "Changing Password"),
        (rstpass, "Reseting Password"),
        (course, "Message"),
        (chapter, "Notification"),
        (topic, "Posts"),
        (other, "Other"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=types, default="", help_text="choose Which one is not working for you?")
    issue = models.TextField(help_text="write your specific problems that you found.")

    class Meta:
        verbose_name_plural = "Issue"

    def __str__(self):
        return self.issue
