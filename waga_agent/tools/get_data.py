import os
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()

key: str = os.getenv("SUPABASE_KEY")
url: str = os.getenv("SUPABASE_URL")

SUPABASE_CLIENT: Client = create_client(url, key)
