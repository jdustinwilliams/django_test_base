from django import forms


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=255, required=False, label="Search Products"
    )
