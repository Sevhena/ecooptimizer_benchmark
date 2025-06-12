# too-many-arguments snippets for librosa

# File: /root/ecooptimizer/librosa/librosa/sequence.py
# Line: 61

def dtw(
    X: np.ndarray,
    Y: np.ndarray,
    *,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[False],
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[False] = ...,

# ==================================================
# Line: 79

def dtw(
    *,
    C: np.ndarray,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[False],
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[False] = ...,

# ==================================================
# Line: 96

def dtw(
    X: np.ndarray,
    Y: np.ndarray,
    *,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[False],
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[True],

# ==================================================
# Line: 114

def dtw(
    *,
    C: np.ndarray,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[False],
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[True],

# ==================================================
# Line: 131

def dtw(
    X: np.ndarray,
    Y: np.ndarray,
    *,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[True] = ...,
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[False] = ...,

# ==================================================
# Line: 149

def dtw(
    *,
    C: np.ndarray,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[True] = ...,
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[False] = ...,

# ==================================================
# Line: 166

def dtw(
    X: np.ndarray,
    Y: np.ndarray,
    *,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[True] = ...,
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[True],

# ==================================================
# Line: 184

def dtw(
    *,
    C: np.ndarray,
    metric: str = ...,
    step_sizes_sigma: Optional[np.ndarray] = ...,
    weights_add: Optional[np.ndarray] = ...,
    weights_mul: Optional[np.ndarray] = ...,
    subseq: bool = ...,
    backtrack: Literal[True] = ...,
    global_constraints: bool = ...,
    band_rad: float = ...,
    return_steps: Literal[True],

# ==================================================
# Line: 200

def dtw(
    X: Optional[np.ndarray] = None,
    Y: Optional[np.ndarray] = None,
    *,
    C: Optional[np.ndarray] = None,
    metric: str = "euclidean",
    step_sizes_sigma: Optional[np.ndarray] = None,
    weights_add: Optional[np.ndarray] = None,
    weights_mul: Optional[np.ndarray] = None,
    subseq: bool = False,
    backtrack: bool = True,
    global_constraints: bool = False,
    band_rad: float = 0.25,
    return_steps: bool = False,

# ==================================================
# Line: 515

def __dtw_calc_accu_cost(
    C: np.ndarray,
    D: np.ndarray,
    steps: np.ndarray,
    step_sizes_sigma: np.ndarray,
    weights_mul: np.ndarray,
    weights_add: np.ndarray,
    max_0: int,
    max_1: int,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/filters.py
# Line: 128

def mel(
    *,
    sr: float,
    n_fft: int,
    n_mels: int = 128,
    fmin: float = 0.0,
    fmax: Optional[float] = None,
    htk: bool = False,
    norm: Optional[Union[Literal["slaney"], float]] = "slaney",
    dtype: DTypeLike = np.float32,

# ==================================================
# Line: 266

def chroma(
    *,
    sr: float,
    n_fft: int,
    n_chroma: int = 12,
    tuning: float = 0.0,
    ctroct: float = 5.0,
    octwidth: Union[float, None] = 2,
    norm: Optional[float] = 2,
    base_c: bool = True,
    dtype: DTypeLike = np.float32,

# ==================================================
# Line: 437

def constant_q(
    *,
    sr: float,
    fmin: Optional[_FloatLike_co] = None,
    n_bins: int = 84,
    bins_per_octave: int = 12,
    window: _WindowSpec = "hann",
    filter_scale: float = 1,
    pad_fft: bool = True,
    norm: Optional[float] = 1,
    dtype: DTypeLike = np.complex64,
    gamma: float = 0,
    **kwargs: Any,

# ==================================================
# Line: 602

def constant_q_lengths(
    *,
    sr: float,
    fmin: _FloatLike_co,
    n_bins: int = 84,
    bins_per_octave: int = 12,
    window: _WindowSpec = "hann",
    filter_scale: float = 1,
    gamma: float = 0,

# ==================================================
# Line: 847

def wavelet(
    *,
    freqs: np.ndarray,
    sr: float = 22050,
    window: _WindowSpec = "hann",
    filter_scale: float = 1,
    pad_fft: bool = True,
    norm: Optional[float] = 1,
    dtype: DTypeLike = np.complex64,
    gamma: float = 0,
    alpha: Optional[float] = None,
    **kwargs: Any,

# ==================================================
# Line: 995

def cq_to_chroma(
    n_input: int,
    *,
    bins_per_octave: int = 12,
    n_chroma: int = 12,
    fmin: Optional[_FloatLike_co] = None,
    window: Optional[np.ndarray] = None,
    base_c: bool = True,
    dtype: DTypeLike = np.float32,

# ==================================================
# Line: 1243

def _multirate_fb(
    center_freqs: Optional[np.ndarray] = None,
    sample_rates: Optional[np.ndarray] = None,
    Q: float = 25.0,
    passband_ripple: float = 1,
    stopband_attenuation: float = 50,
    ftype: str = "ellip",
    flayout: str = "sos",

# ==================================================
# Line: 1530

def window_sumsquare(
    *,
    window: _WindowSpec,
    n_frames: int,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    n_fft: int = 2048,
    dtype: DTypeLike = np.float32,
    norm: Optional[float] = None,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/segment.py
# Line: 61

def cross_similarity(
    data: np.ndarray,
    data_ref: np.ndarray,
    *,
    k: Optional[int] = ...,
    metric: str = ...,
    sparse: Literal[False] = ...,
    mode: str = ...,
    bandwidth: Optional[Union[np.ndarray, _FloatLike_co, str]] = None,
    full: bool = False,

# ==================================================
# Line: 76

def cross_similarity(
    data: np.ndarray,
    data_ref: np.ndarray,
    *,
    k: Optional[int] = ...,
    metric: str = ...,
    sparse: Literal[True] = ...,
    mode: str = ...,
    bandwidth: Optional[Union[np.ndarray, _FloatLike_co, str]] = None,
    full: bool = False,

# ==================================================
# Line: 91

def cross_similarity(
    data: np.ndarray,
    data_ref: np.ndarray,
    *,
    k: Optional[int] = None,
    metric: str = "euclidean",
    sparse: bool = False,
    mode: str = "connectivity",
    bandwidth: Optional[Union[np.ndarray, _FloatLike_co, str]] = None,
    full: bool = False,

# ==================================================
# Line: 348

def recurrence_matrix(
    data: np.ndarray,
    *,
    k: Optional[int] = ...,
    width: int = ...,
    metric: str = ...,
    sym: bool = ...,
    sparse: Literal[True] = ...,
    mode: str = ...,
    bandwidth: Optional[Union[np.ndarray, _FloatLike_co, str]] = ...,
    self: bool = ...,
    axis: int = ...,
    full: bool = False,

# ==================================================
# Line: 366

def recurrence_matrix(
    data: np.ndarray,
    *,
    k: Optional[int] = ...,
    width: int = ...,
    metric: str = ...,
    sym: bool = ...,
    sparse: Literal[False] = ...,
    mode: str = ...,
    bandwidth: Optional[Union[np.ndarray, _FloatLike_co, str]] = ...,
    self: bool = ...,
    axis: int = ...,
    full: bool = False,

# ==================================================
# Line: 384

def recurrence_matrix(
    data: np.ndarray,
    *,
    k: Optional[int] = None,
    width: int = 1,
    metric: str = "euclidean",
    sym: bool = False,
    sparse: bool = False,
    mode: str = "connectivity",
    bandwidth: Optional[Union[np.ndarray, _FloatLike_co, str]] = None,
    self: bool = False,
    axis: int = -1,
    full: bool = False,

# ==================================================
# Line: 1142

def path_enhance(
    R: np.ndarray,
    n: int,
    *,
    window: _WindowSpec = "hann",
    max_ratio: float = 2.0,
    min_ratio: Optional[float] = None,
    n_filters: int = 7,
    zero_mean: bool = False,
    clip: bool = True,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/beat.py
# Line: 36

def beat_track(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    onset_envelope: Optional[np.ndarray] = None,
    hop_length: int = 512,
    start_bpm: float = 120.0,
    tightness: float = 100,
    trim: bool = True,
    bpm: Optional[Union[_FloatLike_co, np.ndarray]] = None,
    prior: Optional[scipy.stats.rv_continuous] = None,
    units: str = "frames",
    sparse: bool = True

# ==================================================
# Line: 267

def plp(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    onset_envelope: Optional[np.ndarray] = None,
    hop_length: int = 512,
    win_length: int = 384,
    tempo_min: Optional[float] = 30,
    tempo_max: Optional[float] = 300,
    prior: Optional[scipy.stats.rv_continuous] = None,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/effects.py
# Line: 66

def hpss(
    y: np.ndarray,
    *,
    kernel_size: Union[
        _IntLike_co, Tuple[_IntLike_co, _IntLike_co], List[_IntLike_co]
    ] = 31,
    power: float = 2.0,
    mask: bool = False,
    margin: Union[
        _FloatLike_co, Tuple[_FloatLike_co, _FloatLike_co], List[_FloatLike_co]
    ] = 1.0,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# Line: 166

def harmonic(
    y: np.ndarray,
    *,
    kernel_size: Union[
        _IntLike_co, Tuple[_IntLike_co, _IntLike_co], List[_IntLike_co]
    ] = 31,
    power: float = 2.0,
    mask: bool = False,
    margin: Union[
        _FloatLike_co, Tuple[_FloatLike_co, _FloatLike_co], List[_FloatLike_co]
    ] = 1.0,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# Line: 252

def percussive(
    y: np.ndarray,
    *,
    kernel_size: Union[
        _IntLike_co, Tuple[_IntLike_co, _IntLike_co], List[_IntLike_co]
    ] = 31,
    power: float = 2.0,
    mask: bool = False,
    margin: Union[
        _FloatLike_co, Tuple[_FloatLike_co, _FloatLike_co], List[_FloatLike_co]
    ] = 1.0,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/onset.py
# Line: 29

def onset_detect(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    onset_envelope: Optional[np.ndarray] = None,
    hop_length: int = 512,
    backtrack: bool = False,
    energy: Optional[np.ndarray] = None,
    units: str = "frames",
    normalize: bool = True,
    sparse: bool = True,
    **kwargs: Any,

# ==================================================
# Line: 216

def onset_strength(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    lag: int = 1,
    max_size: int = 1,
    ref: Optional[np.ndarray] = None,
    detrend: bool = False,
    center: bool = True,
    feature: Optional[Callable] = None,
    aggregate: Optional[Union[Callable, bool]] = None,
    **kwargs: Any,

# ==================================================
# Line: 445

def onset_strength_multi(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    lag: int = 1,
    max_size: int = 1,
    ref: Optional[np.ndarray] = None,
    detrend: bool = False,
    center: bool = True,
    feature: Optional[Callable] = None,
    aggregate: Optional[Union[Callable, bool]] = None,
    channels: Optional[Union[Sequence[int], Sequence[slice]]] = None,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/display.py
# Line: 305

def __init__(
    self,
    Sa: float,
    octave: bool = True,
    major: bool = True,
    abbr: bool = False,
    mela: Optional[Union[str, int]] = None,
    unicode: bool = True,

# ==================================================
# Line: 395

def __init__(
    self,
    *,
    fmin: int,
    n_bins: int,
    bins_per_octave: int,
    intervals: Union[str, Collection[float]],
    major: bool = True,
    unison: Optional[str] = None,
    unicode: bool = True,

# ==================================================
# Line: 681

def __init__(
    self,
    times: np.ndarray,
    y: np.ndarray,
    steps: Line2D,
    envelope: PolyCollection,
    sr: float = 22050,
    max_samples: int = 11025,
    transpose: bool = False,

# ==================================================
# Line: 924

def specshow(
    data: np.ndarray,
    *,
    x_coords: Optional[np.ndarray] = None,
    y_coords: Optional[np.ndarray] = None,
    x_axis: Optional[str] = None,
    y_axis: Optional[str] = None,
    sr: float = 22050,
    hop_length: int = 512,
    n_fft: Optional[int] = None,
    win_length: Optional[int] = None,
    fmin: Optional[float] = None,
    fmax: Optional[float] = None,
    tempo_min: Optional[float] = 16,
    tempo_max: Optional[float] = 480,
    tuning: float = 0.0,
    bins_per_octave: int = 12,
    key: str = "C:maj",
    Sa: Optional[Union[float, int]] = None,
    mela: Optional[Union[str, int]] = None,
    thaat: Optional[str] = None,
    auto_aspect: bool = True,
    htk: bool = False,
    unicode: bool = True,
    intervals: Optional[Union[str, np.ndarray]] = None,
    unison: Optional[str] = None,
    ax: Optional[mplaxes.Axes] = None,
    **kwargs: Any,

# ==================================================
# Line: 1383

def __decorate_axis(
    axis,
    ax_type,
    key="C:maj",
    Sa=None,
    mela=None,
    thaat=None,
    unicode=True,
    fmin=None,
    unison=None,
    intervals=None,
    bins_per_octave=None,
    n_bins=None,

# ==================================================
# Line: 1834

def waveshow(
    y: np.ndarray,
    *,
    sr: float = 22050,
    max_points: int = 11025,
    axis: Optional[str] = "time",
    offset: float = 0.0,
    marker: Union[str, MplPath, MarkerStyle] = "",
    where: str = "post",
    label: Optional[str] = None,
    transpose: bool = False,
    ax: Optional[mplaxes.Axes] = None,
    x_axis: Optional[Union[str, Deprecated]] = Deprecated(),
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/feature/rhythm.py
# Line: 24

def tempogram(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    onset_envelope: Optional[np.ndarray] = None,
    hop_length: int = 512,
    win_length: int = 384,
    center: bool = True,
    window: _WindowSpec = "hann",
    norm: Optional[float] = np.inf,

# ==================================================
# Line: 179

def fourier_tempogram(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    onset_envelope: Optional[np.ndarray] = None,
    hop_length: int = 512,
    win_length: int = 384,
    center: bool = True,
    window: _WindowSpec = "hann",

# ==================================================
# Line: 281

def tempo(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    onset_envelope: Optional[np.ndarray] = None,
    tg: Optional[np.ndarray] = None,
    hop_length: int = 512,
    start_bpm: float = 120,
    std_bpm: float = 1.0,
    ac_size: float = 8.0,
    max_tempo: Optional[float] = 320.0,
    aggregate: Optional[Callable[..., Any]] = np.mean,
    prior: Optional[scipy.stats.rv_continuous] = None,

# ==================================================
# Line: 457

def tempogram_ratio(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    onset_envelope: Optional[np.ndarray] = None,
    tg: Optional[np.ndarray] = None,
    bpm: Optional[np.ndarray] = None,
    hop_length: int = 512,
    win_length: int = 384,
    start_bpm: float = 120,
    std_bpm: float = 1.0,
    max_tempo: Optional[float] = 320.0,
    freqs: Optional[np.ndarray] = None,
    factors: Optional[np.ndarray] = None,
    aggregate: Optional[Callable[..., Any]] = None,
    prior: Optional[scipy.stats.rv_continuous] = None,
    center: bool = True,
    window: _WindowSpec = "hann",
    kind: str = "linear",
    fill_value: float = 0,
    norm: Optional[float] = np.inf,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/feature/inverse.py
# Line: 110

def mel_to_audio(
    M: np.ndarray,
    *,
    sr: float = 22050,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    power: float = 2.0,
    n_iter: int = 32,
    length: Optional[int] = None,
    dtype: DTypeLike = np.float32,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/feature/spectral.py
# Line: 45

def spectral_centroid(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    freq: Optional[np.ndarray] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# Line: 192

def spectral_bandwidth(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    freq: Optional[np.ndarray] = None,
    centroid: Optional[np.ndarray] = None,
    norm: bool = True,
    p: float = 2,

# ==================================================
# Line: 352

def spectral_contrast(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    freq: Optional[np.ndarray] = None,
    fmin: float = 200.0,
    n_bands: int = 6,
    quantile: float = 0.02,
    linear: bool = False,

# ==================================================
# Line: 533

def spectral_rolloff(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    freq: Optional[np.ndarray] = None,
    roll_percent: float = 0.85,

# ==================================================
# Line: 681

def spectral_flatness(
    *,
    y: Optional[np.ndarray] = None,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    amin: float = 1e-10,
    power: float = 2.0,

# ==================================================
# Line: 801

def rms(
    *,
    y: Optional[np.ndarray] = None,
    S: Optional[np.ndarray] = None,
    frame_length: int = 2048,
    hop_length: int = 512,
    center: bool = True,
    pad_mode: _PadMode = "constant",
    dtype: DTypeLike = np.float32,

# ==================================================
# Line: 914

def poly_features(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    order: int = 1,
    freq: Optional[np.ndarray] = None,

# ==================================================
# Line: 1132

def chroma_stft(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    norm: Optional[float] = np.inf,
    n_fft: int = 2048,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    tuning: Optional[float] = None,
    n_chroma: int = 12,
    **kwargs: Any,

# ==================================================
# Line: 1289

def chroma_cqt(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    C: Optional[np.ndarray] = None,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    norm: Optional[Union[int, float]] = np.inf,
    threshold: float = 0.0,
    tuning: Optional[float] = None,
    n_chroma: int = 12,
    n_octaves: int = 7,
    window: Optional[np.ndarray] = None,
    bins_per_octave: Optional[int] = 36,
    cqt_mode: str = "full",

# ==================================================
# Line: 1419

def chroma_cens(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    C: Optional[np.ndarray] = None,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    tuning: Optional[float] = None,
    n_chroma: int = 12,
    n_octaves: int = 7,
    bins_per_octave: int = 36,
    cqt_mode: str = "full",
    window: Optional[np.ndarray] = None,
    norm: Optional[float] = 2,
    win_len_smooth: Optional[int] = 41,
    smoothing_window: _WindowSpec = "hann",

# ==================================================
# Line: 1567

def chroma_vqt(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    V: Optional[np.ndarray] = None,
    hop_length: int = 512,
    fmin: Optional[float] = None,
    intervals: Union[str, Collection[float]],
    norm: Optional[float] = np.inf,
    threshold: float = 0.0,
    n_octaves: int = 7,
    bins_per_octave: int = 12,
    gamma: float = 0,

# ==================================================
# Line: 1834

def mfcc(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_mfcc: int = 20,
    dct_type: int = 2,
    norm: Optional[str] = "ortho",
    lifter: float = 0,
    mel_norm: Optional[Union[Literal["slaney"], float]] = "slaney",
    **kwargs: Any,

# ==================================================
# Line: 2013

def melspectrogram(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    power: float = 2.0,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/util/utils.py
# Line: 1202

def __peak_pick(x, pre_max, post_max, pre_avg, post_avg, delta, wait, peaks):
    """Vectorized wrapper for the peak-picker"""
    # Special case the first frame
    peaks[0] = (x[0] >= np.max(x[:min(post_max, x.shape[0])]))
    peaks[0] &= (x[0] >= np.mean(x[:min(post_avg, x.shape[0])]) + delta)

    if peaks[0]:
        n = wait + 1
    else:
        n = 1

    while n < x.shape[0]:
        maxn = np.max( x[max(0, n-pre_max):min(n+post_max, x.shape[0])])

        # Are we the local max and sufficiently above average?
        peaks[n] = (x[n] == maxn) 
        
        if not peaks[n]:
            n += 1
            continue

        avgn = np.mean(x[max(0, n-pre_avg):min(n+post_avg, x.shape[0])])
        peaks[n] &= (x[n] >= avgn + delta)

        if not peaks[n]:
            n += 1
            continue

        # Skip the next `wait` frames
        n += wait + 1



# ==================================================
# Line: 1234

def peak_pick(
    x: np.ndarray,
    *,
    pre_max: int,
    post_max: int,
    pre_avg: int,
    post_avg: int,
    delta: float,
    wait: int,
    sparse: bool = True,
    axis: int = -1

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/constantq.py
# Line: 28

def cqt(
    y: np.ndarray,
    *,
    sr: float = 22050,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    n_bins: int = 84,
    bins_per_octave: int = 12,
    tuning: Optional[float] = 0.0,
    filter_scale: float = 1,
    norm: Optional[float] = 1,
    sparsity: float = 0.01,
    window: _WindowSpec = "hann",
    scale: bool = True,
    pad_mode: _PadMode = "constant",
    res_type: Optional[str] = "soxr_hq",
    dtype: Optional[DTypeLike] = None,

# ==================================================
# Line: 193

def hybrid_cqt(
    y: np.ndarray,
    *,
    sr: float = 22050,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    n_bins: int = 84,
    bins_per_octave: int = 12,
    tuning: Optional[float] = 0.0,
    filter_scale: float = 1,
    norm: Optional[float] = 1,
    sparsity: float = 0.01,
    window: _WindowSpec = "hann",
    scale: bool = True,
    pad_mode: _PadMode = "constant",
    res_type: str = "soxr_hq",
    dtype: Optional[DTypeLike] = None,

# ==================================================
# Line: 377

def pseudo_cqt(
    y: np.ndarray,
    *,
    sr: float = 22050,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    n_bins: int = 84,
    bins_per_octave: int = 12,
    tuning: Optional[float] = 0.0,
    filter_scale: float = 1,
    norm: Optional[float] = 1,
    sparsity: float = 0.01,
    window: _WindowSpec = "hann",
    scale: bool = True,
    pad_mode: _PadMode = "constant",
    dtype: Optional[DTypeLike] = None,

# ==================================================
# Line: 534

def icqt(
    C: np.ndarray,
    *,
    sr: float = 22050,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    bins_per_octave: int = 12,
    tuning: float = 0.0,
    filter_scale: float = 1,
    norm: Optional[float] = 1,
    sparsity: float = 0.01,
    window: _WindowSpec = "hann",
    scale: bool = True,
    length: Optional[int] = None,
    res_type: str = "soxr_hq",
    dtype: Optional[DTypeLike] = None,

# ==================================================
# Line: 760

def vqt(
    y: np.ndarray,
    *,
    sr: float = 22050,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    n_bins: int = 84,
    intervals: Union[str, Collection[float]] = "equal",
    gamma: Optional[float] = None,
    bins_per_octave: int = 12,
    tuning: Optional[float] = 0.0,
    filter_scale: float = 1,
    norm: Optional[float] = 1,
    sparsity: float = 0.01,
    window: _WindowSpec = "hann",
    scale: bool = True,
    pad_mode: _PadMode = "constant",
    res_type: Optional[str] = "soxr_hq",
    dtype: Optional[DTypeLike] = None,

# ==================================================
# Line: 1049

def __vqt_filter_fft(
    sr,
    freqs,
    filter_scale,
    norm,
    sparsity,
    hop_length=None,
    window="hann",
    gamma=0.0,
    dtype=np.complex64,
    alpha=None,

# ==================================================
# Line: 1120

def __cqt_response(
    y, n_fft, hop_length, fft_basis, mode, window="ones", phase=True, dtype=None

# ==================================================
# Line: 1159

def __early_downsample(
    y, sr, hop_length, res_type, n_octaves, nyquist, filter_cutoff, scale

# ==================================================
# Line: 1209

def griffinlim_cqt(
    C: np.ndarray,
    *,
    n_iter: int = 32,
    sr: float = 22050,
    hop_length: int = 512,
    fmin: Optional[_FloatLike_co] = None,
    bins_per_octave: int = 12,
    tuning: float = 0.0,
    filter_scale: float = 1,
    norm: Optional[float] = 1,
    sparsity: float = 0.01,
    window: _WindowSpec = "hann",
    scale: bool = True,
    pad_mode: _PadMode = "constant",
    res_type: str = "soxr_hq",
    dtype: Optional[DTypeLike] = None,
    length: Optional[int] = None,
    momentum: float = 0.99,
    init: Optional[str] = "random",
    random_state: Optional[
        Union[int, np.random.RandomState, np.random.Generator]
    ] = None,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/harmonic.py
# Line: 18

def salience(
    S: np.ndarray,
    *,
    freqs: np.ndarray,
    harmonics: Sequence[float],
    weights: Optional[ArrayLike] = None,
    aggregate: Optional[Callable] = None,
    filter_peaks: bool = True,
    fill_value: float = np.nan,
    kind: str = "linear",
    axis: int = -2,

# ==================================================
# Line: 303

def f0_harmonics(
    x: np.ndarray,
    *,
    f0: np.ndarray,
    freqs: np.ndarray,
    harmonics: ArrayLike,
    kind: str = "linear",
    fill_value: float = 0,
    axis: int = -2,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/audio.py
# Line: 56

def load(
    path: Union[
        str, int, os.PathLike[Any], sf.SoundFile, audioread.AudioFile, BinaryIO
    ],
    *,
    sr: Optional[float] = 22050,
    mono: bool = True,
    offset: float = 0.0,
    duration: Optional[float] = None,
    dtype: DTypeLike = np.float32,
    res_type: str = "soxr_hq",

# ==================================================
# Line: 290

def stream(
    path: Union[str, int, sf.SoundFile, BinaryIO],
    *,
    block_length: int,
    frame_length: int,
    hop_length: int,
    mono: bool = True,
    offset: float = 0.0,
    duration: Optional[float] = None,
    fill_value: Optional[float] = None,
    dtype: DTypeLike = np.float32,

# ==================================================
# Line: 514

def resample(
    y: np.ndarray,
    *,
    orig_sr: float,
    target_sr: float,
    res_type: str = "soxr_hq",
    fix: bool = True,
    scale: bool = False,
    axis: int = -1,
    **kwargs: Any,

# ==================================================
# Line: 690

def get_duration(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: int = 512,
    center: bool = True,
    path: Optional[Union[str, os.PathLike[Any]]] = None,
    filename: Optional[Union[str, os.PathLike[Any], Deprecated]] = Deprecated(),

# ==================================================
# Line: 1043

def __lpc(
    y: np.ndarray,
    order: int,
    ar_coeffs: np.ndarray,
    ar_coeffs_prev: np.ndarray,
    reflect_coeff: np.ndarray,
    den: np.ndarray,
    epsilon: float,

# ==================================================
# Line: 1285

def clicks(
    *,
    times: Optional[_SequenceLike[_FloatLike_co]] = None,
    frames: Optional[_SequenceLike[_IntLike_co]] = None,
    sr: float = 22050,
    hop_length: int = 512,
    click_freq: float = 1000.0,
    click_duration: float = 0.1,
    click: Optional[np.ndarray] = None,
    length: Optional[int] = None,

# ==================================================
# Line: 1494

def chirp(
    *,
    fmin: _FloatLike_co,
    fmax: _FloatLike_co,
    sr: float = 22050,
    length: Optional[int] = None,
    duration: Optional[float] = None,
    linear: bool = False,
    phi: Optional[float] = None,

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/spectrum.py
# Line: 55

def stft(
    y: np.ndarray,
    *,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    dtype: Optional[DTypeLike] = None,
    pad_mode: _PadModeSTFT = "constant",
    out: Optional[np.ndarray] = None,

# ==================================================
# Line: 394

def istft(
    stft_matrix: np.ndarray,
    *,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    n_fft: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    dtype: Optional[DTypeLike] = None,
    length: Optional[int] = None,
    out: Optional[np.ndarray] = None,

# ==================================================
# Line: 646

def __reassign_frequencies(
    y: np.ndarray,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    dtype: Optional[DTypeLike] = None,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# Line: 809

def __reassign_times(
    y: np.ndarray,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    dtype: Optional[DTypeLike] = None,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# Line: 990

def reassigned_spectrogram(
    y: np.ndarray,
    *,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: int = 2048,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    reassign_frequencies: bool = True,
    reassign_times: bool = True,
    ref_power: Union[float, Callable] = 1e-6,
    fill_nan: bool = False,
    clip: bool = True,
    dtype: Optional[DTypeLike] = None,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# Line: 1477

def iirt(
    y: np.ndarray,
    *,
    sr: float = 22050,
    win_length: int = 2048,
    hop_length: Optional[int] = None,
    center: bool = True,
    tuning: float = 0.0,
    pad_mode: _PadMode = "constant",
    flayout: str = "sos",
    res_type: str = "soxr_hq",
    **kwargs: Any,

# ==================================================
# Line: 2101

def fmt(
    y: np.ndarray,
    *,
    t_min: float = 0.5,
    n_fmt: Optional[int] = None,
    kind: str = "cubic",
    beta: float = 0.5,
    over_sample: float = 1,
    axis: int = -1,

# ==================================================
# Line: 2300

def pcen(
    S: np.ndarray,
    *,
    sr: float = ...,
    hop_length: int = ...,
    gain: float = ...,
    bias: float = ...,
    power: float = ...,
    time_constant: float = ...,
    eps: float = ...,
    b: Optional[float] = ...,
    max_size: int = ...,
    ref: Optional[np.ndarray] = ...,
    axis: int = ...,
    max_axis: Optional[int] = ...,
    zi: Optional[np.ndarray] = ...,
    return_zf: Literal[False] = ...,

# ==================================================
# Line: 2322

def pcen(
    S: np.ndarray,
    *,
    sr: float = ...,
    hop_length: int = ...,
    gain: float = ...,
    bias: float = ...,
    power: float = ...,
    time_constant: float = ...,
    eps: float = ...,
    b: Optional[float] = ...,
    max_size: int = ...,
    ref: Optional[np.ndarray] = ...,
    axis: int = ...,
    max_axis: Optional[int] = ...,
    zi: Optional[np.ndarray] = ...,
    return_zf: Literal[True],

# ==================================================
# Line: 2344

def pcen(
    S: np.ndarray,
    *,
    sr: float = ...,
    hop_length: int = ...,
    gain: float = ...,
    bias: float = ...,
    power: float = ...,
    time_constant: float = ...,
    eps: float = ...,
    b: Optional[float] = ...,
    max_size: int = ...,
    ref: Optional[np.ndarray] = ...,
    axis: int = ...,
    max_axis: Optional[int] = ...,
    zi: Optional[np.ndarray] = ...,
    return_zf: bool = ...,

# ==================================================
# Line: 2366

def pcen(
    S: np.ndarray,
    *,
    sr: float = 22050,
    hop_length: int = 512,
    gain: float = 0.98,
    bias: float = 2,
    power: float = 0.5,
    time_constant: float = 0.400,
    eps: float = 1e-6,
    b: Optional[float] = None,
    max_size: int = 1,
    ref: Optional[np.ndarray] = None,
    axis: int = -1,
    max_axis: Optional[int] = None,
    zi: Optional[np.ndarray] = None,
    return_zf: bool = False,

# ==================================================
# Line: 2634

def griffinlim(
    S: np.ndarray,
    *,
    n_iter: int = 32,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    n_fft: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    dtype: Optional[DTypeLike] = None,
    length: Optional[int] = None,
    pad_mode: _PadModeSTFT = "constant",
    momentum: float = 0.99,
    init: Optional[str] = "random",
    random_state: Optional[
        Union[int, np.random.RandomState, np.random.Generator]
    ] = None,

# ==================================================
# Line: 2863

def _spectrogram(
    *,
    y: Optional[np.ndarray] = None,
    S: Optional[np.ndarray] = None,
    n_fft: Optional[int] = 2048,
    hop_length: Optional[int] = 512,
    power: float = 1,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",

# ==================================================
# File: /root/ecooptimizer/librosa/librosa/core/pitch.py
# Line: 181

def piptrack(
    *,
    y: Optional[np.ndarray] = None,
    sr: float = 22050,
    S: Optional[np.ndarray] = None,
    n_fft: Optional[int] = 2048,
    hop_length: Optional[int] = None,
    fmin: float = 150.0,
    fmax: float = 4000.0,
    threshold: float = 0.1,
    win_length: Optional[int] = None,
    window: _WindowSpec = "hann",
    center: bool = True,
    pad_mode: _PadModeSTFT = "constant",
    ref: Optional[Union[float, Callable]] = None,

# ==================================================
# Line: 476

def yin(
    y: np.ndarray,
    *,
    fmin: float,
    fmax: float,
    sr: float = 22050,
    frame_length: int = 2048,
    win_length: Optional[Union[int, Deprecated]] = Deprecated(),
    hop_length: Optional[int] = None,
    trough_threshold: float = 0.1,
    center: bool = True,
    pad_mode: _PadMode = "constant",

# ==================================================
# Line: 652

def pyin(
    y: np.ndarray,
    *,
    fmin: float,
    fmax: float,
    sr: float = 22050,
    frame_length: int = 2048,
    win_length: Optional[Union[int, Deprecated]] = Deprecated(),
    hop_length: Optional[int] = None,
    n_thresholds: int = 100,
    beta_parameters: Tuple[float, float] = (2, 18),
    boltzmann_parameter: float = 2,
    resolution: float = 0.1,
    max_transition_rate: float = 35.92,
    switch_prob: float = 0.01,
    no_trough_prob: float = 0.01,
    fill_na: Optional[float] = np.nan,
    center: bool = True,
    pad_mode: _PadMode = "constant",

# ==================================================
# Line: 896

def __pyin_helper(
    yin_frames,
    parabolic_shifts,
    sr,
    thresholds,
    boltzmann_parameter,
    beta_probs,
    no_trough_prob,
    min_period,
    fmin,
    n_pitch_bins,
    n_bins_per_semitone,

# ==================================================
