from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22353451"))
API_HASH = getenv("API_HASH", "6c7fef11674ea37fc361a0a04e027a9e")

BOT_TOKEN = getenv("BOT_TOKEN", "6036097392:AAHy6AZmnTlixl0gz2o6KxMhoJGQiQY13bc")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6136633222"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQAWLKr4DcSGmgdxdT3pWQr5wPwxI-ruJOtZbGbNL4edh5apjDgPKQiOoHvAOXyrjvsmp7Pof3PpRaEyDqT8MN5XQFuJFGa2Ght30zWkZ3eG6gOdI0IytM9L6FRnzaeMLTGieK5nzlsfwir8UtOiafheg3kghrQJwGTUA3lbuPzr5X5mDW78EDZ23ULY7CRmL6Gsl_KioRtoE9qZmtVZ7yPNjDB0XVSz55O1shZ3vC12nCX5-rVdCAUwfViotuMVoH1llx-ZmrZUkCLRjUhEafJwgU8HxfZDrSBkb1oDrxTMuHpqKqNjhO3fdPhHAGJeq8F9EpnOS_vDCGJtzAI6eOfhAAAAAU64uvkA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615696633").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
