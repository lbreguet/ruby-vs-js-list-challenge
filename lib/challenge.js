'use strict';
// Requirements

function any(list, block) {
  list = [];
  block = function () {
    for (let i = 0; i < list.length; i++) {
      if (list[i] !== undefined) {
        return true;
      } else {
        return false;
      }
    }
  };
}

function none(list, block) {
  list = [];
  block = function() {
    for (let i = 0; i < list.length; i++) {
      if (list[i] === undefined) {
        return true;
      } else {
        return false;
      }
    }
  };
}

// Bonuses

function one(/* Your function parameters here. */) {
  // Your function body here.
}

function all(/* Your function parameters here. */) {
  // Your function body here.
}

// Do not change this.
module.exports = { all, any, none, one };
