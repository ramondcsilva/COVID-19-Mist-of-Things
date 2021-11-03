// const Fi = require('../model/Ficha')
const database = require("../db");
let array=[]
/**
 * Manipula os dados do BD
 */
class FichaRepository {
  /**
   * Pega todos os Pacientes
   */
  get_all() {
    const sql = `SELECT * from ficha`;
    let paci=[];
    database.all(sql, [], (err, rows) => {
      if (err) {
        console.log(err);
      }
      paci = rows;
      // rows.forEach((row) => {
      //   array.push(row)
      //   // console.log(row)
      // });
      return paci
    });
    
    // database.close();
  }
}

module.exports = FichaRepository;

// const ficha = new FichaRepository();

// ficha.get_all();
