const database = require('../db')


class RespiracaoRepository{
    get_all_respiracao(){
        const sql = `SELECT * FROM respiracao`
        
        database.all(sql,[],(err,rows)=>{
            if(err){
                console.log(err)
            }

            rows.forEach(row=>{
                return row;
            })
        })
    }
}


module.exports = RespiracaoRepository;

// const resp = new RespiracaoRepository();

// console.log(resp.get_all_respiracao());