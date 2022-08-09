from scrapy import signals
from scrapy import crawler


class AlertOnChange(object):
    @classmethod
    def from_crawler(cls, crawler):

        ectension = cls()

        crawler.signals.connect(ectension.engine_stopped, signal=signals.engine_stopped)

        return ectension

    def engine_stopped(self):
        print("@@@@@@ MY_CUSTOM_EXTENSION ------ JOB_DONE  @@@@@@@")
