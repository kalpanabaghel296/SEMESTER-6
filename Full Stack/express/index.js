const express = require('express');
const server = express();
const fs = require('fs');
server.use(express.json());

const user =[{
    "name":"abec",
    "roll":"039"

},{
    "name":"kalpana",
    "roll":"0339",

}]

const home = fs.readFileSync("home.html",'utf-8');
const contact = fs.readFileSync("contact.html",'utf-8');
const about = fs.readFileSync("about.html",'utf-8');
server.get('/',(req,res)=>{
    res.json(user);
})

server.get('/about',(req,res)=>{
    res.send(about);
})
server.post('/home',(req,res)=>{
    console.log(req.body);
    user.push(req.body);
    console.log(user);
    res.send("post configured");
})
server.put('/home',(req,res)=>{
    res.send("put cmd done");
})

server.patch('/home',(req,res)=>{
    res.send("fetch cmd done");
})
server.get('/home',(req,res)=>{
    res.send(home);
})
server.get('/contact',(req,res)=>{
    res.send(contact);
})

server.get('/home/about/contact',(req,res)=>{
    res.send(contact);
})

server.get('/home/about/',(req,res)=>{
    res.send(about);
})
//console.log(user);
user.forEach((i)=>{
    console.log(i);
})
server.listen(5000,()=>{
    console.log("server running at 5000 port");
})