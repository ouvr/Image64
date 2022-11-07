import base64,os

os.system('clear')

direct = input('Masukkan Direktori Foto : ')

os.system('clear')

# Image -> Base64

with open(direct, 'rb') as binary_file:

    binary_file_data = binary_file.read()

    base64_encoded_data = base64.b64encode(binary_file_data)

    base64_message = base64_encoded_data.decode('utf-8')

    print('\nBASE64 : ', base64_message)

# Base64 -> Image

base64_img_bytes = base64_message.encode('utf-8')

with open('decode_image.png', 'wb') as file_to_save:

    decoded_image_data = base64.decodebytes(base64_img_bytes)

    file_to_save.write(decoded_image_data)

