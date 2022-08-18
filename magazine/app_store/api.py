from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions

from .models import Items
from .serializers import UserSerializer, GroupSerializer, ItemsSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


class ItemsList(generics.ListAPIView):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Items.objects.prefetch_related('review').all()
        form = self.request.query_params.get('choices')
        if form is not None:
            queryset = queryset.order_by(form)
        return queryset
