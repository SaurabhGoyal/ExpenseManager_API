from rest_framework import serializers as rest_serializers

from apps.account import models as account_models
from apps.activity import models as activity_models


class ActivityCategorySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for ActivityCategory model having field 'name'
    """
    class Meta:
        model = activity_models.ActivityCategory
        fields = (u'name', )


class ActivitySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Activity model having fields 'name' and 'category'
    """
    category = ActivityCategorySerializer()

    class Meta:
        model = activity_models.Activity
        fields = (u'name', u'category', )


class UserActivitySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for UserActivity model having fields 'user', 'activity' and 'order'
    """
    user = rest_serializers.PrimaryKeyRelatedField(queryset=account_models.User.objects.all())
    activity = ActivitySerializer()
    order = rest_serializers.IntegerField(required=False)

    def validate_user(self, value):
        print 'here'
        return value

    class Meta:
        model = activity_models.UserActivity
        fields = (u'user', u'activity', u'order', )

    def create(self, validated_data):
        user = validated_data.get(u'user')
        activity = validated_data.get(u'activity')
        user_activities = activity_models.UserActivity.objects.filter(user=user)
        order = validated_data.get(u'order') or ((user_activities.latest().order if user_activities else 0) + 1)
        validated_data[u'order'] = order
        return super(UserActivitySerializer, self).create(validated_data)
