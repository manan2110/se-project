from unicodedata import category
from urllib import response
from django.test import TestCase
from api.models import *
from django.urls import reverse

# Create your tests here.


def test_lists_all_shops(self):
    response = self.client.get(reverse("shops"))
    self.assertEqual(response.status_code, 200)
    self.assertTrue("is_paginated" in response.context)
    self.assertTrue(response.context["is_paginated"] == True)
    self.assertEqual(len(response.context["shop_list"]), 10)


def test_redirect_if_not_logged_in(self):
    response = self.client.get(reverse("add_subscription"))
    self.assertRedirects(response, "/login")


def test_logged_in_uses_correct_template(self):
    login = self.client.login(username="manan.co.in@gmail.com", password="test@123")
    response = self.client.get(reverse("add_subscription"))

    # Check our user is logged in
    self.assertEqual(str(response.context["user"]), "manan.co.in@gmail.com")
    # Check that we got a response "success"
    self.assertEqual(response.status_code, 200)
    # Check if we used correct template
    self.assertTemplateUsed(response, "add_subscription/")
