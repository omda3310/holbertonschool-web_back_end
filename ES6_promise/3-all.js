import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  let msg = '';
  return Promise.all([
    uploadPhoto(),
    createUser(),
  ]).then((data) => {
    msg += `${data[0].body} ${data[1].firstName} ${data[2].lastName}`;
    console.log(ms);
  }).catch(() => {
    console.log('Signup system offline');
  });
}
