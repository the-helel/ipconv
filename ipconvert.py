# pip install ipaddress
from ipaddress import IPv4Address

# pip install pyttsx3
# This Module converts Text To Speech 
import pyttsx3 as tts

# Get ipaddress from User
a = IPv4Address(input("Enter IP Address : "))

# Speak The Text
tts.speak("Breaking IP Address into its 4 octet components")

# Printing Converted Text
print("After Breaking IP Address into its 4 octet components  : " , end="")
print(int(a))