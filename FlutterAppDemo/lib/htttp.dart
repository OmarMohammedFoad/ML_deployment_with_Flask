import 'dart:async';



import 'dart:convert';


import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';

class Test1 extends StatefulWidget {

  @override
  State<Test1> createState() => _TestState();
}

class _TestState extends State<Test1> {

 String?body = "";
  // Future getpost() async  
  // {
  // //  var url = Uri.http('192.168.1.121:3000', "/admin/user");
  //   // print(url);
  //     var response = await http.get(Uri.parse("http://10.0.2.2:5000/result"));
  //     print(response);
      
  //   var response_body = await response.body;
  //   print(response_body);
  // }
  File? _file; 
  Future UploadImage () async 
  {
    final myfile = await  ImagePicker().pickImage(source: ImageSource.gallery);
    setState(() {
      _file = File(myfile!.path);
    }); 


  }










  Future  Predict () async 
  {
   
    
    if(_file == null) return "";

    String base64 =  base64Encode(_file!.readAsBytesSync());

  

    Map<String, String> requestHeaders ={'Content-type': 'application/json',
    'Accept': 'application/json',}; 
    var  response = await http.put(Uri.parse("http://10.0.2.2:5000/api"),body: base64,headers:requestHeaders );
   
        print(response.body);
     setState(() {
       body = response.body;
     });

    }


     
    



  
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:const Text('Flutter Demo'),
    ),
  body:
        SingleChildScrollView(
          child: Center(
            child: Padding(
              padding: const EdgeInsets.all(25.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
              _file == null ? Text("Image not found") :Image.file(_file!),
        
                  Text(body!),
                Row(
                mainAxisAlignment: MainAxisAlignment.center,
                  children:[
                
                    TextButton(onPressed:() =>UploadImage(), child:Text("Upload ")),
                TextButton(onPressed:() =>Predict(), child:Text(" Predict"))
                ])]),
            ),
          ),
        )  
   ,
   );

  }
}