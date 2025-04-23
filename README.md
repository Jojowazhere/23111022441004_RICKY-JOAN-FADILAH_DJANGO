# 23111022441004_RICKY-JOAN-FADILAH_DJANGO

1. buat folder .venv (disini saya memakai .venv)

2. masuk folder .venv dan buat virtualenv menggunakan perintah 
 ```
 py -m venv .venv
 ```
3. aktifkan .venv dengan ketik 
 ```
 cd .venv/Scripts
 ```
4. setelah masuk di dalam folder Scripts, ketik 
 ```
activate
 ```
5. jika .venv telah aktif, kita bisa melanjutkan menginstall django dengan mengetik
 ```
 pip install django
 ```
6. untuk mengetahui library django terinstall, ketik 
 ```
 pip list
 ```
7. selanjutnya kita akan membuat project django dengan mengetik 
 ```
 "django-admin startproject portofolio"
 ``` 
 8. untuk mengecek django terinstal, ketik 
 ```
 py manage.py runserver
 ```