from .models import Item, Categories
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializers, CategorySerializers
from django.db.models import Q
from math import radians, cos, sin, asin, sqrt
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
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

@api_view(['PUT', 'GET'])
def itemUpdate(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item does not exist'})

    serializer = ItemSerializers(instance=item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def itemDelete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("ITEM DELETED")

#Calculating the distance between request maker and the Item Object
EARTH_RADIUS_KM =6371
@api_view(['GET'])
def calculate_distance(request):
    user_lat= float(request.query_params.get('user_latitude'))
    user_lon= float(request.query_params.get('user_longitude'))

    item_locations = Item.objects.all()
    distances_km = []
    #For loop through objects and get their locations
    for item_location in item_locations:
        item_id = item_location.id
        item_lat = float(item_location.latitude)
        item_lon = float(item_location.longitude)
        #make copies of every user lat and long to use inside the loop
        ulat, ulon = user_lat, user_lon
        #convert decimal degrees to radians
        ulat, ulon, item_lat, item_lon = map(radians, [ulat, ulon, item_lat, item_lon])
        #Haversine formula
        dlon = item_lon - ulon
        dlat = item_lat - ulat
        a = sin(dlat/2)**2 + cos(ulat) * cos(item_lat) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        distance_km = EARTH_RADIUS_KM * c
        #append every object distance to an array linked to its respective item id
        distances_km.append({'item_id': item_id, 'distance_kms': distance_km})

    return Response({'distances': distances_km})

# # GETTING ITEMS BASED ON DISTANCE QUERY
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

@api_view(['GET'])
def itemListCategories(request):
    queryset = Item.objects.all()

    # Obtenemos las palabras de búsqueda desde los parámetros de la solicitud
    search_categories = request.query_params.get('categories', None)
    
    if search_categories:
        # Convertimos las palabras de búsqueda en una lista de categorías
        categories = search_categories.split(',')

        # Creamos una consulta que busque cualquier artículo que tenga al menos una categoría que coincida con las palabras de búsqueda
        category_query = Q()
        for category in categories:
            category_query |= Q(categories__contains=category)
        
        queryset = queryset.filter(category_query)

    serializer = ItemSerializers(queryset, many=True)
    return Response(serializer.data)

#views-increment-update
@api_view(['GET'])
def viewsUpdate(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item does not exist'})

    serializer = ItemSerializers(instance=item, data=request.data, partial=True)
    
    if serializer.is_valid():
        item.views += 1  # increment the views field by 1
        item.save()  # save the updated instance to the database
        serializer.save()  # update the instance with the serializer data
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#views-increment-update
@api_view(['GET'])
def likesUpdate(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item does not exist'})

    serializer = ItemSerializers(instance=item, data=request.data, partial=True)
    
    if serializer.is_valid():
        item.likes += 1  # increment the views field by 1
        item.save()  # save the updated instance to the database
        serializer.save()  # update the instance with the serializer data
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def dislikeUpdate(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item does not exist'})

    serializer = ItemSerializers(instance=item, data=request.data, partial=True)
    
    if serializer.is_valid():
        item.likes -= 1  # increment the views field by 1
        if item.likes > 0:
            item.save()  # save the updated instance to the database
            serializer.save()
        else:
            item.likes = 0
            item.save()
            serializer.save()  # update the instance with the serializer data
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def categoryCreate(request):
    serializer = CategorySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"status": "Category succesfully created"})

@api_view(['GET'])
def getCategories(request):
    items = Categories.objects.all()
    serializer = CategorySerializers(items, many=True)
    return Response(serializer.data)