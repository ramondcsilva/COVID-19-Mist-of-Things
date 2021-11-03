const database = require('../db')


class SaturacaoRepository{

    get_all_saturacao(){
        const sql = `SELECT * FROM saturacao`;

        database.all(sql,[],(err,rows)=>{
            if(err){
                console.log(err);
            }

            rows.forEach((row)=>{
                console.log(row)
            })
        })
    }
}


module.exports = SaturacaoRepository;

// const sat = new SaturacaoRepository();

// sat.get_all_saturacao();