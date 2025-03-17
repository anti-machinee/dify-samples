import os
import unittest

from services.model_provider_service import ModelProviderService

from test_dify.setup_tests.setup_app import setup_app_real


class TestModelProviderService(unittest.TestCase):
    def setUp(self):
        self.app = setup_app_real()
        self.tenant_id = os.getenv("TENANT_ID")
        self.model_provider_service = ModelProviderService()

    def test_get_provider_list_without_model_type(self):
        with self.app.app_context():
            self.model_provider_service.get_provider_list(
                tenant_id=self.tenant_id,
                model_type=None
            )
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
