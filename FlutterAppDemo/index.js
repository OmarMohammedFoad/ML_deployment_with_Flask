const {spawn} = require('child_process');

const py = spawn('python', ['c:/Users/pc/OneDrive/Desktop/FLutter_Project/LOGOGON/xxxx/python_script.py', 'omar']);

py.stdin.on('data',(data)=>
{
try{
 console.log(data);   
}
catch(e)
{
    console.log("dsss");
}
}
);


py.stdin.on('data',(data)=>
{

}
);



py.on('close',(code)=>
{
    console.log(code)
})
