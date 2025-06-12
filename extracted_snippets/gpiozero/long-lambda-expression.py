# long-lambda-expression snippets for gpiozero

# File: /root/ecooptimizer/gpiozero/gpiozero/output_devices.py
# Line: 1113

lerp = lambda t, fade_in: tuple(
    (1 - t) * off + t * on
    if fade_in else
    (1 - t) * on + t * off
    for off, on in zip(off_color, on_color)
    )

# ==================================================
