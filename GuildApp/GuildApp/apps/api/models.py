from django.db import models

class Role(models.Model):
    role = models.CharField(max_length=200)



    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.role



class Class(models.Model):
    class_name = models.CharField(max_length=90)
    class_description = models.CharField(max_length=255)
    class_spec = models.CharField(max_length=55)
    class_race = models.CharField(max_length=55)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
            verbose_name = "Class"
            verbose_name_plural = "Classes"

    def __str__(self):
            return self.class_name



class Difficulty(models.Model):
    difficulty = models.CharField(max_length=50)



    class Meta:
        verbose_name = "difficulty"
        verbose_name_plural = "difficulties"

    def __str__(self):
        return self.difficulty




class Boss(models.Model):
    boss_name = models.CharField(max_length=90)
    boss_description = models.CharField(max_length=500)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)

    class Meta:
            verbose_name = "boss"
            verbose_name_plural = "bosses"

    def __str__(self):
            return self.boss_name


class Player(models.Model):
    player_name = models.CharField(max_length=90)
    player_description = models.CharField(max_length=255)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    player_spec = models.CharField(max_length=55)
    player_race = models.CharField(max_length=55)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
            verbose_name = "Player"
            verbose_name_plural = "Players"

    def __str__(self):
            return self.player_name

