from rce.secret.auth_secret import AuthSecret

def test_auth_secret_from_json():
    auth_secret = AuthSecret.from_json_config()
    assert len(auth_secret.username) > 0
    assert len(auth_secret.password) > 0