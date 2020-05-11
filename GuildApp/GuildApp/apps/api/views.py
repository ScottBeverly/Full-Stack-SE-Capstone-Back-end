from apps.api.models import Role, Class, Difficulty, Boss, Player
from apps.api.serializers import RoleSerializer, ClassSerializer, DifficultySerializer, BossSerializer, PlayerSerializer
from rest_framework import generics

class RoleListCreateView(generics.ListCreateAPIView):


    queryset = Role.objects.all()

    serializer_class = RoleSerializer
    def perform_create(self, serializer):

        serializer.save()

class RoleDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Role.objects.all()

    serializer_class = RoleSerializer



class CreateClassView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def perform_create(self, serializer):
        serializer.save()

class ClassDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer



class DifficultyListCreateView(generics.ListCreateAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
    def perform_create(self, serializer):

        serializer.save()

class DifficultyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer




class CreateBossView(generics.ListCreateAPIView):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer

    def perform_create(self, serializer):
        serializer.save()

class BossDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer



class CreatePlayerView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def perform_create(self, serializer):
        serializer.save()

class PlayerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


