from .models import Item
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializers
# Create your views here.

#Item CRUD Handles

@api_view(['GET'])
def apiOverview(request):
    return Response("API BASE POINT")

@api_view(['GET'])
def itemList(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializers(items, many=False)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def itemCreate(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"status": "Item succesfully created"})


@api_view(['POST', 'GET'])
def itemUpdate(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializers(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
     

@api_view(['DELETE'])
def itemDelete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("ITEM DELETED")



