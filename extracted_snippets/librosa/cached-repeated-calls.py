# cached-repeated-calls snippets for librosa

# File: /root/ecooptimizer/librosa/librosa/sequence.py
# Occurrences: Lines 916-918 (3 instances)

sim_values = np.zeros(3)

# ==================================================
# Line: 974

backtrack[i, j] = np.argmax(score_values[:init_limit])

# ==================================================
# Line: 983

backtrack[i, j] = np.argmax(vec[:init_limit])

# ==================================================
# Line: 996

backtrack[i, j] = np.argmax(score_values[:init_limit])

# ==================================================
# Line: 1006

backtrack[i, j] = np.argmax(vec[:init_limit])

# ==================================================
# Line: 1513

p_state = np.empty(n_states)

# ==================================================
# Line: 1524

p_init = np.empty(n_states)

# ==================================================
# Line: 1729

p_state = np.empty(n_states)

# ==================================================
# Line: 1740

p_init = np.empty(n_states)

# ==================================================
# Occurrences: Lines 1755-1756 (2 instances)

p_state_binary = np.empty(2)

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/segment.py
# Occurrences: Lines 1291-1295 (4 instances)

R_smooth = scipy.ndimage.convolve(R, kernel, **kwargs)

# ==================================================
# Occurrences: Lines 1382-1383 (2 instances)

sigma_i_data = np.empty_like(rec.data)

# ==================================================
# Occurrences: Lines 1390-1397 (4 instances)

out = np.array((sigma_i_data + sigma_j_data) / 2)

# ==================================================
# Occurrences: Lines 1408-1410 (2 instances)

out = np.array((sigma_i_data + sigma_j_data) / 2)

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/beat.py
# Line: 529

N = len(onset_envelope)

# ==================================================
# Line: 538

for i in range(len(onset_envelope)):

# ==================================================
# Occurrences: Lines 545-548 (2 instances)

elif len(frames_per_beat) == len(onset_envelope):

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/decompose.py
# Occurrences: Lines 389-392 (2 instances)

harm = np.empty_like(S)

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/display.py
# Line: 1423

degrees = np.mod(degrees + Sa, 12)

# ==================================================
# Line: 1437

degrees = np.mod(degrees + Sa, 12)

# ==================================================
# Line: 1445

fmin = core.note_to_hz("C1")

# ==================================================
# Occurrences: Lines 1523-1523 (2 instances)

log_C1 = np.log2(core.note_to_hz("C1"))

# ==================================================
# Occurrences: Lines 1537-1537 (2 instances)

sa_offset = 2.0 ** (np.log2(Sa) - np.floor(np.log2(Sa)))

# ==================================================
# Line: 1552

fmin = core.note_to_hz("C1")

# ==================================================
# Line: 1563

log_fmin = np.log2(fmin)

# ==================================================
# Occurrences: Lines 1592-1594 (2 instances)

fmin = core.note_to_hz("C1")

# ==================================================
# Occurrences: Lines 1610-1612 (2 instances)

fmin = core.note_to_hz("C1")

# ==================================================
# Occurrences: Lines 1628-1628 (2 instances)

log_C1 = np.log2(core.note_to_hz("C1"))

# ==================================================
# Occurrences: Lines 1643-1643 (2 instances)

log_C1 = np.log2(core.note_to_hz("C1"))

# ==================================================
# Line: 1655

log_Sa = np.log2(Sa)

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/notation.py
# Line: 750

translations = str.maketrans({"♯": "#", "𝄪": "##", "♭": "b", "𝄫": "bb", "♮": "n"})

# ==================================================
# Line: 844

translations = str.maketrans({"♯": "#", "𝄪": "##", "♭": "b", "𝄫": "bb", "♮": "n"})

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/constantq.py
# Line: 953

lengths, filter_cutoff = filters.wavelet_lengths(
    freqs=freqs,
    sr=sr,
    window=window,
    filter_scale=filter_scale,
    gamma=gamma,
    alpha=alpha,
)

# ==================================================
# Line: 1032

lengths, _ = filters.wavelet_lengths(
    freqs=freqs,
    sr=sr,
    window=window,
    filter_scale=filter_scale,
    gamma=gamma,
    alpha=alpha,
)

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/audio.py
# Line: 172

y, sr_native = __audioread_load(path, offset, duration, dtype)

# ==================================================
# Line: 184

y, sr_native = __audioread_load(path, offset, duration, dtype)

# ==================================================
# Occurrences: Lines 640-640 (2 instances)

if int(orig_sr) != orig_sr or int(target_sr) != target_sr:

# ==================================================
# Occurrences: Lines 648-649 (2 instances)

orig_sr = int(orig_sr)

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/spectrum.py
# Line: 545

y = np.zeros(shape, dtype=dtype)

# ==================================================
# Line: 569

head_buffer = np.zeros(shape, dtype=dtype)

# ==================================================
# Occurrences: Lines 1643-1645 (2 instances)

start_idx = np.arange(
    0, cur_filter_output.shape[-1] - win_length_STMSP_round, hop_length_STMSP
)

# ==================================================
# Occurrences: Lines 1651-1655 (2 instances)

start_idx = np.arange(
    0,
    cur_filter_output.shape[-1] - win_length_STMSP_round,
    hop_length_STMSP,
)

# ==================================================
# Line: 2816

inverse = istft(
    angles,
    hop_length=hop_length,
    win_length=win_length,
    n_fft=n_fft,
    window=window,
    center=center,
    dtype=dtype,
    length=length,
    out=inverse,
)

# ==================================================
# Line: 2850

return istft(
    angles,
    hop_length=hop_length,
    win_length=win_length,
    n_fft=n_fft,
    window=window,
    center=center,
    dtype=dtype,
    length=length,
    out=inverse,
)

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/pitch.py
# Occurrences: Lines 334-335 (2 instances)

pitches = np.zeros_like(S)

# ==================================================
