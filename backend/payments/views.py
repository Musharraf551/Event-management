from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer

class CreateBookingView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Later we will add Stripe/Razorpay payment integration here
