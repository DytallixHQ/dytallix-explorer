# Dytallix Explorer

Public block explorer for the Dytallix testnet.

The live explorer is served from the main Dytallix site and exposes chain
status, recent blocks, recent transactions, validator stats, and wallet
lookups.

## Live Service

- Explorer page: `https://dytallix.com/build/blockchain`
- Blockchain API base: `https://dytallix.com/api/blockchain`
- Verified against the live deployment on April 5, 2026

There is no live public `explorer.dytallix.com` host. The supported explorer
page lives at `dytallix.com/build/blockchain`.

## What The Explorer Uses

The deployed explorer page currently calls these public endpoints:

- `GET /api/blockchain/status`
- `GET /api/blockchain/blocks?limit=10`
- `GET /api/blockchain/block/:id`
- `GET /api/blockchain/transactions?limit=10`
- `GET /api/blockchain/transactions/:hash`
- `GET /api/blockchain/metrics`
- `GET /api/blockchain/api/staking/validators`
- `GET /api/blockchain/account/:address`
- `GET /api/blockchain/balance/:address`

## Search Inputs

The live search box accepts:

- D-Addr wallet addresses
- transaction hashes
- block heights
- block hashes
- `latest`

## Quick Checks

### Node Status

```bash
curl https://dytallix.com/api/blockchain/status
```

Observed response on April 5, 2026:

```json
{
  "chain_id": "dyt-local-1",
  "gas": {
    "default_gas_limit": 2000,
    "default_signed_fee": 2000000,
    "fee_denom": "udgt",
    "min_gas_price": 1000,
    "per_additional_signature": 700,
    "per_byte": 2,
    "per_kv_read": 40,
    "per_kv_write": 120,
    "transfer_base": 500,
    "version": 1
  },
  "latest_height": 265063,
  "mempool_size": 0,
  "status": "healthy",
  "syncing": false,
  "timestamp": 1775412747
}
```

### Recent Blocks

```bash
curl 'https://dytallix.com/api/blockchain/blocks?limit=2'
```

Observed response excerpt on April 5, 2026:

```json
{
  "blocks": [
    {
      "asset_hashes": [],
      "hash": "0x0442fa9041563ddf27c1f860dcb09eab2f7c9161298f5eb18a2d519521a53046",
      "height": 265063,
      "timestamp": 1775412737,
      "txs": []
    },
    {
      "asset_hashes": [],
      "hash": "0x5adf1c8ebd1b9bfdb47e8057f3b3080c432087cf4f3397fb271b55db17f6976e",
      "height": 265062,
      "timestamp": 1775412722,
      "txs": []
    }
  ]
}
```

### Latest Block

```bash
curl https://dytallix.com/api/blockchain/block/latest
```

### Recent Transactions

```bash
curl 'https://dytallix.com/api/blockchain/transactions?limit=3'
```

Observed response excerpt on April 5, 2026:

```json
{
  "transactions": [
    {
      "amount": "1000000",
      "block_height": 264655,
      "denom": "udrt",
      "fee": "2049000",
      "from": "dytallix1as40k2hz7sh8srfqrtfxlw38873r5gg97dmx9sc5mlqt0jjajc6q6rfwd6",
      "hash": "0xea54025c2c56ba27bde0d5c4ec435b33f27549f1213fe4c4b96b2ea3ba9707b3",
      "nonce": 0,
      "status": "confirmed",
      "timestamp": 1775406617,
      "to": "dytallix1as40k2hz7sh8srfqrtfxlw38873r5gg97dmx9sc5mlqt0jjajc6q6rfwd6"
    }
  ]
}
```

### Transaction Lookup

```bash
curl https://dytallix.com/api/blockchain/transactions/0xea54025c2c56ba27bde0d5c4ec435b33f27549f1213fe4c4b96b2ea3ba9707b3
```

### Wallet Lookup

```bash
curl https://dytallix.com/api/blockchain/account/dytallix1as40k2hz7sh8srfqrtfxlw38873r5gg97dmx9sc5mlqt0jjajc6q6rfwd6
curl https://dytallix.com/api/blockchain/balance/dytallix1as40k2hz7sh8srfqrtfxlw38873r5gg97dmx9sc5mlqt0jjajc6q6rfwd6
```

Observed balance response on April 5, 2026:

```json
{
  "address": "dytallix1as40k2hz7sh8srfqrtfxlw38873r5gg97dmx9sc5mlqt0jjajc6q6rfwd6",
  "balances": {
    "udgt": {
      "balance": "7951000",
      "description": "Governance token for voting and staking",
      "formatted": "7 DGT",
      "type": "governance"
    },
    "udrt": {
      "balance": "101000000",
      "description": "Reward token for transaction fees and staking rewards",
      "formatted": "101 DRT",
      "type": "reward"
    }
  },
  "legacy_balance": "7951000"
}
```

### Validator Stats

```bash
curl https://dytallix.com/api/blockchain/api/staking/validators
```

The live response currently reports `4` active validators.

### Metrics Feed

```bash
curl https://dytallix.com/api/blockchain/metrics
```

This is a Prometheus text endpoint used by the explorer for throughput and node
metrics.

## Related Repositories

- SDK: https://github.com/DytallixHQ/dytallix-sdk
- Faucet: https://github.com/DytallixHQ/dytallix-faucet
- Node: https://github.com/DytallixHQ/dytallix-node
- Docs: https://github.com/DytallixHQ/dytallix-docs
- Org profile: https://github.com/DytallixHQ

## Support

- Website: https://dytallix.com
- Discord: https://discord.gg/eyVvu5kmPG
