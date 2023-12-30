import  mongoose  from "mongoose";
import cors from "cors";
import express from "express";
const app = express();
import { Productx, Bid, User } from '/downloads/biddingappln/server/models/Item.js';
app.use(express.json());
app.use(cors());

mongoose.connect(
  "mongodb+srv://lielife24:lielife24@cluster0.iiianrk.mongodb.net/cllgd1?retryWrites=true&w=majority",
  {
    useNewUrlParser: true,
  }
);

app.get("/insertx", async (req, res) => {
  const u0 = new User({
    emailId: "pqrs@gmail.com",
  });
  const b0 = new Bid({
    uId: "pqrs@gmail.com",
    uAmnt: 0,
  });
  const p0 = new Productx({
    pId: 0,
    pImage: "pqrs",
    pName: "pqrs",
    predefDate: new Date("2023-12-31T12:00:00Z"),
    predefTime: "00:00:00",
    started: true,
    active: true,
    users: [],
    live: [],
  });
  try {
    await u0.save();
    await b0.save();
    await p0.save();
    res.send("inserted!!");
  } catch (err) {
    console.log(err);
  }
});

app.listen(8080, () => {
  console.log("server running on port 8080....");
});
