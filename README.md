# Cake Store Mommy Dashboard — Gallery API and Admin Panel

Backend for Cake Store Mommy: a Django REST API and admin panel that manages the bakery's gallery images and categories, consumed in real time by the landing page.

## Tech Stack

- **Django 4.2** — web framework
- **Django REST Framework** — read-only gallery and categories API
- **django-jazzmin** — customized admin interface with image previews
- **PostgreSQL** — database
- **Amazon S3** (django-storages + boto3) — image and static storage
- **Pillow** — automatic image dimension capture
- **Docker + Gunicorn** — deployment

## Features

- Read-only REST API: gallery images (category filter, pagination, ordering) and categories, protected with token authentication
- `GalleryImage` model that auto-captures width/height on save
- Customized Jazzmin admin: image thumbnails in lists and forms, category/date filters, description search
- Management commands: bulk image upload from folders, dimension recalculation, and seed category loading
- Unified error response envelope for all API exceptions
- Test suite: API view tests plus Selenium browser tests for the admin panel

## Setup

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# copy .env.dev and adjust DB/storage settings
python manage.py migrate
python manage.py apps_loaddata
python manage.py runserver
```

---

## Contact

Developed by [Dari Developer](https://darideveloper.com)

- 🌐 [darideveloper.com](https://darideveloper.com)
- 💬 [WhatsApp](https://api.whatsapp.com/send?phone=5214493402622)
- 📂 [View project in portfolio](https://darideveloper.com/portafolio/cakestoremommy)

---

# Cake Store Mommy Dashboard — API de Galería y Panel Administrativo

Backend de Cake Store Mommy: una API REST y panel administrativo en Django que gestiona las imágenes de la galería y categorías de la pastelería, consumidas en tiempo real por la página de inicio.

## Tech Stack

- **Django 4.2** — framework web
- **Django REST Framework** — API de solo lectura para galería y categorías
- **django-jazzmin** — interfaz administrativa personalizada con vistas previas de imágenes
- **PostgreSQL** — base de datos
- **Amazon S3** (django-storages + boto3) — almacenamiento de imágenes y archivos estáticos
- **Pillow** — captura automática de dimensiones de imágenes
- **Docker + Gunicorn** — despliegue

## Características

- API REST de solo lectura: imágenes de galería (filtro por categoría, paginación, ordenamiento) y categorías, protegida con autenticación por token
- Modelo `GalleryImage` que captura automáticamente ancho y alto al guardar
- Admin Jazzmin personalizado: miniaturas de imágenes en listas y formularios, filtros por categoría/fecha, búsqueda por descripción
- Comandos de gestión: carga masiva de imágenes desde carpetas, recálculo de dimensiones y carga de categorías iniciales
- Envoltorio de errores unificado para todas las excepciones de la API
- Suite de pruebas: pruebas de vistas de API y pruebas Selenium del panel administrativo

## Instalación

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# copiar .env.dev y ajustar configuración de BD/almacenamiento
python manage.py migrate
python manage.py apps_loaddata
python manage.py runserver
```

---

## Contacto

Desarrollado por [Dari Developer](https://darideveloper.com)

- 🌐 [darideveloper.com](https://darideveloper.com)
- 💬 [WhatsApp](https://api.whatsapp.com/send?phone=5214493402622)
- 📂 [Ver proyecto en el portafolio](https://darideveloper.com/portafolio/cakestoremommy)
