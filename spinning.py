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
def spin_words(x):
    str(x)
    x = x + " "
    z = ""
    a = 0
    g = ""
    for c in x:
        if c != " ":
            a += 1
            z += c
        else:
            if a >= 5:
                b = z[::-1]
                g += b
                g += " "
            else:
                d = z
                g += d
                g += " "
            a = 0
            z = ""
            continue
    if "suboba" in g:
        new_g = g.replace("suboba", "amogus_ne_lubim")
        return new_g
    else:
        return g

print (spin_words("suti voprosa takova blablabla abobus"))
#ЭТО ТЕСТЫ ИХ НЕ ТРОГАТЬ!!!!!!
def test_spins():
    assert spin_words("самара владивосток владикавказ омск москва") == "арамас котсовидалв заквакидалв омск авксом"
def test_abobus_spin():
    assert spin_words("suti voprosa takova blablabla abobus") == "suti asorpov avokat albalbalb amogus_ne_lubim"

