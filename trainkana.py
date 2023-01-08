from random import shuffle
hiragana = {'あ': 'a',  'い': 'i',   'う': 'u',   'え': 'e',  'お': 'o',   # Level 01
            'か': 'ka', 'き': 'ki',  'く': 'ku',  'け': 'ke', 'こ': 'ko',  # Level 02
            'さ': 'sa', 'し': 'shi', 'す': 'su',  'せ': 'se', 'そ': 'so',  # Level 03
            'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',  # Level 04
            'な': 'na', 'に': 'ni',  'ぬ': 'nu',  'ね': 'ne', 'の': 'no',  # Level 05
            'は': 'ha', 'ひ': 'hi',  'ふ': 'fu',  'へ': 'he', 'ほ': 'ho',  # Level 06
            'ま': 'ma', 'み': 'mi',  'む': 'mu',  'め': 'me', 'も': 'mo',  # Level 07
            'や': 'ya',             'ゆ': 'yu',              'よ': 'yo',  # Level 08
            'ら': 'ra', 'り': 'ri',  'る': 'ru',  'れ': 're', 'ろ': 'ro',  # Level 09
            'わ': 'wa',                                      'を': 'wo',  # Level 10
            'ん': 'n'}
 
kanas_per_level = {1: 5,  2: 10, 3: 15, 4: 20,  5: 25,
                   6: 30, 7: 35, 8: 38, 9: 43, 10: 46}
level = int(input('[1-10] Level: '))
kanas = kanas_per_level[level]
quiz = list(hiragana.items())[:kanas]
shuffle(quiz)
score = 0
for kana, answer in quiz:
    guess = input(f'{kana} = ')
    if guess == answer:
        score += 1
    else:
        print(f'❌ The right answer was "{answer}"')
print(f'Score: {score}/{kanas}, {(score / kanas) * 100:.1f}%')
