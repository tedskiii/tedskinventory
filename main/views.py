from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = [
        {
            'name': 'T-Shirt Garis Lengan Pendek',
            'price': 'Rp.199.000',
            'description': 'T-Shirt dengan motif garis-garis dari bahan kualitas terbaik di Indonesia',
            'amount': 25,
        },
        {   
            'name': 'Celana Jeans Slim Fit',
            'price': 'Rp.299.000',
            'description': 'Celana jeans dengan potongan slim fit dari bahan kualitas terbaik di Indonesia',
            'amount': 15,
        },
        {
            'name': 'Jaket Casual',
            'price': 'Rp.399.000',
            'description': 'Jaket casual dengan desain trendy dari bahan kualitas terbaik di Indonesia',
            'amount': 10,
        },
        {
            'name': 'Sepatu Sneakers',
            'price': 'Rp.499.000',
            'description': 'Sepatu sneakers dengan desain sporty dari bahan kualitas terbaik di Indonesia',
            'amount': 20
        }
    ]

    context = {
        'products': products
    }

    return render(request, "main.html", context)
