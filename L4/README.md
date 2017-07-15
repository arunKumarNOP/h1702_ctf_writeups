## Level 1

>Hope you kept your notes.
>
>(Note: Levels 1-4 use the same application)</br>
>[ctfone-490954d49dd51911bc730d8161541cf13e7416f9.apk](./../challanges/ctfone-490954d49dd51911bc730d8161541cf13e7416f9.apk)

This challange was guessing game for me. There is only one native function left to be analyzed and it takes 3 string arguments and returns a string.

Its defined in MonteCarlo class in com.h1702ctf.ctfone package as
```java
public native String functionnameLeftbraceOneCommaTwoCommaThreeCommaRightbraceFour(String str, String str2, String str3);
```

I ended up analyzing it in IDA. I found that it was creating a hash of 32 characters using libsodium [crypto_generichash](https://download.libsodium.org/doc/hashing/generic_hashing.html) and then xoring it with some constant and finally returning a String.

I thought there will be some bug in the crypto so i started searching but nothing. Also 32 bytes doesn't seem bruteforcable so that was out of equation. I kind of moved to next challange and solved it before i did this.

After solving i re-read the challange description and an idea came to my mind i.e what if we need to input the past three flags.

I quickly fired [Frida](https://www.frida.re/) and with a javascript, passed the last three flags.
```javascript
Java.perform(function()
{
	var monteCarloClass = Java.use("com.h1702ctf.ctfone.MonteCarlo");
	var ans = monteCarloClass.functionnameLeftbraceOneCommaTwoCommaThreeCommaRightbraceFour("cApwN{WELL_THAT_WAS_SUPER_EASY}","CAPWN{CRYP706R4PHY_15_H4RD_BR0}","cApwN{1_4m_numb3r_7hr33}");
	console.log("Ans : "+ans);
});
```
We get our Level 4 flag

Flag - <b>cApwN{w1nn3r_w1nn3r_ch1ck3n_d1nn3r!}</b>


#### Author
Arun Kumar Shreevastava