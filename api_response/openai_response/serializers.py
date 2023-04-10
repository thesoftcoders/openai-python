from rest_framework import serializers

class AnswerSerializer(serializers.Serializer):
    answer = serializers.CharField(max_length=1024)