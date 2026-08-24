[app]

title = Mi App Procesamiento
package.name = miappprocesamiento
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

[app]

# ... (resto de tus configuraciones)

# Forzar hostpython3 para que Pillow/Cython puedan compilar C
requirements = python3,hostpython3,kivy,pillow

# OBLIGATORIO: Forzar NDK 25b y API 33
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Aceptar licencias automáticamente
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
