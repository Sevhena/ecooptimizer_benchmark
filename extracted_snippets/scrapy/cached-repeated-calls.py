# cached-repeated-calls snippets for scrapy

# File: /root/ecooptimizer/scrapy/scrapy/commands/parse.py
# Occurrences: Lines 154-157 (2 instances)

d = deferred_from_coro(result)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/check.py
# Occurrences: Lines 109-111 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spiders/feed.py
# Line: 89

nodes = selector.xpath(f"//{self.itertag}")

# ==================================================
# Line: 95

nodes = selector.xpath(f"//{self.itertag}")

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/_compression.py
# Occurrences: Lines 62-62 (2 instances)

output_chunk = decompressor.decompress(input_chunk)

# ==================================================
# Occurrences: Lines 71-71 (2 instances)

output_chunk = decompressor.decompress(input_chunk)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/response.py
# Line: 64

start = body.find(b"<!--")

# ==================================================
# Line: 70

start = body.find(b"<!--")

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/spider.py
# Occurrences: Lines 45-48 (2 instances)

d = deferred_from_coro(result)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/exporters.py
# Occurrences: Lines 87-90 (2 instances)

field_iter = self.fields_to_export.items()

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/pqueues.py
# Occurrences: Lines 168-168 (2 instances)

m = q.pop()

# ==================================================
# Occurrences: Lines 181-181 (2 instances)

m = q.pop()

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/httpcache.py
# Occurrences: Lines 343-345 (2 instances)

body = f.read()

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/feedexport.py
# Line: 483

self.feeds[uri] = feed_complete_default_values_from_settings(
    feed_options, self.settings
)

# ==================================================
# Line: 493

self.feeds[uri] = feed_complete_default_values_from_settings(
    feed_options, self.settings
)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/spidermw.py
# Line: 259

last_result_is_async = isinstance(result, AsyncIterator)

# ==================================================
# Occurrences: Lines 296-296 (2 instances)

assert isinstance(result, AsyncIterator)

# ==================================================
# Occurrences: Lines 332-332 (2 instances)

last_result_is_async = isinstance(result, AsyncIterator)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/middleware.py
# Line: 54

method = cast(Callable, method)

# ==================================================
# Line: 79

method = cast(Callable, method)

# ==================================================
# Line: 97

method = cast(Callable, method)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/handlers/__init__.py
# Line: 82

self._notconfigured[scheme] = str(ex)

# ==================================================
# Line: 91

self._notconfigured[scheme] = str(ex)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/handlers/s3.py
# Occurrences: Lines 48-51 (2 instances)

anon = kw.get("anon")

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/redirect.py
# Occurrences: Lines 36-37 (2 instances)

source_request_scheme = urlparse_cached(source_request).scheme

# ==================================================
# Line: 48

parsed_source_request = urlparse_cached(source_request)

# ==================================================
# Line: 56

parsed_redirect_request = urlparse_cached(redirect_request)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/pipelines/images.py
# Occurrences: Lines 212-219 (4 instances)

background = self._Image.new("RGBA", image.size, (255, 255, 255))

# ==================================================
