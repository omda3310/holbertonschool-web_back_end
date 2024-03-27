const assert = require('assert');
const mocha = require('mocha');

const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('Return sum of integers', () => {
    assert.strictEqual(calculateNumber(1, 5), 6);
    assert.strictEqual(calculateNumber(4, 0), 4);
    assert.strictEqual(calculateNumber(3, -5), -2);
  })
  it('Return rounded number', () => {
    assert.strictEqual(calculateNumber(1.5, 7.3), 9);
    assert.strictEqual(calculateNumber(3, -5.4),-2);
    assert.strictEqual(calculateNumber(2.6, 3.9), 7);
    assert.strictEqual(calculateNumber(1.3, 0.1), 1);
  })
})
