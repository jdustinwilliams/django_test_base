from django.views.generic import ListView, DetailView

from .models import Product
from .forms import ProductSearchForm


class ProductListView(ListView):
    model = Product
    paginate_by = 10

    extra_context = {"search_form": ProductSearchForm()}

    def get_queryset(self):
        search_query = self.request.GET.get("search_query")

        if search_query:
            return Product.objects.filter(name__icontains=search_query)
        else:
            return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
