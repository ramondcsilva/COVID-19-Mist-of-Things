const database = require("../db");

class ArterialRepository {
  get_all_arterial() {
    const sql = `SELECT * from arterial`;

    database.all(sql, [], (err, rows) => {
      if (err) {
        console.log(err);
      }
      rows.forEach((row) => {
        return row; //  Retornar
      });
    });

    database.close();
  }
}

module.exports = ArterialRepository;

// const art = new ArterialRepository();

// console.log(art.get_all_arterial());
