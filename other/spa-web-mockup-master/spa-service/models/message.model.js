const mongoose = require('mongoose');

const { toJSON } = require('./plugins');

const messageSchema = new mongoose.Schema({
    text: {
        type: String,
    },
});

messageSchema.plugin(toJSON);

const Message = mongoose.model('Message', messageSchema);

module.exports = Message;
