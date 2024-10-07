from django.forms import ModelForm
from main.models import Product

from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'bouquet_type', 'wrap_color']

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_wrap_color(self):
        wrap_color = self.cleaned_data["wrap_color"]
        return strip_tags(wrap_color)