from django.db import models

from PIL import Image as PILImage


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Nombre de la categoría"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]


class GalleryImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="gallery_images/", verbose_name="Imagen")
    description = models.TextField(
        blank=True, null=True, verbose_name="Descripción (text alternativo)"
    )
    categories = models.ManyToManyField(
        Category, related_name="gallery_images", verbose_name="Categoría"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    width = models.PositiveIntegerField(editable=False, null=True, blank=True)
    height = models.PositiveIntegerField(editable=False, null=True, blank=True)
    
    def __str__(self):
        return self.description if self.description else f"Image {self.id}"

    class Meta:
        verbose_name = "Imagen de Galería"
        verbose_name_plural = "Imágenes de Galería"
        ordering = ["-created_at"]
        
    def save(self, *args, **kwargs):
        if self.image:
            img = PILImage.open(self.image)
            self.width, self.height = img.size
        super().save(*args, **kwargs)