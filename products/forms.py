from django import forms


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        label="Search Products",
        widget=forms.TextInput(attrs={"class": "form-control my-1"}),
    )
