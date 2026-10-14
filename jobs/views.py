from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Job, Application
from .serializers import (
    JobSerializer,
    RegisterSerializer,
    ApplicationSerializer
)


class JobListView(APIView):

    def get(self, request):
        jobs = Job.objects.all()

        serializer = JobSerializer(
            jobs,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class JobDetailView(APIView):

    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)

        except Job.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = JobSerializer(job)

        return Response(serializer.data)

    def put(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)

        except Job.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = JobSerializer(
            job,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)

        except Job.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = JobSerializer(
            job,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)

        except Job.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        job.delete()

        return Response(
            {"message": "Job deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Registration successful"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ApplicationListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        applications = Application.objects.filter(
            user=request.user
        ).select_related("job")

        serializer = ApplicationSerializer(
            applications,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        job_id = request.data.get("job")

        if Application.objects.filter(
            user=request.user,
            job_id=job_id
        ).exists():

            return Response(
                {
                    "error": "You have already applied for this job."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ApplicationSerializer(
            data=request.data
        )

        if serializer.is_valid():
            application = serializer.save(
                user=request.user
            )

            return Response(
                ApplicationSerializer(application).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
