# Peonies Site

[Peonies Site Website] (https://rizki-amani-peoniessite.pbp.cs.ui.ac.id)

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. **Membuat Proyek Django Baru:**
    - Membuat direktori baru yang sesuai dengan nama aplikasi, peonies-site
    - Aktifkan virtual environment
    - Buat proyek baru dengan perintah: `django-admin startproject`

2. **Membuat Aplikasi:**
    - Buat aplikasi baru dengan perintah `python3 manage.py startapp main`
    - Menamakannya dengan main sesuai perintah tugas

3. **Melakukan routing pada proyek:**
    - Tambahkan aplikasi `main` ke dalam `INSTALLED_APPS` di `settings.py` proyek:
     ```python
     INSTALLED_APPS = [
         ...
         'main',
     ]
     ```

    - Konfigurasikan routing dengan menambahkan `main.urls` ke `urls.py` proyek:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('main.urls')),
     ]
     ```
4. **Membuat Models:**
    - Mendefinisikan model pada `models.py` yang sesuai dengan aplikasi.
     ```python
    from django.db import models

    class Product(models.Model):
        BOUQUET_TYPE_CHOICES = [
            ('single', 'Single'),
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('big', 'Big')
        ]

        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        bouquet_type = models.CharField(max_length=10, choices=BOUQUET_TYPE_CHOICES, default='single')  # Type of bouquet
        wrap_color = models.CharField(max_length=50, default='')  # Wrap color

        def __str__(self):
            return self.name
        
        @property
        def is_in_stock(self):
            return self.stock > 0
     ```
    - Jalankan migrasi untuk membuat tabel `Product` di database, menggunakan perintah `python manage.py makemigrations` dan `python manae.py migrate`

5. **Membuat Fungsi pada Views dan Template HTML:**
    - Tambahkan fungsi pada `views.py` di aplikasi `main`:
     ```python
    from django.shortcuts import render
    from .models import Product

    def product_list(request):
        context = {
            'name': 'Rizki Amani Hasanah',  
            'npm': '2306213376', 
            'class_name': 'PBP B',  
            'app_name': 'Peonies Site'
        }

        return render(request, 'main.html', context)
     ```
    - Lalu membuat html yang sesuai dengan keinginan

6. **Routing pada urls.py Aplikasi Main:**
   - Tambahkan konfigurasi routing pada `urls.py` aplikasi `main`:
     ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.product_list, name='main'),
    ]
     ```

7. **Deployment ke PWS:**
   - Gunakan `python manage.py runserver` untuk pengujian pada server lokal
   - Memasukkan url pws di `settings.py`, tepatnya ALLOWED_HOSTS
   - Deploy aplikasi ke platform hosting PWS 

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](bagan.jpeg)

- **urls.py**: Mengarahkan URL dari client ke fungsi yang sesuai di `views.py`.
- **views.py**: Menangani logika bisnis dan memproses data, termasuk mengambil data dari model (jika diperlukan) dan mengirimkan ke template.
- **models.py**: Mengelola interaksi dengan database (misalnya, mengambil atau menyimpan data).
- **Template HTML**: Menyediakan format tampilan yang dikirimkan sebagai respon ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi terdistribusi yang memungkinkan pengembang untuk mengelola perubahan dalam kode sumber proyek perangkat lunak. Fungsinya meliputi melacak perubahan dengan menyimpan riwayat dalam repositori, sehingga bisa kembali ke versi sebelumnya jika diperlukan. Selain itu, Git memfasilitasi kolaborasi tim dengan mengelola perubahan yang dilakukan oleh beberapa pengembang secara bersamaan melalui cabang (branches) dan merge. Git juga berfungsi sebagai cadangan kode, memungkinkan pemulihan jika terjadi masalah dengan menyimpan salinan kode yang dikendalikan oleh sistem.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dipilih sebagai framework pemula karena beberapa alasan:
- **Kemudahan Penggunaan:** Django memiliki dokumentasi yang lengkap dan komunitas yang aktif
- **Batteries Included:** Django menyediakan banyak fitur bawaan yang memudahkan pengembangan aplikasi web, seperti ORM, sistem autentikasi, dan admin interface.
- **Struktur yang Jelas:** Django mengikuti pola desain Model-View-Template (MVT) yang memisahkan logika aplikasi dari presentasi

### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena menyediakan cara untuk berinteraksi dengan database menggunakan objek Python daripada menulis query SQL secara langsung. ORM memungkinkan pemetaan antara kelas Python dan tabel database, membuat pengembangan lebih intuitif dan mengurangi kebutuhan untuk penulisan query SQL yang rumit.


    