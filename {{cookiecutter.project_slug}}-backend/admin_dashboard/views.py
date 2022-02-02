from django.shortcuts import render
from datetime import datetime

# dashboard home view
def dashboard_home(request):
	now = datetime.now()
	data = {
		'monthly_sales': order.objects.filter(placed_on__year=now.year, placed_on__month=now.month).count,
		'monthly_sales_amount': order.objects.filter(placed_on__year=now.year, placed_on__month=now.month).aggregate(Count('amount_charged')),

	}
