# damaris
uses barebone aes  and rsa logic for encryption and decryption

HYBRID CRYPTOGRAPHIC ALGORITHM (HCA) 

The Hybrid Cryptographic Algorithm described in this paper is a combination of RSA and 
AES cryptographic algorithms. It takes the following steps: 

Key Generation part of the Hybrid System

i Select two primes, P and Q such that: 
    P*Q = N, ………….(1) 
    Where N is a public key parameter 
    
ii Using Euler’s totient function which is denoted as φ(n), compute: 
    φ(n) = (P-1) *(Q-1)………(2)
    
iii Choose integer ‘e’ such that the Greatest Common Divisor of φ(n) and e is equal to 1, and e 
    is not a factor of φ(n). 
GCD(φ(n), e) =1∣ e∉ φ(n), where 1< e< φ(n)…..(3) 

iv 	Calculate d, where e is the multiplicative inverse of d in mod φ(n) 
 d=e-1 mod φ(n)…….(4) 
ed mod φ(n)=1…….(5) 
d= (1+k φ(n)) ∕ e……….(6) 
 


Encryption part of the Hybrid System 

i 	Let Plaintext be M, such that M1*M2=M1M2 
ii 	Using RSA public key (N, e), compute C1=M1e mod N and C2=M2e mod N 
iii 	Compute C3=C1*C2 iv 	Compute C3 mod N
 v 	Convert C3 into 8bit binary
 vi 	Divide the resulting 8bit into two 4bit binary and convert to hexadecimal values. 
vii 	Transform into equivalent byte using S-box table 
viii 	Convert the resulting byte to equivalent binary 
ix 	Convert binary to decimal 
x 	Perform final encryption using RSA public key (N, e) to generate the final 
ciphertext(C′) 


Decryption part of the Hybrid System 


i	Using RSA private key (N, d), compute C=C′(d) mod N 
ii	Convert C into 8bit binary iii	Divide the resulting 8bit into two 4bit binary and convert to hexadecimal values. 
iv	Transform into equivalent byte using inverse S-box table
 v 	Convert the resulting byte to equivalent binary 
vi 	Convert binary to decimal 
vii 	Perform final decryption using RSA private key (N, d) to generate the plaintext viii 	Verify that the result corresponds to the value of the plaintext
 
 
