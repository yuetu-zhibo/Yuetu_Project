from unittest import TestCase
import requests

base_url = 'http://localhost:8080/user/'


class TestSearch(TestCase):
    def test_search(self):
        url = base_url+"search/"
        data = {
            "userid":"000001"
        }
        resp = requests.post(url,json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('status'), 0)

        print(resp.json())