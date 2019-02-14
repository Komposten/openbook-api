from django.conf import settings
from rest_framework import serializers

from openbook.settings import COLOR_ATTR_MAX_LENGTH
from openbook_categories.models import Category
from openbook_categories.validators import category_name_exists
from openbook_common.validators import hex_color_validator
from openbook_communities.models import Community
from openbook_communities.serializers_fields import IsMemberField, IsInvitedField, IsCreatorField
from openbook_communities.validators import community_name_characters_validator, community_name_not_taken_validator


class CreateCommunitySerializer(serializers.Serializer):
    type = serializers.ChoiceField(allow_blank=False, choices=Community.COMMUNITY_TYPES)
    name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                 allow_blank=False, validators=[community_name_characters_validator])
    title = serializers.CharField(max_length=settings.COMMUNITY_TITLE_MAX_LENGTH,
                                  allow_blank=False)
    description = serializers.CharField(max_length=settings.COMMUNITY_DESCRIPTION_MAX_LENGTH,
                                        allow_blank=True, required=False)
    rules = serializers.CharField(max_length=settings.COMMUNITY_RULES_MAX_LENGTH,
                                  allow_blank=True, required=False)
    user_adjective = serializers.CharField(max_length=settings.COMMUNITY_USER_ADJECTIVE_MAX_LENGTH,
                                           allow_blank=True, required=False)
    users_adjective = serializers.CharField(max_length=settings.COMMUNITY_USERS_ADJECTIVE_MAX_LENGTH,
                                            allow_blank=True, required=False)
    avatar = serializers.ImageField(required=False)
    cover = serializers.ImageField(required=False)
    invites_enabled = serializers.BooleanField(required=False, allow_null=False)
    color = serializers.CharField(max_length=COLOR_ATTR_MAX_LENGTH, required=True,
                                  validators=[hex_color_validator])
    categories = serializers.ListField(
        required=True,
        min_length=settings.COMMUNITY_CATEGORIES_MIN_AMOUNT,
        max_length=settings.COMMUNITY_CATEGORIES_MAX_AMOUNT,
        child=serializers.CharField(max_length=settings.TAG_NAME_MAX_LENGTH, validators=[category_name_exists]),
    )


class CommunityNameCheckSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                 allow_blank=False,
                                 validators=[community_name_characters_validator, community_name_not_taken_validator])


class GetJoinedCommunitiesSerializer(serializers.Serializer):
    count = serializers.IntegerField(
        required=False,
        max_value=20
    )
    offset = serializers.IntegerField(
        required=False,
    )


class GetFavoriteCommunitiesSerializer(serializers.Serializer):
    count = serializers.IntegerField(
        required=False,
        max_value=20
    )
    offset = serializers.IntegerField(
        required=False,
    )


class SearchCommunitiesSerializer(serializers.Serializer):
    count = serializers.IntegerField(
        required=False,
        max_value=20
    )
    query = serializers.CharField(
        max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
        allow_blank=False,
        required=True
    )


class TrendingCommunitiesSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=settings.CATEGORY_NAME_MAX_LENGTH,
                                     allow_blank=True,
                                     required=False,
                                     validators=[category_name_exists])


class GetCommunitiesCommunityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'title',
            'color'
        )


class CommunitiesCommunitySerializer(serializers.ModelSerializer):
    categories = GetCommunitiesCommunityCategorySerializer(many=True)
    is_member = IsMemberField()
    is_invited = IsInvitedField()
    is_creator = IsCreatorField()

    class Meta:
        model = Community
        fields = (
            'id',
            'name',
            'title',
            'avatar',
            'cover',
            'members_count',
            'color',
            'user_adjective',
            'users_adjective',
            'categories',
            'type',
            'is_member',
            'is_invited',
            'is_creator',
            'invites_enabled',
        )
