from rest_framework import serializers
from places.models import Place

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()
    image = serializers.ImageField()


    def validate(self, data):
        name = data.get('name')

        if len(name)<4:
            result = {
                "status":False,
                "message": "Name len is less than 4"
            }

            raise serializers.ValidationError(result)

        address = data.get('address')

        if address.isalpha():
            result = {
                "status": False,
                "message": "Address ichida sonlar ham ishtirok etishi lozim"
            }

            raise serializers.ValidationError(result)

        return data


    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        address = validated_data.get('address')
        image = validated_data.get('image')

        Place.objects.create(
            name=name,
            address=address,
            description=description,
            image=image
        )

        return validated_data