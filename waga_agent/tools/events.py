from .get_data import get_supabase_client

SUPABASE_CLIENT = get_supabase_client()
# TODO create a view only to get upcoming event


def get_events():
    """
    Retrieves information about all the upcoming events 


    """
    events = SUPABASE_CLIENT.table(
        "event_with_speakers").select("*").execute()
    return events.data
