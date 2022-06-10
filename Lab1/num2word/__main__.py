"""This module number convert to word."""
import num2word.phrases as phrase
import num2word.w2n2w as word2num2word

if __name__ == "__main__":
    phrase.hello()
    print("Number to Word:", word2num2word.num_to_word(phrase.request_num()))
