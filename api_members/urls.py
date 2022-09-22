from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/member', TlbMembersViewset , 'member')
router.register('api/JobPosition', TlbJobPositionViewset , 'Job_position')
router.register('api/StatusCivil', TlbStatusCivilViewset , 'Status_Civil')
router.register('api/MemberDetail', TlbMemberDetailViewset , 'Member_Detail')
router.register('api/MemberEmail', TlbMemberEmailViewset , 'Member_Email')
router.register('api/MemberJob', TlbMemberJobViewset , 'Member_Job')
router.register('api/MemberPhone', TlbMemberPhoneViewset , 'Member_Phone')


urlpatterns = router.urls
