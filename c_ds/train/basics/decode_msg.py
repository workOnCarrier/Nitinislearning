class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decod_key = {}
        result = ""
        val_arr = 'abcdefghijklmnopqrstuvwxyz'
        key_offset = 0
        for key_char in key:
            if key_char == ' ':
                continue
            if key_char not in decod_key.keys():
                # print(f'{key_offset}:{key_char}')
                decod_key[key_char] = ord(val_arr[key_offset])
                key_offset += 1
        # print(decod_key)
        for en_char in message:
            if en_char == " ":
                result += en_char
            else:
                result += chr(decod_key[en_char])
        return result


def main():
    s = Solution()
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(f"\t message:{message} \n\t decoded:{s.decodeMessage(key, message)}")


if __name__ == "__main__":
    main()