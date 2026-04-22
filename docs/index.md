# Coinone Documentation

<!-- English -->
## English

Welcome to the **Coinone** documentation for bt_api.

**Coinone** is a South Korean cryptocurrency exchange offering Spot trading. It is known for its strong presence in the Korean Won (KRW) market.

### Overview

`bt_api_coinone` provides a unified interface to Coinone exchange through the bt_api plugin architecture. It supports:

- **Spot Trading**: Market data and order placement for spot pairs
- **Market Data**: Ticker, Order Book, K-Lines, Trade History, Exchange Info
- **Account**: Balance queries, Order management

### Installation

```bash
pip install bt_api_coinone
```

### Quick Start

```python
from bt_api_py import BtApi

# Initialize without authentication (public data only)
api = BtApi()

# Spot ticker (public)
ticker = api.get_tick("COINONE___SPOT", "BTCKRW")
print(f"BTC/KRW spot: {ticker}")

# With authentication
api_auth = BtApi(exchange_kwargs={
    "COINONE___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

# Get balance
balance = api_auth.get_balance("COINONE___SPOT")

# Place order
order = api_auth.make_order(
    exchange_name="COINONE___SPOT",
    symbol="BTCKRW",
    size=0.001,
    price=50000000,
    order_type="bid",
)
```

### Supported Operations

#### Spot (COINONE___SPOT)

| Operation | Auth Required | Description |
|-----------|---------------|-------------|
| `get_tick` / `get_ticker` | No | Rolling ticker |
| `get_depth` | No | Order book depth |
| `get_kline` | No | Candlestick data |
| `get_exchange_info` | No | Market listings |
| `get_trade_history` / `get_trades` | No | Trade execution records |
| `get_balance` | Yes | Asset balances |
| `get_account` | Yes | Account information |
| `make_order` | Yes | Place order |
| `cancel_order` | Yes | Cancel pending order |
| `query_order` | Yes | Query order by ID |
| `get_open_orders` | Yes | Get all open orders |
| `get_deals` | Yes | Get deal history |

### Supported Symbols

- **Spot**: `BTCKRW`, `ETHKRW`, `XRPKRW`, `EOSKRW`, and 50+ KRW trading pairs

### Exchange Codes

```
COINONE___SPOT     # Spot trading (Korean Won market)
```

### Error Handling

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINONE___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("COINONE___SPOT")
except Exception as e:
    print(f"Error: {e}")
```

### More Information

- [GitHub Repository](https://github.com/cloudQuant/bt_api_coinone)
- [Issue Tracker](https://github.com/cloudQuant/bt_api_coinone/issues)
- [bt_api Documentation](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base Documentation](https://bt-api-base.readthedocs.io/)

---

## 中文

欢迎使用 bt_api 的 **Coinone** 文档。

**Coinone** 是一家韩国加密货币交易所，提供现货交易。它在韩元（KRW）市场有很强的存在感。

### 概述

`bt_api_coinone` 通过 bt_api 插件架构提供连接 Coinone 交易所的统一接口。支持：

- **现货交易**：现货交易对的市场数据和下单
- **行情数据**：行情、订单簿、K线、成交历史、交易所信息
- **账户**：余额查询、订单管理

### 安装

```bash
pip install bt_api_coinone
```

### 快速开始

```python
from bt_api_py import BtApi

# 初始化（无需认证，仅获取公开数据）
api = BtApi()

# 现货行情（公开接口）
ticker = api.get_tick("COINONE___SPOT", "BTCKRW")
print(f"BTC/KRW 现货: {ticker}")

# 需要认证的操作
api_auth = BtApi(exchange_kwargs={
    "COINONE___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

# 获取余额
balance = api_auth.get_balance("COINONE___SPOT")

# 下单
order = api_auth.make_order(
    exchange_name="COINONE___SPOT",
    symbol="BTCKRW",
    size=0.001,
    price=50000000,
    order_type="bid",
)
```

### 支持的操作

#### 现货 (COINONE___SPOT)

| 操作 | 需要认证 | 说明 |
|------|---------|------|
| `get_tick` / `get_ticker` | 否 | 滚动行情 |
| `get_depth` | 否 | 订单簿深度 |
| `get_kline` | 否 | K线数据 |
| `get_exchange_info` | 否 | 市场列表 |
| `get_trade_history` / `get_trades` | 否 | 成交记录 |
| `get_balance` | 是 | 资产余额 |
| `get_account` | 是 | 账户信息 |
| `make_order` | 是 | 下单 |
| `cancel_order` | 是 | 取消挂单 |
| `query_order` | 是 | 按ID查询订单 |
| `get_open_orders` | 是 | 获取所有挂单 |
| `get_deals` | 是 | 获取成交历史 |

### 支持的交易对

- **现货**: `BTCKRW`, `ETHKRW`, `XRPKRW`, `EOSKRW` 等 50+ 韩元交易对

### 交易所代码

```
COINONE___SPOT     # 现货交易（韩元市场）
```

### 错误处理

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINONE___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("COINONE___SPOT")
except Exception as e:
    print(f"错误: {e}")
```

### 更多信息

- [GitHub 仓库](https://github.com/cloudQuant/bt_api_coinone)
- [问题反馈](https://github.com/cloudQuant/bt_api_coinone/issues)
- [bt_api 文档](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base 文档](https://bt-api-base.readthedocs.io/)