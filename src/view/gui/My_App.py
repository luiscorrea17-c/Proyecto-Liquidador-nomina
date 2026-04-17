from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout

import sys
sys.path.append( 'src')

from model import logica_liquidador 


class liquidador_nomina(App):
    def build(self):
        self.layout = GridLayout(cols=2, padding=10, spacing=10)

        self.salario_input = TextInput(hint_text='Ingrese tu salario mensual', multiline=False)
        self.extras_input = TextInput(hint_text='Ingrese el valor de las horas extra', multiline=False)
        self.bonificaciones_input = TextInput(hint_text='Ingrese el valor de las bonificaciones', multiline=False)
        self.comisiones_input = TextInput(hint_text='Ingrese el valor de las comisiones', multiline=False)
        self.auxilios_input = TextInput(hint_text='Ingrese el valor de los aux', multiline=False)
        self.salud_input = TextInput(hint_text='Ingrese el porcentaje de salud que paga', multiline=False)
        self.pension_input = TextInput(hint_text='Ingrese el porcentaje de pensión que paga', multiline=False)
        self.impuesto_input = TextInput(hint_text='Ingrese el valor de los impuestos que paga', multiline=False)

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

        self.layout.add_widget(Label(text='Salud (%):'))
        self.layout.add_widget(self.salud_input)

        self.layout.add_widget(Label(text='Pensión (%):'))
        self.layout.add_widget(self.pension_input)

        self.layout.add_widget(Label(text='Impuestos:'))
        self.layout.add_widget(self.impuesto_input)


        self.button = Button(text='Calcular Nómina')
        self.button.bind(on_press=self.calcular_nomina)
        self.result_label = Label(text='Aqui va el resultado')  # Etiqueta para mostrar el resultado
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.result_label)


        return self.layout

    def calcular_nomina(self, instance):
        # Aquí puedes agregar la lógica para calcular la nómina del empleado
        salario = self.salario_input.text
        extras = self.extras_input.text
        bonificaciones = self.bonificaciones_input.text
        comisiones = self.comisiones_input.text
        auxilios = self.auxilios_input.text
        salud = self.salud_input.text
        pension = self.pension_input.text
        impuesto = self.impuesto_input.text

        # Convertir los valores a números (si es posible)
        try:
            salario = float(salario) if salario else 0
            extras = float(extras) if extras else 0
            bonificaciones = float(bonificaciones) if bonificaciones else 0
            comisiones = float(comisiones) if comisiones else 0
            auxilios = float(auxilios) if auxilios else 0
            salud = float(salud) if salud else 0
            pension = float(pension) if pension else 0
            impuesto = float(impuesto) if impuesto else 0
        except ValueError:
            self.result_label.text = "Por favor, ingrese valores numéricos válidos."
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
        self.result_label.text = f"El salario neto es: {salario_neto}"

        
if __name__ == '__main__':
    liquidador_nomina().run()