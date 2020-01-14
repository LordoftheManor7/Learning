def hugs_and_kisses(number_hugs, number_kisses):

  prompt = 'Hmm?\n'
  prompt2 = 'Is that ok?\n'

  print(f"\nI want to give you {number_hugs} big hugs because you make me happy!")
  print("\nHow many hugs would you like to give me?\n")
  hugs = input(prompt)
  print("\nReally? Thanks!")
  print(f"\nNow I'd like to give you {number_kisses} kisses...\n")
  approve = input(prompt2)
  print("\nMuah!" * 5)

print("I love you!")

hugs_and_kisses(3, 5)
