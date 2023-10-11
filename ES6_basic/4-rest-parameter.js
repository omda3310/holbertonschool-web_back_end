export default function returnHowManyArguments(...args) {
  let numbers = 0;
  for(let arg in args) numbers += 1;
  return numbers;
}
