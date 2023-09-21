const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/bienvenido/', (req, res) => {
  res.send('Hola!');
});

app.get('/alumno/', (req, res) => {
    res.send('Soy un alumno');
  });

app.listen(port, () => {
  console.log(`El servidor se encuentra corriendo en el puerto ${port}`);
});