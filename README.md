# 🏭 SISTEMA DE CONTROL DE CALIDAD - PLANTA ATUNERA


==============================================================================================
* **Institución:** Escuela Superior Politécnica Agropecuaria de Manabí "Manuel Félox López"
* **Curso:** Desarrollo de Software II / Estructura de Datos y Algoritmos
* **Materia:** Programación Orientada a Objetos (POO)
* **Estudiante:** Sylvia Soraya Sánchez Soria
* **PROYECTO:** Gestión de Producción y Control de Fileteo de Pescado
* **Lenguaje Asignado:** Python 3.15 (Migración desde Java)


---

## 📌 1. DESCRIPCIÓN DEL PROYECTO
Este repositorio contiene la migración **completa y optimizada** del sistema de software desarrollado originalmente en Java para la Hackatón POO. La solución preserva rigurosamente el paradigma de Orientación a Objetos, garantizando el encapsulamiento de datos y la validación de las invariantes críticas del negocio en la planta de procesamiento de atún.

---

## 🛠️ 2. REQUISITOS E INSTALACIÓN

Para el despliegue e inspección del entorno de software, asegúrese de cumplir con los siguientes componentes en su estación de trabajo:

| Componente | Requisito Mínimo | Propósito |
| :--- | :--- | :--- |
| **Intérprete** | Python 3.10 o superior | Entorno de ejecución principal |
| **Editor IDE** | Visual Studio Code / PyCharm | Visualización y depuración de clases |
| **Extensión** | Python Extension (Microsoft) | Soporte técnico dentro del IDE |

---

## 🚀 3. COMANDOS DE EJECUCIÓN

Secuencia de pasos en la terminal deL sistema operativo para poner en marcha la solución funcional:

1. **Clonar o descargar** el archivo `Main.py` en un directorio local.
2. **Abrir la terminal** de comandos (CMD o terminal integrada del IDE) en la ruta de la carpeta.
3. **Ejecutar** el archivo utilizando el intérprete nativo de Python mediante el siguiente comando:

```bash
python Main.py
```

---

## 🧪 4. DEMOSTRACIÓN DE INVARIANTES DE NEGOCIO

El flujo del script principal (`if __name__ == "__main__":`) incluye una batería de pruebas automáticas para evaluar el comportamiento del sistema ante datos correctos y erróneos:

```diff
+ [CASO VÁLIDO] Lote-100:
  - Registra lomos (48.0 kg) y desperdicio (52.0 kg) sobre un peso inicial de 100.0 kg.
  - El sistema calcula un 48.0% de rendimiento (Evaluación: Rendimiento Bueno).

- [CASO INVÁLIDO] Lote-101 (Fallo de Invariante de Masa):
  - Intenta ingresar un peso inicial de 100.0 kg pero con lomos y desperdicio que suman 90.0 kg.
  - El sistema frena la operación lanzando una excepción controlada: ValueError.

+ [CASO VÁLIDO] Lote-102 (Rendimiento Fuera de Rango):
  - Registra la conservación de masa (40.0 kg + 60.0 kg = 100.0 kg).
  - El sistema procesa los datos pero detecta que el 40.0% de lomos está fuera del rango óptimo (Evaluación: Rendimiento Malo).
