from gohighlevel_api import Client
from gohighlevel_api.models.create_contact_dto import CreateContactDto

def test_client_import():
    """Verify that the Client class can be imported."""
    assert Client is not None

def test_model_import_and_instantiation():
    """Verify that a model can be imported and instantiated."""
    assert CreateContactDto is not None
