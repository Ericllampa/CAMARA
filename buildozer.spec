[app]
title = MiAppCamara
package.name = miappcamara
package.domain = org.ejemplo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requerimientos (asegúrate de incluir python3)
requirements = python3,kivy,pillow

# Forzar la rama estable de python-for-android
p4a.branch = master

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
