message="-R-a-v-i-"
print(message[1:8:2])   #startIndex:endIndex:letterchoose
print(message[0:8:2])
msg="-F-a-l-l-s-"
print(msg[0:12:2])
print(msg[1:12:2])

pin="3924"
is_digit=pin.isdigit()
print(is_digit)

pin="3924ig"
is_digit=pin.isdigit()
print(is_digit)

mbl="  9035793924  "
mbl=mbl.strip()
print(mbl)

mbl="  903 5793924"
mbl=mbl.strip()
print(mbl)

mbl="--9035793924--"
mbl1="--90357--93924--"
mbl=mbl.strip("-")
mbl1=mbl1.strip("-")
print(mbl)
print(mbl1)

name="..,,,chai..,,  "
name=name.strip(" ,.")
print(name)

statement="teh cat and teh dog"
statement=statement.replace("teh","the")
print(statement)

url="https://onthegomodel.com"
is_secure_url=url.startswith("https://")
print(is_secure_url)

url="https:onthegomodel.com"
is_secure_url=url.startswith("https://")
print(is_secure_url)

url="onthegomodel.com"
is_secure_url=url.startswith("onthe")
print(is_secure_url)

email_id="chaiThej@gmail.com"
is_gmail_id=email_id.endswith("@gmail.com")
print(is_gmail_id)

email_id="chaiThejgmail.com"
is_gmail_id=email_id.endswith("@gmail.com")
print(is_gmail_id)

name="chaiThej"
print(name.upper())

name="cHAITHEJ"
print(name.lower())

myster_color="*p%u&r*p%l&e."
color=myster_color[1::1]
print(color)

myster_color="#B2r2e2a2d@"
color=myster_color[1::1]
print(color)

myster_color="%I%S%L%A%N%D%"
color=myster_color[::2]
print(color)

weights="1000g, 100g, 250g, 500g"
weights.replace("g","Kg")
print(weights)

height="6ft"
height=height.replace("ft","")
is_digit=height.isdigit()
print(is_digit)

myster_color="Jellyfish"
color=myster_color[1::4]
print(color)

str1="5 ** 3"
result=str1.isdigit()
print(result)