from chatterbot import ChatBot
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

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    try:
        request=input(name+':')
        if request=='Bye' or request =='bye' or request =='thank you':
            print('Bot: Bye')
            break
        else:
            response=chatbot.get_response(request)
            print('Bot:',response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break