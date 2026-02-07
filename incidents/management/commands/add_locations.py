from django.core.management.base import BaseCommand
from incidents.models import Location


class Command(BaseCommand):
    help = "Populate the Location table with 50 Halifax businesses"

    def handle(self, *args, **kwargs):
        business_names = [
            "Sobeys Halifax Store {}",
            "Canadian Tire Halifax {}",
            "Walmart Halifax {}",
            "Superstore Halifax {}",
            "No Frills Halifax {}",
            "Shoppers Drug Mart Halifax {}",
            "Home Depot Halifax {}",
            "Lowe's Halifax {}",
            "Costco Halifax {}",
            "Best Buy Halifax {}",
            "The Brick Halifax {}",
            "Tim Hortons Halifax {}",
            "McDonald's Halifax {}",
            "Starbucks Halifax {}",
            "PetSmart Halifax {}",
            "Dollarama Halifax {}",
            "Farmers Market Halifax {}",
            "RONA Halifax {}",
            "Indigo Halifax {}",
            "The Source Halifax {}",
        ]

        total_locations = 50
        count = 0

        for i in range(total_locations):
            # Cycle through the list of business name templates
            template = business_names[i % len(business_names)]
            store_number = (i // len(business_names)) + 1
            name = template.format(store_number)

            # Create Location instance
            Location.objects.create(location=name)
            count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully added {count} locations."))
