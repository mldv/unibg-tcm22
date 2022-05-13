import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import './globals.dart';

Future<List<String>> fetchClasses(String raceid) async {
  final response = await http.get(Uri.parse('$apiUrl/list_classes?id=$raceid'));

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return List<String>.from(jsonDecode(response.body));
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load classes');
  }
}

class ClassesRoute extends StatefulWidget {
  final String raceid;
  const ClassesRoute(this.raceid, {Key? key}) : super(key: key);

  @override
  _ClassesRouteState createState() => _ClassesRouteState();
}

class _ClassesRouteState extends State<ClassesRoute> {
  late Future<List<String>> futureClasses;

  @override
  void initState() {
    super.initState();
    futureClasses = fetchClasses(widget.raceid);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Classes'),
      ),
      body: Center(
        child: FutureBuilder<List<String>>(
          future: futureClasses,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              List<String> classes = snapshot.data!;
              return ListView.builder(
                  itemCount: classes.length,
                  itemBuilder: ((context, index) => Text(classes[index])));
            } else if (snapshot.hasError) {
              return Text('${snapshot.error}');
            }

            // By default, show a loading spinner.
            return const CircularProgressIndicator();
          },
        ),
      ),
    );
  }
}
