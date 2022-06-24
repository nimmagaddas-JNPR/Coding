let inputList = [
  ["dog", "mammal"],
  ["shark", "fish"],
  ["cat", "mammal"],
  ["mammal", "animal"],
  ["fish", "animal"]
];

inputList.reduce((result, currentVal) => {
  const [child, parent] = currentVal;

  if (result[child]) {
    if (!result[parent]) {
      result[parent] = {};
    }
    result[parent][child] = { ...result[child] };
    delete result[child];
  } else {
    if (!result[parent]) {
      result[parent] = {};
    }

    result[parent][child] = {};
  }
  
  return result;
}, {});
