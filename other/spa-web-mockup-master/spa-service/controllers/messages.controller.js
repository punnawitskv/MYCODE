const httpStatus = require('http-status');

const { messageService } = require('../services');
const catchAsync = require('../utils/catchAsync');

const createMessage = catchAsync(async (req, res) => {
    const message = await messageService.createMessage({ ...req.body, text: req.body.text });
    res.status(httpStatus.CREATED).send(message);
});

const getMessages = catchAsync(async (req, res) => {
    const messages = await messageService.getMessages();
    res.send(messages);
});

const deleteMessage = catchAsync(async (req, res) => {
    await messageService.deleteMessageById(req.params.messageId);
    res.status(httpStatus.NO_CONTENT).send();
});

module.exports = {
    createMessage,
    getMessages,
    deleteMessage,
};
