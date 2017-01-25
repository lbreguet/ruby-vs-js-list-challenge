// Requirements

function any(array, predicate) {
  return array.some(predicate);
}

function none(array, predicate) {
  return !array.some(predicate);
}

// Bonuses

function one(array, predicate) {
  return array.filter(predicate).length === 1;
}

function all(array, predicate) {
  return array.every(predicate);
}

// Do not change this.
module.exports = { all, any, none, one };
