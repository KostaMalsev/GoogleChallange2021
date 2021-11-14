function nonDivisibleSubset(k, s) {

  let res = getClean(s,k);

  console.log(res.length,res);
  return res.length
}


function getClean(s,k)
{
  let res1 = [];
  let res2 = [];

  pair = checkPair(s,k)

  if(pair.length == 0){
    //a valid group
    return s;
  }else{
    
    let s1 = s.splice();
    let s2 = s.splice();
    removeEl(s1,pair[0]);
    removeEl(s2,pair[1]);

    res1 = getClean(s1,k);
    res2 = getClean(s2,k);
    if(res1.length >= res2.length) return res1;
    else return res2;

}

function removeEl(s,el)
{
  const index = s.indexOf(el);
  if (index > -1) {
    s.splice(index, 1);
  }
  return s;
}

function checkPair(s,k)
{
  n = s.length;

  for(let i=0; i < n; i++)
  {
    for(let ii=i; ii < n ; ii++)
    {
      if( (s[i] + s[ii]) % k == 0) {
        return [ s[i],s[ii] ];
      }
    }
  }
  return []
}

