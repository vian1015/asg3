from django.shortcuts import render
from wishlist.models import ItemWishlist
from django.shortcuts import render

# Create your views here.
def show_wishlist(request):
    data_wishlist_item = ItemWishlist.objects.all()
    context = {
        'list_item': data_wishlist_item,
        'name': 'Jovian'
    }

    return render(request, "wishlist.html", context)
