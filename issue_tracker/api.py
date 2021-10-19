from rest_framework import routers
from issue_tracker import api_views

router = routers.DefaultRouter()
router.register(r'bug', api_views.BugViewset)
