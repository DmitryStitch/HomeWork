import unittest
import Runner_2

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        print("Результаты забегов:")
        cls.all_results = {}

    def setUp(self):
        self.Усейн = Runner_2.Runner("Усейн", speed=10)
        self.Андрей = Runner_2.Runner("Андрей", speed=9)
        self.Ник = Runner_2.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"Место {place}: {runner.name}")

    def test_Усейн_Ник(self):
        tournament = Runner_2.Tournament(90, self.Усейн, self.Ник)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)
        self.all_results = {place: runner.name for place, runner in self.all_results.items()}
        print(self.all_results)

    def test_Андрей_Ник(self):
        tournament = Runner_2.Tournament(90, self.Андрей, self.Ник)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)
        self.all_results = {place: runner.name for place, runner in self.all_results.items()}
        print(self.all_results)

    def test_Усейн_Андрей_Ник(self):
        tournament = Runner_2.Tournament(90, self.Усейн, self.Андрей, self.Ник)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.Ник)
        self.all_results = {place: runner.name for place, runner in self.all_results.items()}
        print(self.all_results)

if __name__ == '__main__':
    unittest.main()
