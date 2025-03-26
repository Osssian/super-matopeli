# test_wormgame.py
# Yksikkötestit matopelin tärkeimmille törmäystarkistuksille
import pytest
# Tarkistaa osuuko mato ruudun ulkopuolelle (seinään)
def tormaako_seinaan(x, y, leveys, korkeus):
    return x < 0 or x >= leveys or y < 0 or y >= korkeus

# Tarkistaa osuuko mato itseensä
def tormaako_itseensa(mato_lista):
    pää = mato_lista[-1] # pään koordinaatit
    return pää in mato_lista[:-1] # Onko pää osa muuta matoa

# Testaa seinään törmäämistä:
def test_tormaako_seinaan():
    # Pitäisi törmätä: vasemmalta ulos, oikealta ulos, ylhäältä ulos, alhaalta ulos
    assert tormaako_seinaan(-10, 50, 600, 400)
    assert tormaako_seinaan(600, 100, 600, 400)
    assert not tormaako_seinaan(100, 100, 600, 400)

# Testaa itseensä törmäämistä:
def test_tormaako_itseensa():
    mato = [[100, 100], [110, 100], [120, 100], [130, 100], [120, 100]]
    # Pitäisi törmätä: mato on törmännyt itseensä
    mato2 = [[100, 100], [110, 100], [120, 100], [130, 100], [140, 100]]
    #
    assert tormaako_itseensa(mato)
    assert not tormaako_itseensa(mato2)
