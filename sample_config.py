HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "5815712338:AAFQu1nCijZiAz2A8Visbm8jTZUSbITvlyQ"
    ARQ_API_KEY = "ZQTOWB-ACELVV-QRYUKX-BGFRTA-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "hinglish"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
