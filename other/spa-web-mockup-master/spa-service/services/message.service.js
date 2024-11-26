const httpStatus = require('http-status');

const { Message } = require('../models');

const createMessage = async (messageBody) => {
    return Message.create(messageBody);
};

const getMessages = async () => {
    const messages = await Message.find();
    return messages;
};

const getMessageById = async (id) => {
    const message = await Message.findById(id);
    return message;
};

const deleteMessageById = async (id) => {
    const message = await getMessageById(id);
    if (!message) {
        throw new ApiError(httpStatus.NOT_FOUND, 'message not found');
    }
    await message.remove();
    return message;
};

module.exports = {
    createMessage,
    getMessages,
    getMessageById,
    deleteMessageById,
};
