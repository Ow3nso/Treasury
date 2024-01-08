# ----- 3rd Party Libraries ------
from import_export import resources

# ----- In-Built Libraries -----
from .models import Process_Statement

# ----- Resources -----
class Process_Statement_Resource(resources.ModelResource):
    class Meta:
        model = Process_Statement
        import_id_fields = ["receipt_number"]
        skip_unchanged = True
        use_bulk = True