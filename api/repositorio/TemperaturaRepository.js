const database = require("../db");

class TemperaturaRepository {
  get_all_temp() {
    const sql = `SELECT * from temperatura`;

    database.all(sql, [], (err, rows) => {
      if (err) {
        console.log(err);
      }
      rows.forEach((row) => {
        console.log(row);
      });
    });

    database.close();
  }
}

module.exports = TemperaturaRepository;

// const temp = new TemperaturaRepository();

// temp.get_all_temp()
