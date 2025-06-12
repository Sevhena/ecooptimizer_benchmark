# long-lambda-expr snippets for scrapy

# File: /root/ecooptimizer/scrapy/scrapy/core/engine.py
# Line: 270

lambda f: logger.info(
    "Error while handling downloader output",
    exc_info=failure_to_exc_info(f),
    extra={"spider": self.spider},
)

# ==================================================
# Occurrences: Lines 283-296 (2 instances)

lambda f: logger.info(
    "Error while removing request from slot",
    exc_info=failure_to_exc_info(f),
    extra={"spider": self.spider},
)

# ==================================================
# Line: 490

lambda _: self.signals.send_catch_log_deferred(
    signal=signals.spider_closed,
    spider=spider,
    reason=reason,
)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/pipelines/files.py
# Line: 602

lambda f: logger.error(
    self.__class__.__name__ + ".store.stat_file",
    exc_info=failure_to_exc_info(f),
    extra={"spider": info.spider},
)

# ==================================================
