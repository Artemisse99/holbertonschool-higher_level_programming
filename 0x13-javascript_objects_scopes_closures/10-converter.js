exports.converter = function (base) {
  function converterr (val) {
    return val.toString(base);
  }
  return converterr;
};
