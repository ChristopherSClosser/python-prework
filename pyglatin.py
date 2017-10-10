print 'Welcome to the English to Pyg Latin translator'

# suffix
pyg = 'ay'

# user input to translate
original = raw_input('Enter a word:')

# check if input
if len(original) > 0:
  # no numbers
  if original.isalpha():
  	word = original.lower()
  	first = word[0]
 	new_word = word[1:len(word)] + first + pyg
  	print new_word
  else:
    print 'You may not use numbers.'
else:
  print 'You did not enter anything to translate.'
