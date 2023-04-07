from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404, ListCreateAPIView, )
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ijara_uz.models import CustomUser, User, Apartment
from ijara_uz.permissions import IsOwnerOrReadOny
from ijara_uz.serializers import RegisterSerializer, UserSerializer, ApartmentSerializer


# Create your views here.
class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserListView(ListAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'phone'

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, phone='+' + kwargs['phone'])
        serializer = UserSerializer(get_object_or_404(User, phone=user), many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = get_object_or_404(CustomUser, phone='+' + kwargs['phone'])
        serializer = UserSerializer(get_object_or_404(User, phone=instance), data=request.data, partial=partial,
                                    many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ApartmentListCreateView(ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ApartmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (IsOwnerOrReadOny,)


@api_view(('GET',))
def search(request):
    print(request.GET)
    result = Apartment.objects.all()
    query = request.GET.get("query")
    for_men = request.GET.get("for_men")
    is_flat = request.GET.get("is_flat")
    contract = request.GET.get("contract")
    if not for_men:
        for_men = ''

    if not is_flat:
        is_flat = ''

    if not contract:
        contract = ''

    if query:
        result = result.filter(
            (Q(title__icontains=query) | Q(address__icontains=query) | Q(description__icontains=query) |
             Q(list_date__icontains=query) |
             Q(city__icontains=query)) & Q(for_men__icontains=for_men) & Q(is_flat__icontains=is_flat) &
            Q(contract__icontains=contract)
        ).distinct()
    serializer = ApartmentSerializer(result, many=True)
    return Response(serializer.data)
