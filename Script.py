class script(object):
    START_TXT = """ð·ð´ð»ð¾ {},
ð¼ð¢ ðððð , <a href=https://t.me/film_provider_bot>Thanos</a>, ð¸ð'ð ðððð¢ ðððð¢ ðððð ððð ðð ðð ð¢ððð ððððð ððð ðððð ðð ððððð, ððððð ððð ð¸'ðð ððððððð ðððððð ððððð ð¤
"""
    HELP_TXT = """ð·ð´ð {}
ðð¦ð³ð¦ ðð´ ðð©ð¦ ðð¦ð­ð± ðð°ð³ ððº ðð°ð®ð®ð¢ð¯ð¥ð´."""
    ABOUT_TXT = """
ððð¢ð¨ð§ ð ð¦ð ðð ðððððð
âµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµ
ââââââ° êªá¥êª®êªð½ êªð´á§ â±âââ±âÛªÛª
ââ­ââââââââââââââââ£ 
ââ£âª¼ ðð ððªð¶ð® - ðð·ð°ð½ð¾ð
ââ£âª¼ ðð²ð«ð»ðªð»ð»ð - ð¿ððð¾ð¶ðð°ð¼
ââ£âª¼ ððªð·ð°ð¾ðªð°ð® - ð¿ððð·ð¾ð½ ð¹
ââ£âª¼ ððªð½ðª ððªð¼ð® - ð¼ð¾ð½ð¶ð¾ ð³ð±
ââ£âª¼ ðð¸ð½ ð¼ð®ð»ð¿ð®ð» -  ð·ð´ðð¾ðºð
ââ£âª¼ ðð¾ð²ðµð­ ð¢ð½ðªð½ð¾ð¼ - v1.0.1 [ ð±ð´ðð° ]
ââ°ââââââââââââââââ£ âââââââââââââââââââââ±âÛªÛª"""
    SOURCE_TXT = """<b>NOTE:</b>
- ð° ðð  ð ðððððð ðððððð ððððððð. 

ð ðð¦ð§ðð¥:
<a href="https://t.me/geronimo1234"> Geronimo Lover </a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

â¢/whois :-give a user full details"""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
â¢ /alive - check me alive or deadð¤§
Just for a rasamð"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
â¡ï¸ /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

â¡ï¸ <b>example</b> : - /covid India"""
    STICKER_TXT ="""<b>Hey Buddy Send me a sticker and then I give U the sticker id (No Commands)</b>"""
    SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

ð Command

â¢ /song or /mp3 (songname) - download song from yt servers.
â¢ /video or /mp4 (songname) - download video from yt servers

Usage
- working pm and groups"""
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json

Features:
Message Editting JSON
Pm Support
Group Support

Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>ð Commands & Usage:</b>

â /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

â /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>ð² NOTHING MUCH JUST SOME FUN THINGS</b>
tðð ðððð ð®ðð: 
ð£. /dice - Roll The Dice 
ð¤. /Throw ðð /Dart - ð³ð ð¬ðºðð¾ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - add a filter in chat.
â¢ /filters - list all the filters of a chat.
â¢ /del - delete a specific filter in chat.
â¢ /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - connect a particular chat to your PM.
â¢ /disconnect  - disconnect from a chat.
â¢ /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
â¢ /paste [text] - paste the given text on Pasty
â¢ /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
â¢ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
â¢ /id - get id of a specifed user.
â¢ /info  - get information about a user.
â¢ /json - get the json details of a message.

<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
â¢ /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on both pm and group.
â¢ IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
â¢ /imdb  - get the film information from IMDb source.
â¢ /search  - get the film information from various sources.

<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ More search tools can be found on inline.
â¢ Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
â¢ /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on group.
â¢ These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
â¢ /ban - ban a user.
â¢ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
â¢ /mute - mute a user.
â¢ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
â¢ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on group.
â¢ These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - to get the rescent errors.
â¢ /stats - to get status of files in db.
â¢ /delete - to delete a specific file from db.
â¢ /users - to get list of my users and ids.
â¢ /chats - to get list of the my chats and ids.
â¢ /leave - to leave from a chat.
â¢ /disable - do disable a chat.
â¢ /ban_users - to ban a user.
â¢ /unban_users - to unban a user.
â¢ /channel - to get list of total connected channels.
â¢ /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**â¦ï¸ READ THIS INSTRUCTION â¦ï¸**

__ð£ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately ð__

**ð JOIN THIS CHANNEL & TRY AGAIN ð**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
â¢ /inkick - command with required arguments and i will kick members from group.
â¢ /instatus - to check current status of chat member from group.
â¢ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
â¢ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
â¢ /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """âYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âï¸ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """ð® Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """âI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """âï¸ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
