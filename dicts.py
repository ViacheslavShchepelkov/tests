def get_val(collection, key, default='git'):
    if not isinstance(collection, dict):
        return default

    return collection.get(key, default)