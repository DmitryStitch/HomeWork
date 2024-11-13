import unittest
import Runner_2

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.Усейн = Runner_2.Runner("Усейн", speed=10)
        self.Андрей = Runner_2.Runner("Андрей", speed=9)
        self.Ник = Runner_2.Runner("Ник", speed=3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        self.Усейн.challenge(self.Андрей)
        self.assertEqual(self.Усейн.distance, 10)
        self.assertEqual(self.Андрей.distance, 0)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        self.Усейн.run()
        self.assertEqual(self.Усейн.distance, 10)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        self.Усейн.walk()
        self.assertEqual(self.Усейн.distance, 1)


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
        tournament = Runner_2.Tournament(90, self.Усейн, self.Ник)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        tournament = Runner_2.Tournament(90, self.Андрей, self.Ник)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        tournament = Runner_2.Tournament(90, self.Усейн, self.Андрей, self.Ник)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)

