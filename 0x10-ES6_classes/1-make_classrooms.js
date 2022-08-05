import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const sizee = [19, 20, 34];
  const array = [];

  for (const size of sizee) {
    array.push(new ClassRoom(size));
  }
  return array;
}
