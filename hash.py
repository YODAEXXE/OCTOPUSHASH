import hashlib

polvo = r"""
                 ___
              .-"   "-.
            .'  .-. .-. '.
           /   ( o Y o )  \
          |     .-^^^-.    |
          |    /  ___  \   |
           \   | (___) |  /
            '-.\_____./.-'
            /   \___/   \
        ___/  /\   /\  \___
       /     /  \_/  \     \
      /_____/    |    \_____\
         /  \    |    /  \
        /    \   |   /    \
       /      \  |  /      \
      /        \ | /        \
     /          \|/          \
    /            |            \
   /             |             \
  /              |              \
 /               |               \
/________________|________________\
"""


print("=" * 50)
print(polvo)
print("        OCTOPUSHASH")
print("=" * 50)


senha = input("Enter the password: ")

print("---------------")


def SHA256(senha):
    hash_obj = hashlib.sha256(senha.encode())
    hash_hex = hash_obj.hexdigest()
    print(f"SHA256 hash: {hash_hex}")


def SHA512(senha):
    hash_obj = hashlib.sha512(senha.encode())
    hash_hex = hash_obj.hexdigest()
    print(f"SHA512 hash: {hash_hex}")


def MD5(senha):
    hash_obj = hashlib.md5(senha.encode())
    hash_hex = hash_obj.hexdigest()
    print(f"MD5 hash: {hash_hex}")


def SHA224(senha):
    hash_obj = hashlib.sha224(senha.encode())
    hash_hex = hash_obj.hexdigest()
    print(f"SHA224 hash: {hash_hex}")


def SHA384(senha):
    hash_obj = hashlib.sha384(senha.encode())
    hash_hex = hash_obj.hexdigest()
    print(f"SHA384 hash: {hash_hex}")


while True:
    print("Choose a hash algorithm:")
    print("--------------")
    print("1. SHA256 → secure")
    print("--------------")
    print("2. SHA512 → robust")
    print("--------------")
    print("3. MD5 → insecure")
    print("--------------")
    print("4. SHA224 → intermediate")
    print("--------------")
    print("5. SHA384 → strong")
    print("--------------")
    print("0. exit")

    hash = input("Choose an option (enter a number): ")

    if hash == "1":
        print("Secure choice.")
        print("############")
        SHA256(senha)
        break
    elif hash == "2":
        print("Good choice.")
        print("############")
        SHA512(senha)
        break
    elif hash == "3":
        print("Extremely insecure!")
        print("############")
        MD5(senha)
        break
    elif hash == "4":
        print("Intermediate.")
        print("############")
        SHA224(senha)
        break
    elif hash == "5":
        print("Great choice.")
        print("############")
        SHA384(senha)
        break
    elif hash == "0":
        exit()
    else:
        print("Choose a number from the list.")
