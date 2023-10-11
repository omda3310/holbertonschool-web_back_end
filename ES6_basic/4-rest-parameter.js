export default function returnHowManyArguments(...args) {
  let numbers = 0;
  for (let arg of args) numbers += 1;
  return numbers;
}
