from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Nombre de la categoría"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]


class GalleryImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="gallery_images/", verbose_name="Imagen")
    desciption = models.TextField(
        blank=True, null=True, verbose_name="Descripción (text alternativo)"
    )
    category = models.ManyToManyField(
        Category, related_name="gallery_images", verbose_name="Categoría"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desciption if self.desciption else f"Image {self.id}"

    class Meta:
        verbose_name = "Imagen de Galería"
        verbose_name_plural = "Imágenes de Galería"
        ordering = ["-created_at"]