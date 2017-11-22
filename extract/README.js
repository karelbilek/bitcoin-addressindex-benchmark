How to extract random addresses
===

This goes through blockchain and randomly selects sample of addresses, around 70 000 of them (around every 10.000 address)


```bash
yarn # or npm install
cat ~/.bitcoin/blocks/blk*.dat | node do.js > addresses_sorted
cat addresses_sorted | grep -v '^bc1' | sort -R | uniq > addresses

```
