import os
from dotenv import load_dotenv
from supabase.client import Client, create_client

load_dotenv()

class SupabaseInit:
    def __init__(self):
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        if not supabase_url or not supabase_key:
            raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")
        self.client: Client = create_client(supabase_url, supabase_key)

    def get_client(self) -> Client:
        return self.client
    
    def get_tracked_wallets_list(self, table_name: str, discord_user__id: str):
        return self.client.table(table_name) \
            .select("tracked_wallets_list") \
            .eq("discord_user__id", discord_user__id) \
            .execute()
    
    def delete_tracked_wallet(self, table_name: str, discord_user__id: str, tracked_wallet_address: str):
        return self.client.table(table_name) \
            .delete() \
            .eq("discord_user__id", discord_user__id) \
            .eq("tracked_wallet_address", tracked_wallet_address) \
            .execute()
    
    def insert_tracked_wallet(self, table_name: str, discord_user__id: str, tracked_wallet_address: str):
        return self.client.table(table_name) \
            .insert({
                "discord_user__id": discord_user__id,
                "tracked_wallet_address": tracked_wallet_address
            }) \
            .execute()