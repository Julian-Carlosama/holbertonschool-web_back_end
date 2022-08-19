const assert = require('assert');
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', function() {
  it('Round the result of a + b numbers', function() {
    assert.equal(calculateNumber(3.9, 5.6), 10);
  });
  it('Show the result of a + b negative numbers', function() {
    assert.equal(calculateNumber(-7, 3), -4);
  });
  it('Show the result of a + b negative numbers', function() {
    assert.equal(calculateNumber(-7, -3), -10);
  });
  it('Show the result of a + b numbers, when the b is decimal', function() {
    assert.equal(calculateNumber(5, 0.0), 5);
  });
  it('Without arguments', function() {
    //assert(isNaN(calculateNumber(0),), 'no have a number');
    //assert(isNaN(calculateNumber(0,)));
    //assert(isNaN(calculateNumber()));
  });
  it('Processing with number zero', function() {
    assert.equal(calculateNumber(0, 0), 0);
    assert.equal(calculateNumber(0.0, 0), 0);
  });
  it('Tetsting for two integers numbers', function() {
    assert.equal(calculateNumber(0, 0), 0);
    assert.equal(calculateNumber(0.0, 0), 0);
  });
  it('Testing throw error', function () {
    assert.throws(() => calculateNumber(NaN, 5), 'The argument not is a number');
  });
});
