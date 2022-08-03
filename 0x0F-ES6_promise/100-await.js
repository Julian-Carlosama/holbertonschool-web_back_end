import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  let pht;
  let user;

  try {
    pht = await uploadPhoto();
    user = await createUser();
  }
  catch (e) {
    pht = null;
    user = null;
  }

  const newUser = {
    pht,
    user,
  };

  return newUser;
}
