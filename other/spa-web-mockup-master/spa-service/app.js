const express = require('express');
const cors = require('cors');
const httpStatus = require('http-status');

const { errorConverter, errorHandler } = require('./middlewares/error');
const routes = require('./routes/v1');
const ApiError = require('./utils/ApiError');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors({ origin: '*' }));

app.use('/v1', routes);
app.use((req, res, next) => {
    next(new ApiError(httpStatus.NOT_FOUND, 'Not found'));
});

app.use(errorConverter);
app.use(errorHandler);

module.exports = app;
