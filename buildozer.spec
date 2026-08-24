[app]

# (main.py es el archivo de entrada)
title = Mi App Camara
package.name = miappcamara
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Requerimientos para OpenCV
requirements = python3,kivy,numpy,opencv

# Permisos requeridos
android.permissions = CAMERA

# SDK, NDK y Build-Tools
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.sdk_build_tools = 33.0.2

# Aceptar licencias de Android automáticamente
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
