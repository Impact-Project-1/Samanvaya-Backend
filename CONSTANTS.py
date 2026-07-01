# file sizes by memory
FILESIZE_5MB = 5 * 1024 * 1024
FILESIZE_10MB = 10 * 1024 * 1024
FILESIZE_50MB = 50 * 1024 * 1024

# file sizes by category
FILESIZE_LARGE = FILESIZE_50MB * 2 # large file, size 100MB
FILESIZE_MEDIUM = FILESIZE_50MB # medium file, size 50 MB
FILESIZE_SMALL = FILESIZE_10MB

# Profile properties
PROP_PROFILE_VERIFIED = 1<<8 # check whether the proifle was verified
PROP_PROFILE_COMPLETED = 1<<7 # flag to check whether profile has been completed
PROP_PROFILE_VISIBLE = 1<<6 # controls profile visiblity

# types of user
USER_ADMIN = 1<<2
USER_CUSTOMER = 1<<3
USER_VENDOR = 1<<4

# Chat Status variables
CHAT_OPENED = 1<<2
CHAT_CLOSED = 1<<3
CHAT_ACTIVE = 1<<4 # if the chat is activve in realtime
CHAT_ARCHIVED = 1<<5
CHAT_OLD = 1<<6 # chat has been closed after opening after transaction, and moved to old chats (chat history)

# chat control variables
CHAT_INITIATED = 1<<2 # chat initiated by customer
CHAT_DISMISSED = 1<<3 # chat closed by customer
CHAT_REOPEN = 1<<4 # chat was reopened by customer