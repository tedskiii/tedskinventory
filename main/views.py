from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = [
        {
            'name': 'T-Shirt Garis Lengan Pendek',
            'image_url': 'https://image.uniqlo.com/UQ/ST3/AsianCommon/imagesgoods/437241/item/goods_69_437241.jpg?width=750', 
            'price': 'Rp.199.000',
            'description': 'T-Shirt dengan motif garis-garis dari bahan kualitas terbaik di Indonesia',
            'amount': 25,
        },
        {
            'name': 'Jaket Casual',
            'image_url': 'https://image.uniqlo.com/UQ/ST3/AsianCommon/imagesgoods/459591/sub/goods_459591_sub14.jpg?width=750',
            'price': 'Rp.249.000',
            'description': 'Jaket casual dengan desain trendy dari bahan kualitas terbaik di Indonesia',
            'amount': 10,
        },
        {
            'name': 'Celana Jeans Slim Fit',
            'image_url': 'https://image.uniqlo.com/UQ/ST3/AsianCommon/imagesgoods/459688/sub/goods_459688_sub14.jpg?width=750',
            'price': 'Rp.299.000',
            'description': 'Celana jeans dengan potongan slim fit dari bahan kualitas terbaik di Indonesia',
            'amount': 15,
        },
    ]

    context = {
        'products': products
    }

    return render(request, "main.html", context)

