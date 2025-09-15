from .get_data import SUPABASE_CLIENT


# TODO create a view only to get published courses
def get_courses():
    """
    Retrieves information about all the published courses 


    """
    courses = SUPABASE_CLIENT.table(
        "courses").select("*").execute()
    return courses.data
