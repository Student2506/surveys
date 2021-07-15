from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from surveys.models import Survey, Question, Answer, User, Customer, SurveyInstance
from .serializers import (AnswerSerializer, QuestionSerializer,
                          SurveySerializer, UserSerializer,
                          CustomerSerializer, SurveyISerializer)


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        survey_id = self.kwargs.get('survey_id')
        return get_object_or_404(Question, survey=survey_id)

    def perform_create(self, serializer):
        survey_id = self.kwargs.get('survey_id')
        survey = get_object_or_404(Survey, survey=survey_id)
        serializer.save(author=self.request.user, survey=survey)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        question_id = self.kwarg.get('question_id')
        new_queryset = get_object_or_404(Answer, pk=question_id)
        return new_queryset

    def perform_create(self, serializer):
        question_id = self.kwargs.get('question_id')
        question = get_object_or_404(Question, question=question_id)
        serializer.save(author=self.request.user, question=question)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
