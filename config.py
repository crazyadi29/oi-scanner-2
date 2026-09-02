# ─────────────────────────────────────────────
#  S4-DEPTH BOT  |  config.py
#  Separate bot — shows top 3 CE/PE with live writing detection
# ─────────────────────────────────────────────
import os

# ── Telegram (SEPARATE bot — use new token/chat id) ────
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN_2")
TELEGRAM_CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID_2")

if not TELEGRAM_BOT_TOKEN:
    raise EnvironmentError(
        "Missing required environment variable: TELEGRAM_BOT_TOKEN_2. "
        "Set it in Railway project settings for this service (or .env locally)."
    )
if not TELEGRAM_CHAT_ID:
    raise EnvironmentError(
        "Missing required environment variable: TELEGRAM_CHAT_ID_2. "
        "Set it in Railway project settings for this service (or .env locally)."
    )

# ── Fyers (SEPARATE app id — create a new app on myapi.fyers.in) ──
FYERS_CLIENT_ID    = os.getenv("FYERS_APP_ID_2", "")
FYERS_SECRET_KEY   = os.getenv("FYERS_SECRET_KEY_2", "")
FYERS_REDIRECT_URI = os.getenv("FYERS_REDIRECT_URI_2", "https://trade.fyers.in/api-login/redirect-uri/index.html")
FYERS_ACCESS_TOKEN = os.getenv("FYERS_ACCESS_TOKEN_2", "")

# ── Strategy settings (SAME as main bot) ───────
MIN_MOVE_PCT       = 1.5
SCAN_INTERVAL_SEC  = 8
MAX_STOCKS_PER_RUN = 100
COOLDOWN_MINUTES   = 30
TOP_N_OTM          = 3          # ← changed: top 3 instead of top 2

# ── Market hours (IST, 24h) ────────────────────
MARKET_OPEN_H  = 9
MARKET_OPEN_M  = 15
MARKET_CLOSE_H = 15
MARKET_CLOSE_M = 30
