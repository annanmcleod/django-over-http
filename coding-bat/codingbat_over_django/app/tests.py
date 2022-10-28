from django.test import SimpleTestCase
from django.test import TestCase


class TestNearHundred(SimpleTestCase):
    def test_number_121(self):
        response = self.client.get("/near-hundred/93")
        self.assertContains(response, "True")

    def test_number_90(self):
        response = self.client.get("/near-hundred/90")
        self.assertContains(response, "True")

    def test_number_5(self):
        response = self.client.get("/near-hundred/89")
        self.assertContains(response, "False")


class TestStringSplosion(SimpleTestCase):
    def test_string_code(self):
        response = self.client.get("/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_string_kitten(self):
        response = self.client.get("/string-splosion/abc")
        self.assertContains(response, "aababc")

    def test_string_aab(self):
        response = self.client.get("/string-splosion/ab")
        self.assertContains(response, "aab")


class TestCatDog(SimpleTestCase):
    def test_cat_1(self):
        response = self.client.get("/cat-dog/catdog")
        self.assertContains(response, "True")

    def test_cat_2(self):
        response = self.client.get("/cat-dog/catcat")
        self.assertContains(response, "False")

    def test_cat_3(self):
        response = self.client.get("/cat-dog/1cat1cadodog")
        self.assertContains(response, "True")


class TestLoneSum(SimpleTestCase):
    def test_lone_1(self):
        response = self.client.get("/lone-sum/1/2/3")
        self.assertContains(response, "6")

    def test_lone_2(self):
        response = self.client.get("/lone-sum/3/2/3")
        self.assertContains(response, "2")

    def test_lone_3(self):
        response = self.client.get("/lone-sum/3/3/3")
        self.assertContains(response, "0")
