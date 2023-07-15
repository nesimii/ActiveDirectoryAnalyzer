# Create your views here.
from rest_framework import generics

from analyzer.neomodel.models import Group, User, Computer
from analyzer.neomodel.serializers import GroupSerializer, UserSerializer, ComputerSerializer


class GroupsListView(generics.ListAPIView):
    queryset = Group.nodes.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.nodes

    def get_object(self):
        distinguished_name = self.kwargs['distinguishedName']
        return self.get_queryset().get(distinguishedName=distinguished_name)


class UsersListView(generics.ListAPIView):
    queryset = User.nodes.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.nodes

    def get_object(self):
        distinguished_name = self.kwargs['distinguishedName']
        return self.get_queryset().get(distinguishedName=distinguished_name)


class ComputersListView(generics.ListAPIView):
    queryset = Computer.nodes.all()
    serializer_class = ComputerSerializer


class ComputerDetailView(generics.RetrieveAPIView):
    serializer_class = ComputerSerializer

    def get_queryset(self):
        return Computer.nodes

    def get_object(self):
        distinguished_name = self.kwargs['distinguishedName']
        return self.get_queryset().get(distinguishedName=distinguished_name)
