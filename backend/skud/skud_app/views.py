from django.shortcuts import render
from rest_framework import viewsets
from .models import Log
from .serializers import LogSerializer
# Create your views here.
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Article, Log
# from .serializers import LogSerializer
# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets
# from rest_framework.routers import DefaultRouter
# class ArticleView(APIView):
    # def get(self, request):
        # articles = Article.objects.all()
        # serializer = ArticleSerializer(articles, many=True)
        # return Response({"articles": serializer.data})	
    # def post(self, request):
        # article = request.data.get('article')
        # # Create an article from the above data
        # serializer = ArticleSerializer(data=article)
        # if serializer.is_valid(raise_exception=True):
            # article_saved = serializer.save()
        # return Response({"success": "Article '{}' created successfully".format(article_saved.title)})			
    # def put(self, request, pk):
        # saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        # data = request.data.get('article')
        # serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        # if serializer.is_valid(raise_exception=True):
            # article_saved = serializer.save()
        # return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
    # def delete(self, request, pk):
    # # Get object with this pk
        # article = get_object_or_404(Article.objects.all(), pk=pk)
        # article.delete()
        # return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)
		
# class LogsView(viewsets.ViewSet):
    # def list(self, request):
        # queryset = Log.objects.all()
        # serializer = LogSerializer(queryset, many=True)
        # return Response(serializer.data)
    # def retrieve(self, request, pk=None):
        # queryset = Log.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        # serializer = LogSerializer(user)
        # return Response(serializer.data)
		
class LogsViewSet(viewsets.ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()