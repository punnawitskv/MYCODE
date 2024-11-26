const express = require('express');

const messagesRoute = require('./messages.route');

const router = express.Router();

const defaultRoutes = [
    {
        path: '/messages',
        route: messagesRoute,
    },
];

defaultRoutes.forEach((route) => {
    router.use(route.path, route.route);
});

module.exports = router;
