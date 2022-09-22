from dataclasses import fields
from rest_framework import serializers
from .models import *

class TlbMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TlbMembers
        fields=['id_member','member_name','status_memb','create_at']
        read_only_fields=('create_at',)

class TlbJobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TlbJobPosition
        fields=['id_position','desc_position']
        #read_only_fields=('',)   

class TlbStatusCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = TlbStatusCivil
        fields=['id_civilstatus','desc_civil']
        #read_only_fields=('',) 
        
class TlbMemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TlbMemberDetail
        fields=['detail_id','id_member','date_bith','direction','civil_status','dependents']
        #read_only_fields=('',)         

class TlbMemberEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TlbMemberEmail
        fields=['id_email','id_member','email']
        #read_only_fields=('',)                 

class TlbMemberJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = TlbMemberJob
        fields=['job_id','id_member','id_position','date_entry','direction','job_name']
        #read_only_fields=('',)            

class tlbmemberphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = tlb_member_phone
        fields=['id_contact','id_member','phone1','type_phone','status_fone']
        #read_only_fields=('',)      