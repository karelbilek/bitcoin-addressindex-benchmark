var BlockStream = require('blkdat-stream');
var blockStream = new BlockStream();
var bitcoin = require('bitcoinjs-lib');

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

process.stdin.pipe(new BlockStream()).on('data', function (blockBuffer) {
  const block = bitcoin.Block.fromBuffer(blockBuffer)
  block.transactions.forEach(tx => {
    tx.outs.forEach(outp => {
      try {
        const add = bitcoin.address.fromOutputScript(outp.script);
        if (getRandomInt(10000) === 2) {
          console.log(add);
        }
      } catch (e) {
    //    console.log("OOPS");
      }
    });
  });
})
