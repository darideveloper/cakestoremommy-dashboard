"""Save all images to recalculate width and height"""

import os

from django.core.management.base import BaseCommand

from content import models

BASE_FILE = os.path.basename(__file__)


class Command(BaseCommand):
    help = "Upload local gallery images to DB and remote media storage"

    def handle(self, *args, **kwargs):

        images = models.GalleryImage.objects.all()
        for image in images:
            if image.image:
                # Save the image to recalculate width and height
                image.save()
                message = (
                    f"Image '{image.description}' saved with new dimensions: "
                    f"{image.width} x {image.height}"
                )
                print(message)
            else:
                print(f"Image '{image.description}' has no image file associated.")
