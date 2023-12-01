import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  let ms = '';
  return Promise.all([
    uploadPhoto(),
    createUser(),
  ]).then((data) => {
    ms += `${data[0].body} ${data[1].firstName} ${data[2].lastName}`;
    console.log(ms);
  }).catch(() => {
    console.log('body firstName lastName');
  });
}