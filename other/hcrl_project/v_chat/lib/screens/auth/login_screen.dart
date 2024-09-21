import 'package:flutter/material.dart';
import 'package:v_chat/screens/home_screen.dart';

import '../../main.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  bool _isAnimate = false;

  @override
  void initState() {
    super.initState();
    Future.delayed(const Duration(microseconds: 500), () {
      setState(() {
        _isAnimate = true;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    mq = MediaQuery.of(context).size;

    return Scaffold(
        appBar: AppBar(
          automaticallyImplyLeading: false,
          title: const Text('Welcome to V Chat'),
        ),
        body: Stack(
          children: [
            AnimatedPositioned(
              top: mq.height * .15,
              // right: _isAnimate ? mq.width * .25 : -mq.width * .5,
              left: mq.width * .25,
              width: mq.width * .5,
              duration: const Duration(seconds: 1),
              child: Image.asset('images/icon.png'),
            ),
            Positioned(
              bottom: mq.height * .15,
              left: mq.width * .05,
              width: mq.width * .9,
              height: mq.height * .06,
              child: ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                    backgroundColor: const Color.fromARGB(255, 39, 157, 147),
                    shape: StadiumBorder(),
                    elevation: 1),
                onPressed: () {
                  Navigator.pushReplacement(context,
                      MaterialPageRoute(builder: (_) => const HomeScreen()));
                },
                icon: Image.asset(
                  'images/google.png',
                  height: mq.height * .04,
                ),
                label: RichText(
                  text: const TextSpan(
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                      ),
                      children: [
                        TextSpan(text: 'Login with '),
                        TextSpan(
                            text: 'Google',
                            style: TextStyle(fontWeight: FontWeight.w500))
                      ]),
                ),
              ),
            ),
          ],
        ));
  }
}
