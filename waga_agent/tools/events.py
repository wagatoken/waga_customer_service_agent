from .get_data import SUPABASE_CLIENT


# TODO create a view only to get upcoming event
def get_events():
    """
    Retrieves information about all the upcoming events 


    """
    events = SUPABASE_CLIENT.table(
        "event_with_speakers").select("*").execute()
    return events.data
