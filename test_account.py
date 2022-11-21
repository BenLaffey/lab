import pytest
from account import *


class Test:

    def setup_method(self):
        self.account1 = Account('John')

    def teardown_method(self):
        del self.account1

    def test___init__(self):
        assert self.account1.get_name() == 'John'
        assert self.account1.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(10.2) is True
        assert self.account1.get_balance() == pytest.approx(10.2, abs=0.001)
        assert self.account1.deposit(-10) is False
        assert self.account1.get_balance() == pytest.approx(10.2, abs=0.001)
        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == pytest.approx(10.2, abs=0.001)

    def test_withdraw(self):
        self.account1.deposit(10.2)
        assert self.account1.get_balance() == pytest.approx(10.2, abs=0.001)
        assert self.account1.withdraw(5) is True
        assert self.account1.get_balance() == pytest.approx(5.2, abs=0.001)
        assert self.account1.withdraw(10) is False
        assert self.account1.get_balance() == pytest.approx(5.2, abs=0.001)
        assert self.account1.withdraw(-10) is False
        assert self.account1.get_balance() == pytest.approx(5.2, abs=0.001)
        assert self.account1.withdraw(0) is False
        assert self.account1.get_balance() == pytest.approx(5.2, abs=0.001)
