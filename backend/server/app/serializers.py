from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.fields import CharField
from rest_framework.response import Response
from rest_framework import status
from .models import SpotifyInfo, Instrument, Song, Section, File
from django.contrib.auth.password_validation import validate_password


class BlankableFloatField(serializers.FloatField):
    """
    We wanted to be able to receive an empty string ('') for a decimal field
    and in that case turn it into a None number. 
    """

    def to_internal_value(self, data):
        if data == '':
            """
           if you return None you shall get a type error ```TypeError: '>' not supported between instances of 'NoneType' and 'int'```
            """
            return 0
        return super(BlankableFloatField, self).to_internal_value(data)


class SpotifyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpotifyInfo
        fields = ('access_token', 'refresh_token', 'device_id')


class UserSerializer(serializers.ModelSerializer):
    spotify_info = SpotifyInfoSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'spotify_info')


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                {"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this user."})
        instance.username = validated_data['username']
        instance.save()

        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


def get_primary_key_related_model(model_class, **kwargs):
    """
    Nested serializers are a mess. https://stackoverflow.com/a/28016439/2689986
    This lets us accept ids when saving / updating instead of nested objects.
    Representation would be into an object (depending on model_class).
    """
    class PrimaryKeyNestedMixin(model_class):

        def to_internal_value(self, data):
            try:
                return model_class.Meta.model.objects.get(pk=data)
            except model_class.Meta.model.DoesNotExist:
                self.fail('does_not_exist', pk_value=data)
            except (TypeError, ValueError):
                self.fail('incorrect_type', data_type=type(data).__name__)

        def to_representation(self, data):
            return model_class.to_representation(self, data)

    return PrimaryKeyNestedMixin(**kwargs)


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'year', 'image', 'uploaded_image', 'genre', 'duration', 'explicit', 'key', 'mode', 'lyrics', 'time_signature', 'tempo',
                  'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'valence', 'original', 'spotify_url', 'spotify_id', 'created_at', 'updated_at', 'sections']


class SectionSerializer(serializers.ModelSerializer):

    song = get_primary_key_related_model(SongSerializer)
    tempo = BlankableFloatField(
        min_value=0, default=0, allow_null=True, initial=0)

    class Meta:
        model = Section
        fields = ["id", "name",
                  "start",
                  "duration",
                  "loudness",
                  "tempo",
                  "key",
                  "mode",
                  "lyrics",
                  "learned",
                  "time_signature",
                  'created_at',
                  'updated_at',
                  "song",
                  "instruments"]


class InstrumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument
        fields = ['id', 'make', 'model', 'name', 'family',
                  'tonal_range', 'year', 'sections', 'created_at', 'updated_at']


class FileSerializer(serializers.ModelSerializer):

    # song = get_primary_key_related_model(SongSerializer)
    # section = get_primary_key_related_model(SectionSerializer)

    class Meta:
        model = File
        fields = '__all__'
