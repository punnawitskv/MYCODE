import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:v_chat/main.dart';

class ChatUserCard extends StatefulWidget {
  const ChatUserCard({super.key});

  @override
  State<ChatUserCard> createState() => _ChatUserCardState();
}

class _ChatUserCardState extends State<ChatUserCard> {
  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    return Card(
      margin: EdgeInsets.symmetric(horizontal: mq.width * .04, vertical: 4),
      // color: Colors.teal.shade100,
      elevation: 0.5,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
      child: InkWell(
        onTap: () {},
        child: const ListTile(
          leading: CircleAvatar(
            child: Icon(CupertinoIcons.person),
          ),
          title: Text('Demo User'),
          subtitle: Text(
            'Last user message',
            maxLines: 1,
          ),
          trailing: Text(
            '12:00 PM',
            style: TextStyle(color: Colors.black54),
          ),
        ),
      ),
    );
  }
}
