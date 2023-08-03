import re
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from rest_framework import serializers
from .models import Project, Technology


# helper functions
def letter_only_validator(value):
    name = value.strip().lower().capitalize()
    if " " in value:
        raise serializers.ValidationError("No spaces allowed in the name")
    if not value.isalpha():
        raise serializers.ValidationError("Only letters allowed in the name")
    # no special characters allowed
    if re.match(r"\W", value):
        raise serializers.ValidationError("No special characters allowed in the name")
    return name


# Custom Slug Related Field that will create a new object if it doesn't exist
class CreateSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail(
                "does_not_exist", slug_name=self.slug_field, value=smart_str(data)
            )
        except (TypeError, ValueError):
            self.fail("invalid")


# Project serializer
class ProjectSerializer(serializers.ModelSerializer):
    technologies = CreateSlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Technology.objects.all(),
        allow_null=True,
        required=True,
    )

    class Meta:
        model = Project
        fields = ["id", "title", "description", "technologies", "progress", "link"]

    # create a project method
    def create(self, validated_data):
        technologies = validated_data.pop("technologies")
        project = Project.objects.create(**validated_data)
        for technology in technologies:
            technology, _ = Technology.objects.get_or_create(name=technology)
            project.technologies.add(technology)
        return project

    def update(self, instance, validated_data):
        technologies = validated_data.pop("technologies")
        project = Project.objects.get(id=instance.id)
        project.title = validated_data.get("title", project.title)
        project.description = validated_data.get("description", project.description)
        project.progress = validated_data.get("progress", project.progress)
        project.link = validated_data.get("link", project.link)
        for technology in technologies:
            technology, _ = Technology.objects.get_or_create(name=technology)
            project.technologies.add(technology)
        project.save()
        return project
