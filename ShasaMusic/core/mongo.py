#
# Copyright (C) 2021-2022 by MdNoor786@Github, < https://github.com/MdNoor786 >.
#
# This file is part of < https://github.com/MdNoor786/ShasaVcPlayer > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MdNoor786/ShasaVcPlayer/blob/master/LICENSE >
#
# All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

import config

_mongo_async_ = _mongo_client_(config.MONGO_DB_URL)
_mongo_sync_ = MongoClient(config.MONGO_DB_URL)

mongodb = _mongo_async_.Shasa
pymongodb = _mongo_sync_.Shasa
