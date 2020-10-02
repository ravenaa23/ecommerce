from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
	  'EBOT',
	  input_adapter='chatterbot.input.TerminalAdapter',
      output_adapter='chatterbot.output.TerminalAdapter',
      logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': ' ',
            'output_text': 'Please email us'
        }
    ]
	)
    
trainer1 = ListTrainer(chatbot)
trainer2 = ChatterBotCorpusTrainer(chatbot)

trainer1.train(
[ 
'hi',
'Hello there!',
'i am looking for best sellers',
'You\'ll be redirected to the best sellers page soon',
])
trainer1.train(
[
'hello',
'Hi! What can i do for you?',
'What are the best sellers',
'This is what I found : https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers'
])
trainer1.train(
[
'hi',
'Hi!Lets begin',
'i wanna see the best sellers',
'Check it out here : https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers',
'what are the delivery days?',
'We deliver 5 days a week ! Fell free to order to us anytime',
'Thank you'
])
trainer2.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)