require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const app = express();

const PORT = process.env.PORT;

try {
    mongoose.connect(process.env.MONGO_URI);
} catch (error) {
    process.exit(1);
}
const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    }
});
const UserModel = mongoose.model('User', UserSchema);

// custom middleware declaration
const log = (request, response, next) => {
    console.log(`path ${request.path} accessed by ${request.ip}`);
    next();
}

// use middleware
app.use(log);
app.use(express.json());

// routes
app.get('/', async(request, response) => {
    // response.send(users);
    // response.send('id: ' + request.query.id);
    // const userFilter = users.find((user) => user.id == request.query.id);
    // response.send(userFilter);
    let user = await UserModel.find();
    response.send(user);
});

app.get('/:id', async(request, response) => {
    // const userFilter = users.find((user) => user.id == request.params.id);
    // console.log(request.params.id);
    // console.log(userFilter);
    // response.send(userFilter);
    const user = await UserModel.findById(request.params.id);
    response.send(user);
});

app.post('/', async(request, response) => {
    // users.push(request.body.name);
    // response.send({
    //     "message" : "OK"
    // });
    let user = await new UserModel(request.body).save();
    response.send(user);
});

// running and start listening
app.listen(PORT, () => {
    console.log(`express is running on http://localhost:${PORT}`);
});
