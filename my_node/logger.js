const EventEmitter = require('events');
const emitter = new EventEmitter();
const url = 'http://mylogger.io/log';

function log(message) {
  console.log(message);
  emitter.emit('startme', { id: 1, url: 'http://' });
}

module.exports = log;
