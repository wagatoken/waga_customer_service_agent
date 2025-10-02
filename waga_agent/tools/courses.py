from .get_data import get_supabase_client

SUPABASE_CLIENT = get_supabase_client()


def get_courses():
    """
    Retrieves information about all the published courses 


    """
    courses = SUPABASE_CLIENT.table(
        "courses").select("*").execute()
    return courses.data
