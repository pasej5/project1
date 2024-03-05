import bcrypt

password = b"SecretPassword55"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
print(hashed)

b'$2b$12$WvL4yoAgkJj/POmPvup5beqAWWezYjKNU4tnzPm9LnL8SG84sBDtC'

b'$2b$12$mzyNdzjH0C9M2J4rCJYGpem6Wj7em8BdILbnxOP1/SjkqVz1ULzBK'