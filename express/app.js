const express = require('express');
const cookieParser = require('cookie-parser');
const PORT = require('./config/PORT');
const { setCookie, getCookie } = require('./helpers/cookieHelpers');
const { setHeader, getHeader } = require('./helpers/headerHelpers');
const mongoose = require('./config/mongoConnection');
const User = require('./models/users');

mongoose.connectDB(); 
const app = express();
app.use(cookieParser());
app.use(express.json());


app.get('/cookie/set', (req, res) => {
  const { name, value } = req.query;
  setCookie(res, name, value, true);
  res.json({ message: `Cookie set: ${name} = ${value}` });
});

app.get('/cookie/get/:name', (req, res) => {
  const name = req.params.name;
  const value = getCookie(req, name);
  res.json({ [name]: value });
});


app.get('/header/set', (req, res) => {
  const { name, value } = req.query;
  console.log(`Setting header: name=${name}, value=${value}`); 
  if (!name || !value) {
    return res.status(400).json({ error: "Missing name or value" });
  }
  setHeader(res, name, value);
  res.json({ message: `Header set: ${name} = ${value}` });
});


app.get('/header/get/:name', (req, res) => {
  const name = req.params.name;
  const value = getHeader(req, name);
  res.json({ [name]: value });
});

app.get('/users', async (req, res) => {
  try {
    const users = await User.find();
    //res.send(users);
    res.send('Hello dis is da express endpoint open up')
  } catch (error) {
    res.status(500).send(error);
  }
});


app.post('/users', async (req, res) => {
  try {
    const user = new User({
      username: req.body.username,
      email: req.body.email,
      first_name: req.body.first_name,
      last_name: req.body.last_name,
      is_admin: req.body.is_admin,
      profession: req.body.profession,
    });
    await user.save();
    res.status(201).send(user);
  } catch (error) {
    res.status(400).send(error);
  }
});

app.put('/users/:id', async (req, res) => {
  try {
    const user = await User.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
    if (!user) {
      return res.status(404).send();
    }
    res.send(user);
  } catch (error) {
    res.status(400).send(error);
  }
});

app.delete('/users/:id', async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);
    if (!user) {
      return res.status(404).send();
    }
    res.send(user);
  } catch (error) {
    res.status(500).send(error);
  }
});





app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
