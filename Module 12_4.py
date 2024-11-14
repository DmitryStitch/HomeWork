import unittest
import logging
import Runner_2

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.Усейн = Runner_2.Runner("Усейн", speed=10)
        self.Андрей = Runner_2.Runner("Андрей", speed=9)
        self.Ник = Runner_2.Runner("Ник", speed=3)


    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner_2.Runner(123, 10) # Неверный тип данных для name
            logging.info('"test_run" выполнен успешно')
            runner.run()
            self.assertEqual(runner.distance, 20)
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = Runner_2.Runner("Петя", speed=-5) # Отрицательная скорость
            logging.info('"test_walk" выполнен успешно')
            runner.walk()
            self.assertEqual(runner.distance, -5) # Проверка пройдена, но это -5, логика может быть другой
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        print("Результаты забегов:")
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"Место {place}: {runner.name}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        tournament = Runner_2.Tournament(101, self.Усейн, self.Ник) # Изменено: distance=101
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        tournament = Runner_2.Tournament(101, self.Андрей, self.Ник) # Изменено: distance=101
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        tournament = Runner_2.Tournament(101, self.Усейн, self.Андрей, self.Ник) # Изменено: distance=101
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)