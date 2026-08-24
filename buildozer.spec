[app]

title = Mi App Procesamiento
package.name = miappprocesamiento
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Requerimientos livianos (sin NDK pesado de C++)
requirements = python3,kivy,pillow

# Permisos requeridos para capturar imagen o abrir archivos
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


# Fijar API y Build Tools estables
android.api = 33
android.minapi = 21
android.sdk_build_tools = 33.0.2

# Aceptar licencias del SDK automáticamente
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
