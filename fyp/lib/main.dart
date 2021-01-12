import 'package:flutter/material.dart';

import 'Dashboard/Home_Page.dart';
import 'Initial_Pages/sign_in.dart';
import 'Initial_Pages/sign_up.dart';
import 'Initial_Pages/start_up_page.dart';

void main() => runApp(MaterialApp(
      initialRoute: '/start',
      routes: {
        '/start': (context) => Start_Up_Page(),
        '/home': (context) => Home(),
        '/signin': (context) => SignIn(),
        '/signup': (context) => SignUp(),
      },
    )
);

