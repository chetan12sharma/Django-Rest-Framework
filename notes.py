
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
# this is used for creating the dropdown of the pilot list
# slug_field = "name" => it is used for display the value

# ? what is rest_framework.filters.orderingfilter and searchfilter ????
# This class allows the client to control how the results are ordered with a
# single query parameter.We can specify which fields may be ordered against.


# ? what is rest_framework.filters searchfilter ????
# kjakjsl this is trying
