from cipher_xs2428_mds import cipher_xs2428_mds

def test_cipher():
    expected = 'Bqqmf'
    actual = cipher_xs2428_mds.cipher('Apple', 1, True)
    assert actual == expected