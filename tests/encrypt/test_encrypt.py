from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("string", "number")

    with pytest.raises(TypeError, match="tipo inválido para message"):    
        encrypt_message(1, 1)

    result = encrypt_message('Tryber', 3)
    assert result == "yrT_reb"

    result = encrypt_message('Tryber', 4)
    assert result == "re_byrT"

    result = encrypt_message('Tryber', 10)
    assert result == "rebyrT"