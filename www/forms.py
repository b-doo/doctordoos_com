from mezzanine.conf import settings
from cartridge.shop.forms import OrderForm, AddProductForm
from django import forms
from www.models import DDLPFeedback, FrequentlyAskedQuestion

class DDLPOrderForm(OrderForm):
    """
        customizations order form
    """
    def __init__(self, request, step, data=None, initial=None, errors=None):
        super(DDLPOrderForm, self).__init__(request, step, data, initial, errors)

        if not isinstance(self.fields['billing_detail_first_name'].widget, forms.HiddenInput):
            self.fields['billing_detail_first_name'].widget.attrs['class'] = 'form-control'
            self.fields['billing_detail_first_name'].widget.attrs['autocomplete'] = 'given-name'
        if not isinstance(self.fields['billing_detail_last_name'].widget, forms.HiddenInput):
            self.fields['billing_detail_last_name'].widget.attrs['class'] = 'form-control'
            self.fields['billing_detail_last_name'].widget.attrs['autocomplete'] = 'family-name'
        if not isinstance(self.fields['billing_detail_street'].widget, forms.HiddenInput):
            self.fields['billing_detail_street'].widget.attrs['class'] = 'form-control'
            self.fields['billing_detail_street'].widget.attrs['autocomplete'] = 'street-address'
        if not isinstance(self.fields['billing_detail_city'].widget, forms.HiddenInput):
            self.fields['billing_detail_city'].widget.attrs['class'] = 'form-control'
        if not isinstance(self.fields['billing_detail_state'].widget, forms.HiddenInput):
            self.fields['billing_detail_state'].widget.attrs['class'] = 'form-control'
        if not isinstance(self.fields['billing_detail_postcode'].widget, forms.HiddenInput):
            self.fields['billing_detail_postcode'].widget.attrs['class'] = 'form-control'
            self.fields['billing_detail_postcode'].widget.attrs['autocomplete'] = 'postal-code'
        if not isinstance(self.fields['billing_detail_country'].widget, forms.HiddenInput):
            self.fields['billing_detail_country'].widget.attrs['class'] = 'form-control'
            self.fields['billing_detail_country'].widget.attrs['autocomplete'] = 'country-name'
        if not isinstance(self.fields['billing_detail_phone'].widget, forms.HiddenInput):
            self.fields['billing_detail_phone'].widget.attrs['class'] = 'form-control'
            self.fields['billing_detail_phone'].widget.attrs['autocomplete'] = 'tel'
            self.fields['billing_detail_phone'].widget.attrs['inputmode'] = 'tel'
        if not isinstance(self.fields['billing_detail_email'].widget, forms.HiddenInput):
            self.fields['billing_detail_email'].widget.attrs['class'] = 'form-control'
            self.fields['billing_detail_email'].widget.attrs['autocomplete'] = 'email'
            self.fields['billing_detail_email'].widget.attrs['inputmode'] = 'email'
        if not isinstance(self.fields['same_billing_shipping'].widget, forms.HiddenInput):
            self.fields['same_billing_shipping'].widget.attrs['class'] = 'form-control'
            self.fields['same_billing_shipping'].widget.attrs['style'] = 'display: inline; width: 1.5em'

        if not isinstance(self.fields['shipping_detail_first_name'].widget, forms.HiddenInput):
            self.fields['shipping_detail_first_name'].widget.attrs['class'] = 'form-control'
            self.fields['shipping_detail_first_name'].widget.attrs['autocomplete'] = 'given-name'
        if not isinstance(self.fields['shipping_detail_last_name'].widget, forms.HiddenInput):
            self.fields['shipping_detail_last_name'].widget.attrs['class'] = 'form-control'
            self.fields['shipping_detail_last_name'].widget.attrs['autocomplete'] = 'family-name'
        if not isinstance(self.fields['shipping_detail_street'].widget, forms.HiddenInput):
            self.fields['shipping_detail_street'].widget.attrs['class'] = 'form-control'
            self.fields['shipping_detail_street'].widget.attrs['autocomplete'] = 'street-address'
        if not isinstance(self.fields['billing_detail_city'].widget, forms.HiddenInput):
            self.fields['shipping_detail_city'].widget.attrs['class'] = 'form-control'
        if not isinstance(self.fields['shipping_detail_state'].widget, forms.HiddenInput):
            self.fields['shipping_detail_state'].widget.attrs['class'] = 'form-control'
        if not isinstance(self.fields['shipping_detail_postcode'].widget, forms.HiddenInput):
            self.fields['shipping_detail_postcode'].widget.attrs['class'] = 'form-control'
            self.fields['shipping_detail_postcode'].widget.attrs['autocomplete'] = 'postal-code'
        if not isinstance(self.fields['shipping_detail_country'].widget, forms.HiddenInput):
            self.fields['shipping_detail_country'].widget.attrs['class'] = 'form-control'
            self.fields['shipping_detail_country'].widget.attrs['autocomplete'] = 'country-name'
        if not isinstance(self.fields['shipping_detail_phone'].widget, forms.HiddenInput):
            self.fields['shipping_detail_phone'].widget.attrs['class'] = 'form-control'
            self.fields['shipping_detail_phone'].widget.attrs['autocomplete'] = 'tel'
            self.fields['shipping_detail_phone'].widget.attrs['inputmode'] = 'tel'
        if not isinstance(self.fields['additional_instructions'].widget, forms.HiddenInput):
            self.fields['additional_instructions'].widget.attrs['class'] = 'form-control'
        if not isinstance(self.fields['remember'].widget, forms.HiddenInput):
            self.fields['remember'].widget.attrs['class'] = 'form-control'
            self.fields['remember'].widget.attrs['style'] = 'display: inline;width: 1.5em'


        if not isinstance(self.fields['card_name'].widget, forms.HiddenInput):
            self.fields['card_name'].widget.attrs['class'] = 'form-control'
            self.fields['card_name'].widget.attrs['autocomplete'] = 'cc-name'
        if not isinstance(self.fields['card_type'].widget, forms.HiddenInput):
            self.fields['card_type'].widget = forms.Select(choices=((x,x) for x in settings.SHOP_CARD_TYPES), attrs={'class': 'form-control', 'autocomplete': 'cc-type'})
        if not isinstance(self.fields['card_expiry_month'].widget, forms.HiddenInput):
            self.fields['card_expiry_month'].widget.attrs['class'] = 'form-control'
            self.fields['card_expiry_month'].widget.attrs['autocomplete'] = 'cc-exp-month'
        if not isinstance(self.fields['card_expiry_year'].widget, forms.HiddenInput):
            self.fields['card_expiry_year'].widget.attrs['class'] = 'form-control'
            self.fields['card_expiry_year'].widget.attrs['autocomplete'] = 'cc-exp-year'
        if not isinstance(self.fields['card_number'].widget, forms.HiddenInput):
            self.fields['card_number'].widget.attrs['class'] = 'form-control'
            self.fields['card_number'].widget.attrs['inputmode'] = 'numeric'
            self.fields['card_number'].widget.attrs['autocomplete'] = 'cc-number'
        if not isinstance(self.fields['card_ccv'].widget, forms.HiddenInput):
            self.fields['card_ccv'].widget.attrs['class'] = 'form-control'
            self.fields['card_ccv'].widget.attrs['style'] = 'width: unset;'
            self.fields['card_ccv'].widget.attrs['size'] = '3'
            self.fields['card_ccv'].widget.attrs['maxlength'] = '3'
            self.fields['card_ccv'].widget.attrs['inputmode'] = 'numeric'
            self.fields['card_ccv'].widget.attrs['autocomplete'] = 'cc-csc'

class DDLPAddProductForm(AddProductForm):
    """
        customizations for product form
    """
    def __init__(self, request, product=None, initial=None, to_cart=False):
        super(DDLPAddProductForm, self).__init__(request, product=product, initial=initial, to_cart=to_cart)

        if not isinstance(self.fields['quantity'].widget, forms.HiddenInput):
            self.fields['quantity'].widget.attrs['class'] = 'form-control'
            self.fields['quantity'].widget.attrs['maxlength'] = '3'
            self.fields['quantity'].widget.attrs['style'] = 'width: unset'
        if not isinstance(self.fields['option1'].widget, forms.HiddenInput):
            self.fields['option1'].widget.attrs['class'] = 'form-control'
            self.fields['option1'].widget.attrs['style'] = 'width: unset'


class DDLPFeedbackForm(forms.ModelForm):
    class Meta:
        model = DDLPFeedback
        fields = ['name', 'email', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control'})
        }


class FAQForm(forms.ModelForm):
    class Meta:
        model = FrequentlyAskedQuestion
        exclude = []