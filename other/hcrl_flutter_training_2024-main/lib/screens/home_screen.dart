import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import '../repositories/mock_data.dart';
import '../widgets/quizcard.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.indigo[900],
        title: Text(
          'Quiz App',
          style: GoogleFonts.prompt(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(10),
        child: Center(
          child: Column(
            children: [
              Text("Quiz List",
                  style: GoogleFonts.prompt(
                      fontSize: 20, fontWeight: FontWeight.bold)),
              SizedBox(
                width: MediaQuery.of(context).size.width * 0.75,
                height: MediaQuery.of(context).size.height * 0.8,
                child: ListView.separated(
                    itemBuilder: (BuildContext context, int index) {
                      return quizCard(quizzes[index], context);
                    },
                    separatorBuilder: (BuildContext context, int index) {
                      return const SizedBox(height: 10);
                    },
                    itemCount: quizzes.length),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
