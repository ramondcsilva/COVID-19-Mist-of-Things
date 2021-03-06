const database = require("../db");
const express = require("express");
const cors = require("cors");
const { response } = require("express");
const app = express();

app.use(cors());
app.use(express.json());

/**
 * Regra de Negócio -
 */
const PacienteService = (id) => {
  const sql = id
    ? `SELECT ficha.id, ficha.nome,ficha.estado,ficha.pontuacao, temperatura.valortemperatura,
    saturacao.valorsaturacao,cardiaca.valorcardiaca,respiracao.valorrespiracao, 
    arterial.valorarterial from ficha, temperatura,saturacao,cardiaca,respiracao,arterial WHERE ficha.id=temperatura.id and ficha.id=saturacao.id
    and ficha.id = cardiaca.id and ficha.id = respiracao.id and ficha.id=arterial.id and ficha.id =?
    `
    : `SELECT ficha.id, ficha.nome,ficha.estado,ficha.pontuacao, temperatura.valortemperatura,
    saturacao.valorsaturacao,cardiaca.valorcardiaca,respiracao.valorrespiracao, 
    arterial.valorarterial from ficha, temperatura,saturacao,cardiaca,respiracao,arterial WHERE ficha.id=temperatura.id and ficha.id=saturacao.id
    and ficha.id = cardiaca.id and ficha.id = respiracao.id and ficha.id=arterial.id`;
  return new Promise((resolve, reject) => {
    database.all(sql, [id], (err, rows) => {

      if (err) {
        console.log(err);
      }
      resolve(rows);
    });
    // database.close();
  });
};

app.get("/paciente", (req, res) => {
  if (req.query.id) {
    PacienteService(req.query.id).then((pa) => {
      return res.json(pa);
    });
  } else {
    PacienteService().then((pa) => {
      return res.json(pa);
    });
  }
});

app.listen(3004, () => {
  console.log("Runnig Server at http://localhost:3004");
});
