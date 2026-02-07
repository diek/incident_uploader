import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from incidents.models import IncidentReport, Shift  # adjust import to your project


class Command(BaseCommand):
    help = "Create 30 fake retail security incident reports"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Faker.seed(123)

        shifts = list(Shift.objects.all())
        if not shifts:
            self.stdout.write(self.style.ERROR("No shifts found. Create shifts first."))
            return

        incident_templates = [
            "Suspect observed concealing merchandise and exiting without payment.",
            "Customer attempted to leave store with unpaid items; recovered at exit.",
            "Verbal altercation between customers required staff intervention.",
            "Suspicious individual loitering in high-theft area.",
            "Group distracted cashier while attempting to remove merchandise.",
            "Shoplifting incident involving cosmetics aisle.",
            "Individual fled when approached by loss prevention.",
            "Confrontation occurred near self-checkout area.",
            "Merchandise found abandoned in fitting room.",
            "Customer dispute escalated; security notified.",
        ]

        merchandise_items = [
            "cosmetics",
            "electronics accessories",
            "clothing",
            "designer handbags",
            "perfume",
            "razor blades",
            "over-the-counter medication",
            "shoes",
            "jewelry",
        ]

        created = 0

        for _ in range(30):
            is_theft = random.choice([True, False])
            multiple_people = random.choice([True, False]) if is_theft else False

            number_persons = random.randint(2, 4) if multiple_people else 1

            merchandise_cost = (
                Decimal(random.randint(10, 500))
                + Decimal(random.random()).quantize(Decimal("0.01"))
                if is_theft
                else None
            )

            incident = IncidentReport.objects.create(
                shift=random.choice(shifts),
                date_time_incident=fake.date_time_between(
                    start_date="-90d",
                    end_date="now",
                    tzinfo=timezone.get_current_timezone(),
                ),
                summary=random.choice(incident_templates),
                merchandise_cost=merchandise_cost,
                is_multiple_person=multiple_people,
                number_persons=number_persons,
                merchandise_description=random.choice(merchandise_items)
                if is_theft
                else "",
                is_theft=is_theft,
            )

            created += 1

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {created} incident reports.")
        )
