from datetime import datetime

# ==========================================
# 1. CLASE: OperarioProducción
# ==========================================
class OperarioProduccion:
    def __init__(self, codigo: str, nombre: str, turno: str):
        self._codigo = codigo
        self._nombre = nombre
        self._turno = turno

    def obtener_codigo(self) -> str:
        return self._codigo

    def obtener_nombre(self) -> str:
        return self._nombre

    def obtener_turno(self) -> str:
        return self._turno


# ==========================================
# 2. CLASE: RegistroFileteo
# ==========================================
class RegistroFileteo:
    def __init__(self, fecha_produccion: datetime, lote: str, peso_inicial: float, peso_lomos: float, peso_desperdicio: float, operario: OperarioProduccion):
        # Validación: Conservación de masa con margen de precisión (0.001)
        if abs((peso_lomos + peso_desperdicio) - peso_inicial) > 0.001:
            raise ValueError("Error de Invariante de Masa: pesoLomos + pesoDesperdicio debe ser igual al pesoInicial.")
        
        # Validación: Pesos negativos e inicial mayor a cero
        if peso_inicial <= 0 or peso_lomos < 0 or peso_desperdicio < 0:
            raise ValueError("Los pesos no pueden ser negativos y el peso inicial debe ser mayor a cero.")

        self._fecha_produccion = fecha_produccion
        self._lote = lote
        self._peso_inicial = peso_inicial
        self._peso_lomos = peso_lomos
        self._peso_desperdicio = peso_desperdicio
        self._operario = operario

    def calcular_rendimiento_porcentaje(self) -> float:
        return (self._peso_lomos / self._peso_inicial) * 100.0

    def evaluar_rendimiento(self) -> str:
        rendimiento = self.calcular_rendimiento_porcentaje()
        if 45.0 <= rendimiento <= 51.0:
            return "Rendimiento Bueno"
        else:
            return "Rendimiento Malo"


# ==========================================
# 3. CLASE: GestorProducción
# ==========================================
class GestorProduccion:
    def __init__(self):
        self._registros = []

    def agregar_registro(self, registro: RegistroFileteo):
        self._registros.append(registro)

    def cerrar_registro_fileteo(self):
        buenos = 0
        malos = 0

        for reg in self._registros:
            evaluacion = reg.evaluar_rendimiento()
            if evaluacion == "Rendimiento Bueno":
                buenos += 1
            else:
                malos += 1

        print("=== CIERRE DE REGISTRO DE FILETEO ===")
        print(f"Total de registros evaluados: {len(self._registros)}")
        print(f"Productos con Rendimiento Bueno: {buenos}")
        print(f"Productos con Rendimiento Malo: {malos}")


# ==========================================
# 4. FLUJO DE EJECUCIÓN (Principal)
# ==========================================
if __name__ == "__main__":
    # Creación del operario y gestor
    operacion = OperarioProduccion("OP-001", "Carlos Pérez", "Matutino")
    gestor = GestorProduccion()

    try:
        # Ejemplo 1: Cumple con la masa y da un rendimiento del 48% (Bueno)
        reg1 = RegistroFileteo(datetime.now(), "LOTE-100", 100.0, 48.0, 52.0, operacion)
        gestor.agregar_registro(reg1)
        print(f"Registro 1 agregado correctamente. Rendimiento: {reg1.calcular_rendimiento_porcentaje()}% -> {reg1.evaluar_rendimiento()}")

        # Ejemplo 2: Rompe la regla de conservación de masa (Lanza excepción)
        try:
            reg_error = RegistroFileteo(datetime.now(), "LOTE-101", 100.0, 40.0, 50.0, operacion)
            gestor.agregar_registro(reg_error)
        except ValueError as mi:
            print(f"Error detectado correctamente: {mi}")

        # Ejemplo 3: Cumple con la masa pero da un rendimiento del 40% (Malo)
        reg2 = RegistroFileteo(datetime.now(), "LOTE-102", 100.0, 40.0, 60.0, operacion)
        gestor.agregar_registro(reg2)
        print(f"Registro 2 agregado correctamente. Rendimiento: {reg2.calcular_rendimiento_porcentaje()}% -> {reg2.evaluar_rendimiento()}")

        print()  # Línea en blanco
        
        # Ejecutar el cierre de turno
        gestor.cerrar_registro_fileteo()

    except ValueError as mi:
        print(f"Validación fallida: {mi}")
