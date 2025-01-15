class Crypt:
    def __init__(self, pub_key, priv_key):
        self.pub_key = pub_key
        self.priv_key = priv_key


    def encrypt(self, text):
        max_block_size = (self.pub_key[1].bit_length()) - 1
        blocks = []
        num = ''

        for i in text:

            if int(num + str(ord(i))).bit_length() >= max_block_size:
                blocks.append(int(num))
                num = ''
                num += str(ord(i))

            else:
                num += str(ord(i))

        enc = []
        for block in blocks:
            enc.append(pow(block, self.pub_key[0], self.pub_key[1]))
        return blocks, enc

    def decrypt(self, text):
        dec = []
        for block in text:
            dec.append(pow(block, self.priv_key[0], self.priv_key[1]))
        return dec