# Sources

https://platzi.com/cursos/unit-testing-python/

https://docs.python.org/3/library/unittest.html

# **Tipos de Testing:**

1. **Testing Unitario**: Verifica el correcto funcionamiento de unidades individuales de código, como funciones o métodos.
    
    Se suele automatizar y es la base del TDD (Test Driven Development)
    
2. **Testing de Integración**: Asegura que los diferentes módulos o componentes funcionen bien en conjunto.
    
    Agregué el detalle sobre probar la interacción de módulos ya probados individualmente y las formas en que se puede realizar (incremental vs. "big bang").
    
3. **Testing de Sistema**: Evalúa el sistema completo para asegurarse de que cumple con los requisitos especificados.
    
    Incorporé una referencia a **requisitos no funcionales** (rendimiento, seguridad, etc.) que son parte clave de esta fase de pruebas.
    
4. **Testing de Aceptación**: Verifica que el software satisface las necesidades del usuario final.
    
    Normalmente lo realiza el cliente o el equipo de QA en su nombre. Suele dividirse en dos subtipos: **pruebas de aceptación del usuario (UAT)** y **pruebas de aceptación operativas**.
    
5. **Testing de Regresión**: Asegura que los cambios o actualizaciones no hayan introducido nuevos errores en funcionalidades ya existentes.
    
    Añadí un comentario sobre la ***automatización***, que es muy relevante para este tipo de testing, especialmente en proyectos grandes.
    

# Unit Test

- **Pytest** es ideal si buscas una herramienta flexible, con una sintaxis más limpia y una comunidad activa que ofrece muchos plugins.
- **Unittest** es una buena opción si prefieres una herramienta integrada en la biblioteca estándar de Python y una estructura más clásica.

## Assert simple

Cuando la condición de adentro da True, no pasa nada. Cuando da False u otra cosa, raise an AssertException

```python
def calculate_total(products, discount_coupon):
    total = 0
    for product in products:
        total += (product["price"] - (discount_coupon * product["price"]))
    return total

def test_calculate_total_with_empty_list():
    print("Test passed 1")
    assert calculate_total([],0) == 0

def test_calculate_total_with_single_product():
    products = [{"name": "Product 1", "price": 10}]
    print("Test passed 2")
    assert calculate_total(products,0.10) == 9

def test_calculate_total_with_multiple_products():
    products = [{"name": "Product 1", "price": 10}, {"name": "Product 2", "price": 20}]
    print("Test passed 3")
    assert calculate_total(products,0.10) == 27

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()

```

## UnitTest

[unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)

### Crear y activar el venv

**Crear el entorno virtual** (Windows y Linux):

```bash
python -m venv .venv
```

**Activar el entorno virtual:**

- **Windows (CMD):**
    
    ```
    .venv\Scripts\activate
    ```
    
- **Windows (PowerShell):**
    
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
    
- **Linux/Mac:**
    
    ```bash
    source .venv/bin/activate
    ```
    

**Desactivar el entorno virtual** (Windows y Linux):

```bash
deactivate
```

### Folder Structure

```python
mi_proyecto/
├── .venv/
├── src/
│   ├── __init__.py
│   ├── modulo1.py
│   ├── modulo2.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_modulo1.py
│   ├── test_modulo2.py
│   └── test_utils.py
├── .gitignore
└── README.md
```

### Tests structure example

Cada función de test DEBE comenzar por test_, así unittest sabe que eso es un test. (Duh)

```python
import unittest

from src.calculator import sum, subtract

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 6

    def test_subtract(self):
        assert subtract(10, 5) == 5
```

### setUp()

Heredar este método y definirlo, nos permite ejecutar código antes de cada test. Lo que se cree, se podrá llamar desde self.

El setUp se ejecuta CADA VEZ que se ejecute otra prueba.

```python
import unittest

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800
    
    def test_get_balance(self):
        assert self.account.get_balance() == 1000
```

### tearDown()

Igual que setUp, pero en este caso se ejecuta al final de cada prueba.

### Asserts de Unittest

Lo bueno de usar estos, es que te imprime el error o qué fue lo que no era igual en cada test, además de que puedes agregarle un mensaje como parámetro si quieres `msg=<wea>`

Ejemplo:

```python
import unittest, os

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
```

- **Igualdad y desigualdad:**
    
    ```python
    assertEqual(a, b)
    assertNotEqual(a, b)
    
    ```
    
- **Verdadero y falso:**
    
    ```python
    assertTrue(x)
    assertFalse(x)
    
    ```
    
- **Nulo y no nulo:**
    
    ```python
    assertIsNone(x)
    assertIsNotNone(x)
    
    ```
    
- **Identidad:**
    
    ```python
    assertIs(a, b)
    assertIsNot(a, b)
    
    ```
    
- **Pertenencia:**
    
    ```python
    assertIn(a, b)
    assertNotIn(a, b)
    
    ```
    
- **Instancia:**
    
    ```python
    assertIsInstance(a, b)
    assertNotIsInstance(a, b)
    
    ```
    
- **Excepciones:**
    
    ```python
    assertRaises(exc, func, *args, **kwds)
    assertRaisesRegex(exc, regex, func, *args, **kwds)
    
    ```
    
- **Advertencias:**
    
    ```python
    assertWarns(warn, func, *args, **kwds)
    assertWarnsRegex(warn, regex, func, *args, **kwds)
    
    ```
    
- **Comparación de secuencias:**
    
    (También tienen NotEqual)
    
    ```python
    assertListEqual(a, b)
    assertTupleEqual(a, b)
    assertSetEqual(a, b)
    assertDictEqual(a, b)
    
    ```
    
- **Comparación general:**
    
    ```python
    assertGreater(a, b)
    assertGreaterEqual(a, b)
    assertLess(a, b)
    assertLessEqual(a, b)
    
    ```
    
- **Casi iguales (flotantes):**
    
    ```python
    assertAlmostEqual(a, b, places=7)
    assertNotAlmostEqual(a, b, places=7)
    
    ```
    
- **Errores de subproceso:**
    
    ```python
    assertLogs(logger, level)
    
    ```
    

### Skips

Existen razones para por qué quisieras saltarte una prueba

- **Saltar siempre:**
    
    ```python
    @unittest.skip("Motivo del salto")
    
    ```
    
- **Saltar si una condición es verdadera:**
    
    ```python
    @unittest.skipIf(condición, "Motivo del salto")
    
    ```
    
- **Saltar a menos que una condición sea verdadera:**
    
    ```python
    @unittest.skipUnless(condición, "Motivo del salto")
    
    ```
    
- **Salto dinámico dentro de un test:**
    
    ```python
    self.skipTest("Motivo del salto")
    
    ```
    
- **Si esperas que el test falle:**
    
    Marca un test que se espera que falle porque se supone que la funcionalidad está mala o sin terminar. Si falla, se cuenta como éxito; si pasa, se considera un error inesperado.
    
    ```python
    @unittest.expectedFailure
    ```
    

### Suites

El parámetro de `discover` en la línea de comandos, sirve para reconocer todos los archivos test de una carpeta, reconocer sus clases, y de estas sus funciones, para finalmente con todo esto crear automáticamente una suite y correrla. Pero puedes crear tu propia suite personalizada para correr lo que quieras en el orden que quieras.

```python
import unittest

from tests.test_bank_account import BankAccountTests

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
```

Y corres esa suite como cualquier código de python. Si no funciona, ve a troubleshoot.

### Patching and Mocking

Para este código:

```python
import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }

if __name__ == "__main__":
    print(get_location("8.8.8.8"))
```

El mock de la respuesta de requests.get() debería hacerse así:

```python
import unittest
from src.api_client import get_location
from unittest.mock  import patch

class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
```

### side_effect

Si quieres que se intente varias veces el usar esa función, incluso puedes hacer que algunos de esos intentos resulten mal o sean erróneos, para ver que tu aplicación no se muere y sigue corriendo. 

```python
  	@patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI",
                },
            ),
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
```

### SubTest

Quieres que se ejecute cada iteración de un mismo test como una prueba separada?, evaluable independientemente?, pues creamos subtests, y así no hay que crear función para cada una ni nada

```python
def test_deposit_multiple_ammounts(self):

        test_cases = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])
```

Acá, por cada caso se le está creando un subTest. El testing interface de VSC puede reconocer estos subtests, tienen su propio desplegable

### Ejecución

Verás, no podrás correr las pruebas si antes no las “descubres”, el runner necesita saber que esos archivos existen, así que la primera vez necesitarás agregar `discover` en el comando. Las demás veces no será necesario, aunque agregues funciones en los mismos archivos. Pero necesitarás volver a usar discover cuando agregues un archivo nuevo.

- CMD:
    - No verbose:
        
        Las pruebas que funcionaron salen como un punto. El output podría ser algo tipo  “. . . . .”. En el caso de arriba, sería `python -m unittest discover -s tests`
        
        ```bash
        python -m unittest discover -s <carpeta_de_los_tests>
        ```
        
    - Verbose:
        
        Dice qué pruebas se ejecutaron y su ubicación
        
        ```bash
        python -m unittest discover -v -s <carpeta_de_los_tests>
        ```
        
        Sólo es agregar un `-v`
        
    - Correr todos los tests de una clase específica:
        
        ```bash
        python -m <módulo/carpeta_si_hay>.<archivo>.<clase>
        ```
        
        Por ejemplo: `python -m unittest test_calculator.CalculatorTest`
        
    - Correr un test en específico de una clase específica:
        
        ```bash
        python -m <módulo_si_hay>.<archivo>.<clase>.<función_test>
        ```
        
        Por ejemplo: `python -m unittest test_calculator.CalculatorTest.test_sum`
        
    - Para correr una suite hecha a mano:
        
        ```bash
        python tests/suites.py
        - o -
        PYTHONPATH=. python tests/suites.py
        ```
        
- Visual Studio Code:
    
    Tiene su propio submenú para hacer estas cosas. Se llama Testing y se ve como uno de esos vasos de laboratorio/pociones.
    
    ![image.png](attachment:2667ab2f-6432-4338-9742-614c391a629c:image.png)
    
    Seleccionas que estás usando unittest en vez de pytest, decimo en qué carpeta están nuestras pruebas, y qué patrón de nombre siguen los archivos de estas pruebas. En nuestro caso son `test_*.py`.
    

### Troubleshooting

- Si no encuentra módulos o códigos:
    
    Usar `PYTHONPATH=<folder>` cuando lo corras en consola, para que eso sepa desde qué carpeta tiene que ponerse a buscar los archivos/módulos
    
    También poner los archivos `/__init__.py` necesarios para inicializar como módulo cada carpeta
    

## PyTest

Este tipo hizo todo el curso en PyTest, puedes ver las diferencias. Es más limpio, me habría gustado usar pytest.

https://github.com/JimcostDev/unit-testing

Es la competencia de UnitTest, pero parece que PyTest es mejor, tiene mejores funciones, está más decorada, y tales.

Por ejemplo este test:

```python
import pytest
from src.bank_account import BankAccount

@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_ammounts(ammount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected
```

### Ejecución

Aunque seguramente también tenga suites y tales, aquí correremos un solo código de tests

```bash
pytest <código>
```

También tiene la opción verbose. `pytest <código> -v`

### Tutorial simple

1. En la carpeta de pruebas, crea un archivo llamado `test_pytest.py`.
2. Importa PyTest en tu archivo:
    
    ```python
    import pytest
    
    ```
    
3. Crea una función de prueba simple como esta:
    
    ```python
    def test_suma():
        a = 4
        b = 4
        assert a + b == 8
    
    ```
    
4. Ejecuta la prueba con el siguiente comando:
    
    ```
    pytest test_pytest.py
    
    ```
    

PyTest no requiere la creación de clases para agrupar pruebas, lo cual simplifica el código. En este caso, las pruebas se agrupan por archivo.

## DocTest

Puedes correr tests en los propios comentarios, creando allí sesiones interactivas que sólo se verán cuando los resultados no sean los esperados.

### Happy path

```python
def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b
```

### Exceptions

```python
def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: La división por cero no está permitida
    """

    if b == 0:
        raise ValueError("La división por cero no está permitida")
    return a / b

```

### Ejecución

```bash
python -m doctest <ruta_del_código>
```

Sólo imprimirá errores cuando las pruebas saquen algo que no es. Parece que sólo sirve para assertEquals entonces, no es tan completo.

## Faker Usage

Pues para crear datos ficticios fácilmente, ya la has usado pibe

Para este código

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)

```

Se usó este testfile

```python
import unittest, os
from faker import Faker

from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)

    def test_user_with_multiple_accounts(self):
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension=".txt")
            )
            self.user.add_account(account=bank_account)

        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value, expected_value)

    def tearDown(self) -> None:
        for account in self.user.accounts:
            os.remove(account.log_file)

```

## Coverage

Pues lo instalas como siempre

Puedes hacer `pip freeze | grep coverage` luego del `pip install coverage`para que te dé la besto versión actual que usaste, para ponerla en requirements.

En windows, parece que eso viene siendo así: `py -m pip freeze > requirements.txt`

Se recomienda tener el proyecto por encima del 80% o 90% del coverage.

### Primera Ejecución

```bash
coverage run -m unittest discover -s tests
```

- El problema de la de arriba, es que también le saca cobertura a los tests, y no hacemos tests de los tests. Entonces mejor le pasamos un parámetro para que sepa de dónde sacar el source.
    
    ```bash
    coverage run --source src -m unittest discover -s test
    ```
    

### Reporte de cobertura en consola

```bash
coverage report
```

Saca algo tipo:

![image.png](attachment:1470db09-e8fd-4f7c-88b1-3f18cc1c0372:image.png)

### Reporte con HTML

```bash
coverage html
```

Ahora nos da el reporte en HTML para que podamos ver cada línea del código, cómo es o no cubierta. Se crea una carpeta llamada `/htmlcov` en donde está un index.html al que debemos entrar.

### Settings

Si por ejemplo quieres que salga un error si no se cumple con un mínimo del 90% del coverage, puedes colocarlo en un archivo de configuración

1. Crea un .coveragerc en la raíz del proyecto
2. Pega esto
    
    ```bash
    [report]
    fail_under = 90
    ```
    
    Y ya. Esta configuración hará que se muestre un error si tus pruebas no superan el 90% de cobertura