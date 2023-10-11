export default function returnHowManyArguments(...args) {
   let n_args = 0;
   for(let arg in args) n_args += 1;
   return n_args;
}
