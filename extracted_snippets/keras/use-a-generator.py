# use-a-generator snippets for keras

# File: /root/ecooptimizer/keras/keras/src/trainers/compile_utils.py
# Line: 494

and all([not tree.is_nested(_loss) for _loss in loss])

# ==================================================
# Line: 528

return all(
    [isinstance(obj, dict) and key in obj for obj in objs]
)

# ==================================================
# Line: 536

return all(
    [
        issubclass(type(obj), (list, tuple)) and key < len(obj)
        for obj in objs
    ]
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/applications_test.py
# Line: 135

does_not_support_channels_first = any(
    [
        unsupported_name.lower() in app.__name__.lower()
        for unsupported_name in MODELS_UNSUPPORTED_CHANNELS_FIRST
    ]
)

# ==================================================
