import csv
import os
import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from incidents.models import Location, Shift


class Command(BaseCommand):
    help = "Create shifts for all locations based on shifts.csv shift names"

    def handle(self, *args, **kwargs):
        # Path to your shifts.csv
        csv_path = os.path.join("shifts.csv")  # Adjust as needed

        # Load all users
        users = list(User.objects.all())
        if not users:
            self.stdout.write(
                self.style.ERROR("No users found. Please add users first.")
            )
            return

        # Load all locations from the database
        locations = list(Location.objects.all())
        if not locations:
            self.stdout.write(self.style.ERROR("No locations found in the database."))
            return

        # Load shift names from CSV
        shift_names = set()
        with open(csv_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                shift_name = row["name"].strip()
                shift_names.add(shift_name)

        total_shifts_created = 0
        # For each location, create all shifts from shift_names
        for location in locations:
            for shift_name in shift_names:
                # Check if this shift-location-shift_name already exists
                if not Shift.objects.filter(
                    shift=shift_name, location=location
                ).exists():
                    employee = random.choice(users)
                    Shift.objects.create(
                        shift=shift_name, employee=employee, location=location
                    )
                    total_shifts_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {total_shifts_created} new shifts across {len(locations)} locations."
            )
        )
