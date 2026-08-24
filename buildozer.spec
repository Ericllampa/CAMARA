[app]

# (1) Título de tu aplicación
title = MiAppCamara

# (2) Nombre del paquete en formato alfanumérico (sin guiones ni símbolos)
package.name = miappcamara

# (3) Dominio de la organización (identificador único)
package.domain = org.ejemplo

# (4) Directorio del código fuente (. indica la carpeta raíz)
source.dir = .

# Archivos a incluir en el APK
source.include_exts = py,png,jpg,kv,atlas

# (5) Versión de la aplicación
version = 0.1

# Requerimientos de Python y librerías C
requirements = python3,kivy,pillow

# Arquitectura y compatibilidad Android
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
