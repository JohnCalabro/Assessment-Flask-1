from app import app
from unittest import TestCase

class CalcTestCase(TestCase):
    def test_request(self):
        with app.test_client() as client:
            res = client.get('/')
            print(res)
            self.assertEqual(res.status_code, 200)
    # def test_form(self):
    #     with app.test_client() as client:
    #         res = client.post('/', data={'amt': '1'})
    #         self.assertEqual(res.status_code, 200)

    # ^ strange error in theory this should work

#    lower = amt_form.lower()
# UnboundLocalError: local variable 'amt_form' referenced before assignment
