const express = require('express');
const cookieParser = require('cookie-parser');
const PORT = require('./config/PORT');
const { setCookie, getCookie } = require('./helpers/cookieHelpers');
const { setHeader, getHeader } = require('./helpers/headerHelpers');

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


app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
