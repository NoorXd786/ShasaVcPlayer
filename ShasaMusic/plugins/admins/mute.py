#
# Copyright (C) 2021-2022 by MdNoor@Github, < https://github.com/MdNoor786 >.
#
# This file is part of < https://github.com/MdNoor786/ShasaVcPlayer > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MdNoor786/ShasaVcPlayer/blob/main/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from ShasaMusic import app
from ShasaMusic.core.call import Shasa
from ShasaMusic.utils.database import is_muted, mute_on
from ShasaMusic.utils.decorators import AdminRightsCheck
from strings import get_command

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(filters.command(MUTE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await Shasa.mute_stream(chat_id)
    await message.reply_text(_["admin_6"].format(message.from_user.mention))
