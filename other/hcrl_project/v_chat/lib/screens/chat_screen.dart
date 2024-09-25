import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:v_chat/main.dart';
import 'package:v_chat/models/chat_user.dart';

class ChatScreen extends StatefulWidget {
  final ChatUser user;

  const ChatScreen({super.key, required this.user});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          automaticallyImplyLeading: false,
          flexibleSpace: _appBar(),
        ),
        body: Column(
          children: [_chatInput()],
        ),
      ),
    );
  }

  // app bar widget
  Widget _appBar() {
    return InkWell(
      onTap: () {},
      child: Row(
        children: [
          // back btn
          IconButton(
              onPressed: () => Navigator.pop(context),
              icon: const Icon(
                Icons.arrow_back,
                color: Colors.white,
              )),

          // some space
          const SizedBox(height: 100),

          // user profile
          ClipRRect(
            borderRadius: BorderRadius.circular(mq.height * .3),
            child: CachedNetworkImage(
              width: mq.height * .05,
              height: mq.height * .05,
              imageUrl: widget.user.image,
              errorWidget: (context, url, error) =>
                  const CircleAvatar(child: Icon(CupertinoIcons.person)),
            ),
          ),

          // some space
          const SizedBox(width: 10),

          // username
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                widget.user.name,
                style: const TextStyle(
                  fontSize: 16,
                  color: Colors.white,
                  fontWeight: FontWeight.w900,
                ),
              ),

              // some space
              const SizedBox(height: 2),

              // last seen
              const Text(
                'Last seen not available',
                style: TextStyle(
                    fontSize: 13,
                    color: Colors.white,
                    fontWeight: FontWeight.w600),
              )
            ],
          )
        ],
      ),
    );
  }

  // bottom chat input field
  Widget _chatInput() {
    return Padding(
      padding: EdgeInsets.symmetric(
          vertical: mq.height * .01, horizontal: mq.width * .025),
      child: Row(
        children: [
          Expanded(
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15)),
              child: Row(
                children: [
                  // emo btn
                  IconButton(
                      onPressed: () {},
                      icon: const Icon(
                        Icons.emoji_emotions,
                        color: Colors.teal,
                        size: 25,
                      )),

                  Expanded(
                      child: TextField(
                    keyboardType: TextInputType.multiline,
                    maxLines: null,
                    decoration: InputDecoration(
                        hintText: 'type something...',
                        hintStyle: TextStyle(color: Colors.teal[200]),
                        border: InputBorder.none),
                  )),

                  // pick img btn
                  IconButton(
                    onPressed: () {},
                    icon: const Icon(
                      Icons.image,
                      color: Colors.teal,
                      size: 26,
                    ),
                  ),

                  // take img cameera btn
                  IconButton(
                    onPressed: () {},
                    icon: const Icon(
                      Icons.camera_alt,
                      color: Colors.teal,
                      size: 26,
                    ),
                  ),

                  SizedBox(width: mq.width * .02),
                ],
              ),
            ),
          ),

          // send msg btn
          MaterialButton(
            onPressed: () {},
            minWidth: 0,
            padding:
                const EdgeInsets.only(top: 10, bottom: 10, right: 10, left: 10),
            shape: const CircleBorder(),
            color: Colors.teal,
            child: const Icon(
              Icons.send,
              color: Colors.white,
              size: 28,
            ),
          )
        ],
      ),
    );
  }
}
