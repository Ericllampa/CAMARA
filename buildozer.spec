# 1. Requerimientos
requirements = python3,kivy,numpy,opencv

# 2. Configuración de API y NDK (Crucial para que compile C++)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# 3. Forzar p4a actualizado que maneje las recetas de C++
p4a.branch = master

# 4. Arquitecturas compatibles
android.archs = arm64-v8a
