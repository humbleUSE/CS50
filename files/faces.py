def main():
	modified_reply=convert()
	print(modified_reply)

def convert():
  reply=input("Enter a message: ")
  emoticons_dict={":)":"🙂",":(":"☹️"}
  for emoticon in emoticons_dict:
    reply=reply.replace(emoticon,emoticons_dict[emoticon])
  return reply

if __name__=="__main__":
  main()