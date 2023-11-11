from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="reviewer1",
            email="reviewer1@test.com",
            password="testpassw1234",
        )
        cls.book = Book.objects.create(
            title="Grimms Fairy Tales",
            author="Grimm Brothers",
            price="29.99",
        )
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="Fantastic!",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Grimms Fairy Tales")
        self.assertEqual(f"{self.book.author}", "Grimm Brothers")
        self.assertEqual(f"{self.book.price}", "29.99")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Grimms Fairy Tales")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Grimms Fairy Tales")
        self.assertContains(response, "Fantastic!")
        self.assertTemplateUsed(response, "books/book_detail.html")
