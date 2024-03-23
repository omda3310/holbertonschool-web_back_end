import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const singUser = await signUpUser(firstName, lastName).then((data) => ({
    status: 'fulfilled',
    value: data,
  }));

  const upPhoto = await uploadPhoto(fileName).catch((error) => ({
    status: 'rejected',
    value: error.toString(),
  }));

  return [singUser, upPhoto];
}
