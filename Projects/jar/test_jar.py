from jar import Jar


def test_init():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3
    jar.deposit(1)
    assert jar.size == 4
def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9