import django_filters
from items.models import Item


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name' ,label='نام:')
    hero = django_filters.CharFilter(lookup_expr='icontains', field_name='hero' ,label='هیرو:')
    price_gt = django_filters.NumberFilter(lookup_expr='gt', field_name='price', label='قیمت بیشتر از:')
    price_lt = django_filters.NumberFilter(lookup_expr='lt', field_name='price', label='قیمت کمتر از:')
    class Meta:
        model = Item
        fields = ['name','hero' , 'price_gt', 'price_lt' , 'rarities', 'type']