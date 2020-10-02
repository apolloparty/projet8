from django.test import TestCase
from django.urls import reverse
from .models import Product_vanilla, Product_saved
from django.contrib.auth.models import User
# Create your tests here.

# Datadisp views
class Home_page_test_case(TestCase):


    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class Datadisp_page_test_case(TestCase):


    def setUp(self):
        product_instance = Product_vanilla.objects.create(
            id = 1,
            product = "pizza aux noix",
            brand = "testeur",
            nutriscore = "a",
            image_url = "www.lafa.com",
            category = "pizza",
            energy = "1",
            energy_kcal = "1", 
            fat = "1",
            saturated_fat = "1",
            carbohydrates = "1",
            sugar = "1",
            protein = "1",
            salt = "8",
            url = "www.blabla.com"
        )

        user_instance = User.objects.create(username = "fostin")
        user_instance.set_password("password")
        user_instance.save()
        self.user_instance = user_instance

        Product_saved.objects.create(
            id = 1,
            product_requested = product_instance,
            user = user_instance
        )

    def test_datadisp(self):
        """
        """
        response = self.client.post('/datadisp', {
            'product_search': 'pizza'
            })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'datadisp.html')
        self.assertEquals(Product_vanilla.objects.first().product, 'pizza aux noix')

    def test_saved_check_details(self):
        """
        """
        response = self.client.post('/saved', {
            'btn_details': ['1', '1', 'pizza']
        })
        self.assertEquals(response.status_code, 200)

    def test_myfood_favorite_exist(self):
        self.client.login(username= "fostin", password = "password")
        """
        # Error id already exist meansthere is already something on id:1
        response = self.client.post("/myfood", {
            'btn_save': ['1', '1', 'pizza']
        })
        """
        self.assertEquals(Product_saved.objects.first().user, self.user_instance)
        print(Product_saved.objects.get(id=1))

    def test_myfood_delete_favorite(self):
        self.client.login(username= "fostin", password = "password")
        response = self.client.post("/myfood", {
            'btn_delete': '1' 
        })
        self.assertEquals(response.status_code, 200)
        saved_list = list(Product_saved.objects.values())
        self.assertEquals(len(saved_list), 0)

    def test_myfood_connected(self):
        self.client.login(username= "fostin", password = "password")
        response = self.client.get(reverse('myfood'))
        self.assertTemplateUsed("myfood")
        self.assertEqual(response.status_code, 200)