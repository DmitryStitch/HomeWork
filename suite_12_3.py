import unittest
import test_12_3 # Импортируем модуль test_12_3

# Создаем объект TestSuite
test_suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest)) # Добавляем тесты RunnerTest
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest)) # Добавляем тесты TournamentTest

# Создаем объект TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тесты
result = runner.run(test_suite)