from rest_framework import serializers
from apps.api.models import Role, Class, Difficulty, Boss, Player



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role', )


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'class_name', 'class_description', 'class_spec', 'class_race', 'role', )


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ('id', 'difficulty',)


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = ('id', 'boss_name', 'boss_description', 'difficulty',)

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'player_name', 'player_description', 'Class', 'player_spec', 'player_race', 'role',)


