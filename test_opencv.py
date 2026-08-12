# test_opencv.py
import os
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

# Pedir permisos de Android
try:
  from android.permissions import Permission, request_permissions

  request_permissions([Permission.CAMERA])
except ImportError:
  pass


class OpenCVCameraApp(App):

  def build(self):
    self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

    # Estado / Salida de depuración
    self.label_info = Label(
        text='Inicializando OpenCV en Android...',
        size_hint_y=0.15,
        font_size='16sp',
    )
    self.layout.add_widget(self.label_info)

    # Widget de Kivy donde renderizaremos los frames procesados por OpenCV
    self.img_widget = Image(size_hint_y=0.75)
    self.layout.add_widget(self.img_widget)

    # Botón para cerrar
    btn_salir = Button(text='Cerrar Prueba', size_hint_y=0.10)
    btn_salir.bind(on_release=lambda x: self.stop())
    self.layout.add_widget(btn_salir)

    # Inicializar la cámara nativa de Kivy de forma oculta/de fondo
    try:
      from kivy.uix.camera import Camera

      self.kivy_cam = Camera(play=True, resolution=(640, 480))
      # Programamos el bucle de procesamiento de OpenCV a 30 FPS
      Clock.schedule_interval(self.procesar_frame_opencv, 1.0 / 30.0)
      self.label_info.text = 'Cámara iniciada. Cargando OpenCV...'
    except Exception as e:
      self.label_info.text = f'Error iniciando cámara: {e}'

    return self.layout

  def procesar_frame_opencv(self, dt):
    """Aquí ocurre la magia de OpenCV sobre la cámara de Android."""
    if not hasattr(self, 'kivy_cam') or not self.kivy_cam.texture:
      return

    try:
      # LA REGLA DE ORO: Importación bajo demanda dentro del método
      import cv2
      import numpy as np

      # 1. Obtener los bytes de la textura de la cámara
      texture = self.kivy_cam.texture
      size = texture.size
      pixels = texture.pixels

      # 2. Convertir los pixels de Kivy (RGBA) a una matriz NumPy de OpenCV
      frame = np.frombuffer(pixels, dtype=np.uint8)
      frame = frame.reshape(size[1], size[0], 4)

      # 3. --- PROCESAMIENTO OPENCV ---
      # Invertir verticalmente (Kivy dibuja las texturas invertidas en el eje Y)
      frame = cv2.flip(frame, 0)

      # Convertir a Escala de Grises
      gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)

      # Detección de bordes con Canny (Demostración visual de OpenCV trabajando)
      edges = cv2.Canny(gray, 100, 200)

      # Convertir los bordes de vuelta a BGR/RGB para mostrarlo en pantalla
      frame_procesado = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

      # Si tienes la función de lectura de código de OpenCV (cv2.QRCodeDetector o BarcodeDetector):
      # detector = cv2.barcode.BarcodeDetector()
      # retval, decoded_info, decoded_type, points = detector.detectAndDecode(gray)
      # if retval:
      #     self.label_info.text = f"¡Código detectado!: {decoded_info[0]}"

      # 4. Volver a convertir el array de OpenCV a una Textura de Kivy para dibujarlo
      buf = frame_procesado.tobytes()
      image_texture = Texture.create(
          size=(frame_procesado.shape[1], frame_procesado.shape[0]),
          colorfmt='rgb',
      )
      image_texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

      # Actualizar el widget gráfico de Kivy
      self.img_widget.texture = image_texture
      self.label_info.text = 'OpenCV procesando a 30 FPS ✅'

    except ImportError:
      self.label_info.text = '❌ Error: Módulo cv2 no encontrado en la APK'
    except Exception as e:
      self.label_info.text = f'Error en procesamiento: {str(e)}'


if __name__ == '__main__':
  OpenCVCameraApp().run()
