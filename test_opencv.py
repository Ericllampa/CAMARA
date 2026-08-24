import os
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

# Importación de Pillow (PIL)
from PIL import Image as PILImage, ImageFilter, ImageOps

# Pedir permisos de Android
try:
    from android.permissions import Permission, request_permissions
    request_permissions([Permission.CAMERA])
except ImportError:
    pass


class PillowCameraApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Estado / Salida de depuración
        self.label_info = Label(
            text='Inicializando Pillow en Android...',
            size_hint_y=0.15,
            font_size='16sp',
        )
        self.layout.add_widget(self.label_info)

        # Widget de Kivy donde renderizaremos los frames procesados
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
            # Programamos el bucle de procesamiento a 30 FPS
            Clock.schedule_interval(self.procesar_frame_pillow, 1.0 / 30.0)
            self.label_info.text = 'Cámara iniciada. Cargando Pillow...'
        except Exception as e:
            self.label_info.text = f'Error iniciando cámara: {e}'

        return self.layout

    def procesar_frame_pillow(self, dt):
        """Procesamiento digital de imágenes sobre la cámara usando Pillow."""
        if not hasattr(self, 'kivy_cam') or not self.kivy_cam.texture:
            return

        try:
            # 1. Obtener los bytes de la textura de la cámara de Kivy
            texture = self.kivy_cam.texture
            size = texture.size
            pixels = texture.pixels

            # 2. Cargar directamente los pixels RGBA en una imagen de Pillow
            img = PILImage.frombytes('RGBA', size, pixels)

            # 3. Corregir orientación (Kivy dibuja las texturas invertidas en el eje Y)
            img = ImageOps.flip(img)

            # 4. --- PROCESAMIENTO DIGITAL CON PILLOW ---
            # Convertir a Escala de Grises ('L' = Luminance/Grayscale)
            gray = img.convert('L')

            # Detección de bordes (Equivalente al Canny/Sobel de OpenCV)
            edges = gray.filter(ImageFilter.FIND_EDGES)

            # Convertir de vuelta a RGB para renderizar en pantalla
            frame_procesado = edges.convert('RGB')

            # 5. Convertir la imagen procesada a Textura de Kivy
            buf = frame_procesado.tobytes()
            image_texture = Texture.create(
                size=frame_procesado.size,
                colorfmt='rgb',
            )
            image_texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

            # Actualizar el widget gráfico
            self.img_widget.texture = image_texture
            self.label_info.text = 'Pillow procesando bordes a 30 FPS ✅'

        except Exception as e:
            self.label_info.text = f'Error en procesamiento: {str(e)}'


if __name__ == '__main__':
    PillowCameraApp().run()
