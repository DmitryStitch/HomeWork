import unittest
import Runner

class RunnerTest(unittest.TestCase):
    def test_salk(self):
        runner = Runner.Runner("John")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Distance should be 50 after 10 walks")

    def test_run(self):
        runner = Runner.Runner("Jane")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Distance should be 100 after 10 runs")

    def test_challenge(self):
        runner1 = Runner.Runner("Alice")
        runner2 = Runner.Runner("Bob")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, "Distances should be different after challenge")

    if __name__ == '__main__':
        unittest.main()
