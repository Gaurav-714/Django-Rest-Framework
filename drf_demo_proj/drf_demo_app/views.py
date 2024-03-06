from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .serializer import TodoSerializer, TodoTimingSerializer
from .models import Todo, TodoTiming

# For Class Based Views..
from rest_framework.views import APIView

# To Create API's In A Simplest Way..
from rest_framework import viewsets 

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.core.paginator import Paginator
from .helpers import paginate

# Create your views here...

# The Simplest Way of Creating API's...
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail = False, methods = ['GET'])
    def get_todo_date(self, request):
        todo_objs = TodoTiming.objects.filter(user = request.user)

        page = request.GET.get('page', 1)
        page_obj = Paginator(todo_objs, page)
        print(page_obj)
        results = paginate(todo_objs, page_obj, page)
        print(results)

        serializer = TodoTimingSerializer(todo_objs, many = True)
        return Response({
            'status' : True ,
            'message': 'Todo Fetched',
            'data' : serializer.data
        })

    @action(detail = True, methods = ['POST'])
    def post_todo_date(self, request, pk):
        try:
            print(pk)
            data = request.data
            data['user'] = request.user.id
            serializer = TodoTimingSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : True ,
                    'message': 'Success data',
                    'data' : serializer.data
                })
            return Response({
                    'status' : False ,
                    'message': 'Invalid data',
                    'data' : serializer.errors
                })
        except Exception as ex:
            print(ex)
        return Response({
            'status' : False ,
            'message': 'Error!! Something went wrong..'
        })



# API Showing On Blank Route...
@api_view(['GET','POST','PATCH'])
def home(request):

    if request.method == 'GET':
        return Response({
            'status' : 200 ,
            'message': 'Yes!! DRF is working..',
            'method' : 'You called GET method'
        })
    
    elif request.method == 'POST':
        return Response({
            'status' : 200 ,
            'message': 'Yes!! DRF is working..',
            'method' : 'You called POST method'
        })
    
    elif request.method == 'PATCH':
        return Response({
            'status' : 200 ,
            'message': 'Yes!! DRF is working..',
            'method' : 'You called PATCH method'
        })
    
    else:
        return Response({
            'status' : 405 ,
            'message': 'Yes!! DRF is working..',
            'method' : 'You called invalid method'
        })
    

# Class Based Views To Create API's For 'GET','POST','PATCH' Inside A Single Class...
class TodoView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    ### 'GET' API...
    def get(self, request):
        todo_objs = Todo.objects.filter(user = request.user)

        page = request.GET.get('page', 1)
        page_obj = Paginator(todo_objs, page)
        print(page_obj)
        results = paginate(todo_objs, page_obj, page)
        print(results)

        serializer = TodoSerializer(todo_objs, many = True)
        return Response({
            'status' : True ,
            'message': 'Todo Fetched',
            'data' : serializer.data
        })
    
    ### 'POST' API...
    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : True ,
                    'message': 'Success data',
                    'data' : serializer.data
                })
            return Response({
                    'status' : False ,
                    'message': 'Invalid data',
                    'data' : serializer.errors
                })
        except Exception as ex:
            print(ex)
        return Response({
            'status' : False ,
            'message': 'Error!! Something went wrong..'
        })
    
    ### 'PATCH' API...
    def patch(self, request):
            try:
                data = request.data
                if not data.get('uuid'):
                    return Response({
                        'status' : False ,
                        'message': 'uid is necessary',
                        'data' : {}
                    })
                obj = Todo.objects.get(uuid = data.get('uuid'))
                serializer = TodoSerializer(obj, data = data, partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status' : True ,
                        'message': 'Success data',
                        'data' : serializer.data
                    })
                return Response({
                    'status' : False ,
                    'message': 'Invalid data',
                    'data' : serializer.errors
                })     
            except Exception as ex:
                print(ex)
            return Response({
                'status' : False ,
                'message': 'Invalid uid',
                'data' : {}
            })

    ### 'PUT' API...
    def put(self, request):
        # Code for 'PUT' API.
        pass

    ### 'DELETE' API...
    def delete(self, request):
        # Code for 'DELETE' API.
        pass
    




# Creating Seperate API's For 'GET' , 'POST' , 'PATCH' 

@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many = True)

    return Response({
        'status' : True ,
        'message': 'Todo Fetched',
        'data' : serializer.data
    })


@api_view(['POST'])
def post_todo(request):

    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True ,
                'message': 'Success data',
                'data' : serializer.data
            })
        
        return Response({
                'status' : False ,
                'message': 'Invalid data',
                'data' : serializer.errors
            })
    
    except Exception as ex:
        print(ex)
    
    return Response({
        'status' : False ,
        'message': 'Error!! Something went wrong..'
    })


api_view(['PATCH'])
def patch_todo(request):

    try:
        data = request.data
        if not data.get('uuid'):
            return Response({
                'status' : False ,
                'message': 'uid is necessary',
                'data' : {}
            })
        
        obj = Todo.objects.get(uuid = data.get('uuid'))
        serializer = TodoSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True ,
                'message': 'Success data',
                'data' : serializer.data
            })
        
        return Response({
            'status' : False ,
            'message': 'Invalid data',
            'data' : serializer.errors
        })     
    
    except Exception as ex:
        print(ex)

    return Response({
        'status' : False ,
        'message': 'Invalid uid',
        'data' : {}
    })