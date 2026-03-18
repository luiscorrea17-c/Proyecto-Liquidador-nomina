# Liquidador de Nómina


## 👥 Autores

* **Sebastián Rendón Grisales**
* **Juan Camilo Gómez Gómez**

---

## 📌 Descripción

Este proyecto corresponde a una aplicación web para el curso **Código Limpio** de la **Universidad de Medellín**.

El **Liquidador de Nómina** permite calcular el valor total a pagar a un empleado, teniendo en cuenta:

* Los **valores devengados** (salario base, horas extra, bonificaciones, etc.)
* Las **deducciones de ley** aplicables

El valor final de la nómina se obtiene como la diferencia entre los valores devengados y las deducciones.

---

## 🎯 Objetivo

Desarrollar una aplicación clara, funcional y bien estructurada que aplique los principios de **Código Limpio**.

## ⚙️ Funcionalidades principales

* Cálculo del total devengado por el empleado
* Cálculo del valor neto a pagar
* Separación clara de responsabilidades
* Código legible y modular
---
## Funcionamiento

Ubicados en la carpeta raiz del proyecto, ejecute:
```
py src/view/consola_liquidador.py
```
---
## Construcción
- carpeta docs: Contenido extra que posee la aplicación. Contiene archivos propios relacionados a la aplicación en general.
- carpeta src: Codigo fuente de la aplicación. Posee subcarpetas que contienen las diferentes capas que permiten el funcionamiento general.
- carpeta tests: Pruebas unitarias de la aplicación.

Cada carpeta posee __init__.py para que python reconozca cada una y pueda relacionar su respectivo import.

---
## Ejecución de pruebas
Para ejecutar las pruebas unitarias, dirijase la carpeta raiz y use el siguiente el comando:
```
py tests\test_liquidador.py
```
---
## Entrevista

Este repositorio incluye una entrevista relacionado al proyecto a un invitado con mayor conocimiento, es un intercambio de ideas antes de la construcción del mismo.

📁 La entrevista completa se encuentra en la carpeta `entrevista`.

---
## Documento casos de prueba

Este repositorio incluye el documento de excel el cual tiene los casos de pruebas propuestos para el proyecto.

📁 El documento de excel se encuentra en `CASOS DE PRUEBA PROYECTO_1`

---
## 📤 Entradas y procesos de salida

**Entradas:**
* Salario
* Horas extras
* Bonificaciones
* Comisiones
* Auxilios
* Salud (porcentaje)
* Pension (porcentaje
* Impuestos (porcentaje)

**Proceso:**

Durante el proceso operativo se realiza la suma del salario con los beneficios extra (Valores devengados) que incluyen **horas extra**, **Bonificaciones**, **Comisiones**, **Auxilios** y se le restan las deducciones de ley siendo estas **Salud**, **Pension**, **Impuestos** (a estas ultimas en caso de que apliquen). 

**Salidas:**
* Salario Neto

---

## 🏫 Institución

**Universidad de Medellín**

Curso: **Código Limpio**
