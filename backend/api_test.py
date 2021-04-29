import api
import datetime
import unittest

class TestAPI(unittest.TestCase):

    def test_build_response(self):
        pass
    
    def test_is_any_none(self):
        self.assertFalse(api.is_any_none())
        self.assertFalse(api.is_any_none("hello", "world", 123))
        self.assertTrue(api.is_any_none("hello", None, "world"))
        self.assertTrue(api.is_any_none(None, None, None))
    
    def test_generate_error(self):
        pass

    def test_get_route(self):
        pass

    def test_get_uber_rides(self):
        pass

    def test_get_lyft_rides(self):
        pass

    def test_get_rides(self):
        pass
    
    def test_locstring(self):
        self.assertEquals(api.locstring(0.1, 0.2), "0.1,0.2")

    def test_random_time_in_range(self):
        lower = 10
        upper = 20
        now = datetime.datetime.now()
        time = datetime.datetime.fromisoformat(api.random_time_in_range(lower, upper))
        self.assertTrue(now + datetime.timedelta(seconds=(lower * 60)) <= time)
        self.assertTrue(time <= now + datetime.timedelta(seconds=(upper * 60)))

if __name__ == "__main__":
    unittest.main()
