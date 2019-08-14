
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
