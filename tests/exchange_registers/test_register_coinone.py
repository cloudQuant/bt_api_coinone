from __future__ import annotations

from bt_api_coinone.exchange_registers import register_coinone


class TestRegisterCoinone:
    def test_module_imports(self):
        assert register_coinone is not None
