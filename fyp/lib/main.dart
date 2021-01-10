import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: Home()));

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
