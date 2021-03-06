const database = require("./db");
const express = require("express");
const { response } = require("express");
const app = express();

app.use(express.json());

/**
 * Regra de Negócio -
 */
const PacienteService = () => {
  const sql = `SELECT ficha.id, ficha.nome,ficha.estado,ficha.pontuacao, temperatura.valor_temperatura,
    saturacao.valor_saturacao,cardiaca.valor_cardiaca,respiracao.valor_respiracao, 
    arterial.valor_arterial from ficha, temperatura,saturacao,cardiaca,respiracao,arterial WHERE ficha.id=temperatura.id and ficha.id=saturacao.id
    and ficha.id = cardiaca.id and ficha.id = respiracao.id and ficha.id=arterial.id
    `;
  return new Promise((resolve, reject) => {
    database.all(sql, [], (err, rows) => {
      let temperatura = [];

      if (err) {
        console.log(err);
      }
      resolve(rows);
    });
    // database.close();
  });
};

app.get("/paciente", (req, res) => {
  let p;
  PacienteService().then(pa =>{
    return res.json(pa)
  })
});

app.listen(3004, () => {
  console.log("Runnig Server at http://localhost:3004");
});

