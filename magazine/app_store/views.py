from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView
from django_filters.views import FilterView

from .filters import ItemsFilter
from .forms import ReviewForm, SortForm, TagsForm
from .models import Items, Reviews, Category
from cart.forms import CartAddProductForm


class MainTest(TemplateView):
    template_name = 'app_store/index.html'


class Main(FilterView):
    template_name = 'app_store/main_page.html'
    model = Items
    paginate_by = 10
    context_object_name = 'items'
    filterset_class = ItemsFilter

    def get_queryset(self):
        qs = super(Main, self).get_queryset()
        qs = qs.select_related().prefetch_related('review').all()
        sort = self.request.GET.get('choices')
        if sort is not None:
            qs = qs.order_by(sort)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        context['form'] = SortForm(self.request.GET)
        # todo нужно перехватить get_queryset и найти все продукты
        #  с выбранным тегом из категории
        # context['limited'] = Items.objects.order_by('count')[:16]
        # context['popular'] = Items.objects.order_by('-sold')[:8]
        return context


class Product(TemplateView):
    template_name = 'app_store/product.html'


class ProductDetail(DetailView):
    model = Items
    template_name = 'app_store/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['form'] = TagsForm(self.request.GET)
        context['cart_product_form'] = CartAddProductForm()
        context['review'] = ReviewForm()
        return context

    def post(self, request, pk=None, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            Reviews.objects.create(
                profile=request.user,
                item=self.get_object(),
                text=text,
            )
        return HttpResponseRedirect(reverse('store:product_detail', args=[pk]))


class CategoryDetail(DetailView):
    model = Category
    template_name = 'app_store/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['products'] = Items.objects.filter(category=self.get_object())
        return context


class About(TemplateView):
    template_name = 'app_store/about.html'


class Catalog(TemplateView):
    template_name = 'app_store/catalog.html'
