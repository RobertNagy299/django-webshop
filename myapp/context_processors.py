def cart_count(request):
    cart = request.session.get('cart', [])
    total_items = sum(item.get('quantity', 1) for item in cart)
    return {
        'cart_count': total_items
    }
