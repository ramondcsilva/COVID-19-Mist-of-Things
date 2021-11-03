const database = require('../db')

class CardiacaRepository{
    get_all_cardiaca(){
        const sql = `SELECT * FROM cardiaca`
        
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

module.exports=CardiacaRepository;

// const card = new CardiacaRepository;

// console.log(card.get_all_cardiaca())