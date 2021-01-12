import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  final appTitle = 'Drawer Demo';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('FYP'),
        actions: [
          Icon(Icons.favorite),
          Padding(
            padding: EdgeInsets.symmetric(horizontal: 16),
            child: Icon(Icons.search),
          ),
          Icon(Icons.more_vert),
        ],
        backgroundColor: Colors.grey,
      ),
      body: Center(child: Text('My Page!')),
      drawer: Drawer(
        child: ListView(
          // Important: Remove any padding from the ListView.
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  Text('Drawer Header'),
                  // Icon(Icons.menu)
                ],
              ),
              decoration: BoxDecoration(
                color: Colors.cyan,
              ),
            ),
            ListTile(
              dense: true,
              title: Row(
                children: [
                  Icon(Icons.home),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      'Home',
                      textScaleFactor: 1.2,
                    ),
                  ),
                ],
              ),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
              },
            ),
            ListTile(
              dense: true,
              title: Row(
                children: [
                  Icon(Icons.account_box),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      'Profile',
                      textScaleFactor: 1.2,
                    ),
                  ),
                ],
              ),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
              },
            ),
            ListTile(
              dense: true,
              title: Row(
                children: [
                  Icon(Icons.airport_shuttle),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      'Vehicles',
                      textScaleFactor: 1.2,
                    ),
                  ),
                ],
              ),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
              },
            ),
            ListTile(
              dense: true,
              title: Row(
                children: [
                  Icon(Icons.chat_outlined),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      'Summary',
                      textScaleFactor: 1.2,
                    ),
                  ),
                ],
              ),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: SizedBox(height:10),
            ),
            ListTile(
              dense: true,
              subtitle: Row(
                children: [
                  // Icon(Icons.chat_outlined),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      'About Us',
                      textScaleFactor: 1.3,
                    ),
                  ),
                ],
              ),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
              },
            ),
            ListTile(
              dense: true,
              subtitle: Row(
                children: [
                  // Icon(Icons.chat_outlined),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      'Log Out',
                      textScaleFactor: 1.3,
                    ),
                  ),
                ],
              ),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),
    );
  }
}
