const mongoose = require('mongoose');


const connectDB = async () => {
  try {
    await mongoose.connect('mongodb+srv://dbzenko:pppp@cluster0.ntu0tgk.mongodb.net/?retryWrites=true&w=majority', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB connected.');
  } catch (err) {
    console.error('Connection to MongoDB failed', err.message);
  }
};

module.exports = { connectDB };