from rest_framework import routers, serializers, viewsets
from products.models import Catagory,product,ForCart

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catagory
        fields = "__all__"

class productSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = product
        fields = "__all__"        

class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    # category = serializers.SerializerMethodField('get_status_display') 
    class Meta:
        model = product
        fields = "__all__"  
    # def get_status_display(self, obj):
    #     return obj.get_status_display()    

# class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    # class Meta:
    #     model = product
    #     fields = '__all__'
# class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
#     product_url = serializers.HyperlinkedIdentityField(view_name='ProductDetail', lookup_field='pro_slug')

#     class Meta:
#         model = product
#         fields = '__all__'


class addtocartSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = ForCart
        fields = ['name','price','id']

class displaycartSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = ForCart
        fields = ['name','price','id']


