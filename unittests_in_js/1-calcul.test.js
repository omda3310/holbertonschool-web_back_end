const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('should correctly add two numbers and round the result', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  
  it('should correctly subtract two numbers and round the result', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  
  it('should correctly divide two numbers and round the result', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });

  it('should return "Error" if dividing by zero', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
