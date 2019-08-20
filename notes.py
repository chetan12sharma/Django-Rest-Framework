
# ? what is hypelinkedModelSerializer?

# The HyperlinkedModelSerializer is a type of ModelSerializer that uses
# hyperlinked relationships instead of primary key relationships, and
# therefore, it represents the relationships to other model instances with
# hyperlinks instead of primary key values. In addition, the
# HyperlinkedModelSerializer generates a field named url with the URL for the
# resource as its value.

# ? what is get_gender_display means?

# The source string is built with the get_ prefix followed by the field name,
# gender , and the _display suffix. This way, the read-only gender_description
# attribute will render the description for the gender choices instead of
# the single char stored values.


# ? what is slugfieldsused for ?
# Example ::
# pilot = serializers.SlugRelatedField(
#         queryset=Pilot.objects.all(), slug_field='name')
# The SlugRelatedField allows us to change the target of the
# model field from id to username.
# example:
# ! 1.
# drone = Drone.object.all() output: drone: will_show_id
# ! 2.
# drone = serializers.SlugRelatedField(
#     queryset=Drone.objects.all(), slug_field='name')
# * output: drone: will_show_username

# slug_field = "name" => it is used for display the value

# ? what is rest_framework.filters.orderingfilter and searchfilter ????
# This class allows the client to control how the results are ordered with a
# single query parameter.We can specify which fields may be ordered against.


# ? what is rest_framework.filters searchfilter ????


# ? Why do we need serializer in Django?
# Serializers allow complex data such as querysets and model instances
# to be converted to native Python datatypes that can then be easily
# rendered into JSON, XML or other content types
# json to python model and vice-versa


# ? related_name ??

# owner = models.ForeignKey(
# 'auth.User',
# related_name='drones',
# on_delete=models.CASCADE)

# The 'drones' value specified for the related_name argument creates a
# backward relation from the User to the Drone model. Remember that this
# value indicates the name to use for the relation from the related
# User objectback to a Drone object. This way, we will be able
# to access all the drones owned by a specific user.


# linear-gradient(114.1501577487deg, #18b2b8 4.9296141814%, #245fc7 97.838894682%)

# !myntra code
# 8HGYYKLU8WQ

# !DUNZO APP
# CT500

# !cure fit
# CULTCTGZVR45
