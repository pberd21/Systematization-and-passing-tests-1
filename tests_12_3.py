import unittest
from runner import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrei = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Test Walker", speed=5)
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Test Runner", speed=5)
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        RunnerTest.all_results[1] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrei = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results[1] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results[2] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results[3] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")


if __name__ == "__main__":
    unittest.main()