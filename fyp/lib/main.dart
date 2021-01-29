import 'package:flutter/material.dart';
import 'package:fyp/Dashboard/Navigation_Bar/Profile.dart';

import 'Dashboard/Home_Page.dart';
import 'Dashboard/Navigation_Bar/Add_Vehicle.dart';
import 'Initial_Pages/sign_in.dart';
import 'Initial_Pages/sign_up.dart';
import 'Initial_Pages/start_up_page.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MaterialApp(
    initialRoute: '/start',
    routes: {
      '/start': (context) => Start_Up_Page(),
      '/home': (context) => Home(),
      '/signin': (context) => SignIn(),
      '/signup': (context) => SignUp(),
      '/profile': (context) => Profile(),
      '/vehicle': (context) => AddVehicle(),
    },
  ));
}
