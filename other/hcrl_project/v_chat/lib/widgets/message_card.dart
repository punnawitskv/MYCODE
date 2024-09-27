import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:v_chat/api/apis.dart';
import 'package:v_chat/helper/my_date_util.dart';
import 'package:v_chat/main.dart';
import 'package:v_chat/models/message.dart';

class MessageCard extends StatefulWidget {
  const MessageCard({super.key, required this.message});

  final Message message;

  @override
  State<MessageCard> createState() => _MessageCardState();
}

class _MessageCardState extends State<MessageCard> {
  @override
  Widget build(BuildContext context) {
    bool isMe = APIs.user.uid == widget.message.fromId;

    return InkWell(
      onLongPress: () {
        _showBottomSheet(isMe);
      },
      child: isMe ? _rightMessage() : _leftMessage(),
    );
  }

  // sender or another user message
  Widget _leftMessage() {
    if (widget.message.read.isEmpty) {
      APIs.updateMessageReadStatus(widget.message);
    }

    return Row(
      // make message and date between
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Flexible(
          child: Container(
            padding: EdgeInsets.all(widget.message.type == Type.image
                ? mq.width * .03
                : mq.width * .04),
            margin: EdgeInsets.symmetric(
                horizontal: mq.width * .04, vertical: mq.height * .01),
            decoration: BoxDecoration(
                color: Colors.teal.shade100,
                border: Border.all(color: Colors.teal),

                // borders curved const!!!!!!
                borderRadius: const BorderRadius.only(
                    topLeft: Radius.circular(30),
                    topRight: Radius.circular(30),
                    bottomRight: Radius.circular(30))),
            child: widget.message.type == Type.text
                ?
                // show text
                Text(
                    widget.message.msg,
                    style: const TextStyle(fontSize: 15, color: Colors.black),
                  )

                // show img
                : ClipRRect(
                    borderRadius: const BorderRadius.all(Radius.circular(15)),
                    child: CachedNetworkImage(
                      imageUrl: widget.message.msg,
                      fit: BoxFit.cover,
                      placeholder: (context, url) => const Padding(
                        padding: EdgeInsets.all(8.0),
                        child: Padding(
                          padding: EdgeInsets.all(8.0),
                          child: CircularProgressIndicator(strokeWidth: 2),
                        ),
                      ),
                      errorWidget: (context, url, error) =>
                          const Icon(Icons.image, size: 70),
                    ),
                  ),
          ),
        ),

        // msg time
        Padding(
          padding: EdgeInsets.only(right: mq.width * .04),
          child: Text(
            MyDateUtil.getFormattedTime(
                context: context, time: widget.message.sent),
            style: const TextStyle(fontSize: 13, color: Colors.black54),
          ),
        ),
      ],
    );
  }

  // our or user message
  Widget _rightMessage() {
    return Row(
      // make message and date between
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Row(
          children: [
            SizedBox(width: mq.width * .04),

            if (widget.message.read.isNotEmpty)
              const Icon(Icons.done_all_rounded, color: Colors.teal, size: 20),

            const SizedBox(width: 2),

            // sent time
            Text(
              MyDateUtil.getFormattedTime(
                  context: context, time: widget.message.sent),
              style: const TextStyle(fontSize: 13, color: Colors.black54),
            ),
          ],
        ),

        // msg content
        Flexible(
          child: Container(
            padding: EdgeInsets.all(widget.message.type == Type.image
                ? mq.width * .03
                : mq.width * .04),
            margin: EdgeInsets.symmetric(
                horizontal: mq.width * .04, vertical: mq.height * .01),
            decoration: BoxDecoration(
                color: Colors.white,
                border: Border.all(color: Colors.teal),

                // borders curved const!!!!!!
                borderRadius: const BorderRadius.only(
                    topLeft: Radius.circular(30),
                    topRight: Radius.circular(30),
                    bottomLeft: Radius.circular(30))),
            child: widget.message.type == Type.text
                ?
                // show text
                Text(
                    widget.message.msg,
                    style: const TextStyle(fontSize: 15, color: Colors.black),
                  )

                // show img
                : ClipRRect(
                    borderRadius: const BorderRadius.all(Radius.circular(15)),
                    child: CachedNetworkImage(
                      imageUrl: widget.message.msg,
                      placeholder: (context, url) => const Padding(
                        padding: EdgeInsets.all(8.0),
                        child: Padding(
                          padding: EdgeInsets.all(8.0),
                          child: CircularProgressIndicator(strokeWidth: 2),
                        ),
                      ),
                      errorWidget: (context, url, error) =>
                          const Icon(Icons.image, size: 70),
                    ),
                  ),
          ),
        ),
      ],
    );
  }

  void _showBottomSheet(bool isMe) {
    showModalBottomSheet(
        context: context,
        backgroundColor: Colors.white,
        shape: const RoundedRectangleBorder(
            borderRadius: BorderRadius.only(
                topLeft: Radius.circular(20), topRight: Radius.circular(20))),
        builder: (_) {
          return ListView(
            shrinkWrap: true,
            children: [
              Container(
                height: 4,
                margin: EdgeInsets.symmetric(
                    vertical: mq.height * .015, horizontal: mq.width * .4),
                decoration: BoxDecoration(
                    color: Colors.teal, borderRadius: BorderRadius.circular(8)),
              ),

              widget.message.type == Type.text
                  ?
                  // copy
                  _OptionItem(
                      icon: const Icon(
                        Icons.copy_all_rounded,
                        color: Colors.teal,
                        size: 26,
                      ),
                      name: 'Copy Text',
                      onTap: () {},
                    )
                  :
                  // save img
                  _OptionItem(
                      icon: const Icon(
                        Icons.download,
                        color: Colors.teal,
                        size: 26,
                      ),
                      name: 'Save Image',
                      onTap: () {},
                    ),

              if (isMe)
                Divider(
                  endIndent: mq.width * .04,
                  indent: mq.width * .04,
                ),

              // edit
              if (widget.message.type == Type.text && isMe)
                _OptionItem(
                  icon: const Icon(
                    Icons.edit,
                    color: Colors.teal,
                    size: 26,
                  ),
                  name: 'Edit Message',
                  onTap: () {},
                ),

              // del msg
              if (isMe)
                widget.message.type == Type.text
                    ? _OptionItem(
                        icon: const Icon(
                          Icons.delete_forever,
                          color: Colors.teal,
                          size: 26,
                        ),
                        name: 'Delete Message',
                        onTap: () {},
                      )
                    : _OptionItem(
                        icon: const Icon(
                          Icons.delete_forever,
                          color: Colors.teal,
                          size: 26,
                        ),
                        name: 'Delete Image',
                        onTap: () {},
                      ),

              Divider(
                endIndent: mq.width * .04,
                indent: mq.width * .04,
              ),

              // sent time
              _OptionItem(
                icon: const Icon(
                  Icons.send,
                  color: Colors.teal,
                  size: 26,
                ),
                name: 'Sent At: ',
                onTap: () {},
              ),

              // read time
              _OptionItem(
                icon: const Icon(
                  Icons.remove_red_eye,
                  color: Colors.teal,
                  size: 26,
                ),
                name: 'Read At: ',
                onTap: () {},
              ),
            ],
          );
        });
  }
}

class _OptionItem extends StatelessWidget {
  final Icon icon;
  final String name;
  final VoidCallback onTap;

  const _OptionItem(
      {required this.icon, required this.name, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () => onTap,
      child: Padding(
        padding: EdgeInsets.only(
            left: mq.width * .05,
            top: mq.height * .015,
            bottom: mq.height * .015),
        child: Row(
          children: [
            icon,
            Flexible(
                child: Text(
              '   $name',
              style: const TextStyle(
                  fontSize: 15, color: Colors.black, letterSpacing: 0.5),
            ))
          ],
        ),
      ),
    );
  }
}
