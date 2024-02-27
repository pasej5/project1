const EventEmitter = require('events');
const emitter = new EventEmitter();

emitter.on('startme', (arg) => {
  console.log('startme is called', arg);
});

const log = require('./logger');
log('message');
