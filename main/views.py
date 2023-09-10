from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'T-Shirt Garis Lengan Pendek',
        'price': 'Rp.199.000',
        'description': 'T-Shirt dengan bahan katun kualitas terbaik dari Indonesia dengan motif garis garis',
        'amount': 25
    }

    return render(request, "main.html", context)