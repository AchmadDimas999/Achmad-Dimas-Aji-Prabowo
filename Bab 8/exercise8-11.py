def send_messages(messages, sent_messages):
	while messages:
		message = messages.pop(0)
		print(message)
		sent_messages.append(message)


text_messages = [
	"Semoga harimu menyenangkan!",
	"Jangan lupa beristirahat.",
	"Sampai jumpa besok!",
]
sent_messages = []

send_messages(text_messages.copy(), sent_messages)
print("Daftar pesan asli:", text_messages)
print("Pesan terkirim:", sent_messages)
