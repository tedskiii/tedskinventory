from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = [
        {
            'name': 'T-Shirt Garis Lengan Pendek',
            'price': 'Rp.199.000',
            'description': 'T-Shirt dengan bahan katun kualitas terbaik dari Indonesia dengan motif garis-garis',
            'amount': 25
        },
        {
            'name': 'Celana Jeans Slim Fit',
            'price': 'Rp.299.000',
            'description': 'Celana jeans dengan potongan slim fit dengan bahan kualitas terbaik dari Indonesia yang nyaman digunakan sehari-hari',
            'amount': 15
        }
    ]

    context = {
        'products': products
    }

    return render(request, "main.html", context)
