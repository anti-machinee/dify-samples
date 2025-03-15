
import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from unittest.mock import patch, MagicMock

from core.model_runtime.entities.model_entities import ModelType
from services.model_provider_service import ModelProviderService
from controllers.console.workspace.model_providers import ModelProviderListApi

@pytest.fixture
def app():
    app = Flask(__name__)
    app.add_url_rule('/model_provider_list', view_func=ModelProviderListApi.as_view('model_provider_list'))
    
    return app


@pytest.fixture
def client(app: Flask):
    return app.test_client()


@pytest.fixture
def mock_dependencies():
    with patch('your_project.api.resources.model_provider_list.current_user') as mock_user, \
         patch.object(ModelProviderService, 'get_provider_list') as mock_service:
        
        mock_user.current_tenant_id = 'tenant_123'
        mock_service.return_value = [{'provider_id': 1, 'name': 'Provider A'}, {'provider_id': 2, 'name': 'Provider B'}]
        
        yield mock_user, mock_service

def test_get_provider_list(client: FlaskClient, mock_dependencies):
    mock_user, mock_service = mock_dependencies
    response = client.get('/model_provider_list?model_type=some_model_type')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'data' in json_data
    assert len(json_data['data']) == 2
    assert json_data['data'][0]['provider_id'] == 1
    assert json_data['data'][0]['name'] == 'Provider A'

    mock_service.assert_called_with(tenant_id='tenant_123', model_type='some_model_type')

# Test case: test GET request without model_type parameter
def test_get_provider_list_without_model_type(client: FlaskClient, mock_dependencies):
    mock_user, mock_service = mock_dependencies
    
    # Simulate a GET request without model_type
    response = client.get('/model_provider_list')

    # Assert status code
    assert response.status_code == 200
    
    # Assert the response JSON
    json_data = response.get_json()
    assert 'data' in json_data
    assert len(json_data['data']) == 2
    assert json_data['data'][0]['provider_id'] == 1
    assert json_data['data'][0]['name'] == 'Provider A'

    # Assert the mock service was called with None for model_type
    mock_service.assert_called_with(tenant_id='tenant_123', model_type=None)
