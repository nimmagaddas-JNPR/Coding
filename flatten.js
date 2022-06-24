const flatten = (ary) => ary.reduce((result, b) => result.concat(Array.isArray(b) ? flatten(b) : b), [])

const a  = flatten([2,3,[3,6,6,6],[66,[7,8,[6]]],22])

function flattenObj(obj){
  let result = []
  for (const i in obj){
    if (!Array.isArray(obj[i]) && typeof(obj[i]) === 'object'){
      const tmp = flattenObj(obj[i])
      for (const j in tmp){
        result[i + '.' + j] = tmp[j]
      }
    }else{
      result[i] = obj[i]
    }
  }
  return result
}

let ob = {
    Company: "github",
    Address: "USA",
    contact: 1234567890,
    mentor: {
        HTML: "HTML",
        CSS: "CSS",
        JavaScript: "JS"
    }
};
const b = flattenObj(ob)
