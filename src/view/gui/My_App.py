from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window # Nuevo: Para el color de fondo
import sys

sys.path.append('src')
from model import logica_liquidador 

# Cambiamos el color de fondo de la ventana (Gris muy oscuro casi negro)
Window.clearcolor = (0.12, 0.12, 0.12, 1)

class liquidador_nomina(App):
    def build(self):
        # Aumentamos el padding para que no se vea pegado a los bordes
        self.layout = GridLayout(cols=2, padding=30, spacing=15)

        # Usamos input_filter='float' para que el ejecutable sea más robusto (evita letras)
        self.salario_input = TextInput(hint_text='Salario mensual', multiline=False, input_filter='float')
        self.extras_input = TextInput(hint_text='Valor horas extra', multiline=False, input_filter='float')
        self.bonificaciones_input = TextInput(hint_text='Valor bonificaciones', multiline=False, input_filter='float')
        self.comisiones_input = TextInput(hint_text='Valor comisiones', multiline=False, input_filter='float')
        self.auxilios_input = TextInput(hint_text='Valor auxilios', multiline=False, input_filter='float')
        self.salud_input = TextInput(hint_text='Porcentaje salud (ej: 4)', multiline=False, input_filter='float')
        self.pension_input = TextInput(hint_text='Porcentaje pensión (ej: 4)', multiline=False, input_filter='float')
        self.impuesto_input = TextInput(hint_text='Valor impuestos', multiline=False, input_filter='float')


        # Agregamos las etiquetas y los cuadros de texto uno por uno
        self.layout.add_widget(Label(text='Salario mensual:'))
        self.layout.add_widget(self.salario_input)

        self.layout.add_widget(Label(text='Horas extra:'))
        self.layout.add_widget(self.extras_input)

        self.layout.add_widget(Label(text='Bonificaciones:'))
        self.layout.add_widget(self.bonificaciones_input)

        self.layout.add_widget(Label(text='Comisiones:'))
        self.layout.add_widget(self.comisiones_input)

        self.layout.add_widget(Label(text='Auxilios:'))
        self.layout.add_widget(self.auxilios_input)

        self.layout.add_widget(Label(text='Salud (1% - 4%):'))
        self.layout.add_widget(self.salud_input)

        self.layout.add_widget(Label(text='Pensión (1% - 4%):'))
        self.layout.add_widget(self.pension_input)

        self.layout.add_widget(Label(text='Impuestos:'))
        self.layout.add_widget(self.impuesto_input)

        # Botón con un color azul para que se vea profesional en el ejecutable
        self.button = Button(
            text='Calcular Nómina',
            background_color=(0.2, 0.5, 0.8, 1),
            bold=True
        )
        self.button.bind(on_press=self.calcular_nomina)
        
        # Etiqueta para el resultado
        self.result_label = Label(text='Ingrese los datos y presione calcular', bold=True)
        
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calcular_nomina(self, instance):
        try:
            # Convertimos los valores a números (si están vacíos ponemos 0)
            salario = float(self.salario_input.text or 0)
            extras = float(self.extras_input.text or 0)
            bonificaciones = float(self.bonificaciones_input.text or 0)
            comisiones = float(self.comisiones_input.text or 0)
            auxilios = float(self.auxilios_input.text or 0)
            salud = float(self.salud_input.text or 0)
            pension = float(self.pension_input.text or 0)
            impuesto = float(self.impuesto_input.text or 0)

            # --- CONDICIONALES DE CONTROL ---
            # Si salud es menor a 1 o mayor a 4
            if salud < 1 or salud > 4:
                self.result_label.text = "Error: Salud debe estar entre 1 y 4"
                self.result_label.color = (1, 0, 0, 1) # Rojo
                return # Salimos para que no siga calculando

            # Si pensión es menor a 1 o mayor a 4
            if pension < 1 or pension > 4:
                self.result_label.text = "Error: Pensión debe estar entre 1 y 4"
                self.result_label.color = (1, 0, 0, 1) # Rojo
                return # Salimos para que no siga calculando

            # Si todo está bien, calculamos
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
            
            # Formateamos el número para que sea legible ($1,000,000.00)
            self.result_label.color = (1, 1, 1, 1) # Blanco
            self.result_label.text = f"El salario neto es: ${salario_neto:,.2f}"

        except ValueError:
            self.result_label.text = "Por favor, use solo números"
            self.result_label.color = (1, 0, 0, 1)

if __name__ == '__main__':
    liquidador_nomina().run()