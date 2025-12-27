# -*- coding: utf-8 -*-

#
# Copyright (c) MINETA "m10i" Hiroki <h-mineta@0nyx.net>
# This software is released under the MIT License.
#

class SkylarkUtil:
    ticket_type_list = (
        "単勝",
        "複勝",
        "枠単",
        "枠連",
        "馬連",
        "ワイド",
        "馬単",
        "三連複",
        "三連単"
    )

    class_list = (
        "オープン",
        "1600万下",
        "1000万下",
        "500万下",
        "未勝利",
        "新馬"
    )

    @staticmethod
    def convertToTicketType2Int(key: str|None) -> int|None:
        if key is None or key == "":
            return None
        try:
            return SkylarkUtil.ticket_type_list.index(key)
        except ValueError:
            return None

    @staticmethod
    def convertToClass2Int(key: str|None) -> int|None:
        count = 0
        if key is None or key == "":
            return None

        for value in SkylarkUtil.class_list:
            if key.find(value) > 0:
                return count
            count += 1

        return None
