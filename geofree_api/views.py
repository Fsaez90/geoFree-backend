from .models import Item
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializers
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
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

#GETTING ITEMS BASED ON DISTANCE QUERY
@api_view(['GET'])
def itemListDistance(request):
    # Get latitude and longitude from request parameters
    lat = request.query_params.get('lat')
    lon = request.query_params.get('lng')
    distance_param = request.query_params.get('distance')
    # Check if lat and lon are present
    if lat is None or lon is None:
        return Response({'error': 'Please provide latitude and longitude.'}, status=400)
    # Convert latitude and longitude to float and create Point object
    pnt = Point(float(lon), float(lat), srid=4326)
    # Get all objects within 5000 meters of the given point
    objects = Item.objects.annotate(distance=Distance('point', pnt)).filter(distance__lte=distance_param)
    # Serialize the objects
    serializer = ItemSerializers(objects, many=True)
    # Return the serialized objects
    return Response(serializer.data)



