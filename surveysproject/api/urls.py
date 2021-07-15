from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (SurveyViewSet, QuestionViewSet, AnswerViewSet,
                    SurveyInstanceViewSet, CustomerViewSet)

router_v1 = DefaultRouter()
router_v1.register(r'survey', SurveyViewSet, basename='survey')
router_v1.register(
    r'survey/(?P<survey_id>[\d]+)/questions', QuestionViewSet,
    basename='question'
)
router_v1.register(
    r'questions/(?P<survey_id>[\d]+)/answers',
    AnswerViewSet, basename='answers'
)
router_v1.register(r'instance', SurveyInstanceViewSet, basename='instance')
router_v1.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
