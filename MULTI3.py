import unittest
from selenium import webdriver

class PruebaGoogle(unittest.TestCase):

    def setUp(self):
        # Configuración inicial: se ejecuta antes de cada prueba
        self.driver1 = webdriver.Chrome()
        self.driver2 = webdriver.Chrome()

    def test_titulo_google1(self):
        # Prueba en la primera instancia de Chrome
        self.driver1.get("https://www.google.com")
        titulo_pagina = self.driver1.title
        self.assertEqual(titulo_pagina, "Google", f"Título incorrecto en Chrome 1: {titulo_pagina}")

    def test_titulo_google2(self):
        # Prueba en la segunda instancia de Chrome
        self.driver2.get("https://www.google.com")
        titulo_pagina = self.driver2.title
        self.assertEqual(titulo_pagina, "Google", f"Título incorrecto en Chrome 2: {titulo_pagina}")

    def tearDown(self):
        # Limpieza posterior: se ejecuta después de cada prueba
        self.driver1.quit()
        self.driver2.quit()

if __name__ == '__main__':
    unittest.main()
