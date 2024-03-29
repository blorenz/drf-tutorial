from django.forms import widgets
from rest_framework import serializers
from snippets import models
from snippets.models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer2(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()
    title = serializers.CharField(required=False,
                                max_length=100)
    code = serializers.CharField(widget=widgets.Textarea,
                                max_length=100000)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=models.LANGUAGE_CHOICES,
                                    default='python')
    style = serializers.ChoiceField(choices=models.STYLE_CHOICES,
                                    default='friendly')

    def restore_object(self, attrs, instance=None):
        """Create or update a new snippet instance"""
        if instance:
            instance.title = attrs['title']
            instance.code = attrs['code']
            instance.linenos = attrs['linenos']
            instance.language = attrs['language']
            instance.style = attrs['style']
            return instance

        return models.Snippet(**attrs)
    
