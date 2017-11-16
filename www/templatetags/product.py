from django import template
from cartridge.shop.models import Product
from cartridge.shop.forms import AddProductForm
from cartridge.shop.utils import recalculate_cart

register = template.Library()


@register.inclusion_tag('product.html', takes_context=True)
def product(context, form_class=AddProductForm, to_cart=True):
    products = Product.objects.published()
    product_single = products[0]
    request = context.request
    initial_data = {}
    initial_data["quantity"] = 1
    add_product_form = form_class(request.POST or None, product=product_single,
                                  initial=initial_data, to_cart=True)
    if request.POST:
        if add_product_form.is_valid():
            if to_cart:
                quantity = add_product_form.cleaned_data["quantity"]
                request.cart.add_item(add_product_form.variation, quantity)
                recalculate_cart(request)
                return {"redirect": "shop/checkout/"}
    return {"products": products, "add_product_form": add_product_form}
