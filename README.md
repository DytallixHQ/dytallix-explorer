# Dytallix Explorer

Public explorer surface map and endpoint documentation for the Dytallix
testnet.

Keypair, faucet, transfer, and basic contract lifecycle are available for experimentation on the public testnet. Staking, governance, and some advanced or operator paths are not yet production-complete.

The live explorer is served from the main Dytallix site and exposes chain
status, recent blocks, recent transactions, validator stats, and wallet
lookups.

This repository currently documents the public explorer surface. It does not
publish the deployed frontend source for `dytallix.com/build/blockchain`.
The hosted explorer frontend source is not currently published in a separate public repo.

The local source-of-truth file for this docs-only repo is `public-surface.json`.
It captures the live explorer page URL, the read APIs it uses, and the current
validator feed shape so README drift is caught in CI.

## Repository Scope

This is a docs-only service-surface repository. It exists to describe the live
public explorer page and API shape, not to publish the deployed explorer
frontend source.

It is not sufficient on its own to rebuild, audit, or redeploy the live
explorer frontend. Treat this repository as an honest documentation boundary,
not as the canonical frontend source repository.

## Prerequisites

No build toolchain is required to read or use this repository. If you want to
run the local alignment check, use Python 3 for `scripts/check_public_alignment.py`.

## Contributing

Keep changes limited to the documented explorer surface. If the live API or
runtime behavior changed, update `public-surface.json`, the README examples, and
run `python3 scripts/check_public_alignment.py` before opening a PR.

## Live Service

- Explorer page: `https://dytallix.com/build/blockchain`
- Blockchain API base: `https://dytallix.com/api/blockchain`
- Verified against the live deployment on April 13, 2026

The supported explorer page lives at `dytallix.com/build/blockchain` on the
main site.

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

Observed response on April 13, 2026:

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

Observed response excerpt on April 13, 2026:

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

The live response currently reports a single current proposer entry sourced from
validator secrets. This is intentionally different from the older placeholder
four-validator shape.

Observed response excerpt on April 13, 2026:

```json
{
  "active_validators": 1,
  "total_validators": 1,
  "validators": [
    {
      "address": "dytallix1cadh4gx44m3gj5wuu23up5qhgwp52cxq3mv8499xv09ne4q95hdqehq3z6",
      "moniker": "Current Proposer",
      "status": "operator-preview",
      "source": "validator_secrets"
    }
  ]
}
```

### Runtime Capability Contract

Compatible node deployments now expose a machine-readable public contract at:

```bash
curl https://dytallix.com/api/capabilities
```

Explorer-adjacent integrations should prefer that contract over scraping README
copy for staking/governance/public-write assumptions.

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

For canonical public integration guidance, start with the docs repo:
https://github.com/DytallixHQ/dytallix-docs

This repository only covers the explorer surface description. The canonical
frontend source for the hosted explorer page is not currently published in a
separate public repo.

## Support

- Website: https://dytallix.com
- Discord: https://discord.gg/eyVvu5kmPG
