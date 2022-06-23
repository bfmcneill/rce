from rce.secret.app_secret import AppSecret


def test_app_secret_from_config():
    app_secret = AppSecret.from_json_config()
    assert len(app_secret.client_id) > 0
    assert len(app_secret.secret) > 0