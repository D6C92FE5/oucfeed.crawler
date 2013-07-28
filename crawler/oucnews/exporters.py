# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from scrapy.contrib import exporter


class JsonItemExporter(exporter.JsonItemExporter):
    """不启用 ensure_ascii 的 JsonItemExporter"""

    def __init__(self, file, **kwargs):
        self._configure(kwargs)
        self.file = file
        self.encoder = exporter.ScrapyJSONEncoder(ensure_ascii=False, **kwargs)
        self.first_item = True

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(',\n')
        itemdict = dict()
        for key, value in self._get_serialized_fields(item):
            itemdict[self._to_str_if_unicode(key)] = value # 防止解码错误
        self.file.write(self.encoder.encode(itemdict))


class JavascriptItemExporter(JsonItemExporter):
    """输出用于 test-viewer.html 的 JavaScript 文件"""

    def start_exporting(self):
        self.file.write("data = [\n")
