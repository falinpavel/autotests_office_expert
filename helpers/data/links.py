import os

from dotenv import load_dotenv

load_dotenv()


class Links:

    BASE_URL = f"{os.getenv('BASE_URL')}"

    CONTACTS_URL = f"{BASE_URL}/contacts/"
