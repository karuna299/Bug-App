# test_bank.py

import pytest
from bank import withdraw

def test_withdraw_valid():
    """Test withdrawing an amount within balance."""
    assert withdraw(50, 100) == 50  # $50 withdrawn from $100 should leave $50

def test_withdraw_exact():
    """Test withdrawing the exact balance."""
    assert withdraw(100, 100) == 0  # Withdrawing all should leave $0

def test_withdraw_insufficient():
    """Test withdrawing more than the balance (should raise error)."""
    with pytest.raises(ValueError, match="Insufficient funds!"):
        withdraw(200, 100)  # $200 withdrawal should fail when balance is $100
