const Sequelize = require("sequelize");
const sqlite3 = require("sqlite3");

let db = new sqlite3.Database(
  "../../dbPaciente.db",
  sqlite3.OPEN_READONLY,
  (err) => {
    if (err) {
      console.log(err.message);
    }
    console.log("Connected");
  }
);

module.exports = db;
