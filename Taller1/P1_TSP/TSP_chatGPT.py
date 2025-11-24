from typing import List, Tuple, Dict
import itertools

from Taller1.P1_TSP.util import plotear_ruta, generar_ciudades_con_distancias


from typing import List, Tuple, Dict
import itertools

class TSP:
    def __init__(self, ciudades: Dict[str, Tuple[float, float]], distancias: Dict[Tuple[str, str], float]):
        self.ciudades = ciudades
        self.distancias = distancias

    def costo_ruta(self, ruta: List[str]) -> float:
        total = 0
        for i in range(len(ruta) - 1):
            total += self.distancias[(ruta[i], ruta[i+1])]
        total += self.distancias[(ruta[-1], ruta[0])]  # volver al inicio
        return total

    def encontrar_la_ruta_mas_corta(self) -> List[str]:
        ciudades_lista = list(self.ciudades.keys())
        ciudad_inicial = ciudades_lista[0]
        mejores_ciudades = ciudades_lista[1:]

        mejor_ruta = None
        mejor_costo = float('inf')

        for perm in itertools.permutations(mejores_ciudades):
            ruta = [ciudad_inicial] + list(perm)
            costo = self.costo_ruta(ruta)

            if costo < mejor_costo:
                mejor_costo = costo
                mejor_ruta = ruta

        return mejor_ruta

    def plotear_resultado(self, ruta: List[str], mostrar_anotaciones: bool = True):
        from util import plotear_ruta
        plotear_ruta(self.ciudades, ruta, mostrar_anotaciones)

def study_case_1():
    n_cities = 10
    ciudades, distancias = generar_ciudades_con_distancias(n_cities)
    tsp = TSP(ciudades, distancias)
    ruta = ciudades.keys()
    # ruta = tsp.encontrar_la_ruta_mas_corta()
    tsp.plotear_resultado(ruta)

def study_case_2():
    n_cities = 100
    ciudades, distancias = generar_ciudades_con_distancias(n_cities)
    tsp = TSP(ciudades, distancias)
    ruta = ciudades.keys()
    # ruta = tsp.encontrar_la_ruta_mas_corta()
    tsp.plotear_resultado(ruta, False)


if __name__ == "__main__":
    # Solve the TSP problem
    study_case_1()
