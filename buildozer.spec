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

# Configuración NDK / API
android.api = 33
android.minapi = 21
android.sdk_build_tools = 33.0.2
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
