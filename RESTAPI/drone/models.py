from django.db import models


class Common(models.Model):

    name = models.CharField(("name"), max_length=250,
                            default='', blank=False, unique=True)
    inserted_timestamp = models.DateTimeField(
        auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class DroneCategory(Common):

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Drone(Common):
    drone_category = models.ForeignKey(
        DroneCategory,
        verbose_name=(
            "verbose_drone"
        ),
        related_name='drones',
        on_delete=models.CASCADE)

    manufacturing_date = models.DateField(("m_dates"))
    has_it_competed = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Pilot(Common):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICE = ((MALE, 'M'), (FEMALE, 'F'),)

    race_count = models.IntegerField()
    gender = models.CharField(
        choices=GENDER_CHOICE,
        max_length=2, default="MALE"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Competition(Common):
    pilot = models.ForeignKey(
        Pilot, on_delete=models.CASCADE, related_name='competitions')
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)

    distance_in_feet = models.IntegerField()
    distance_achivement_date = models.DateField()

    class Meta:
        ordering = ("-distance_in_feet",)

    def __str__(self):
        return self.name
