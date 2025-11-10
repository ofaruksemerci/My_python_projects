alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input (" type encode to 'encrypt , type decode to 'decrypt : \n'").lower()
text=input (" type your message : \n'").lower()
shift=int(input ("type the shift number : \n"))



def  ceaser(original_text ,shift_amount, encode_or_decode):
  if encode_or_decode == "decode":
      shift_amount *=-1
  output_text = ""
  for letter in original_text:
    

    shifted_pstn =  alphabet.index(letter)+shift_amount
    shifted_pstn %=  len(alphabet)
    output_text += alphabet[shifted_pstn]
  

  print (f"here is your {encode_or_decode} message : {output_text} \n")






ceaser(original_text=text ,shift_amount=shift ,encode_or_decode=direction)