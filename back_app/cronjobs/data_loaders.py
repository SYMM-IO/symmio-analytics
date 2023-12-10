from app.models import (
    Quote,
    DailyHistory,
    TradeHistory,
    Account,
    User,
    Symbol,
    BalanceChange,
    RuntimeConfiguration,
)
from config.settings import Context
from context.graphql_client import Where
from utils.common_utils import convert_timestamps


def tag_tenant_to_id(data, context: Context):
    data["id"] = f"{context.tenant}_{data['id']}"
    return data


def tag_tenant_quote_id(data, context: Context):
    data["quote"] = f"{context.tenant}_{data['quote']}"
    return data


def load_quotes(config: RuntimeConfiguration, context: Context):
    out = context.utils.gc.load_all(
        lambda data: Quote(
            **convert_timestamps(tag_tenant_to_id(data, context)),
            tenant=context.tenant,
        ),
        Quote,
        method="quotes",
        fields=[
            "transaction",
            "partyB",
            "timestamp",
            "updateTimestamp",
            "symbolId",
            "quantity",
            "price",
            "quoteStatus",
            "positionType",
            "collateral",
            "partyBsWhiteList",
            "orderType",
            "openPrice",
            "mm",
            "maxInterestRate",
            "marketPrice",
            "lf",
            "id",
            "cva",
            "deadline",
            "closedAmount",
            "blockNumber",
            "avgClosedPrice",
            "account",
            "liquidatedSide",
        ],
        pagination_field_name="timestamp",
        additional_conditions=[
            Where(
                "updateTimestamp",
                "gte",
                str(int(config.lastSnapshotTimestamp.timestamp())),
            )
        ],
        load_from_database=True,
        save_to_database=True,
        context=context,
    )
    for o in out:
        pass


def load_trade_histories(config: RuntimeConfiguration, context: Context):
    out = context.utils.gc.load_all(
        lambda data: TradeHistory(
            **convert_timestamps(tag_tenant_quote_id(data, context)),
            tenant=context.tenant,
        ),
        TradeHistory,
        method="tradeHistories",
        fields=[
            "volume",
            "updateTimestamp",
            "transaction",
            "timestamp",
            "quoteStatus",
            "id",
            "blockNumber",
            "account",
            "quote",
        ],
        pagination_field_name="timestamp",
        additional_conditions=[
            Where(
                "updateTimestamp",
                "gte",
                str(int(config.lastSnapshotTimestamp.timestamp())),
            )
        ],
        load_from_database=False,
        save_to_database=True,
        context=context,
    )
    for o in out:
        pass


def load_accounts(config: RuntimeConfiguration, context: Context):
    out = context.utils.gc.load_all(
        lambda data: Account(**convert_timestamps(data), tenant=context.tenant),
        Account,
        method="accounts",
        fields=[
            "user",
            "updateTimestamp",
            "transaction",
            "timestamp",
            "quotesCount",
            "positionsCount",
            "name",
            "lastActivityTimestamp",
            "id",
            "accountSource",
        ],
        pagination_field_name="timestamp",
        additional_conditions=[
            Where(
                "updateTimestamp",
                "gte",
                str(int(config.lastSnapshotTimestamp.timestamp())),
            )
        ],
        load_from_database=False,
        save_to_database=True,
        context=context,
    )
    for o in out:
        pass


def load_balance_changes(config: RuntimeConfiguration, context: Context):
    out = context.utils.gc.load_all(
        lambda data: BalanceChange(**convert_timestamps(data), tenant=context.tenant),
        BalanceChange,
        method="balanceChanges",
        fields=[
            "type",
            "transaction",
            "timestamp",
            "id",
            "collateral",
            "amount",
            "account",
        ],
        pagination_field_name="timestamp",
        load_from_database=True,
        save_to_database=True,
        context=context,
    )
    for o in out:
        pass


def load_users(config: RuntimeConfiguration, context: Context):
    out = context.utils.gc.load_all(
        lambda data: User(**convert_timestamps(data), tenant=context.tenant),
        User,
        method="users",
        fields=[
            "transaction",
            "timestamp",
            "id",
        ],
        pagination_field_name="timestamp",
        load_from_database=True,
        save_to_database=True,
        context=context,
    )
    for o in out:
        pass


def load_symbols(config: RuntimeConfiguration, context: Context):
    out = context.utils.gc.load_all(
        lambda data: Symbol(**convert_timestamps(data), tenant=context.tenant),
        Symbol,
        method="symbols",
        fields=[
            "name",
            "timestamp",
            "tradingFee",
            "updateTimestamp",
            "id",
        ],
        pagination_field_name="timestamp",
        additional_conditions=[
            Where(
                "updateTimestamp",
                "gte",
                str(int(config.lastSnapshotTimestamp.timestamp())),
            )
        ],
        load_from_database=False,
        save_to_database=True,
        context=context,
    )
    for o in out:
        pass


def load_daily_histories(config: RuntimeConfiguration, context: Context):
    out = context.utils.gc.load_all(
        lambda data: DailyHistory(**convert_timestamps(data), tenant=context.tenant),
        DailyHistory,
        method="dailyHistories",
        fields=[
            "id",
            "quotesCount",
            "tradeVolume",
            "deposit",
            "withdraw",
            "allocate",
            "deallocate",
            "activeUsers",
            "newUsers",
            "newAccounts",
            "platformFee",
            "openInterest",
            "accountSource",
            "updateTimestamp",
            "timestamp",
        ],
        pagination_field_name="timestamp",
        additional_conditions=[
            Where(
                "updateTimestamp",
                "gte",
                str(int(config.lastSnapshotTimestamp.timestamp())),
            ),
        ],
        load_from_database=False,
        save_to_database=True,
        context=context,
    )
    for o in out:
        pass
