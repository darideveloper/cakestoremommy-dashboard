"""Upload to db and media source the images in local
media/content_gallery_images/*/*.*"""

import os

from django.core.management.base import BaseCommand

from django.conf import settings
from content import models

BASE_FILE = os.path.basename(__file__)


class Command(BaseCommand):
    help = "Upload local gallery images to DB and remote media storage"

    def handle(self, *args, **kwargs):

        images_folder = os.path.join(
            settings.BASE_DIR, "temp_media", "content_gallery_images"
        )

        # Loop subfolder and images
        for subfolder in os.listdir(images_folder):
            subfolder_path = os.path.join(images_folder, subfolder)

            # Loop images
            for image_file in os.listdir(subfolder_path):
                image_path = os.path.join(subfolder_path, image_file)

                with open(image_path, "rb") as img_data:
                    # Create a new Image object
                    gallery_image = models.GalleryImage.objects.create(
                        description=f"{subfolder} image",
                    )

                    # Add image
                    file_name = f"{subfolder}_{image_file}"
                    gallery_image.image.save(file_name, img_data, save=True)

                    # get and add category
                    category = models.Category.objects.get(name=subfolder)
                    gallery_image.categories.add(category)
                    gallery_image.save()

                    print(f"Image '{file_name}' uploaded to category '{category}'")
