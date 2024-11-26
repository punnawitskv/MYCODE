const express = require('express');

const { messageController } = require('../../controllers');

const router = express.Router();

router.route('/').post(messageController.createMessage).get(messageController.getMessages);
router.route('/:messageId').delete(messageController.deleteMessage);

module.exports = router;
