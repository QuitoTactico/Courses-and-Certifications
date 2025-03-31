# Source:

https://platzi.com/cursos/algoritmos-python/

# T(n) - Complejidad Temporal

Pues el tiempo, en bruto, y ya

```python
import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)

if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
```

# O(n) - Complejidad Algorítmica

Así se miden las operaciones.

n (o x en este caso) es el input. Puede tomarse como la longitud del input tmb, o qué tan grande es.

La idea es que el O(n) muestre lo que más está afectando negativamente a la función a medida que n se acerca a infinito. Las cosas como constantes o pequeñas, se volverán despreciables hacia el infinito.

![image.png](attachment:a5bec048-6299-40df-9d12-2c4448805cac:image.png)

Pero mediante crece X, mucha parte de esa función final pues no importa, lo que más afecta es el X^2

Eso es O(n), te muestra lo importante.

## Complejidades

![image.png](attachment:9021e457-0426-4e18-aa6c-a2774d272c63:image.png)

O(n^2) en este caso

![image.png](attachment:e5f9946d-101a-472f-90bc-dbb4f047fd58:image.png)

![image.png](attachment:938000c9-82e7-477b-a0f2-07a9ce41901b:image.png)

![image.png](attachment:845dc126-c3dc-4ea4-b225-0d29359b942f:image.png)

![image.png](attachment:81a9aec1-9029-42f9-bf65-bb480c88cf30:image.png)

1. **O(1) — Tiempo constante:**
    - El tiempo no depende del tamaño de la entrada.
    - Ejemplo: Acceder a un elemento en un array por índice.
2. **O(log⁡ n) — Tiempo logarítmico:**
    - Se reduce el tamaño del problema a la mitad en cada paso.
    - Ejemplo: Búsqueda binaria.
3. **O(n) — Tiempo lineal:**
    - El tiempo crece proporcionalmente al tamaño de la entrada.
    - Ejemplo: Recorrer un array una vez.
4. **O(n log⁡ n)  — Tiempo lineal-logarítmico:**
    - Combina una división logarítmica con un procesamiento lineal en cada nivel.
    - log n niveles, y en cada uno se procesa n. O(n) * O(log n) = **O(n log⁡ n)**
    - Ejemplo: MergeSort, QuickSort (en promedio).
5. **O(n^2) — Tiempo cuadrático:**
    - Se realizan operaciones anidadas sobre cada elemento.
    - Ejemplo: Bubble Sort, comparar todos contra todos.
6. **O(2^n) — Tiempo exponencial:**
    - Cada paso genera múltiples llamadas recursivas.
    - Ejemplo: Fibonacci recursivo sin optimización.
7. **O(n!) — Tiempo factorial:**
    - Explora todas las permutaciones posibles.
    - Ejemplo: Resolver el problema del viajero (TSP) con fuerza bruta.

Cada complejidad refleja cuántas operaciones se necesitan a medida que crece el tamaño del problema. ¿Quieres que profundice en alguno?

## Ley de la suma

Si hay dos cosas secuencialmente, se suman. Pero no se usan los coeficientes, y sólo queda la cosa más compleja (n + n^2) ⇒ (n^2)

![image.png](attachment:39fc361e-3023-48d8-ac57-d3f3a72fa15f:image.png)

![image.png](attachment:c315145f-d787-459c-be1b-15790e5a22ec:image.png)

## Ley de la multiplicación

Se usa para cuando están anidados. Lo de un nivel se multiplica con lo del nivel que tenga adentro.

![image.png](attachment:cb091194-3d80-4518-9fcd-0ede7b24d1e1:image.png)

También se usa por la cantidad de llamadas recursivas de nuestra función. Aquí es 2 porque se llama 2 veces. 

Cada que crece n por 1, los llamados se duplican, por eso 2**n, queda como un arbol binario.

![image.png](attachment:50b2bd52-057b-473d-9794-092d6b268fca:image.png)

# Otras complejidades

- **Peor de los casos**: O(n)
- **Mejor de los casos**: Ω(n)
- **Caso promedio**: Análisis específico o Θ(n) si es aplicable.

## **Big Omega (Ω)**:

Esta notación se utiliza para describir la complejidad en el mejor de los casos. Indica un límite inferior para el tiempo de ejecución de un algoritmo. Por ejemplo, si un algoritmo tiene una complejidad de Ω(n), significa que en el mejor de los casos, el tiempo de ejecución no será menor que una constante multiplicada por n.

## **Big Theta (Θ)**:

Esta notación se utiliza para describir la complejidad en el caso promedio o cuando el tiempo de ejecución de un algoritmo es aproximadamente el mismo en el peor y en el mejor de los casos. Si un algoritmo tiene una complejidad de Θ(n), significa que el tiempo de ejecución es tanto O(n) como Ω(n), es decir, crece linealmente con el tamaño de la entrada.

## **Notación de caso promedio**:

Aunque no tiene un símbolo específico como Big O, Big Omega o Big Theta, el análisis del caso promedio se refiere a la evaluación del tiempo de ejecución de un algoritmo considerando todas las entradas posibles y su probabilidad de ocurrencia.
