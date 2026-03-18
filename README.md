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

## Ejecución

### Prerrequisitos
 
Antes de ejecutar el proyecto, asegúrese de tener instalado lo siguiente:
 
- **Python 3.8** o superior. Puede verificar su versión con:
 
```
python --version
```

### Ejecución del programa
 
Ubicados en la carpeta raíz del proyecto, ejecute:
 
```
py src/view/consola_liquidador.py
```

---
 
## 🧪 Ejecución de pruebas
 
Para ejecutar las pruebas unitarias, diríjase a la carpeta raíz y use el siguiente comando:
 
```
py tests\test_liquidador.py
```

Para poder ejecutarlas desde la carpeta raíz, debe indicar la ruta de búsqueda donde se encuentran los módulos. Incluya las siguientes líneas al inicio del módulo de pruebas:
 
```python
import sys
sys.path.append("src")
```
 
---

## 🏗️ Construcción
- carpeta docs: Contenido extra que posee la aplicación. Contiene archivos propios relacionados a la aplicación en general.
- carpeta src: Codigo fuente de la aplicación. Posee subcarpetas que contienen las diferentes capas que permiten el funcionamiento general.
- carpeta tests: Pruebas unitarias de la aplicación.

Cada carpeta de código fuente contiene un archivo `__init__.py` que permite que Python reconozca la carpeta como un módulo y pueda realizar importaciones correctamente.

### Bibliotecas y dependencias

Las bibliotecas externas utilizadas son:
- `pytest` — para las pruebas unitarias

---
## 📤 Entradas y salidas
 
### Entradas
 
| Campo | Descripción |
|---|---|
| Salario | Salario base del empleado |
| Horas extras | Cantidad y tipo de horas extras trabajadas |
| Bonificaciones | Bonos adicionales al salario |
| Comisiones | Comisiones generadas |
| Auxilios | Auxilios (transporte u otros) |
| Salud (%) | Porcentaje de descuento por salud |
| Pensión (%) | Porcentaje de descuento por pensión |
| Impuestos (%) | Porcentaje de descuento por impuestos (si aplica) |
 
### Proceso
 
Se realiza la suma del salario base con los beneficios extra (**valores devengados**): horas extra, bonificaciones, comisiones y auxilios. A este subtotal se le restan las **deducciones de ley**: salud, pensión e impuestos (en caso de que apliquen).
 
```
Nómina neta = (Salario + Horas extra + Bonificaciones + Comisiones + Auxilios)
            - (Salud + Pensión + Impuestos)
```
 
### Salidas
 
- **Salario Neto** a pagar al empleado
 
---

## Entrevista

Este repositorio incluye una entrevista relacionado al proyecto a un invitado con mayor conocimiento, es un intercambio de ideas antes de la construcción del mismo.

📁 La entrevista completa se encuentra en `docs/Entrevista.m4a`.

---
## Documento casos de prueba

Este repositorio incluye el documento de excel el cual tiene los casos de pruebas propuestos para el proyecto.

📁 El documento de excel se encuentra en `docs/CASOS DE PRUEBA PROYECTO_1.xlsx`

---
## 🏫 Institución

**Universidad de Medellín**

Curso: **Código Limpio**
