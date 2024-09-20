import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:hcrl_flutter_training_2024/screens/quiz_screen.dart';

Widget quizCard(Map<String, dynamic> quiz, BuildContext context) {
  return GestureDetector(
    onTap: () {
      Navigator.push(context, MaterialPageRoute(builder: (context) {
        return QuizScreen(quiz: quiz);
      }));
    },
    child: Container(
      height: 65,
      decoration: BoxDecoration(
        color: Colors.grey[300],
        borderRadius: BorderRadius.circular(10),
      ),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Text(
                  quiz['quiz_name'],
                  style: GoogleFonts.prompt(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                    color: Colors.black,
                  ),
                ),
                const Spacer(),
                const Icon(
                  Icons.arrow_forward_ios,
                  color: Colors.black,
                ),
              ],
            ),
            Text(
              quiz['quiz_description'],
              style: GoogleFonts.prompt(
                fontSize: 12,
                color: Colors.grey[600],
              ),
            ),
          ],
        ),
      ),
    ),
  );
}
