from datadisp.dataexploit import Datagrab
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.db.models import Max
from django.contrib import messages
from .models import Product_vanilla
from .models import Product_saved
from django.contrib.auth.models import User
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
# Create your views here.
def home(request):
    """
    Followed request methods permit to take input tag
    """
    return render(request, 'home.html')

def datadisp(request):
    product_generic = ""
    random_list = []
    id_list2 = []
    obj_list = []
    product_list = [
        "pizza", 
        "ice tea", 
        "pâte à tartiner", 
        "sandwich", 
        "gateaux apéritifs", 
        "salade", 
        "biscuit au chocolat", 
        "compote", 
        "soupe"
        ]
    if 'product_search' in request.POST:
        product_name = (request.POST.get('product_search'))
        if product_name in product_list:
            product_generic = request.POST['product_search']
        else:
            messages.error(request, "Produit non présent dans la base de donnée")
            return redirect(home)
    else:
        context = {}
    """
    # alternative with overall products
    if 'product_search' in request.POST:
        product_generic = (request.POST.get('product_search'))
        vanilla = Datagrab(product_generic).vanilla_product()
        #Permit to add product into database 
        while x != 100:  
            p = Product_vanilla(\
                product = vanilla[x]['name'], \
                brand = vanilla[x]['brand'], \
                nutriscore = vanilla[x]['nutriscore'], \
                image_url = vanilla[x]['image'], \
                category = product_generic, \
                energy = vanilla[x]['energy'], \
                energy_kcal = vanilla[x]['energy_kcal'], \
                fat = vanilla[x]['fat'], \
                saturated_fat = vanilla[x]['saturated_fat'], \
                carbohydrates = vanilla[x]['carbohydrates'], \
                sugar = vanilla[x]['sugar'], \
                protein = vanilla[x]['protein'], \
                salt = vanilla[x]['salt'], \
                url = vanilla[x]['url'], \
                )
            p.save()
            x = x + 1
    else:
        context = {}
    """

    #convert django quieries into dict of dict
    id_list = list(Product_vanilla.objects.filter(
        category=product_generic).values())
    id_len = len(id_list)
    print("id_len :", id_len)

    # randomise selection of products
    for i in range(6):
        randomize = random.randint(1, id_len)
        random_list.append(randomize)
    print("random_list :", random_list)
    for y in random_list:
        print("y:", y)
        id_list2.append(id_list[y-1]['id'])
    
    # products randomized
    for x in range(6):
        globals()[f"obj{x}"] = Product_vanilla.objects.filter(
            category=product_generic
        ).filter(
            id=id_list2[x-1]).values()

    # products substitutes
    nutrigrade = "a"
    nutri_check = False
    product_subs = []
    rest = 6
    while nutri_check == False: 
        print("nutrigrade cherché :", nutrigrade)
        temp = Product_vanilla.objects.filter(
                category=product_generic
            ).filter(
                nutriscore=nutrigrade).values()
        product_sum = len(temp)
        for indi_products in range(product_sum):
            print("indi",indi_products)
            product_subs.append(temp[indi_products])
        if rest > 0:
            rest = rest - product_sum
            nutrigrade = chr(ord(nutrigrade) + 1)
            if nutrigrade == "f":
                break
        if rest <= 0:
            nutri_check = True
        print(rest, product_sum)
        print("nombre de produits de substitutions:", len(product_subs))
        print(product_subs[2])
        
    # convert django queries to str
    obj_raw_list = [obj0, obj1, obj2, obj3, obj4, obj5, product_subs]
    for obj_temp in obj_raw_list:
        for obj in obj_temp:
            obj_list.append(obj)
    # return context
    context = {
        "product1":obj_list[0],
        "product2":obj_list[1],
        "product3":obj_list[2],
        "product4":obj_list[3],
        "product5":obj_list[4],
        "product6":obj_list[5],
        "product_substitutes": product_subs,
        "product_overall":product_generic
    }
    return render(request, 'datadisp.html', context)

def saved(request):
    """
        Recupérer par getlist l'id des produits,
        afficher l'ensemble du produit depuis PSQL
    """
    context = {}
    if 'btn_details' in request.POST:
        save_list = request.POST.getlist('btn_details')
        obj_saved = Product_vanilla.objects.get(id=save_list[0])
        context = {
            "obj_saved":obj_saved,
        }

    return render(request, 'saved.html', context)

@login_required(login_url='myaccount2')
def myfood(request):
    context = {}
    obj_favorite = []
    obj_test = []
    user_id = request.user.id
    user_name = User.objects.get(id=user_id)
    # DB input
    if 'btn_save' in request.POST:
        save_list = request.POST.getlist('btn_save')
        obj_saved = Product_vanilla.objects.get(id=save_list[0])
        p = Product_saved(\
                product_requested = obj_saved, \
                user = user_name, \
                )
        p.save()
    if 'btn_delete' in request.POST:
        obj_saved = request.POST.getlist('btn_delete')
        instance = Product_saved.objects.filter(product_requested=obj_saved[0])
        instance.delete()
    # Displaying part
    user_obj = list(Product_saved.objects.filter(
            user=user_id).values()) # get the multiple users saved product
    #print(user_obj)
    for i in range(0, len(user_obj)): # get whole id of favorite
        print(f"ID Favori {i}: ", user_obj[i]['product_requested_id'])
        obj_favorite.append(user_obj[i]['product_requested_id'])
    for i in obj_favorite:
        print(i)
        obj_saved = Product_vanilla.objects.get(id=i)
        obj_test.append(obj_saved)

    context = {
        "user_name": user_name,
        "obj_favorite": obj_favorite,
        "obj_test": obj_test
    }
    return render(request, 'myfood.html', context)

def contact(request):
    return render(request, 'contact.html')

"""
def account(request):
    return render(request, 'account.html')
"""