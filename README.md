# arkham-fuzzer

This contains the scripts I wrote for the Arkham box on hackthebox.eu.
I've made this repository public now because Arkham has been retired
so solutions are readily available online.

The script is not exactly the cleanest script I've written, but it
works really well. It abuses the Java deserialization bug prevalent
in the challenge by leveraging the payloads created from ysoserial.

I had to modify ysoserial a bit to be a little bit more friendly toward
the challenge itself (namely in that the challenge requires the payload
to be part of a serialized array object), as well as also manipulating
the cookie to use the proper encryption key so that the server would
understand the request.

It's not user friendly at all, but it worked pretty well.
