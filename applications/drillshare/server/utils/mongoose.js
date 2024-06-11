import { connect } from "mongoose";
const dotenv = require('dotenv');
dotenv.config();

const connectionString = `mongodb+srv://${process.env.DB_USERNAME}:${process.env.DB_PASSWORD}@drillshare.pmlbx.mongodb.net/`;

(async () => {
    try {
        const db = await connect(connectionString);
        console.log("DB connected to", db.connection.name);
    } catch (error) {
        console.log(process.env.DB_USERNAME)
        console.error(error);
    }
})();