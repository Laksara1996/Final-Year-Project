import 'package:flutter/material.dart';
import 'package:fyp/Initial_Pages/sign_in.dart';
import 'package:fyp/Initial_Pages/sign_up.dart';

import 'Initial_Pages/start_up_page.dart';

void main() => runApp(MaterialApp(
      initialRoute: '/start',
      routes: {
        '/start': (context) => Start_Up_Page(),
        '/test': (context) => Home(),
        '/signin': (context) => SignIn(),
        '/signup': (context) => SignUp(),


      },
    ));

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('First APP'),
        centerTitle: true,
      ),
      body: Center(
        child: Icon(Icons.airport_shuttle),
      ),
    );
  }
}
