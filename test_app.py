from unittest.mock import patch
from app import app


def test_default_host_and_port():
    with patch("app.app.run") as mock_run:
        app.run(debug=True)
        mock_run.assert_called_once_with(host="localhost", port=5000, debug=True)


def test_custom_host_and_port():
    with patch("app.app.run") as mock_run:
        app.run(host="0.0.0.0", port=8080, debug=True)
        mock_run.assert_called_once_with(host="0.0.0.0", port=8080, debug=True)
