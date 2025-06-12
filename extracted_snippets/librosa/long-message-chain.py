# long-message-chain snippets for librosa

# File: /root/ecooptimizer/librosa/librosa/core/harmonic.py
# Line: 285

xfunc(freqs.swapaxes(axis, -1), x.swapaxes(axis, -1))
.swapaxes(
    # Return the original target axis to its place
    -2,
    axis,
)
.swapaxes(
    # Put the new harmonic axis directly in front of the target axis
    -1,
    axis - 1,
)

# ==================================================
