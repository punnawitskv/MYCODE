import 'package:cloud_firestore/cloud_firestore.dart';

class ChatUser {
  ChatUser({
    required this.image,
    required this.about,
    required this.name,
    required this.id,
    required this.isOnline,
    required this.lastActive,
    required this.createAt,
    required this.email,
    required this.pushToken,
  });
  late String image;
  late String about;
  late String name;
  late String id;
  late bool isOnline;
  late String lastActive;
  late String createAt;
  late String email;
  late String pushToken;

  ChatUser.fromJson(Map<String, dynamic> json,
      [List<QueryDocumentSnapshot<Map<String, dynamic>>>? data]) {
    image = json['image'] ?? '';
    about = json['about'] ?? '';
    name = json['name'] ?? '';
    id = json['id'] ?? '';
    isOnline = json['is_online'] ?? '';
    lastActive = json['last_active'] ?? '';
    createAt = json['create_at'] ?? '';
    email = json['email'] ?? '';
    pushToken = json['push_token'] ?? '';
  }

  Map<String, dynamic> toJson() {
    final data = <String, dynamic>{};
    data['image'] = image;
    data['about'] = about;
    data['name'] = name;
    data['id'] = id;
    data['is_online'] = isOnline;
    data['last_active'] = lastActive;
    data['create_at'] = createAt;
    data['email'] = email;
    data['push_token'] = pushToken;
    return data;
  }
}
