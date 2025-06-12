# long-lambda-expr snippets for matplotlib

# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pgf.py
# Line: 166

return lambda pdffile, pngfile, dpi: subprocess.check_output(
    ["pdftocairo", "-singlefile", "-transp", "-png", "-r", "%d" % dpi,
     pdffile, os.path.splitext(pngfile)[0]],
    stderr=subprocess.STDOUT)

# ==================================================
# Line: 175

return lambda pdffile, pngfile, dpi: subprocess.check_output(
    [gs_info.executable,
     '-dQUIET', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-dNOPROMPT',
     '-dUseCIEColor', '-dTextAlphaBits=4',
     '-dGraphicsAlphaBits=4', '-dDOINTERPOLATE',
     '-sDEVICE=pngalpha', '-sOutputFile=%s' % pngfile,
     '-r%d' % dpi, pdffile],
    stderr=subprocess.STDOUT)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/dviread.py
# Line: 604

widths = _api.deprecated("3.11")(property(lambda self: [
    (1000 * self._tfm.width.get(char, 0)) >> 20
    for char in range(max(self._tfm.width, default=-1) + 1)]))

# ==================================================
