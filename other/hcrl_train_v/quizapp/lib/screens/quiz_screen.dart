import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:percent_indicator/circular_percent_indicator.dart';

class QuizScreen extends StatefulWidget {
  const QuizScreen({required this.quiz, super.key});

  final Map<String, dynamic> quiz;

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  int currentQuestion = 0;
  int score = 0;

  void nextQuestion(int answer) {
    setState(() {
      if (widget.quiz["problems"][currentQuestion]["answer"] == answer) {
        score++;
      }
      if (currentQuestion < widget.quiz["problems"].length - 1) {
        currentQuestion++;
      } else {
        showDialog(
            context: context,
            builder: (context) {
              return AlertDialog(
                title: Text(
                  "Quiz Finished !",
                  textAlign: TextAlign.center,
                  style: GoogleFonts.prompt(
                      fontSize: 20, fontWeight: FontWeight.bold),
                ),
                content: Text(
                  "Your Score is $score / ${widget.quiz["problems"].length}",
                  textAlign: TextAlign.center,
                  style: GoogleFonts.prompt(fontSize: 16),
                ),
                actions: [
                  TextButton(
                      onPressed: () {
                        Navigator.pop(context);
                        Navigator.pop(context);
                      },
                      child: Text(
                        "OK",
                        style: GoogleFonts.prompt(fontSize: 16),
                      )),
                  TextButton(
                      onPressed: () {
                        Navigator.pop(context);
                        setState(() {
                          currentQuestion = 0;
                          score = 0;
                        });
                      },
                      child: Text(
                        "Retry",
                        style: GoogleFonts.prompt(fontSize: 16),
                      ))
                ],
              );
            });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    List<Map<String, dynamic>> problems = widget.quiz["problems"];
    int totalQuestion = problems.length;
    return Scaffold(
      backgroundColor: Colors.indigo[900],
      appBar: AppBar(
        backgroundColor: Colors.lightBlue,
        centerTitle: true,
        title: Text(
          widget.quiz["quiz_name"],
          style: GoogleFonts.prompt(fontSize: 20, fontWeight: FontWeight.bold),
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircularPercentIndicator(
              radius: 50,
              lineWidth: 10,
              progressColor: Colors.lightBlue,
              percent: currentQuestion / totalQuestion,
              center: Text(
                "${(currentQuestion / totalQuestion * 100).toStringAsFixed(2)}%",
                style: GoogleFonts.prompt(color: Colors.white),
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            Text(
              "Questions ${currentQuestion + 1}/${totalQuestion}",
              style: GoogleFonts.prompt(
                  color: Colors.white,
                  fontSize: 16,
                  fontWeight: FontWeight.bold),
            ),
            const SizedBox(
              height: 10,
            ),
            Text(
              problems[currentQuestion]["question"],
              style: GoogleFonts.prompt(
                  color: Colors.white,
                  fontSize: 16,
                  fontWeight: FontWeight.bold),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                TextButton(
                    onPressed: () => nextQuestion(1),
                    style: ButtonStyle(
                        foregroundColor: WidgetStateProperty.all(Colors.black),
                        textStyle: WidgetStateProperty.all(GoogleFonts.prompt(
                            fontSize: 12, color: Colors.black)),
                        backgroundColor: WidgetStateProperty.all(Colors.white)),
                    child: Text(problems[currentQuestion]["options"][0])),
                const SizedBox(
                  width: 10,
                ),
                TextButton(
                    onPressed: () => nextQuestion(2),
                    style: ButtonStyle(
                        foregroundColor: WidgetStateProperty.all(Colors.black),
                        textStyle: WidgetStateProperty.all(GoogleFonts.prompt(
                            fontSize: 12, color: Colors.black)),
                        backgroundColor: WidgetStateProperty.all(Colors.white)),
                    child: Text(problems[currentQuestion]["options"][1])),
              ],
            ),
            const SizedBox(
              height: 10,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                TextButton(
                    onPressed: () => nextQuestion(3),
                    style: ButtonStyle(
                        foregroundColor: WidgetStateProperty.all(Colors.black),
                        textStyle: WidgetStateProperty.all(GoogleFonts.prompt(
                            fontSize: 12, color: Colors.black)),
                        backgroundColor: WidgetStateProperty.all(Colors.white)),
                    child: Text(problems[currentQuestion]["options"][2])),
                const SizedBox(
                  width: 10,
                ),
                TextButton(
                    onPressed: () => nextQuestion(4),
                    style: ButtonStyle(
                        foregroundColor: WidgetStateProperty.all(Colors.black),
                        textStyle: WidgetStateProperty.all(GoogleFonts.prompt(
                            fontSize: 12, color: Colors.black)),
                        backgroundColor: WidgetStateProperty.all(Colors.white)),
                    child: Text(problems[currentQuestion]["options"][3])),
              ],
            )
          ],
        ),
      ),
    );
  }
}
