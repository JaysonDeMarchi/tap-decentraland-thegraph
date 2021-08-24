"""DecentralandTheGraph tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_decentraland_thegraph.orders_streams import (
    WearablesOrdersStream,
    ParcelsOrdersStream,
    EstatesOrdersStream,
    EstatesHistoricalStream,
    NamesOrdersStream,
)

from tap_decentraland_thegraph.bids_streams import (
    WearablesBidsStream,
    ParcelsBidsStream,
    EstatesBidsStream,
    EstatesBidsHistoricalStream,
    NamesBidsStream,
)

from tap_decentraland_thegraph.nfts_streams import (
    WearablesStream,
    EstatesStream,
    ParcelsStream,
    NamesStream
)

from tap_decentraland_thegraph.nfts_streams_polygon import (
    WearablesPolygonStream,
    CollectionsPolygonStream,
    ItemsPolygonStream
)

from tap_decentraland_thegraph.orders_streams_polygon import (
    WearablesOrdersPolygonStream,
    WearablesPrimarySalesPolygonStream,
)

from tap_decentraland_thegraph.bids_streams_polygon import (
    WearablesBidsPolygonStream,
)

from tap_decentraland_thegraph.mana_holders_streams import (
    ETHManaStream,
    PolygonManaStream,
)

STREAM_TYPES = [
    WearablesOrdersStream,
    ParcelsOrdersStream,
    EstatesOrdersStream,
    EstatesHistoricalStream,
    NamesOrdersStream,
    WearablesStream,
    EstatesStream,
    ParcelsStream,
    NamesStream,
    WearablesPolygonStream,
    WearablesBidsStream,
    ParcelsBidsStream,
    EstatesBidsStream,
    EstatesBidsHistoricalStream,
    NamesBidsStream,
    WearablesOrdersPolygonStream,
    WearablesBidsPolygonStream,
    ETHManaStream,
    PolygonManaStream,
    CollectionsPolygonStream,
    ItemsPolygonStream,
    WearablesPrimarySalesPolygonStream,
]


class TapDecentralandTheGraph(Tap):
    """DecentralandTheGraph tap class."""
    name = "tap-decentraland-thegraph"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("start_updated_at", th.IntegerType, default=1),
        th.Property("api_url", th.StringType, default='https://api.thegraph.com/subgraphs/name/decentraland/marketplace'),
        th.Property("polygon_api_url", th.StringType, default='https://api.thegraph.com/subgraphs/name/decentraland/collections-matic-mainnet'),
        th.Property("incremental_limit", th.IntegerType, default=20000),
        th.Property("eth_mana_holder_url", th.StringType, default='https://api.thegraph.com/subgraphs/name/decentraland/mana-ethereum-mainnet'),
        th.Property("polygon_mana_holder_url", th.StringType, default='https://api.thegraph.com/subgraphs/name/decentraland/mana-matic-mainnet'),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
