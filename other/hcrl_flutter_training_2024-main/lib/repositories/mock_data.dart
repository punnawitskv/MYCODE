//Mock Data for Quiz App
List<Map<String, dynamic>> quizzes = [quiz1, quiz2];
Map<String, dynamic> quiz1 = {
  'quiz_id': 'quiz1',
  'quiz_name': 'CE Quiz',
  'quiz_description': 'A computer engineering, KMITL quiz',
  'problems': [
    {
      'question': 'Who is the head of CE department?',
      'options': ['Wiboon P.', 'Amnach K.', 'Thanunchai T.', 'Jirasak S.'],
      'answer': 2
    },
    {
      'question': 'When was CE department established?',
      'options': [2520, 2521, 2522, 2523],
      'answer': 2
    },
    {
      'question': 'Which one is not a CE lab?',
      'options': ['Hardware', 'HCRL', 'SAIG', 'Initial Racing'],
      'answer': 4
    },
    {
      'question':
          'Which activity is held first when you are a student in CE department?',
      'options': ['CE BoostUp', 'Hello CE', 'CE First Drink', 'CE NextGen'],
      'answer': 1
    },
    {
      'question': 'Which one is not a CE course?',
      'options': [
        'Computer Programming',
        'Programming Fundamental',
        'Operating System',
        'Calculus 1'
      ],
      'answer': 1
    }
  ]
};

Map<String, dynamic> quiz2 = {
  'quiz_id': 'quiz2',
  'quiz_name': 'Flutter Quiz',
  'quiz_description': 'A fundamental flutter quiz',
  'problems': [
    {
      'question': 'Who is the creator of Flutter?',
      'options': ['Google', 'Facebook', 'Apple', 'Microsoft'],
      'answer': 1
    },
    {
      'question': 'Which one is ancestor widget?',
      'options': ['Scaffold', 'Container', 'Row', 'Column'],
      'answer': 1
    },
    {
      'question': 'Which file manage dependencies in Flutter?',
      'options': [
        'pubspec.yaml',
        'main.dart',
        'AndroidManifest.xml',
        'build.gradle'
      ],
      'answer': 1
    },
    {
      'question':
          'Which command is used to run Flutter app in the emulator or real device?',
      'options': [
        'flutter run',
        'flutter build',
        'flutter test',
        'flutter doctor'
      ],
      'answer': 1
    },
    {
      'question': 'Which command is used to create a new Flutter project?',
      'options': [
        'flutter create',
        'flutter new',
        'flutter init',
        'flutter start'
      ],
      'answer': 1
    },
    {
      'question': 'Which folder contains all of your code files?',
      'options': ['lib', 'assets', 'test', 'build'],
      'answer': 1
    },
  ]
};
