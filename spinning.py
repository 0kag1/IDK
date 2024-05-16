"""
напиши функцию spin_words которая принимает строку
и если в слове больше или равно 5 букв то переворачивает её.
также если есть слово "abobus" то его нужно заменить на "amogus_ne_lubim"
примеры: 
print(spin_words("suti voprosa takova blablabla abobus"))
>>> suti asorpov avokat albalbalb amogus_ne_lubim
print(spin_words("тагил чечня россия гремания китай украина молдова сша"))
>>> лигат янчеч яиссор яинамерг йатик аниарку аводлом сша
"""
def spin_words(sentence):





#ЭТО ТЕСТЫ ИХ НЕ ТРОГАТЬ!!!!!!
def test_spins():
    assert spin_words("самара владивосток владикавказ омск москва") == "арамас котсовидалв заквакидалв омск авксом"
def test_abobus_spin():
    assert spin_words("suti voprosa takova blablabla abobus") == "suti asorpov avokat albalbalb amogus_ne_lubim"

