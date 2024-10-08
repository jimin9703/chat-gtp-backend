from rest_framework.serializers import Serializer

from board.entity.models import Board


class BoardSerializer(Serializer):
    class Meta:
        model = Board
        fields =['boardId', 'boardName', 'boardContext', 'boardWriter', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']