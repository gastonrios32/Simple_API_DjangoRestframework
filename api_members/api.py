from rest_framework import viewsets,permissions
from .models import *
from .serializers import *


class TlbMembersViewset(viewsets.ModelViewSet):
    queryset = TlbMembers.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  TlbMembersSerializer

class TlbJobPositionViewset(viewsets.ModelViewSet):
    queryset = TlbJobPosition.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  TlbJobPositionSerializer    

class TlbStatusCivilViewset(viewsets.ModelViewSet):
    queryset = TlbStatusCivil.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  TlbStatusCivilSerializer 
    
class TlbMemberDetailViewset(viewsets.ModelViewSet):
    queryset = TlbMemberDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  TlbMemberDetailSerializer    

class TlbMemberEmailViewset(viewsets.ModelViewSet):
    queryset = TlbMemberEmail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  TlbMemberEmailSerializer   

class TlbMemberJobViewset(viewsets.ModelViewSet):
    queryset = TlbMemberJob.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  TlbMemberJobSerializer   

class TlbMemberPhoneViewset(viewsets.ModelViewSet):
    queryset = tlb_member_phone.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  tlbmemberphoneSerializer   