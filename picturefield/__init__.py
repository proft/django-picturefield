try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^picturefield\.fields\.PictureField"])
except ImportError:
    pass
