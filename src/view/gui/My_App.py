from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Line
import sys

import os
import sys

<<<<<<< HEAD
# Esto detecta si corre como .py o como .exe
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Añadimos la ruta de 'src' de forma absoluta
sys.path.append(os.path.join(base_path, 'src'))

from model import logica_liquidador

=======
>>>>>>> 37bc36d8301c583c4a319f30526b24865c79487b
Window.clearcolor = (1, 1, 1, 1)

class liquidador_nomina(App):

    def build(self):
        main_layout = GridLayout(cols=1, padding=30, spacing=20)

        titulo = Label(
            text='Calculadora de Liquidación de Nómina',
            font_size=22,
            bold=True,
            size_hint_y=None,
            height=40,
            color=(0.1, 0.2, 0.4, 1)
        )
        main_layout.add_widget(titulo)

        layout = GridLayout(cols=2, spacing=12, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        def estilo_label(text):
            lbl = Label(
                text=text,
                color=(0, 0, 0, 1),
                size_hint_y=None,
                height=45
            )
            with lbl.canvas.after:
                lbl.border_color = Color(0.3, 0.6, 1, 1)
                lbl.border_line = Line(width=1.2)
            def update_border(*args):
                lbl.border_line.rectangle = (
                    lbl.x, lbl.y,
                    lbl.width, lbl.height
                )
            lbl.bind(pos=update_border, size=update_border)
            return lbl

        def estilo_input(hint):
            input_box = TextInput(
                hint_text=hint,
                multiline=False,
                input_filter='float',
                size_hint_y=None,
                height=45,
                background_normal='',
                background_color=(0.95, 0.95, 0.95, 1),
                foreground_color=(0, 0, 0, 1),
                cursor_color=(0.2, 0.5, 0.9, 1)
            )
            with input_box.canvas.after:
                input_box.border_color = Color(0.7, 0.7, 0.7, 1)
                input_box.border_line = Line(width=1.2)
            def update_border(*args):
                input_box.border_line.rectangle = (
                    input_box.x, input_box.y,
                    input_box.width, input_box.height
                )
            def on_focus(instance, value):
                if value:
                    input_box.border_color.rgb = (0.2, 0.5, 1)
                    input_box.border_line.width = 2
                else:
                    input_box.border_color.rgb = (0.7, 0.7, 0.7)
                    input_box.border_line.width = 1.2
            input_box.bind(pos=update_border, size=update_border)
            input_box.bind(focus=on_focus)
            return input_box

        self.salario_input = estilo_input('2000000')
        self.extras_input = estilo_input('100000')
        self.bonificaciones_input = estilo_input('50000')
        self.comisiones_input = estilo_input('30000')
        self.auxilios_input = estilo_input('100000')
        self.salud_input = estilo_input('1 - 4')
        self.pension_input = estilo_input('1 - 4')
        self.impuesto_input = estilo_input('50000')

        layout.add_widget(estilo_label('Salario'))
        layout.add_widget(self.salario_input)

        layout.add_widget(estilo_label('Horas extra'))
        layout.add_widget(self.extras_input)

        layout.add_widget(estilo_label('Bonificaciones'))
        layout.add_widget(self.bonificaciones_input)

        layout.add_widget(estilo_label('Comisiones'))
        layout.add_widget(self.comisiones_input)

        layout.add_widget(estilo_label('Auxilios'))
        layout.add_widget(self.auxilios_input)

        layout.add_widget(estilo_label('Salud (%)'))
        layout.add_widget(self.salud_input)

        layout.add_widget(estilo_label('Pensión (%)'))
        layout.add_widget(self.pension_input)

        layout.add_widget(estilo_label('Impuestos'))
        layout.add_widget(self.impuesto_input)

        main_layout.add_widget(layout)

        self.button = Button(
            text='CALCULAR',
            size_hint_y=None,
            height=55,
            background_normal='',
            background_color=(0.2, 0.6, 1, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        self.button.bind(on_press=self.calcular_nomina)
        main_layout.add_widget(self.button)

        self.result_label = Label(
            text='Resultado aparecerá aquí',
            size_hint_y=None,
            height=40,
            color=(0, 0, 0, 1)
        )
        main_layout.add_widget(self.result_label)

        return main_layout

    def calcular_nomina(self, instance):
        try:
            salario = float(self.salario_input.text or 0)
            extras = float(self.extras_input.text or 0)
            bonificaciones = float(self.bonificaciones_input.text or 0)
            comisiones = float(self.comisiones_input.text or 0)
            auxilios = float(self.auxilios_input.text or 0)
            salud = float(self.salud_input.text or 0)
            pension = float(self.pension_input.text or 0)
            impuesto = float(self.impuesto_input.text or 0)

            if salud < 1 or salud > 4:
                self.result_label.text = "Error en salud"
                self.result_label.color = (1, 0, 0, 1)
                return

            if pension < 1 or pension > 4:
                self.result_label.text = "Error en pensión"
                self.result_label.color = (1, 0, 0, 1)
                return

            salario_total = logica_liquidador.LiquidacionSalario(
                salario=salario,
                horas_extra=extras,
                bonificaciones=bonificaciones,
                comisiones=comisiones,
                auxilios=auxilios,
                salud=salud,
                pension=pension,
                impuesto_dinero=impuesto
            )

            salario_neto = logica_liquidador.calcular_salario(salario_total)

            self.result_label.color = (0, 0.6, 0, 1)
            self.result_label.text = f"${salario_neto:,.2f}"

        except:
            self.result_label.text = "Error en datos"
            self.result_label.color = (1, 0, 0, 1)


if __name__ == '__main__':
    liquidador_nomina().run()