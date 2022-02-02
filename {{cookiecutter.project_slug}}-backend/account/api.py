from .models import (
		customer
	)

from .serializers import (
		customer_serializer,
	)

# customer api
def customer_detail_view(request):
	query = customer.objects.get(pk=request.GET.get('id'))
	serializer = customer_serializer(model=query, many=False)

	if request.method == 'GET':
		return Response(serializer.data)

	elif request.method == 'POST':
		return

	elif request.method == 'DEL':
		return

def customers_list_view(request):
	query = customer.objects.filter()
	serializer = customer_serializer(model=query, many=True)

	if request.method == 'GET':
		return Response(serializer.data)

	elif request.method == 'POST':
		return

def delete_multiple_users(request):
	if request.method == 'POST':
		customer.objects.filter().delete()
