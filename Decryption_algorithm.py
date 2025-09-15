#!/usr/bin/env python
# coding: utf-8

# In[47]:


def decrypt(Encrypted, KnownWord):
    """
    Decrypts a Caesar cipher encrypted text given a known word from the original plaintext.

    Args:
        Encrypted (str): The encrypted string.
        KnownWord (str): A known word from the original plaintext.

    Returns:
        str: The fully decrypted plaintext.
    """
    #preprocess the entries
    KnownWord = KnownWord.replace(",", "")
    KnownWord = KnownWord.replace(".", "")
    #store the encrypted string in a list
    Decrypt_list = Encrypted.split(" ")
    known_str = str(KnownWord)

    original_words = []
    if len(known_str) == 1:
        for word in Decrypt_list:
            if len(word) == len(known_str):
                Curr_check = word
                if ((Curr_check[0]).isupper() == (known_str[0]).isupper()):

                        shift_number = abs((ord(Curr_check[0]) - 64) - (ord(known_str[0]) - 64))

                elif ((Curr_check[0]).islower() == (known_str[0]).islower()):
                        shift_number = abs((ord(Curr_check[0]) - 96) - (ord(known_str[0]) - 96))
            else:
                return ("Known word not in original string. Decryption could not be completed")

    if len(known_str) > 1:
        #loop through the words in the encrypted
        for word in Decrypt_list:
            if len(word) == len(known_str):
                Curr_check = word
                if ((Curr_check[0]).isupper() == (known_str[0]).isupper()):
                    if abs((ord(Curr_check[0]) - 64) - (ord(known_str[0]) - 64)) == abs((ord(Curr_check[1]) - 96) - (ord(known_str[1]) - 96)):
                        shift_number = abs((ord(Curr_check[0]) - 64) - (ord(known_str[0]) - 64))
                    else:
                        return "Error!!!Invalid known word. Decryption could not be completed"

                elif ((Curr_check[0]).islower() == (known_str[0]).islower()):
                    if abs((ord(Curr_check[0]) - 96) - (ord(known_str[0]) - 96)) == abs((ord(Curr_check[1]) - 96) - (ord(known_str[1]) - 96)):
                        shift_number = abs((ord(Curr_check[0]) - 96) - (ord(known_str[0]) - 96))
                    else:
                        return "Error!!!Invalid known word. Decryption could not be completed"
    #handle null shift_number
    if shift_number is None:
        raise ValueError("Unable to determine shift number with given known word.")

    #Decryption with shift number
    for word in Decrypt_list:
        curr_word = word
        ascii_curr_word = []
        for char in curr_word:
            if char.islower() == True:
                if ord(char) - shift_number < 97:
                    val = ord(char) - shift_number + 26
                elif ord(char) - shift_number >= 97:
                    val = ord(char) - shift_number
                ascii_curr_word.append(val)

            elif char.isupper() == True:
                if ord(char) - shift_number < 65:
                    val = ord(char) - shift_number + 26
                elif ord(char) - shift_number >= 65:
                    val = ord(char) - shift_number
                ascii_curr_word.append(val)

            #Handle punctuation
            else:
                ascii_curr_word.append(ord(char))

            #convert from ascii to char and join the characters to form the words
        decrypt_str = "".join([chr(val) for val in ascii_curr_word])
        original_words.append(decrypt_str)
    #print decrypted words
    return " ".join(original_words)


# In[ ]:




