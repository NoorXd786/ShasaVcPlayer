#
# Copyright (C) 2021-2022 by MdNoor786@Github, < https://github.com/MdNoor786 >.
#
# This file is part of < https://github.com/MdNoor786/ShasaVcPlayer > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MdNoor786/ShasaVcPlayer/blob/master/LICENSE >
#
# All rights reserved.

import re
from os import path

from yt_dlp import YoutubeDL

from ShasaMusic.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.regex = r"^(https:\/\/soundcloud.com\/)(.*)$"
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
        }

    async def valid(self, link: str):
        return bool(re.search(self.regex, link))

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            minfo = d.extract_info(url)
        except:
            return False
        xyz = path.join("downloads", f"{minfo['id']}.{minfo['ext']}")
        duration_min = seconds_to_min(minfo["duration"])
        track_details = {
            "title": minfo["title"],
            "duration_sec": minfo["duration"],
            "duration_min": duration_min,
            "uploader": minfo["uploader"],
            "filepath": xyz,
        }
        return track_details, xyz
