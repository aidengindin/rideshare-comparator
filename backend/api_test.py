import api

import asyncio
import datetime
import math
import unittest

# CWRU to FirstEnergy Stadium
SRCLAT = 41.504601
SRCLON = -81.609879
DESTLAT = 41.506088
DESTLON = -81.697403

class TestAPI(unittest.TestCase):  

    def test_build_response(self):
        response = asyncio.run(api.build_response(SRCLAT, SRCLON, DESTLAT, DESTLON))
        try:
            self.assertIsInstance(response["results"], list)
            self.assertIsInstance(response["path"], dict)
            self.assertIsInstance(response["is-above-avg"], bool)
        except KeyError as e:
            self.fail("build_response raised KeyError: " + str(e))
        
    # Test routing from CWRU to 10 Downing Street - this should fail
    def test_build_response_where_too_far(self):
        response = asyncio.run(api.build_response(SRCLAT, SRCLON, 51.503396, -0.12764))
        try:
            self.assertIsInstance(response["reasons"][0]["message"], str)
        except KeyError as e:
            if "results" in response.keys():
                self.fail("build_response successfully built a response when it should not have: " + str(response))
            else:
                self.fail("build_response raised KeyError: " + str(e))   
    
    def test_is_any_none(self):
        self.assertFalse(api.is_any_none())
        self.assertFalse(api.is_any_none("hello", "world", 123))
        self.assertTrue(api.is_any_none("hello", None, "world"))
        self.assertTrue(api.is_any_none(None, None, None))
    
    def test_generate_error(self):
        test_error = api.generateError("this is the reason for the error")
        self.assertEqual(test_error["reasons"][0]["message"], "this is the reason for the error")

    def test_get_route(self):
        path = asyncio.run(api.get_route(SRCLAT, SRCLON, DESTLAT, DESTLON))
        try:
            route = path["route"]
        except KeyError as e:
            self.fail("get_route raised KeyError: " + str(e))
    
    def test_get_route(self):
        route1 = {"distance": 3}
        route2 = {"not-distance": 3}
        self.assertEqual(api.get_distance(route1), 3)
        self.assertTrue(math.isnan(api.get_distance(route2)))

    def test_get_uber_rides(self):
        uber_rides = asyncio.run(api.get_uber_rides(SRCLAT, SRCLON, DESTLAT, DESTLON))
        try:
            ride = uber_rides[0]
            self.assertEqual(ride["provider"], "Uber")
            self.assertIsInstance(ride["name"], str)
            self.assertIsInstance(ride["pickup"], str)
            self.assertIsInstance(ride["arrival"], str)
            self.assertIsInstance(ride["price"], float)
            self.assertIsInstance(ride["seats"], int)
            self.assertIsInstance(ride["shared"], bool)
        except KeyError as e:
            self.fail("get_uber_rides raised KeyError: " + str(e))

    def test_get_lyft_rides(self):
        lyft_rides = asyncio.run(api.get_lyft_rides(SRCLAT, SRCLON, DESTLAT, DESTLON))
        try:
            ride = lyft_rides[0]
            self.assertEqual(ride["provider"], "Lyft")
            self.assertIsInstance(ride["name"], str)
            self.assertIsInstance(ride["pickup"], str)
            self.assertIsInstance(ride["arrival"], str)
            self.assertIsInstance(ride["price"], float)
            self.assertIsInstance(ride["seats"], int)
            self.assertIsInstance(ride["shared"], bool)
        except KeyError as e:
            self.fail("get_lyft_rides raised KeyError: " + str(e))

    def test_get_rides(self):
        rides = asyncio.run(api.get_rides(SRCLAT, SRCLON, DESTLAT, DESTLON))
        try:
            ride = rides[0]
            self.assertIsInstance(ride["provider"], str)
            self.assertIsInstance(ride["name"], str)
            self.assertIsInstance(ride["pickup"], str)
            self.assertIsInstance(ride["arrival"], str)
            self.assertIsInstance(ride["price"], float)
            self.assertIsInstance(ride["seats"], int)
            self.assertIsInstance(ride["shared"], bool)
        except KeyError as e:
            self.fail("get_lyft_rides raised KeyError: " + str(e))
    
    def test_locstring(self):
        self.assertEqual(api.locstring(0.1, 0.2), "0.1,0.2")

    def test_random_time_in_range(self):
        lower = 10
        upper = 20
        now = datetime.datetime.now()
        time = datetime.datetime.fromisoformat(api.random_time_in_range(lower, upper))
        self.assertTrue(now + datetime.timedelta(seconds=(lower * 60)) <= time)
        self.assertTrue(time <= now + datetime.timedelta(seconds=(upper * 60)))

if __name__ == "__main__":
    unittest.main()
