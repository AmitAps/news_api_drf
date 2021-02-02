#https://www.django-rest-framework.org/api-guide/serializers/
#we are going to a class provided by dango, we need to import first
from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):
    #extra fields
    time_since_publication = serializers.SerializerMethodField()
    #author = JournalistSerializer(read_only=True)
    #author = serializers.StringRelatedField() #this will show author name in string format not author id

    class Meta:
        model = Article
        exclude = ("id",)
        #fields = "__all__" #we want all the fields from model
        #fields = ('title','description','body') #we want to choose a couple of fields

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """
        Object level validation.
        """
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and description must be different from one another")
        return data

    def validate_title(self, value):
        """
        field level validation.
        """
        if len(value) < 30:
            raise serializers.ValidationError("Title must be greater than 30 characters")
        return value

class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='article-detail')
    #articles = ArticleSerializer(read_only=True, many=True)

    class Meta:
        model = Journalist
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     """
#     Serializer and django forms very similar:
#     """
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body =  serializers.CharField()
#     location  = serializers.CharField()
#     publication_date = serializers.CharField()
#     active = serializers.BooleanField()
#     created_at =  serializers.DateTimeField(read_only=True)
#     updated = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         """
#         Object level validation.
#         """
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and description must be different from one another")
#         return data
#
#     def validate_title(self, value):
#         """
#         field level validation.
#         """
#         if len(value) < 60:
#             raise serializers.ValidationError("Title must be greater than 60 characters")
#         return value
