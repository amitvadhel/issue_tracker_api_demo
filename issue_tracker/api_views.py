from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from issue_tracker.serializers import BugSerializer
from issue_tracker.models import Bug


class BugViewset(viewsets.ModelViewSet):
    """
    Create, update, delete, select Bug
    """
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    filterset_fields = ('status', )  # filter


class StatusPartialUpdateView(APIView):
    """
    Partial update for bug status
    URL:
        /api/v1/issue/status/<id>/?status=unresolved
        /api/v1/issue/status/<id>/?status=resolved
    """
    def patch(self, request, pk):
        issue_status = self.request.query_params.get('status')
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Bug, pk=pk)
        # this is the only field we want to update
        data = {'status': issue_status}
        serializer = BugSerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
