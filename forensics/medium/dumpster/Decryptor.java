import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class Decryptor
{
	public static final String FLAG = "S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=";
	/* passHash comes from visualvm: */
	// 1. sudo apt-get install visualvm
	// 2. open visualvm, and load heapdump.hprof
	// 3. Threads -> at Decryptor.main
	// 	      -> local variable Decryptor$Password
	// 	      -> fields passHash = []byte
	public static byte[] passHash = {7, 95, -34, 16, -89, -86, 73, 108, -128, 71, 43, 41, 100, 40, 53, -24};
	
	public static byte[] decrypt(byte[] msg) throws Exception
	{
		SecretKeySpec spec = new SecretKeySpec(passHash, "AES");
		Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
		cipher.init(Cipher.DECRYPT_MODE, spec);
		return cipher.doFinal(msg);
	}
	
	public static void main(String[] args) throws Exception
	{
		System.out.println(new String(decrypt(Base64.getDecoder().decode(FLAG.getBytes()))));
	}
}
