export default function guardrail(mathFunction) {
  const queue = [];
  let valu = 0;
  try {
    valu = mathFunction();
  } catch (err) {
    valu = `${err.name}: ${err.message}`;
  }
  queue.push(valu);
  queue.push('Guardrail was processed');
  return queue;
}
