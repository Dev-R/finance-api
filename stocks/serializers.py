from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from stocks.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','owner', 'stock_symbol', 'stock_name', 'share_number', 'purchase_price', 'purchase_time']